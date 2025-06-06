Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
A key feature of chatbots is their ability to use the content of previous conversational turns as context. This state management can take several forms, including:
  * Simply stuffing previous messages into a chat model prompt.
  * The above, but trimming old messages to reduce the amount of distracting information the model has to deal with.
  * More complex modifications like synthesizing summaries for long running conversations.


We'll go into more detail on a few techniques below!
note
This how-to guide previously built a chatbot using RunnableWithMessageHistory. You can access this version of the guide in the v0.2 docs.
As of the v0.3 release of LangChain, we recommend that LangChain users take advantage of LangGraph persistence to incorporate `memory` into new LangChain applications.
If your code is already relying on `RunnableWithMessageHistory` or `BaseChatMessageHistory`, you do **not** need to make any changes. We do not plan on deprecating this functionality in the near future as it works for simple chat applications and any code that uses `RunnableWithMessageHistory` will continue to work as expected.
Please see How to migrate to LangGraph Memory for more details.
## Setup​
You'll need to install a few packages, and have your OpenAI API key set as an environment variable named `OPENAI_API_KEY`:
```
%pip install --upgrade --quiet langchain langchain-openai langgraphimport getpassimport osifnot os.environ.get("OPENAI_API_KEY"):  os.environ["OPENAI_API_KEY"]= getpass.getpass("OpenAI API Key:")
```

```
OpenAI API Key: ········
```

Let's also set up a chat model that we'll use for the below examples.
```
from langchain_openai import ChatOpenAImodel = ChatOpenAI(model="gpt-4o-mini")
```

**API Reference:**ChatOpenAI
## Message passing​
The simplest form of memory is simply passing chat history messages into a chain. Here's an example:
```
from langchain_core.messages import AIMessage, HumanMessage, SystemMessagefrom langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholderprompt = ChatPromptTemplate.from_messages([    SystemMessage(      content="You are a helpful assistant. Answer all questions to the best of your ability."),    MessagesPlaceholder(variable_name="messages"),])chain = prompt | modelai_msg = chain.invoke({"messages":[      HumanMessage(        content="Translate from English to French: I love programming."),      AIMessage(content="J'adore la programmation."),      HumanMessage(content="What did you just say?"),],})print(ai_msg.content)
```

**API Reference:**AIMessage | HumanMessage | SystemMessage | ChatPromptTemplate | MessagesPlaceholder
```
I said, "I love programming" in French: "J'adore la programmation."
```

We can see that by passing the previous conversation into a chain, it can use it as context to answer questions. This is the basic concept underpinning chatbot memory - the rest of the guide will demonstrate convenient techniques for passing or reformatting messages.
## Automatic history management​
The previous examples pass messages to the chain (and model) explicitly. This is a completely acceptable approach, but it does require external management of new messages. LangChain also provides a way to build applications that have memory using LangGraph's persistence. You can enable persistence in LangGraph applications by providing a `checkpointer` when compiling the graph.
```
from langgraph.checkpoint.memory import MemorySaverfrom langgraph.graph import START, MessagesState, StateGraphworkflow = StateGraph(state_schema=MessagesState)# Define the function that calls the modeldefcall_model(state: MessagesState):  system_prompt =("You are a helpful assistant. ""Answer all questions to the best of your ability.")  messages =[SystemMessage(content=system_prompt)]+ state["messages"]  response = model.invoke(messages)return{"messages": response}# Define the node and edgeworkflow.add_node("model", call_model)workflow.add_edge(START,"model")# Add simple in-memory checkpointermemory = MemorySaver()app = workflow.compile(checkpointer=memory)
```

**API Reference:**MemorySaver | StateGraph
We'll pass the latest input to the conversation here and let LangGraph keep track of the conversation history using the checkpointer:
```
app.invoke({"messages":[HumanMessage(content="Translate to French: I love programming.")]},  config={"configurable":{"thread_id":"1"}},)
```

```
{'messages': [HumanMessage(content='Translate to French: I love programming.', additional_kwargs={}, response_metadata={}, id='be5e7099-3149-4293-af49-6b36c8ccd71b'), AIMessage(content="J'aime programmer.", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 4, 'prompt_tokens': 35, 'total_tokens': 39, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_e9627b5346', 'finish_reason': 'stop', 'logprobs': None}, id='run-8a753d7a-b97b-4d01-a661-626be6f41b38-0', usage_metadata={'input_tokens': 35, 'output_tokens': 4, 'total_tokens': 39})]}
```

```
app.invoke({"messages":[HumanMessage(content="What did I just ask you?")]},  config={"configurable":{"thread_id":"1"}},)
```

```
{'messages': [HumanMessage(content='Translate to French: I love programming.', additional_kwargs={}, response_metadata={}, id='be5e7099-3149-4293-af49-6b36c8ccd71b'), AIMessage(content="J'aime programmer.", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 4, 'prompt_tokens': 35, 'total_tokens': 39, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_e9627b5346', 'finish_reason': 'stop', 'logprobs': None}, id='run-8a753d7a-b97b-4d01-a661-626be6f41b38-0', usage_metadata={'input_tokens': 35, 'output_tokens': 4, 'total_tokens': 39}), HumanMessage(content='What did I just ask you?', additional_kwargs={}, response_metadata={}, id='c667529b-7c41-4cc0-9326-0af47328b816'), AIMessage(content='You asked me to translate "I love programming" into French.', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 13, 'prompt_tokens': 54, 'total_tokens': 67, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_1bb46167f9', 'finish_reason': 'stop', 'logprobs': None}, id='run-134a7ea0-d3a4-4923-bd58-25e5a43f6a1f-0', usage_metadata={'input_tokens': 54, 'output_tokens': 13, 'total_tokens': 67})]}
```

## Modifying chat history​
Modifying stored chat messages can help your chatbot handle a variety of situations. Here are some examples:
### Trimming messages​
LLMs and chat models have limited context windows, and even if you're not directly hitting limits, you may want to limit the amount of distraction the model has to deal with. One solution is trim the history messages before passing them to the model. Let's use an example history with the `app` we declared above:
```
demo_ephemeral_chat_history =[  HumanMessage(content="Hey there! I'm Nemo."),  AIMessage(content="Hello!"),  HumanMessage(content="How are you today?"),  AIMessage(content="Fine thanks!"),]app.invoke({"messages": demo_ephemeral_chat_history+[HumanMessage(content="What's my name?")]},  config={"configurable":{"thread_id":"2"}},)
```

```
{'messages': [HumanMessage(content="Hey there! I'm Nemo.", additional_kwargs={}, response_metadata={}, id='6b4cab70-ce18-49b0-bb06-267bde44e037'), AIMessage(content='Hello!', additional_kwargs={}, response_metadata={}, id='ba3714f4-8876-440b-a651-efdcab2fcb4c'), HumanMessage(content='How are you today?', additional_kwargs={}, response_metadata={}, id='08d032c0-1577-4862-a3f2-5c1b90687e21'), AIMessage(content='Fine thanks!', additional_kwargs={}, response_metadata={}, id='21790e16-db05-4537-9a6b-ecad0fcec436'), HumanMessage(content="What's my name?", additional_kwargs={}, response_metadata={}, id='c933eca3-5fd8-4651-af16-20fe2d49c216'), AIMessage(content='Your name is Nemo.', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 5, 'prompt_tokens': 63, 'total_tokens': 68, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_1bb46167f9', 'finish_reason': 'stop', 'logprobs': None}, id='run-a0b21acc-9dbb-4fb6-a953-392020f37d88-0', usage_metadata={'input_tokens': 63, 'output_tokens': 5, 'total_tokens': 68})]}
```

We can see the app remembers the preloaded name.
But let's say we have a very small context window, and we want to trim the number of messages passed to the model to only the 2 most recent ones. We can use the built in trim_messages util to trim messages based on their token count before they reach our prompt. In this case we'll count each message as 1 "token" and keep only the last two messages:
```
from langchain_core.messages import trim_messagesfrom langgraph.checkpoint.memory import MemorySaverfrom langgraph.graph import START, MessagesState, StateGraph# Define trimmer# count each message as 1 "token" (token_counter=len) and keep only the last two messagestrimmer = trim_messages(strategy="last", max_tokens=2, token_counter=len)workflow = StateGraph(state_schema=MessagesState)# Define the function that calls the modeldefcall_model(state: MessagesState):  trimmed_messages = trimmer.invoke(state["messages"])  system_prompt =("You are a helpful assistant. ""Answer all questions to the best of your ability.")  messages =[SystemMessage(content=system_prompt)]+ trimmed_messages  response = model.invoke(messages)return{"messages": response}# Define the node and edgeworkflow.add_node("model", call_model)workflow.add_edge(START,"model")# Add simple in-memory checkpointermemory = MemorySaver()app = workflow.compile(checkpointer=memory)
```

**API Reference:**trim_messages | MemorySaver | StateGraph
Let's call this new app and check the response
```
app.invoke({"messages": demo_ephemeral_chat_history+[HumanMessage(content="What is my name?")]},  config={"configurable":{"thread_id":"3"}},)
```

```
{'messages': [HumanMessage(content="Hey there! I'm Nemo.", additional_kwargs={}, response_metadata={}, id='6b4cab70-ce18-49b0-bb06-267bde44e037'), AIMessage(content='Hello!', additional_kwargs={}, response_metadata={}, id='ba3714f4-8876-440b-a651-efdcab2fcb4c'), HumanMessage(content='How are you today?', additional_kwargs={}, response_metadata={}, id='08d032c0-1577-4862-a3f2-5c1b90687e21'), AIMessage(content='Fine thanks!', additional_kwargs={}, response_metadata={}, id='21790e16-db05-4537-9a6b-ecad0fcec436'), HumanMessage(content='What is my name?', additional_kwargs={}, response_metadata={}, id='a22ab7c5-8617-4821-b3e9-a9e7dca1ff78'), AIMessage(content="I'm sorry, but I don't have access to personal information about you unless you share it with me. How can I assist you today?", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 27, 'prompt_tokens': 39, 'total_tokens': 66, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_1bb46167f9', 'finish_reason': 'stop', 'logprobs': None}, id='run-f7b32d72-9f57-4705-be7e-43bf1c3d293b-0', usage_metadata={'input_tokens': 39, 'output_tokens': 27, 'total_tokens': 66})]}
```

We can see that `trim_messages` was called and only the two most recent messages will be passed to the model. In this case, this means that the model forgot the name we gave it.
Check out our how to guide on trimming messages for more.
### Summary memory​
We can use this same pattern in other ways too. For example, we could use an additional LLM call to generate a summary of the conversation before calling our app. Let's recreate our chat history:
```
demo_ephemeral_chat_history =[  HumanMessage(content="Hey there! I'm Nemo."),  AIMessage(content="Hello!"),  HumanMessage(content="How are you today?"),  AIMessage(content="Fine thanks!"),]
```

And now, let's update the model-calling function to distill previous interactions into a summary:
```
from langchain_core.messages import HumanMessage, RemoveMessagefrom langgraph.checkpoint.memory import MemorySaverfrom langgraph.graph import START, MessagesState, StateGraphworkflow = StateGraph(state_schema=MessagesState)# Define the function that calls the modeldefcall_model(state: MessagesState):  system_prompt =("You are a helpful assistant. ""Answer all questions to the best of your ability. ""The provided chat history includes a summary of the earlier conversation.")  system_message = SystemMessage(content=system_prompt)  message_history = state["messages"][:-1]# exclude the most recent user input# Summarize the messages if the chat history reaches a certain sizeiflen(message_history)>=4:    last_human_message = state["messages"][-1]# Invoke the model to generate conversation summary    summary_prompt =("Distill the above chat messages into a single summary message. ""Include as many specific details as you can.")    summary_message = model.invoke(      message_history +[HumanMessage(content=summary_prompt)])# Delete messages that we no longer want to show up    delete_messages =[RemoveMessage(id=m.id)for m in state["messages"]]# Re-add user message    human_message = HumanMessage(content=last_human_message.content)# Call the model with summary & response    response = model.invoke([system_message, summary_message, human_message])    message_updates =[summary_message, human_message, response]+ delete_messageselse:    message_updates = model.invoke([system_message]+ state["messages"])return{"messages": message_updates}# Define the node and edgeworkflow.add_node("model", call_model)workflow.add_edge(START,"model")# Add simple in-memory checkpointermemory = MemorySaver()app = workflow.compile(checkpointer=memory)
```

**API Reference:**HumanMessage | RemoveMessage | MemorySaver | StateGraph
Let's see if it remembers the name we gave it:
```
app.invoke({"messages": demo_ephemeral_chat_history+[HumanMessage("What did I say my name was?")]},  config={"configurable":{"thread_id":"4"}},)
```

```
{'messages': [AIMessage(content="Nemo greeted me, and I responded positively, indicating that I'm doing well.", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 16, 'prompt_tokens': 60, 'total_tokens': 76, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_1bb46167f9', 'finish_reason': 'stop', 'logprobs': None}, id='run-ee42f98d-907d-4bad-8f16-af2db789701d-0', usage_metadata={'input_tokens': 60, 'output_tokens': 16, 'total_tokens': 76}), HumanMessage(content='What did I say my name was?', additional_kwargs={}, response_metadata={}, id='788555ea-5b1f-4c29-a2f2-a92f15d147be'), AIMessage(content='You mentioned that your name is Nemo.', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 8, 'prompt_tokens': 67, 'total_tokens': 75, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_1bb46167f9', 'finish_reason': 'stop', 'logprobs': None}, id='run-099a43bd-a284-4969-bb6f-0be486614cd8-0', usage_metadata={'input_tokens': 67, 'output_tokens': 8, 'total_tokens': 75})]}
```

Note that invoking the app again will keep accumulating the history until it reaches the specified number of messages (four in our case). At that point we will generate another summary generated from the initial summary plus new messages and so on.
#### Was this page helpful?
  * Setup
  * Message passing
  * Automatic history management
  * Modifying chat history
    * Trimming messages
    * Summary memory


