Skip to content 
# Adaptive RAG¶
Adaptive RAG is a strategy for RAG that unites (1) query analysis with (2) active / self-corrective RAG.
In the paper, they report query analysis to route across:
  * No Retrieval
  * Single-shot RAG
  * Iterative RAG


Let's build on this using LangGraph. 
In our implementation, we will route between:
  * Web search: for questions related to recent events
  * Self-corrective RAG: for questions related to our index


![Screenshot 2024-03-26 at 1.36.03 PM.png](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/)
## Setup¶
First, let's install our required packages and set our API keys
```
%%capture --no-stderr
%pip install -U langchain_community tiktoken langchain-openai langchain-cohere langchainhub chromadb langchain langgraph tavily-python

```

```
importgetpass
importos


def_set_env(var: str):
  if not os.environ.get(var):
    os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("OPENAI_API_KEY")
# _set_env("COHERE_API_KEY")
_set_env("TAVILY_API_KEY")

```

Set up LangSmith for LangGraph development
Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started here. 
## Create Index¶
```
### Build Index

fromlangchain.text_splitterimport RecursiveCharacterTextSplitter
fromlangchain_community.document_loadersimport WebBaseLoader
fromlangchain_community.vectorstoresimport Chroma
fromlangchain_openaiimport OpenAIEmbeddings

### from langchain_cohere import CohereEmbeddings

# Set embeddings
embd = OpenAIEmbeddings()

# Docs to index
urls = [
  "https://lilianweng.github.io/posts/2023-06-23-agent/",
  "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
  "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

# Load
docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

# Split
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
  chunk_size=500, chunk_overlap=0
)
doc_splits = text_splitter.split_documents(docs_list)

# Add to vectorstore
vectorstore = Chroma.from_documents(
  documents=doc_splits,
  collection_name="rag-chroma",
  embedding=embd,
)
retriever = vectorstore.as_retriever()

```

API Reference: RecursiveCharacterTextSplitter | WebBaseLoader | Chroma | OpenAIEmbeddings | CohereEmbeddings
## LLMs¶
Using Pydantic with LangChain
This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 
```
### Router

fromtypingimport Literal

fromlangchain_core.promptsimport ChatPromptTemplate
fromlangchain_openaiimport ChatOpenAI

frompydanticimport BaseModel, Field


# Data model
classRouteQuery(BaseModel):
"""Route a user query to the most relevant datasource."""

  datasource: Literal["vectorstore", "web_search"] = Field(
    ...,
    description="Given a user question choose to route it to web search or a vectorstore.",
  )


# LLM with function call
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_llm_router = llm.with_structured_output(RouteQuery)

# Prompt
system = """You are an expert at routing a user question to a vectorstore or web search.
The vectorstore contains documents related to agents, prompt engineering, and adversarial attacks.
Use the vectorstore for questions on these topics. Otherwise, use web-search."""
route_prompt = ChatPromptTemplate.from_messages(
  [
    ("system", system),
    ("human", "{question}"),
  ]
)

question_router = route_prompt | structured_llm_router
print(
  question_router.invoke(
    {"question": "Who will the Bears draft first in the NFL draft?"}
  )
)
print(question_router.invoke({"question": "What are the types of agent memory?"}))

```

API Reference: ChatPromptTemplate | ChatOpenAI
```
datasource='web_search'
datasource='vectorstore'

```

```
### Retrieval Grader


# Data model
classGradeDocuments(BaseModel):
"""Binary score for relevance check on retrieved documents."""

  binary_score: str = Field(
    description="Documents are relevant to the question, 'yes' or 'no'"
  )


# LLM with function call
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_llm_grader = llm.with_structured_output(GradeDocuments)

# Prompt
system = """You are a grader assessing relevance of a retrieved document to a user question. \n
  If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
  It does not need to be a stringent test. The goal is to filter out erroneous retrievals. \n
  Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""
grade_prompt = ChatPromptTemplate.from_messages(
  [
    ("system", system),
    ("human", "Retrieved document: \n\n{document}\n\n User question: {question}"),
  ]
)

retrieval_grader = grade_prompt | structured_llm_grader
question = "agent memory"
docs = retriever.invoke(question)
doc_txt = docs[1].page_content
print(retrieval_grader.invoke({"question": question, "document": doc_txt}))

```

```
binary_score='yes'

```

```
### Generate

fromlangchainimport hub
fromlangchain_core.output_parsersimport StrOutputParser

# Prompt
prompt = hub.pull("rlm/rag-prompt")

# LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


# Post-processing
defformat_docs(docs):
  return "\n\n".join(doc.page_content for doc in docs)


# Chain
rag_chain = prompt | llm | StrOutputParser()

# Run
generation = rag_chain.invoke({"context": docs, "question": question})
print(generation)

```

API Reference: StrOutputParser
```
Agent memory in LLM-powered autonomous systems consists of short-term and long-term memory. Short-term memory utilizes in-context learning for immediate tasks, while long-term memory allows agents to retain and recall information over extended periods, often using external storage for efficient retrieval. This memory structure supports the agent's ability to reflect on past actions and improve future performance.

```

```
### Hallucination Grader


# Data model
classGradeHallucinations(BaseModel):
"""Binary score for hallucination present in generation answer."""

  binary_score: str = Field(
    description="Answer is grounded in the facts, 'yes' or 'no'"
  )


# LLM with function call
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_llm_grader = llm.with_structured_output(GradeHallucinations)

# Prompt
system = """You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts. \n
   Give a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""
hallucination_prompt = ChatPromptTemplate.from_messages(
  [
    ("system", system),
    ("human", "Set of facts: \n\n{documents}\n\n LLM generation: {generation}"),
  ]
)

hallucination_grader = hallucination_prompt | structured_llm_grader
hallucination_grader.invoke({"documents": docs, "generation": generation})

```

```
GradeHallucinations(binary_score='yes')

```

```
### Answer Grader


# Data model
classGradeAnswer(BaseModel):
"""Binary score to assess answer addresses question."""

  binary_score: str = Field(
    description="Answer addresses the question, 'yes' or 'no'"
  )


# LLM with function call
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_llm_grader = llm.with_structured_output(GradeAnswer)

# Prompt
system = """You are a grader assessing whether an answer addresses / resolves a question \n
   Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""
answer_prompt = ChatPromptTemplate.from_messages(
  [
    ("system", system),
    ("human", "User question: \n\n{question}\n\n LLM generation: {generation}"),
  ]
)

answer_grader = answer_prompt | structured_llm_grader
answer_grader.invoke({"question": question, "generation": generation})

```

```
GradeAnswer(binary_score='yes')

```

```
### Question Re-writer

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Prompt
system = """You a question re-writer that converts an input question to a better version that is optimized \n
   for vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""
re_write_prompt = ChatPromptTemplate.from_messages(
  [
    ("system", system),
    (
      "human",
      "Here is the initial question: \n\n{question}\n Formulate an improved question.",
    ),
  ]
)

question_rewriter = re_write_prompt | llm | StrOutputParser()
question_rewriter.invoke({"question": question})

```

```
'What are the key concepts and techniques related to agent memory in artificial intelligence?'

```

## Web Search Tool¶
```
### Search

fromlangchain_community.tools.tavily_searchimport TavilySearchResults

web_search_tool = TavilySearchResults(k=3)

```

API Reference: TavilySearchResults
## Construct the Graph¶
Capture the flow in as a graph.
### Define Graph State¶
```
fromtypingimport List

fromtyping_extensionsimport TypedDict


classGraphState(TypedDict):
"""
  Represents the state of our graph.

  Attributes:
    question: question
    generation: LLM generation
    documents: list of documents
  """

  question: str
  generation: str
  documents: List[str]

```

### Define Graph Flow¶
```
fromlangchain.schemaimport Document


defretrieve(state):
"""
  Retrieve documents

  Args:
    state (dict): The current graph state

  Returns:
    state (dict): New key added to state, documents, that contains retrieved documents
  """
  print("---RETRIEVE---")
  question = state["question"]

  # Retrieval
  documents = retriever.invoke(question)
  return {"documents": documents, "question": question}


defgenerate(state):
"""
  Generate answer

  Args:
    state (dict): The current graph state

  Returns:
    state (dict): New key added to state, generation, that contains LLM generation
  """
  print("---GENERATE---")
  question = state["question"]
  documents = state["documents"]

  # RAG generation
  generation = rag_chain.invoke({"context": documents, "question": question})
  return {"documents": documents, "question": question, "generation": generation}


defgrade_documents(state):
"""
  Determines whether the retrieved documents are relevant to the question.

  Args:
    state (dict): The current graph state

  Returns:
    state (dict): Updates documents key with only filtered relevant documents
  """

  print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
  question = state["question"]
  documents = state["documents"]

  # Score each doc
  filtered_docs = []
  for d in documents:
    score = retrieval_grader.invoke(
      {"question": question, "document": d.page_content}
    )
    grade = score.binary_score
    if grade == "yes":
      print("---GRADE: DOCUMENT RELEVANT---")
      filtered_docs.append(d)
    else:
      print("---GRADE: DOCUMENT NOT RELEVANT---")
      continue
  return {"documents": filtered_docs, "question": question}


deftransform_query(state):
"""
  Transform the query to produce a better question.

  Args:
    state (dict): The current graph state

  Returns:
    state (dict): Updates question key with a re-phrased question
  """

  print("---TRANSFORM QUERY---")
  question = state["question"]
  documents = state["documents"]

  # Re-write question
  better_question = question_rewriter.invoke({"question": question})
  return {"documents": documents, "question": better_question}


defweb_search(state):
"""
  Web search based on the re-phrased question.

  Args:
    state (dict): The current graph state

  Returns:
    state (dict): Updates documents key with appended web results
  """

  print("---WEB SEARCH---")
  question = state["question"]

  # Web search
  docs = web_search_tool.invoke({"query": question})
  web_results = "\n".join([d["content"] for d in docs])
  web_results = Document(page_content=web_results)

  return {"documents": web_results, "question": question}


### Edges ###


defroute_question(state):
"""
  Route question to web search or RAG.

  Args:
    state (dict): The current graph state

  Returns:
    str: Next node to call
  """

  print("---ROUTE QUESTION---")
  question = state["question"]
  source = question_router.invoke({"question": question})
  if source.datasource == "web_search":
    print("---ROUTE QUESTION TO WEB SEARCH---")
    return "web_search"
  elif source.datasource == "vectorstore":
    print("---ROUTE QUESTION TO RAG---")
    return "vectorstore"


defdecide_to_generate(state):
"""
  Determines whether to generate an answer, or re-generate a question.

  Args:
    state (dict): The current graph state

  Returns:
    str: Binary decision for next node to call
  """

  print("---ASSESS GRADED DOCUMENTS---")
  state["question"]
  filtered_documents = state["documents"]

  if not filtered_documents:
    # All documents have been filtered check_relevance
    # We will re-generate a new query
    print(
      "---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---"
    )
    return "transform_query"
  else:
    # We have relevant documents, so generate answer
    print("---DECISION: GENERATE---")
    return "generate"


defgrade_generation_v_documents_and_question(state):
"""
  Determines whether the generation is grounded in the document and answers question.

  Args:
    state (dict): The current graph state

  Returns:
    str: Decision for next node to call
  """

  print("---CHECK HALLUCINATIONS---")
  question = state["question"]
  documents = state["documents"]
  generation = state["generation"]

  score = hallucination_grader.invoke(
    {"documents": documents, "generation": generation}
  )
  grade = score.binary_score

  # Check hallucination
  if grade == "yes":
    print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
    # Check question-answering
    print("---GRADE GENERATION vs QUESTION---")
    score = answer_grader.invoke({"question": question, "generation": generation})
    grade = score.binary_score
    if grade == "yes":
      print("---DECISION: GENERATION ADDRESSES QUESTION---")
      return "useful"
    else:
      print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
      return "not useful"
  else:
    pprint("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
    return "not supported"

```

API Reference: Document
### Compile Graph¶
```
fromlanggraph.graphimport END, StateGraph, START

workflow = StateGraph(GraphState)

# Define the nodes
workflow.add_node("web_search", web_search) # web search
workflow.add_node("retrieve", retrieve) # retrieve
workflow.add_node("grade_documents", grade_documents) # grade documents
workflow.add_node("generate", generate) # generatae
workflow.add_node("transform_query", transform_query) # transform_query

# Build graph
workflow.add_conditional_edges(
  START,
  route_question,
  {
    "web_search": "web_search",
    "vectorstore": "retrieve",
  },
)
workflow.add_edge("web_search", "generate")
workflow.add_edge("retrieve", "grade_documents")
workflow.add_conditional_edges(
  "grade_documents",
  decide_to_generate,
  {
    "transform_query": "transform_query",
    "generate": "generate",
  },
)
workflow.add_edge("transform_query", "retrieve")
workflow.add_conditional_edges(
  "generate",
  grade_generation_v_documents_and_question,
  {
    "not supported": "generate",
    "useful": END,
    "not useful": "transform_query",
  },
)

# Compile
app = workflow.compile()

```

API Reference: END | StateGraph | START
## Use Graph¶
```
frompprintimport pprint

# Run
inputs = {
  "question": "What player at the Bears expected to draft first in the 2024 NFL draft?"
}
for output in app.stream(inputs):
  for key, value in output.items():
    # Node
    pprint(f"Node '{key}':")
    # Optional: print full state at each node
    # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
  pprint("\n---\n")

# Final generation
pprint(value["generation"])

```

```
---ROUTE QUESTION---
---ROUTE QUESTION TO WEB SEARCH---
---WEB SEARCH---
"Node 'web_search':"
'\n---\n'
---GENERATE---
---CHECK HALLUCINATIONS---
---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---
---GRADE GENERATION vs QUESTION---
---DECISION: GENERATION ADDRESSES QUESTION---
"Node 'generate':"
'\n---\n'
('The Chicago Bears are expected to draft quarterback Caleb Williams first '
 'overall in the 2024 NFL Draft. They also have a second first-round pick, '
 'where they selected wide receiver Rome Odunze.')

```

```
# Run
inputs = {"question": "What are the types of agent memory?"}
for output in app.stream(inputs):
  for key, value in output.items():
    # Node
    pprint(f"Node '{key}':")
    # Optional: print full state at each node
    # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
  pprint("\n---\n")

# Final generation
pprint(value["generation"])

```

```
---ROUTE QUESTION---
---ROUTE QUESTION TO RAG---
---RETRIEVE---
"Node 'retrieve':"
'\n---\n'
---CHECK DOCUMENT RELEVANCE TO QUESTION---
---GRADE: DOCUMENT NOT RELEVANT---
---GRADE: DOCUMENT RELEVANT---
---GRADE: DOCUMENT NOT RELEVANT---
---GRADE: DOCUMENT RELEVANT---
---ASSESS GRADED DOCUMENTS---
---DECISION: GENERATE---
"Node 'grade_documents':"
'\n---\n'
---GENERATE---
---CHECK HALLUCINATIONS---
---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---
---GRADE GENERATION vs QUESTION---
---DECISION: GENERATION ADDRESSES QUESTION---
"Node 'generate':"
'\n---\n'
('The types of agent memory include short-term memory, long-term memory, and '
 'sensory memory. Short-term memory is utilized for in-context learning, while '
 'long-term memory allows for the retention and recall of information over '
 'extended periods. Sensory memory involves learning embedding representations '
 'for various raw inputs, such as text and images.')

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! Please help us improve this page by adding to the discussion below. 
## Comments
Back to top 
