Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prompt templates help to translate user input and parameters into instructions for a language model. This can be used to guide a model's response, helping it understand the context and generate relevant and coherent language-based output.
Prompt Templates take as input a dictionary, where each key represents a variable in the prompt template to fill in.
Prompt Templates output a PromptValue. This PromptValue can be passed to an LLM or a ChatModel, and can also be cast to a string or a list of messages. The reason this PromptValue exists is to make it easy to switch between strings and messages.
There are a few different types of prompt templates:
## String PromptTemplates​
These prompt templates are used to format a single string, and generally are used for simpler inputs. For example, a common way to construct and use a PromptTemplate is as follows:
```
from langchain_core.prompts import PromptTemplateprompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")prompt_template.invoke({"topic":"cats"})
```

**API Reference:**PromptTemplate
## ChatPromptTemplates​
These prompt templates are used to format a list of messages. These "templates" consist of a list of templates themselves. For example, a common way to construct and use a ChatPromptTemplate is as follows:
```
from langchain_core.prompts import ChatPromptTemplateprompt_template = ChatPromptTemplate([("system","You are a helpful assistant"),("user","Tell me a joke about {topic}")])prompt_template.invoke({"topic":"cats"})
```

**API Reference:**ChatPromptTemplate
In the above example, this ChatPromptTemplate will construct two messages when called. The first is a system message, that has no variables to format. The second is a HumanMessage, and will be formatted by the `topic` variable the user passes in.
## MessagesPlaceholder​
This prompt template is responsible for adding a list of messages in a particular place. In the above ChatPromptTemplate, we saw how we could format two messages, each one a string. But what if we wanted the user to pass in a list of messages that we would slot into a particular spot? This is how you use MessagesPlaceholder.
```
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholderfrom langchain_core.messages import HumanMessageprompt_template = ChatPromptTemplate([("system","You are a helpful assistant"),  MessagesPlaceholder("msgs")])prompt_template.invoke({"msgs":[HumanMessage(content="hi!")]})
```

**API Reference:**ChatPromptTemplate | MessagesPlaceholder | HumanMessage
This will produce a list of two messages, the first one being a system message, and the second one being the HumanMessage we passed in. If we had passed in 5 messages, then it would have produced 6 messages in total (the system message plus the 5 passed in). This is useful for letting a list of messages be slotted into a particular spot.
An alternative way to accomplish the same thing without using the `MessagesPlaceholder` class explicitly is:
```
prompt_template = ChatPromptTemplate([("system","You are a helpful assistant"),("placeholder","{msgs}")# <-- This is the changed part])
```

For specifics on how to use prompt templates, see the relevant how-to guides here.
#### Was this page helpful?
  * String PromptTemplates
  * ChatPromptTemplates
  * MessagesPlaceholder


