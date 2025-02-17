Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
The quality of extractions can often be improved by providing reference examples to the LLM.
Data extraction attempts to generate structured representations of information found in text and other unstructured or semi-structured formats. Tool-calling LLM features are often used in this context. This guide demonstrates how to build few-shot examples of tool calls to help steer the behavior of extraction and similar applications.
tip
While this guide focuses how to use examples with a tool calling model, this technique is generally applicable, and will work also with JSON more or prompt based techniques.
LangChain implements a tool-call attribute on messages from LLMs that include tool calls. See our how-to guide on tool calling for more detail. To build reference examples for data extraction, we build a chat history containing a sequence of:
  * HumanMessage containing example inputs;
  * AIMessage containing example tool calls;
  * ToolMessage containing example tool outputs.


LangChain adopts this convention for structuring tool calls into conversation across LLM model providers.
First we build a prompt template that includes a placeholder for these messages:
```
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder# Define a custom prompt to provide instructions and any additional context.# 1) You can add examples into the prompt template to improve extraction quality# 2) Introduce additional parameters to take context into account (e.g., include metadata#  about the document from which the text was extracted.)prompt = ChatPromptTemplate.from_messages([("system","You are an expert extraction algorithm. ""Only extract relevant information from the text. ""If you do not know the value of an attribute asked ""to extract, return null for the attribute's value.",),# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓    MessagesPlaceholder("examples"),# <-- EXAMPLES!# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑("human","{text}"),])
```

**API Reference:**ChatPromptTemplate | MessagesPlaceholder
Test out the template:
```
from langchain_core.messages import(  HumanMessage,)prompt.invoke({"text":"this is some text","examples":[HumanMessage(content="testing 1 2 3")]})
```

**API Reference:**HumanMessage
```
ChatPromptValue(messages=[SystemMessage(content="You are an expert extraction algorithm. Only extract relevant information from the text. If you do not know the value of an attribute asked to extract, return null for the attribute's value.", additional_kwargs={}, response_metadata={}), HumanMessage(content='testing 1 2 3', additional_kwargs={}, response_metadata={}), HumanMessage(content='this is some text', additional_kwargs={}, response_metadata={})])
```

## Define the schema​
Let's re-use the person schema from the extraction tutorial.
```
from typing import List, Optionalfrom langchain_openai import ChatOpenAIfrom pydantic import BaseModel, FieldclassPerson(BaseModel):"""Information about a person."""# ^ Doc-string for the entity Person.# This doc-string is sent to the LLM as the description of the schema Person,# and it can help to improve extraction results.# Note that:# 1. Each field is an `optional` -- this allows the model to decline to extract it!# 2. Each field has a `description` -- this description is used by the LLM.# Having a good description can help improve extraction results.  name: Optional[str]= Field(..., description="The name of the person")  hair_color: Optional[str]= Field(..., description="The color of the person's hair if known")  height_in_meters: Optional[str]= Field(..., description="Height in METERs")classData(BaseModel):"""Extracted data about people."""# Creates a model so that we can extract multiple entities.  people: List[Person]
```

**API Reference:**ChatOpenAI
## Define reference examples​
Examples can be defined as a list of input-output pairs.
Each example contains an example `input` text and an example `output` showing what should be extracted from the text.
important
This is a bit in the weeds, so feel free to skip.
The format of the example needs to match the API used (e.g., tool calling or JSON mode etc.).
Here, the formatted examples will match the format expected for the tool calling API since that's what we're using.
```
import uuidfrom typing import Dict, List, TypedDictfrom langchain_core.messages import(  AIMessage,  BaseMessage,  HumanMessage,  SystemMessage,  ToolMessage,)from pydantic import BaseModel, FieldclassExample(TypedDict):"""A representation of an example consisting of text input and expected tool calls.  For extraction, the tool calls are represented as instances of pydantic model.  """input:str# This is the example text  tool_calls: List[BaseModel]# Instances of pydantic model that should be extracteddeftool_example_to_messages(example: Example)-> List[BaseMessage]:"""Convert an example into a list of messages that can be fed into an LLM.  This code is an adapter that converts our example to a list of messages  that can be fed into a chat model.  The list of messages per example corresponds to:  1) HumanMessage: contains the content from which content should be extracted.  2) AIMessage: contains the extracted information from the model  3) ToolMessage: contains confirmation to the model that the model requested a tool correctly.  The ToolMessage is required because some of the chat models are hyper-optimized for agents  rather than for an extraction use case.  """  messages: List[BaseMessage]=[HumanMessage(content=example["input"])]  tool_calls =[]for tool_call in example["tool_calls"]:    tool_calls.append({"id":str(uuid.uuid4()),"args": tool_call.dict(),# The name of the function right now corresponds# to the name of the pydantic model# This is implicit in the API right now,# and will be improved over time."name": tool_call.__class__.__name__,},)  messages.append(AIMessage(content="", tool_calls=tool_calls))  tool_outputs = example.get("tool_outputs")or["You have correctly called this tool."]*len(tool_calls)for output, tool_call inzip(tool_outputs, tool_calls):    messages.append(ToolMessage(content=output, tool_call_id=tool_call["id"]))return messages
```

**API Reference:**AIMessage | BaseMessage | HumanMessage | SystemMessage | ToolMessage
Next let's define our examples and then convert them into message format.
```
examples =[("The ocean is vast and blue. It's more than 20,000 feet deep. There are many fish in it.",    Data(people=[]),),("Fiona traveled far from France to Spain.",    Data(people=[Person(name="Fiona", height_in_meters=None, hair_color=None)]),),]messages =[]for text, tool_call in examples:  messages.extend(    tool_example_to_messages({"input": text,"tool_calls":[tool_call]}))
```

Let's test out the prompt
```
example_prompt = prompt.invoke({"text":"this is some text","examples": messages})for message in example_prompt.messages:print(f"{message.type}: {message}")
```

```
system: content="You are an expert extraction algorithm. Only extract relevant information from the text. If you do not know the value of an attribute asked to extract, return null for the attribute's value." additional_kwargs={} response_metadata={}human: content="The ocean is vast and blue. It's more than 20,000 feet deep. There are many fish in it." additional_kwargs={} response_metadata={}ai: content='' additional_kwargs={} response_metadata={} tool_calls=[{'name': 'Data', 'args': {'people': []}, 'id': '240159b1-1405-4107-a07c-3c6b91b3d5b7', 'type': 'tool_call'}]tool: content='You have correctly called this tool.' tool_call_id='240159b1-1405-4107-a07c-3c6b91b3d5b7'human: content='Fiona traveled far from France to Spain.' additional_kwargs={} response_metadata={}ai: content='' additional_kwargs={} response_metadata={} tool_calls=[{'name': 'Data', 'args': {'people': [{'name': 'Fiona', 'hair_color': None, 'height_in_meters': None}]}, 'id': '3fc521e4-d1d2-4c20-bf40-e3d72f1068da', 'type': 'tool_call'}]tool: content='You have correctly called this tool.' tool_call_id='3fc521e4-d1d2-4c20-bf40-e3d72f1068da'human: content='this is some text' additional_kwargs={} response_metadata={}
```

## Create an extractor​
Let's select an LLM. Because we are using tool-calling, we will need a model that supports a tool-calling feature. See this table for available LLMs.
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

Following the extraction tutorial, we use the `.with_structured_output` method to structure model outputs according to the desired schema:
```
runnable = prompt | llm.with_structured_output(  schema=Data,  method="function_calling",  include_raw=False,)
```

## Without examples 😿​
Notice that even capable models can fail with a **very simple** test case!
```
for _ inrange(5):  text ="The solar system is large, but earth has only 1 moon."print(runnable.invoke({"text": text,"examples":[]}))
```

```
people=[Person(name='earth', hair_color='null', height_in_meters='null')]``````outputpeople=[Person(name='earth', hair_color='null', height_in_meters='null')]``````outputpeople=[]``````outputpeople=[Person(name='earth', hair_color='null', height_in_meters='null')]``````outputpeople=[]
```

## With examples 😻​
Reference examples helps to fix the failure!
```
for _ inrange(5):  text ="The solar system is large, but earth has only 1 moon."print(runnable.invoke({"text": text,"examples": messages}))
```

```
people=[]``````outputpeople=[]``````outputpeople=[]``````outputpeople=[]``````outputpeople=[]
```

Note that we can see the few-shot examples as tool-calls in the Langsmith trace.
And we retain performance on a positive sample:
```
runnable.invoke({"text":"My name is Harrison. My hair is black.","examples": messages,})
```

```
Data(people=[Person(name='Harrison', hair_color='black', height_in_meters=None)])
```

#### Was this page helpful?
  * Define the schema
  * Define reference examples
  * Create an extractor
  * Without examples 😿
  * With examples 😻


