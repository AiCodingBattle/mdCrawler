Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Callbacks


LangChain has some built-in callback handlers, but you will often want to create your own handlers with custom logic.
To create a custom callback handler, we need to determine the event(s) we want our callback handler to handle as well as what we want our callback handler to do when the event is triggered. Then all we need to do is attach the callback handler to the object, for example via the constructor or at runtime.
In the example below, we'll implement streaming with a custom handler.
In our custom callback handler `MyCustomHandler`, we implement the `on_llm_new_token` handler to print the token we have just received. We then attach our custom handler to the model object as a constructor callback.
```
from langchain_anthropic import ChatAnthropicfrom langchain_core.callbacks import BaseCallbackHandlerfrom langchain_core.prompts import ChatPromptTemplateclassMyCustomHandler(BaseCallbackHandler):defon_llm_new_token(self, token:str,**kwargs)->None:print(f"My custom handler, token: {token}")prompt = ChatPromptTemplate.from_messages(["Tell me a joke about {animal}"])# To enable streaming, we pass in `streaming=True` to the ChatModel constructor# Additionally, we pass in our custom handler as a list to the callbacks parametermodel = ChatAnthropic(  model="claude-3-sonnet-20240229", streaming=True, callbacks=[MyCustomHandler()])chain = prompt | modelresponse = chain.invoke({"animal":"bears"})
```

**API Reference:**ChatAnthropic | BaseCallbackHandler | ChatPromptTemplate
```
My custom handler, token: HereMy custom handler, token: 'sMy custom handler, token: aMy custom handler, token: bearMy custom handler, token: jokeMy custom handler, token: forMy custom handler, token: youMy custom handler, token: :My custom handler, token: WhyMy custom handler, token: diMy custom handler, token: d theMy custom handler, token: bearMy custom handler, token: dissolMy custom handler, token: veMy custom handler, token: inMy custom handler, token: waterMy custom handler, token: ?My custom handler, token: BecauseMy custom handler, token: itMy custom handler, token: wasMy custom handler, token: aMy custom handler, token: polarMy custom handler, token: bearMy custom handler, token: !
```

You can see this reference page for a list of events you can handle. Note that the `handle_chain_*` events run for most LCEL runnables.
## Next steps​
You've now learned how to create your own custom callback handlers.
Next, check out the other how-to guides in this section, such as how to attach callbacks to a runnable.
#### Was this page helpful?
  * Next steps


