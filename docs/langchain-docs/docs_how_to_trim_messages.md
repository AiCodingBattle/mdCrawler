Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Messages
  * Chat models
  * Chaining
  * Chat history


The methods in this guide also require `langchain-core>=0.2.9`.
All models have finite context windows, meaning there's a limit to how many tokens they can take as input. If you have very long messages or a chain/agent that accumulates a long message history, you'll need to manage the length of the messages you're passing in to the model.
trim_messages can be used to reduce the size of a chat history to a specified token count or specified message count.
If passing the trimmed chat history back into a chat model directly, the trimmed chat history should satisfy the following properties:
  1. The resulting chat history should be **valid**. Usually this means that the following properties should be satisfied: 
     * The chat history **starts** with either (1) a `HumanMessage` or (2) a SystemMessage followed by a `HumanMessage`.
     * The chat history **ends** with either a `HumanMessage` or a `ToolMessage`.
     * A `ToolMessage` can only appear after an `AIMessage` that involved a tool call. This can be achieved by setting `start_on="human"` and `ends_on=("human", "tool")`.
  2. It includes recent messages and drops old messages in the chat history. This can be achieved by setting `strategy="last"`.
  3. Usually, the new chat history should include the `SystemMessage` if it was present in the original chat history since the `SystemMessage` includes special instructions to the chat model. The `SystemMessage` is almost always the first message in the history if present. This can be achieved by setting `include_system=True`.


## Trimming based on token count​
Here, we'll trim the chat history based on token count. The trimmed chat history will produce a **valid** chat history that includes the `SystemMessage`.
To keep the most recent messages, we set `strategy="last"`. We'll also set `include_system=True` to include the `SystemMessage`, and `start_on="human"` to make sure the resulting chat history is valid.
This is a good default configuration when using `trim_messages` based on token count. Remember to adjust `token_counter` and `max_tokens` for your use case.
Notice that for our `token_counter` we can pass in a function (more on that below) or a language model (since language models have a message token counting method). It makes sense to pass in a model when you're trimming your messages to fit into the context window of that specific model:
```
pip install -qU langchain-openai
```

```
Note: you may need to restart the kernel to use updated packages.
```

```
from langchain_core.messages import(  AIMessage,  HumanMessage,  SystemMessage,  ToolMessage,  trim_messages,)from langchain_openai import ChatOpenAImessages =[  SystemMessage("you're a good assistant, you always respond with a joke."),  HumanMessage("i wonder why it's called langchain"),  AIMessage('Well, I guess they thought "WordRope" and "SentenceString" just didn\'t have the same ring to it!'),  HumanMessage("and who is harrison chasing anyways"),  AIMessage("Hmmm let me think.\n\nWhy, he's probably chasing after the last cup of coffee in the office!"),  HumanMessage("what do you call a speechless parrot"),]trim_messages(  messages,# Keep the last <= n_count tokens of the messages.  strategy="last",# Remember to adjust based on your model# or else pass a custom token_encoder  token_counter=ChatOpenAI(model="gpt-4o"),# Most chat models expect that chat history starts with either:# (1) a HumanMessage or# (2) a SystemMessage followed by a HumanMessage# Remember to adjust based on the desired conversation# length  max_tokens=45,# Most chat models expect that chat history starts with either:# (1) a HumanMessage or# (2) a SystemMessage followed by a HumanMessage  start_on="human",# Most chat models expect that chat history ends with either:# (1) a HumanMessage or# (2) a ToolMessage  end_on=("human","tool"),# Usually, we want to keep the SystemMessage# if it's present in the original history.# The SystemMessage has special instructions for the model.  include_system=True,  allow_partial=False,)
```

**API Reference:**AIMessage | HumanMessage | SystemMessage | ToolMessage | trim_messages | ChatOpenAI
```
[SystemMessage(content="you're a good assistant, you always respond with a joke.", additional_kwargs={}, response_metadata={}), HumanMessage(content='what do you call a speechless parrot', additional_kwargs={}, response_metadata={})]
```

## Trimming based on message count​
Alternatively, we can trim the chat history based on **message count** , by setting `token_counter=len`. In this case, each message will count as a single token, and `max_tokens` will control the maximum number of messages.
This is a good default configuration when using `trim_messages` based on message count. Remember to adjust `max_tokens` for your use case.
```
trim_messages(  messages,# Keep the last <= n_count tokens of the messages.  strategy="last",  token_counter=len,# When token_counter=len, each message# will be counted as a single token.# Remember to adjust for your use case  max_tokens=5,# Most chat models expect that chat history starts with either:# (1) a HumanMessage or# (2) a SystemMessage followed by a HumanMessage  start_on="human",# Most chat models expect that chat history ends with either:# (1) a HumanMessage or# (2) a ToolMessage  end_on=("human","tool"),# Usually, we want to keep the SystemMessage# if it's present in the original history.# The SystemMessage has special instructions for the model.  include_system=True,)
```

```
[SystemMessage(content="you're a good assistant, you always respond with a joke.", additional_kwargs={}, response_metadata={}), HumanMessage(content='and who is harrison chasing anyways', additional_kwargs={}, response_metadata={}), AIMessage(content="Hmmm let me think.\n\nWhy, he's probably chasing after the last cup of coffee in the office!", additional_kwargs={}, response_metadata={}), HumanMessage(content='what do you call a speechless parrot', additional_kwargs={}, response_metadata={})]
```

## Advanced Usage​
You can use `trim_message` as a building-block to create more complex processing logic.
If we want to allow splitting up the contents of a message we can specify `allow_partial=True`:
```
trim_messages(  messages,  max_tokens=56,  strategy="last",  token_counter=ChatOpenAI(model="gpt-4o"),  include_system=True,  allow_partial=True,)
```

```
[SystemMessage(content="you're a good assistant, you always respond with a joke.", additional_kwargs={}, response_metadata={}), AIMessage(content="\nWhy, he's probably chasing after the last cup of coffee in the office!", additional_kwargs={}, response_metadata={}), HumanMessage(content='what do you call a speechless parrot', additional_kwargs={}, response_metadata={})]
```

By default, the `SystemMessage` will not be included, so you can drop it by either setting `include_system=False` or by dropping the `include_system` argument.
```
trim_messages(  messages,  max_tokens=45,  strategy="last",  token_counter=ChatOpenAI(model="gpt-4o"),)
```

```
[AIMessage(content="Hmmm let me think.\n\nWhy, he's probably chasing after the last cup of coffee in the office!", additional_kwargs={}, response_metadata={}), HumanMessage(content='what do you call a speechless parrot', additional_kwargs={}, response_metadata={})]
```

We can perform the flipped operation of getting the _first_ `max_tokens` by specifying `strategy="first"`:
```
trim_messages(  messages,  max_tokens=45,  strategy="first",  token_counter=ChatOpenAI(model="gpt-4o"),)
```

```
[SystemMessage(content="you're a good assistant, you always respond with a joke.", additional_kwargs={}, response_metadata={}), HumanMessage(content="i wonder why it's called langchain", additional_kwargs={}, response_metadata={})]
```

## Writing a custom token counter​
We can write a custom token counter function that takes in a list of messages and returns an int.
```
pip install -qU tiktoken
```

```
Note: you may need to restart the kernel to use updated packages.
```

```
from typing import Listimport tiktokenfrom langchain_core.messages import BaseMessage, ToolMessagedefstr_token_counter(text:str)->int:  enc = tiktoken.get_encoding("o200k_base")returnlen(enc.encode(text))deftiktoken_counter(messages: List[BaseMessage])->int:"""Approximately reproduce https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb  For simplicity only supports str Message.contents.  """  num_tokens =3# every reply is primed with <|start|>assistant<|message|>  tokens_per_message =3  tokens_per_name =1for msg in messages:ifisinstance(msg, HumanMessage):      role ="user"elifisinstance(msg, AIMessage):      role ="assistant"elifisinstance(msg, ToolMessage):      role ="tool"elifisinstance(msg, SystemMessage):      role ="system"else:raise ValueError(f"Unsupported messages type {msg.__class__}")    num_tokens +=(      tokens_per_message+ str_token_counter(role)+ str_token_counter(msg.content))if msg.name:      num_tokens += tokens_per_name + str_token_counter(msg.name)return num_tokenstrim_messages(  messages,  token_counter=tiktoken_counter,# Keep the last <= n_count tokens of the messages.  strategy="last",# When token_counter=len, each message# will be counted as a single token.# Remember to adjust for your use case  max_tokens=45,# Most chat models expect that chat history starts with either:# (1) a HumanMessage or# (2) a SystemMessage followed by a HumanMessage  start_on="human",# Most chat models expect that chat history ends with either:# (1) a HumanMessage or# (2) a ToolMessage  end_on=("human","tool"),# Usually, we want to keep the SystemMessage# if it's present in the original history.# The SystemMessage has special instructions for the model.  include_system=True,)
```

**API Reference:**BaseMessage | ToolMessage
```
[SystemMessage(content="you're a good assistant, you always respond with a joke.", additional_kwargs={}, response_metadata={}), HumanMessage(content='what do you call a speechless parrot', additional_kwargs={}, response_metadata={})]
```

## Chaining​
`trim_messages` can be used imperatively (like above) or declaratively, making it easy to compose with other components in a chain
```
llm = ChatOpenAI(model="gpt-4o")# Notice we don't pass in messages. This creates# a RunnableLambda that takes messages as inputtrimmer = trim_messages(  token_counter=llm,# Keep the last <= n_count tokens of the messages.  strategy="last",# When token_counter=len, each message# will be counted as a single token.# Remember to adjust for your use case  max_tokens=45,# Most chat models expect that chat history starts with either:# (1) a HumanMessage or# (2) a SystemMessage followed by a HumanMessage  start_on="human",# Most chat models expect that chat history ends with either:# (1) a HumanMessage or# (2) a ToolMessage  end_on=("human","tool"),# Usually, we want to keep the SystemMessage# if it's present in the original history.# The SystemMessage has special instructions for the model.  include_system=True,)chain = trimmer | llmchain.invoke(messages)
```

```
AIMessage(content='A polygon! Because it\'s a "poly-gone" quiet!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 13, 'prompt_tokens': 32, 'total_tokens': 45, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_057232b607', 'finish_reason': 'stop', 'logprobs': None}, id='run-4fa026e7-9137-4fef-b596-54243615e3b3-0', usage_metadata={'input_tokens': 32, 'output_tokens': 13, 'total_tokens': 45})
```

Looking at the LangSmith trace we can see that before the messages are passed to the model they are first trimmed: https://smith.langchain.com/public/65af12c4-c24d-4824-90f0-6547566e59bb/r
Looking at just the trimmer, we can see that it's a Runnable object that can be invoked like all Runnables:
```
trimmer.invoke(messages)
```

```
[SystemMessage(content="you're a good assistant, you always respond with a joke.", additional_kwargs={}, response_metadata={}), HumanMessage(content='what do you call a speechless parrot', additional_kwargs={}, response_metadata={})]
```

## Using with ChatMessageHistory​
Trimming messages is especially useful when working with chat histories, which can get arbitrarily long:
```
from langchain_core.chat_history import InMemoryChatMessageHistoryfrom langchain_core.runnables.history import RunnableWithMessageHistorychat_history = InMemoryChatMessageHistory(messages=messages[:-1])defdummy_get_session_history(session_id):if session_id !="1":return InMemoryChatMessageHistory()return chat_historyllm = ChatOpenAI(model="gpt-4o")trimmer = trim_messages(  max_tokens=45,  strategy="last",  token_counter=llm,# Usually, we want to keep the SystemMessage# if it's present in the original history.# The SystemMessage has special instructions for the model.  include_system=True,# Most chat models expect that chat history starts with either:# (1) a HumanMessage or# (2) a SystemMessage followed by a HumanMessage# start_on="human" makes sure we produce a valid chat history  start_on="human",)chain = trimmer | llmchain_with_history = RunnableWithMessageHistory(chain, dummy_get_session_history)chain_with_history.invoke([HumanMessage("what do you call a speechless parrot")],  config={"configurable":{"session_id":"1"}},)
```

**API Reference:**InMemoryChatMessageHistory | RunnableWithMessageHistory
```
AIMessage(content='A "polygon"!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 4, 'prompt_tokens': 32, 'total_tokens': 36, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_c17d3befe7', 'finish_reason': 'stop', 'logprobs': None}, id='run-71d9fce6-bb0c-4bb3-acc8-d5eaee6ae7bc-0', usage_metadata={'input_tokens': 32, 'output_tokens': 4, 'total_tokens': 36})
```

Looking at the LangSmith trace we can see that we retrieve all of our messages but before the messages are passed to the model they are trimmed to be just the system message and last human message: https://smith.langchain.com/public/17dd700b-9994-44ca-930c-116e00997315/r
## API reference​
For a complete description of all arguments head to the API reference: https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.trim_messages.html
#### Was this page helpful?
  * Trimming based on token count
  * Trimming based on message count
  * Advanced Usage
  * Writing a custom token counter
  * Chaining
  * Using with ChatMessageHistory
  * API reference


