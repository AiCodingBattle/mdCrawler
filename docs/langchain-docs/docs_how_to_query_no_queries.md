Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Sometimes, a query analysis technique may allow for any number of queries to be generated - including no queries! In this case, our overall chain will need to inspect the result of the query analysis before deciding whether to call the retriever or not.
We will use mock data for this example.
## Setup​
#### Install dependencies​
```
%pip install -qU langchain langchain-community langchain-openai langchain-chroma
```

```
Note: you may need to restart the kernel to use updated packages.
```

#### Set environment variables​
We'll use OpenAI in this example:
```
import getpassimport osif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass.getpass()# Optional, uncomment to trace runs with LangSmith. Sign up here: https://smith.langchain.com.# os.environ["LANGSMITH_TRACING"] = "true"# os.environ["LANGSMITH_API_KEY"] = getpass.getpass()
```

### Create Index​
We will create a vectorstore over fake information.
```
from langchain_chroma import Chromafrom langchain_openai import OpenAIEmbeddingsfrom langchain_text_splitters import RecursiveCharacterTextSplittertexts =["Harrison worked at Kensho"]embeddings = OpenAIEmbeddings(model="text-embedding-3-small")vectorstore = Chroma.from_texts(  texts,  embeddings,)retriever = vectorstore.as_retriever()
```

**API Reference:**OpenAIEmbeddings | RecursiveCharacterTextSplitter
## Query analysis​
We will use function calling to structure the output. However, we will configure the LLM such that is doesn't NEED to call the function representing a search query (should it decide not to). We will also then use a prompt to do query analysis that explicitly lays when it should and shouldn't make a search.
```
from typing import Optionalfrom pydantic import BaseModel, FieldclassSearch(BaseModel):"""Search over a database of job records."""  query:str= Field(...,    description="Similarity search query applied to job record.",)
```

```
from langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import RunnablePassthroughfrom langchain_openai import ChatOpenAIsystem ="""You have the ability to issue search queries to get information to help answer user information.You do not NEED to look things up. If you don't need to, then just respond normally."""prompt = ChatPromptTemplate.from_messages([("system", system),("human","{question}"),])llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)structured_llm = llm.bind_tools([Search])query_analyzer ={"question": RunnablePassthrough()}| prompt | structured_llm
```

**API Reference:**ChatPromptTemplate | RunnablePassthrough | ChatOpenAI
We can see that by invoking this we get an message that sometimes - but not always - returns a tool call.
```
query_analyzer.invoke("where did Harrison Work")
```

```
AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_korLZrh08PTRL94f4L7rFqdj', 'function': {'arguments': '{"query":"Harrison"}', 'name': 'Search'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 95, 'total_tokens': 109}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-ea94d376-37bf-4f80-abe6-e3b42b767ea0-0', tool_calls=[{'name': 'Search', 'args': {'query': 'Harrison'}, 'id': 'call_korLZrh08PTRL94f4L7rFqdj', 'type': 'tool_call'}], usage_metadata={'input_tokens': 95, 'output_tokens': 14, 'total_tokens': 109})
```

```
query_analyzer.invoke("hi!")
```

```
AIMessage(content='Hello! How can I assist you today?', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 93, 'total_tokens': 103}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'stop', 'logprobs': None}, id='run-ebdfc44a-455a-4ca6-be85-84559886b1e1-0', usage_metadata={'input_tokens': 93, 'output_tokens': 10, 'total_tokens': 103})
```

## Retrieval with query analysis​
So how would we include this in a chain? Let's look at an example below.
```
from langchain_core.output_parsers.openai_tools import PydanticToolsParserfrom langchain_core.runnables import chainoutput_parser = PydanticToolsParser(tools=[Search])
```

**API Reference:**PydanticToolsParser | chain
```
@chaindefcustom_chain(question):  response = query_analyzer.invoke(question)if"tool_calls"in response.additional_kwargs:    query = output_parser.invoke(response)    docs = retriever.invoke(query[0].query)# Could add more logic - like another LLM call - herereturn docselse:return response
```

```
custom_chain.invoke("where did Harrison Work")
```

```
Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1
```

```
[Document(page_content='Harrison worked at Kensho')]
```

```
custom_chain.invoke("hi!")
```

```
AIMessage(content='Hello! How can I assist you today?', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 93, 'total_tokens': 103}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'stop', 'logprobs': None}, id='run-e87f058d-30c0-4075-8a89-a01b982d557e-0', usage_metadata={'input_tokens': 93, 'output_tokens': 10, 'total_tokens': 103})
```

#### Was this page helpful?
  * Setup
    * Create Index
  * Query analysis
  * Retrieval with query analysis


