Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
`LLMMathChain` enabled the evaluation of mathematical expressions generated by a LLM. Instructions for generating the expressions were formatted into the prompt, and the expressions were parsed out of the string response before evaluation using the numexpr library.
This is more naturally achieved via tool calling. We can equip a chat model with a simple calculator tool leveraging `numexpr` and construct a simple chain around it using LangGraph. Some advantages of this approach include:
  * Leverage tool-calling capabilities of chat models that have been fine-tuned for this purpose;
  * Reduce parsing errors from extracting expression from a string LLM response;
  * Delegation of instructions to message roles (e.g., chat models can understand what a `ToolMessage` represents without the need for additional prompting);
  * Support for streaming, both of individual tokens and chain steps.


```
%pip install --upgrade --quiet numexpr
```

```
import osfrom getpass import getpassif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()
```

## Legacy​
Details
```
from langchain.chains import LLMMathChainfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_openai import ChatOpenAIllm = ChatOpenAI(model="gpt-4o-mini")chain = LLMMathChain.from_llm(llm)chain.invoke("What is 551368 divided by 82?")
```

**API Reference:**LLMMathChain | ChatPromptTemplate | ChatOpenAI
```
{'question': 'What is 551368 divided by 82?', 'answer': 'Answer: 6724.0'}
```

## LangGraph​
Details
```
import mathfrom typing import Annotated, Sequenceimport numexprfrom langchain_core.messages import BaseMessagefrom langchain_core.runnables import RunnableConfigfrom langchain_core.tools import toolfrom langchain_openai import ChatOpenAIfrom langgraph.graph import END, StateGraphfrom langgraph.graph.message import add_messagesfrom langgraph.prebuilt.tool_node import ToolNodefrom typing_extensions import TypedDict@tooldefcalculator(expression:str)->str:"""Calculate expression using Python's numexpr library.  Expression should be a single line mathematical expression  that solves the problem.  Examples:    "37593 * 67" for "37593 times 67"    "37593**(1/5)" for "37593^(1/5)"  """  local_dict ={"pi": math.pi,"e": math.e}returnstr(    numexpr.evaluate(      expression.strip(),      global_dict={},# restrict access to globals      local_dict=local_dict,# add common mathematical functions))llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)tools =[calculator]llm_with_tools = llm.bind_tools(tools, tool_choice="any")classChainState(TypedDict):"""LangGraph state."""  messages: Annotated[Sequence[BaseMessage], add_messages]asyncdefacall_chain(state: ChainState, config: RunnableConfig):  last_message = state["messages"][-1]  response =await llm_with_tools.ainvoke(state["messages"], config)return{"messages":[response]}asyncdefacall_model(state: ChainState, config: RunnableConfig):  response =await llm.ainvoke(state["messages"], config)return{"messages":[response]}graph_builder = StateGraph(ChainState)graph_builder.add_node("call_tool", acall_chain)graph_builder.add_node("execute_tool", ToolNode(tools))graph_builder.add_node("call_model", acall_model)graph_builder.set_entry_point("call_tool")graph_builder.add_edge("call_tool","execute_tool")graph_builder.add_edge("execute_tool","call_model")graph_builder.add_edge("call_model", END)chain = graph_builder.compile()
```

**API Reference:**BaseMessage | RunnableConfig | tool | ChatOpenAI | StateGraph | add_messages | ToolNode
```
# Visualize chain:from IPython.display import ImageImage(chain.get_graph().draw_mermaid_png())
```

![](https://python.langchain.com/docs/versions/migrating_chains/llm_math_chain/)
```
# Stream chain steps:example_query ="What is 551368 divided by 82"events = chain.astream({"messages":[("user", example_query)]},  stream_mode="values",)asyncfor event in events:  event["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================What is 551368 divided by 82==================================[1m Ai Message [0m==================================Tool Calls: calculator (call_1ic3gjuII0Aq9vxlSYiwvjSb) Call ID: call_1ic3gjuII0Aq9vxlSYiwvjSb Args:  expression: 551368 / 82=================================[1m Tool Message [0m=================================Name: calculator6724.0==================================[1m Ai Message [0m==================================551368 divided by 82 equals 6724.
```

## Next steps​
See guides for building and working with tools here.
Check out the LangGraph documentation for detail on building with LangGraph.
#### Was this page helpful?
  * Legacy
  * LangGraph
  * Next steps


