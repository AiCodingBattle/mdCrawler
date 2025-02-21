Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * LangChain Tools
  * LangChain Toolkits


## Tools​
LangChain has a large collection of 3rd party tools. Please visit Tool Integrations for a list of the available tools.
important
When using 3rd party tools, make sure that you understand how the tool works, what permissions it has. Read over its documentation and check if anything is required from you from a security point of view. Please see our security guidelines for more information.
Let's try out the Wikipedia integration.
```
!pip install -qU langchain-community wikipedia
```

```
from langchain_community.tools import WikipediaQueryRunfrom langchain_community.utilities import WikipediaAPIWrapperapi_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)tool = WikipediaQueryRun(api_wrapper=api_wrapper)print(tool.invoke({"query":"langchain"}))
```

**API Reference:**WikipediaQueryRun | WikipediaAPIWrapper
```
Page: LangChainSummary: LangChain is a framework designed to simplify the creation of applications
```

The tool has the following defaults associated with it:
```
print(f"Name: {tool.name}")print(f"Description: {tool.description}")print(f"args schema: {tool.args}")print(f"returns directly?: {tool.return_direct}")
```

```
Name: wikipediaDescription: A wrapper around Wikipedia. Useful for when you need to answer general questions about people, places, companies, facts, historical events, or other subjects. Input should be a search query.args schema: {'query': {'description': 'query to look up on wikipedia', 'title': 'Query', 'type': 'string'}}returns directly?: False
```

## Customizing Default Tools​
We can also modify the built in name, description, and JSON schema of the arguments.
When defining the JSON schema of the arguments, it is important that the inputs remain the same as the function, so you shouldn't change that. But you can define custom descriptions for each input easily.
```
from langchain_community.tools import WikipediaQueryRunfrom langchain_community.utilities import WikipediaAPIWrapperfrom pydantic import BaseModel, FieldclassWikiInputs(BaseModel):"""Inputs to the wikipedia tool."""  query:str= Field(    description="query to look up in Wikipedia, should be 3 or less words")tool = WikipediaQueryRun(  name="wiki-tool",  description="look up things in wikipedia",  args_schema=WikiInputs,  api_wrapper=api_wrapper,  return_direct=True,)print(tool.run("langchain"))
```

**API Reference:**WikipediaQueryRun | WikipediaAPIWrapper
```
Page: LangChainSummary: LangChain is a framework designed to simplify the creation of applications
```

```
print(f"Name: {tool.name}")print(f"Description: {tool.description}")print(f"args schema: {tool.args}")print(f"returns directly?: {tool.return_direct}")
```

```
Name: wiki-toolDescription: look up things in wikipediaargs schema: {'query': {'description': 'query to look up in Wikipedia, should be 3 or less words', 'title': 'Query', 'type': 'string'}}returns directly?: True
```

## How to use built-in toolkits​
Toolkits are collections of tools that are designed to be used together for specific tasks. They have convenient loading methods.
All Toolkits expose a `get_tools` method which returns a list of tools.
You're usually meant to use them this way:
```
# Initialize a toolkittoolkit = ExampleTookit(...)# Get list of toolstools = toolkit.get_tools()
```

#### Was this page helpful?
  * Tools
  * Customizing Default Tools
  * How to use built-in toolkits


