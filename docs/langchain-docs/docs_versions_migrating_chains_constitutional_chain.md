Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
ConstitutionalChain allowed for a LLM to critique and revise generations based on principles, structured as combinations of critique and revision requests. For example, a principle might include a request to identify harmful content, and a request to rewrite the content.
`Constitutional AI principles` are based on the Constitutional AI: Harmlessness from AI Feedback paper.
In `ConstitutionalChain`, this structure of critique requests and associated revisions was formatted into a LLM prompt and parsed out of string responses. This is more naturally achieved via structured output features of chat models. We can construct a simple chain in LangGraph for this purpose. Some advantages of this approach include:
  * Leverage tool-calling capabilities of chat models that have been fine-tuned for this purpose;
  * Reduce parsing errors from extracting expression from a string LLM response;
  * Delegation of instructions to message roles (e.g., chat models can understand what a `ToolMessage` represents without the need for additional prompting);
  * Support for streaming, both of individual tokens and chain steps.


```
%pip install --upgrade --quiet langchain-openai
```

```
import osfrom getpass import getpassif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()
```

## Legacy​
Details
```
from langchain.chains import ConstitutionalChain, LLMChainfrom langchain.chains.constitutional_ai.models import ConstitutionalPrinciplefrom langchain_core.prompts import PromptTemplatefrom langchain_openai import OpenAIllm = OpenAI()qa_prompt = PromptTemplate(  template="Q: {question} A:",  input_variables=["question"],)qa_chain = LLMChain(llm=llm, prompt=qa_prompt)constitutional_chain = ConstitutionalChain.from_llm(  llm=llm,  chain=qa_chain,  constitutional_principles=[    ConstitutionalPrinciple(      critique_request="Tell if this answer is good.",      revision_request="Give a better answer.",)],  return_intermediate_steps=True,)result = constitutional_chain.invoke("What is the meaning of life?")
```

**API Reference:**ConstitutionalChain | LLMChain | ConstitutionalPrinciple | PromptTemplate | OpenAI
```
result
```

```
{'question': 'What is the meaning of life?', 'output': 'The meaning of life is a deeply personal and ever-evolving concept. It is a journey of self-discovery and growth, and can be different for each individual. Some may find meaning in relationships, others in achieving their goals, and some may never find a concrete answer. Ultimately, the meaning of life is what we make of it.', 'initial_output': ' The meaning of life is a subjective concept that can vary from person to person. Some may believe that the purpose of life is to find happiness and fulfillment, while others may see it as a journey of self-discovery and personal growth. Ultimately, the meaning of life is something that each individual must determine for themselves.', 'critiques_and_revisions': [('This answer is good in that it recognizes and acknowledges the subjective nature of the question and provides a valid and thoughtful response. However, it could have also mentioned that the meaning of life is a complex and deeply personal concept that can also change and evolve over time for each individual. Critique Needed.',  'The meaning of life is a deeply personal and ever-evolving concept. It is a journey of self-discovery and growth, and can be different for each individual. Some may find meaning in relationships, others in achieving their goals, and some may never find a concrete answer. Ultimately, the meaning of life is what we make of it.')]}
```

Above, we've returned intermediate steps showing:
  * The original question;
  * The initial output;
  * Critiques and revisions;
  * The final output (matching a revision).


## LangGraph​
Details
Below, we use the .with_structured_output method to simultaneously generate (1) a judgment of whether a critique is needed, and (2) the critique. We surface all prompts involved for clarity and ease of customizability.
Note that we are also able to stream intermediate steps with this implementation, so we can monitor and if needed intervene during its execution.
```
from typing import List, Optional, Tuplefrom langchain.chains.constitutional_ai.models import ConstitutionalPrinciplefrom langchain.chains.constitutional_ai.prompts import(  CRITIQUE_PROMPT,  REVISION_PROMPT,)from langchain_core.output_parsers import StrOutputParserfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_openai import ChatOpenAIfrom langgraph.graph import END, START, StateGraphfrom typing_extensions import Annotated, TypedDictllm = ChatOpenAI(model="gpt-4o-mini")classCritique(TypedDict):"""Generate a critique, if needed."""  critique_needed: Annotated[bool,...,"Whether or not a critique is needed."]  critique: Annotated[str,...,"If needed, the critique."]critique_prompt = ChatPromptTemplate.from_template("Critique this response according to the critique request. ""If no critique is needed, specify that.\n\n""Query: {query}\n\n""Response: {response}\n\n""Critique request: {critique_request}")revision_prompt = ChatPromptTemplate.from_template("Revise this response according to the critique and reivsion request.\n\n""Query: {query}\n\n""Response: {response}\n\n""Critique request: {critique_request}\n\n""Critique: {critique}\n\n""If the critique does not identify anything worth changing, ignore the ""revision request and return 'No revisions needed'. If the critique ""does identify something worth changing, revise the response based on ""the revision request.\n\n""Revision Request: {revision_request}")chain = llm | StrOutputParser()critique_chain = critique_prompt | llm.with_structured_output(Critique)revision_chain = revision_prompt | llm | StrOutputParser()classState(TypedDict):  query:str  constitutional_principles: List[ConstitutionalPrinciple]  initial_response:str  critiques_and_revisions: List[Tuple[str,str]]  response:strasyncdefgenerate_response(state: State):"""Generate initial response."""  response =await chain.ainvoke(state["query"])return{"response": response,"initial_response": response}asyncdefcritique_and_revise(state: State):"""Critique and revise response according to principles."""  critiques_and_revisions =[]  response = state["initial_response"]for principle in state["constitutional_principles"]:    critique =await critique_chain.ainvoke({"query": state["query"],"response": response,"critique_request": principle.critique_request,})if critique["critique_needed"]:      revision =await revision_chain.ainvoke({"query": state["query"],"response": response,"critique_request": principle.critique_request,"critique": critique["critique"],"revision_request": principle.revision_request,})      response = revision      critiques_and_revisions.append((critique["critique"], revision))else:      critiques_and_revisions.append((critique["critique"],""))return{"critiques_and_revisions": critiques_and_revisions,"response": response,}graph = StateGraph(State)graph.add_node("generate_response", generate_response)graph.add_node("critique_and_revise", critique_and_revise)graph.add_edge(START,"generate_response")graph.add_edge("generate_response","critique_and_revise")graph.add_edge("critique_and_revise", END)app = graph.compile()
```

**API Reference:**ConstitutionalPrinciple | CRITIQUE_PROMPT | REVISION_PROMPT | StrOutputParser | ChatPromptTemplate | ChatOpenAI | StateGraph
```
constitutional_principles =[  ConstitutionalPrinciple(    critique_request="Tell if this answer is good.",    revision_request="Give a better answer.",)]query ="What is the meaning of life? Answer in 10 words or fewer."asyncfor step in app.astream({"query": query,"constitutional_principles": constitutional_principles},  stream_mode="values",):  subset =["initial_response","critiques_and_revisions","response"]print({k: v for k, v in step.items()if k in subset})
```

```
{}{'initial_response': 'Finding purpose, connection, and joy in our experiences and relationships.', 'response': 'Finding purpose, connection, and joy in our experiences and relationships.'}{'initial_response': 'Finding purpose, connection, and joy in our experiences and relationships.', 'critiques_and_revisions': [("The response exceeds the 10-word limit, providing a more elaborate answer than requested. A concise response, such as 'To seek purpose and joy in life,' would better align with the query.", 'To seek purpose and joy in life.')], 'response': 'To seek purpose and joy in life.'}
```

## Next steps​
See guides for generating structured output here.
Check out the LangGraph documentation for detail on building with LangGraph.
#### Was this page helpful?
  * Legacy
  * LangGraph
  * Next steps


