Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Runnables
  * Tools
  * Agents


Here we will demonstrate how to convert a LangChain `Runnable` into a tool that can be used by agents, chains, or chat models.
## Dependencies​
**Note** : this guide requires `langchain-core` >= 0.2.13. We will also use OpenAI for embeddings, but any LangChain embeddings should suffice. We will use a simple LangGraph agent for demonstration purposes.
```
%%capture --no-stderr%pip install -U langchain-core langchain-openai langgraph
```

LangChain tools are interfaces that an agent, chain, or chat model can use to interact with the world. See here for how-to guides covering tool-calling, built-in tools, custom tools, and more information.
LangChain tools-- instances of BaseTool-- are Runnables with additional constraints that enable them to be invoked effectively by language models:
  * Their inputs are constrained to be serializable, specifically strings and Python `dict` objects;
  * They contain names and descriptions indicating how and when they should be used;
  * They may contain a detailed args_schema for their arguments. That is, while a tool (as a `Runnable`) might accept a single `dict` input, the specific keys and type information needed to populate a dict should be specified in the `args_schema`.


Runnables that accept string or `dict` input can be converted to tools using the as_tool method, which allows for the specification of names, descriptions, and additional schema information for arguments.
## Basic usage​
With typed `dict` input:
```
from typing import Listfrom langchain_core.runnables import RunnableLambdafrom typing_extensions import TypedDictclassArgs(TypedDict):  a:int  b: List[int]deff(x: Args)->str:returnstr(x["a"]*max(x["b"]))runnable = RunnableLambda(f)as_tool = runnable.as_tool(  name="My tool",  description="Explanation of when to use tool.",)
```

**API Reference:**RunnableLambda
```
print(as_tool.description)as_tool.args_schema.schema()
```

```
Explanation of when to use tool.
```

```
{'title': 'My tool', 'type': 'object', 'properties': {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'array', 'items': {'type': 'integer'}}}, 'required': ['a', 'b']}
```

```
as_tool.invoke({"a":3,"b":[1,2]})
```

```
'6'
```

Without typing information, arg types can be specified via `arg_types`:
```
from typing import Any, Dictdefg(x: Dict[str, Any])->str:returnstr(x["a"]*max(x["b"]))runnable = RunnableLambda(g)as_tool = runnable.as_tool(  name="My tool",  description="Explanation of when to use tool.",  arg_types={"a":int,"b": List[int]},)
```

Alternatively, the schema can be fully specified by directly passing the desired args_schema for the tool:
```
from pydantic import BaseModel, FieldclassGSchema(BaseModel):"""Apply a function to an integer and list of integers."""  a:int= Field(..., description="Integer")  b: List[int]= Field(..., description="List of ints")runnable = RunnableLambda(g)as_tool = runnable.as_tool(GSchema)
```

String input is also supported:
```
deff(x:str)->str:return x +"a"defg(x:str)->str:return x +"z"runnable = RunnableLambda(f)| gas_tool = runnable.as_tool()
```

```
as_tool.invoke("b")
```

```
'baz'
```

## In agents​
Below we will incorporate LangChain Runnables as tools in an agent application. We will demonstrate with:
  * a document retriever;
  * a simple RAG chain, allowing an agent to delegate relevant queries to it.


We first instantiate a chat model that supports tool calling:
Select chat model:
Groq▾
* Groq
* OpenAI
* Anthropic
* Azure
* Google Vertex
* AWS
* Cohere
* NVIDIA
* Fireworks AI
* Mistral AI
* Together AI
* IBM watsonx
* Databricks
```
pip install -qU "langchain[groq]"
```

```
import getpassimport osifnot os.environ.get("GROQ_API_KEY"): os.environ["GROQ_API_KEY"]= getpass.getpass("Enter API key for Groq: ")from langchain.chat_models import init_chat_modelllm = init_chat_model("llama3-8b-8192", model_provider="groq")
```

Following the RAG tutorial, let's first construct a retriever:
```
from langchain_core.documents import Documentfrom langchain_core.vectorstores import InMemoryVectorStorefrom langchain_openai import OpenAIEmbeddingsdocuments =[  Document(    page_content="Dogs are great companions, known for their loyalty and friendliness.",),  Document(    page_content="Cats are independent pets that often enjoy their own space.",),]vectorstore = InMemoryVectorStore.from_documents(  documents, embedding=OpenAIEmbeddings())retriever = vectorstore.as_retriever(  search_type="similarity",  search_kwargs={"k":1},)
```

**API Reference:**Document | InMemoryVectorStore | OpenAIEmbeddings
We next create use a simple pre-built LangGraph agent and provide it the tool:
```
from langgraph.prebuilt import create_react_agenttools =[  retriever.as_tool(    name="pet_info_retriever",    description="Get information about pets.",)]agent = create_react_agent(llm, tools)
```

**API Reference:**create_react_agent
```
for chunk in agent.stream({"messages":[("human","What are dogs known for?")]}):print(chunk)print("----")
```

```
{'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_W8cnfOjwqEn4cFcg19LN9mYD', 'function': {'arguments': '{"__arg1":"dogs"}', 'name': 'pet_info_retriever'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 19, 'prompt_tokens': 60, 'total_tokens': 79}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': None, 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-d7f81de9-1fb7-4caf-81ed-16dcdb0b2ab4-0', tool_calls=[{'name': 'pet_info_retriever', 'args': {'__arg1': 'dogs'}, 'id': 'call_W8cnfOjwqEn4cFcg19LN9mYD'}], usage_metadata={'input_tokens': 60, 'output_tokens': 19, 'total_tokens': 79})]}}----{'tools': {'messages': [ToolMessage(content="[Document(id='86f835fe-4bbe-4ec6-aeb4-489a8b541707', page_content='Dogs are great companions, known for their loyalty and friendliness.')]", name='pet_info_retriever', tool_call_id='call_W8cnfOjwqEn4cFcg19LN9mYD')]}}----{'agent': {'messages': [AIMessage(content='Dogs are known for being great companions, known for their loyalty and friendliness.', response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 134, 'total_tokens': 152}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-9ca5847a-a5eb-44c0-a774-84cc2c5bbc5b-0', usage_metadata={'input_tokens': 134, 'output_tokens': 18, 'total_tokens': 152})]}}----
```

See LangSmith trace for the above run.
Going further, we can create a simple RAG chain that takes an additional parameter-- here, the "style" of the answer.
```
from operator import itemgetterfrom langchain_core.output_parsers import StrOutputParserfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import RunnablePassthroughsystem_prompt ="""You are an assistant for question-answering tasks.Use the below context to answer the question. Ifyou don't know the answer, say you don't know.Use three sentences maximum and keep the answerconcise.Answer in the style of {answer_style}.Question: {question}Context: {context}"""prompt = ChatPromptTemplate.from_messages([("system", system_prompt)])rag_chain =({"context": itemgetter("question")| retriever,"question": itemgetter("question"),"answer_style": itemgetter("answer_style"),}| prompt| llm| StrOutputParser())
```

**API Reference:**StrOutputParser | ChatPromptTemplate | RunnablePassthrough
Note that the input schema for our chain contains the required arguments, so it converts to a tool without further specification:
```
rag_chain.input_schema.schema()
```

```
{'title': 'RunnableParallel<context,question,answer_style>Input', 'type': 'object', 'properties': {'question': {'title': 'Question'}, 'answer_style': {'title': 'Answer Style'}}}
```

```
rag_tool = rag_chain.as_tool(  name="pet_expert",  description="Get information about pets.",)
```

Below we again invoke the agent. Note that the agent populates the required parameters in its `tool_calls`:
```
agent = create_react_agent(llm,[rag_tool])for chunk in agent.stream({"messages":[("human","What would a pirate say dogs are known for?")]}):print(chunk)print("----")
```

```
{'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_17iLPWvOD23zqwd1QVQ00Y63', 'function': {'arguments': '{"question":"What are dogs known for according to pirates?","answer_style":"quote"}', 'name': 'pet_expert'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 28, 'prompt_tokens': 59, 'total_tokens': 87}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': None, 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-7fef44f3-7bba-4e63-8c51-2ad9c5e65e2e-0', tool_calls=[{'name': 'pet_expert', 'args': {'question': 'What are dogs known for according to pirates?', 'answer_style': 'quote'}, 'id': 'call_17iLPWvOD23zqwd1QVQ00Y63'}], usage_metadata={'input_tokens': 59, 'output_tokens': 28, 'total_tokens': 87})]}}----{'tools': {'messages': [ToolMessage(content='"Dogs are known for their loyalty and friendliness, making them great companions for pirates on long sea voyages."', name='pet_expert', tool_call_id='call_17iLPWvOD23zqwd1QVQ00Y63')]}}----{'agent': {'messages': [AIMessage(content='According to pirates, dogs are known for their loyalty and friendliness, making them great companions for pirates on long sea voyages.', response_metadata={'token_usage': {'completion_tokens': 27, 'prompt_tokens': 119, 'total_tokens': 146}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-5a30edc3-7be0-4743-b980-ca2f8cad9b8d-0', usage_metadata={'input_tokens': 119, 'output_tokens': 27, 'total_tokens': 146})]}}----
```

See LangSmith trace for the above run.
#### Was this page helpful?
  * Dependencies
  * Basic usage
  * In agents


