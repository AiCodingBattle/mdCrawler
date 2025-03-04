Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
As our query analysis becomes more complex, the LLM may struggle to understand how exactly it should respond in certain scenarios. In order to improve performance here, we can add examples to the prompt to guide the LLM.
Let's take a look at how we can add examples for a LangChain YouTube video query analyzer.
## Setup​
#### Install dependencies​
```
# %pip install -qU langchain-core langchain-openai
```

#### Set environment variables​
We'll use OpenAI in this example:
```
import getpassimport osif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass.getpass()# Optional, uncomment to trace runs with LangSmith. Sign up here: https://smith.langchain.com.# os.environ["LANGSMITH_TRACING"] = "true"# os.environ["LANGSMITH_API_KEY"] = getpass.getpass()
```

## Query schema​
We'll define a query schema that we want our model to output. To make our query analysis a bit more interesting, we'll add a `sub_queries` field that contains more narrow questions derived from the top level question.
```
from typing import List, Optionalfrom pydantic import BaseModel, Fieldsub_queries_description ="""\If the original question contains multiple distinct sub-questions, \or if there are more generic questions that would be helpful to answer in \order to answer the original question, write a list of all relevant sub-questions. \Make sure this list is comprehensive and covers all parts of the original question. \It's ok if there's redundancy in the sub-questions. \Make sure the sub-questions are as narrowly focused as possible."""classSearch(BaseModel):"""Search over a database of tutorial videos about a software library."""  query:str= Field(...,    description="Primary similarity search query applied to video transcripts.",)  sub_queries: List[str]= Field(    default_factory=list, description=sub_queries_description)  publish_year: Optional[int]= Field(None, description="Year video was published")
```

## Query generation​
```
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholderfrom langchain_core.runnables import RunnablePassthroughfrom langchain_openai import ChatOpenAIsystem ="""You are an expert at converting user questions into database queries. \You have access to a database of tutorial videos about a software library for building LLM-powered applications. \Given a question, return a list of database queries optimized to retrieve the most relevant results.If there are acronyms or words you are not familiar with, do not try to rephrase them."""prompt = ChatPromptTemplate.from_messages([("system", system),    MessagesPlaceholder("examples", optional=True),("human","{question}"),])llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)structured_llm = llm.with_structured_output(Search)query_analyzer ={"question": RunnablePassthrough()}| prompt | structured_llm
```

**API Reference:**ChatPromptTemplate | MessagesPlaceholder | RunnablePassthrough | ChatOpenAI
Let's try out our query analyzer without any examples in the prompt:
```
query_analyzer.invoke("what's the difference between web voyager and reflection agents? do both use langgraph?")
```

```
Search(query='difference between web voyager and reflection agents', sub_queries=['what is web voyager', 'what are reflection agents', 'do both web voyager and reflection agents use langgraph?'], publish_year=None)
```

## Adding examples and tuning the prompt​
This works pretty well, but we probably want it to decompose the question even further to separate the queries about Web Voyager and Reflection Agents.
To tune our query generation results, we can add some examples of inputs questions and gold standard output queries to our prompt.
```
examples =[]
```

```
question ="What's chat langchain, is it a langchain template?"query = Search(  query="What is chat langchain and is it a langchain template?",  sub_queries=["What is chat langchain","What is a langchain template"],)examples.append({"input": question,"tool_calls":[query]})
```

```
question ="How to build multi-agent system and stream intermediate steps from it"query = Search(  query="How to build multi-agent system and stream intermediate steps from it",  sub_queries=["How to build multi-agent system","How to stream intermediate steps from multi-agent system","How to stream intermediate steps",],)examples.append({"input": question,"tool_calls":[query]})
```

```
question ="LangChain agents vs LangGraph?"query = Search(  query="What's the difference between LangChain agents and LangGraph? How do you deploy them?",  sub_queries=["What are LangChain agents","What is LangGraph","How do you deploy LangChain agents","How do you deploy LangGraph",],)examples.append({"input": question,"tool_calls":[query]})
```

Now we need to update our prompt template and chain so that the examples are included in each prompt. Since we're working with OpenAI function-calling, we'll need to do a bit of extra structuring to send example inputs and outputs to the model. We'll create a `tool_example_to_messages` helper function to handle this for us:
```
import uuidfrom typing import Dictfrom langchain_core.messages import(  AIMessage,  BaseMessage,  HumanMessage,  SystemMessage,  ToolMessage,)deftool_example_to_messages(example: Dict)-> List[BaseMessage]:  messages: List[BaseMessage]=[HumanMessage(content=example["input"])]  openai_tool_calls =[]for tool_call in example["tool_calls"]:    openai_tool_calls.append({"id":str(uuid.uuid4()),"type":"function","function":{"name": tool_call.__class__.__name__,"arguments": tool_call.json(),},})  messages.append(    AIMessage(content="", additional_kwargs={"tool_calls": openai_tool_calls}))  tool_outputs = example.get("tool_outputs")or["You have correctly called this tool."]*len(openai_tool_calls)for output, tool_call inzip(tool_outputs, openai_tool_calls):    messages.append(ToolMessage(content=output, tool_call_id=tool_call["id"]))return messagesexample_msgs =[msg for ex in examples for msg in tool_example_to_messages(ex)]
```

**API Reference:**AIMessage | BaseMessage | HumanMessage | SystemMessage | ToolMessage
```
from langchain_core.prompts import MessagesPlaceholderquery_analyzer_with_examples =({"question": RunnablePassthrough()}| prompt.partial(examples=example_msgs)| structured_llm)
```

**API Reference:**MessagesPlaceholder
```
query_analyzer_with_examples.invoke("what's the difference between web voyager and reflection agents? do both use langgraph?")
```

```
Search(query="What's the difference between web voyager and reflection agents? Do both use langgraph?", sub_queries=['What is web voyager', 'What are reflection agents', 'Do web voyager and reflection agents use langgraph?'], publish_year=None)
```

Thanks to our examples we get a slightly more decomposed search query. With some more prompt engineering and tuning of our examples we could improve query generation even more.
You can see that the examples are passed to the model as messages in the LangSmith trace.
#### Was this page helpful?
  * Setup
  * Query schema
  * Query generation
  * Adding examples and tuning the prompt


