Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
You may want to do query analysis to create a filter on a categorical column. One of the difficulties here is that you usually need to specify the EXACT categorical value. The issue is you need to make sure the LLM generates that categorical value exactly. This can be done relatively easy with prompting when there are only a few values that are valid. When there are a high number of valid values then it becomes more difficult, as those values may not fit in the LLM context, or (if they do) there may be too many for the LLM to properly attend to.
In this notebook we take a look at how to approach this.
## Setup​
#### Install dependencies​
```
%pip install -qU langchain langchain-community langchain-openai faker langchain-chroma
```

```
Note: you may need to restart the kernel to use updated packages.
```

#### Set environment variables​
We'll use OpenAI in this example:
```
import getpassimport osif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass.getpass()# Optional, uncomment to trace runs with LangSmith. Sign up here: https://smith.langchain.com.# os.environ["LANGSMITH_TRACING"] = "true"# os.environ["LANGSMITH_API_KEY"] = getpass.getpass()
```

#### Set up data​
We will generate a bunch of fake names
```
from faker import Fakerfake = Faker()names =[fake.name()for _ inrange(10000)]
```

Let's look at some of the names
```
names[0]
```

```
'Jacob Adams'
```

```
names[567]
```

```
'Eric Acevedo'
```

## Query Analysis​
We can now set up a baseline query analysis
```
from pydantic import BaseModel, Field, model_validator
```

```
classSearch(BaseModel):  query:str  author:str
```

```
from langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import RunnablePassthroughfrom langchain_openai import ChatOpenAIsystem ="""Generate a relevant search query for a library system"""prompt = ChatPromptTemplate.from_messages([("system", system),("human","{question}"),])llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)structured_llm = llm.with_structured_output(Search)query_analyzer ={"question": RunnablePassthrough()}| prompt | structured_llm
```

**API Reference:**ChatPromptTemplate | RunnablePassthrough | ChatOpenAI
We can see that if we spell the name exactly correctly, it knows how to handle it
```
query_analyzer.invoke("what are books about aliens by Jesse Knight")
```

```
Search(query='aliens', author='Jesse Knight')
```

The issue is that the values you want to filter on may NOT be spelled exactly correctly
```
query_analyzer.invoke("what are books about aliens by jess knight")
```

```
Search(query='aliens', author='Jess Knight')
```

### Add in all values​
One way around this is to add ALL possible values to the prompt. That will generally guide the query in the right direction
```
system ="""Generate a relevant search query for a library system.`author` attribute MUST be one of:{authors}Do NOT hallucinate author name!"""base_prompt = ChatPromptTemplate.from_messages([("system", system),("human","{question}"),])prompt = base_prompt.partial(authors=", ".join(names))
```

```
query_analyzer_all ={"question": RunnablePassthrough()}| prompt | structured_llm
```

However... if the list of categoricals is long enough, it may error!
```
try:  res = query_analyzer_all.invoke("what are books about aliens by jess knight")except Exception as e:print(e)
```

We can try to use a longer context window... but with so much information in there, it is not garunteed to pick it up reliably
```
llm_long = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)structured_llm_long = llm_long.with_structured_output(Search)query_analyzer_all ={"question": RunnablePassthrough()}| prompt | structured_llm_long
```

```
query_analyzer_all.invoke("what are books about aliens by jess knight")
```

```
Search(query='aliens', author='jess knight')
```

### Find and all relevant values​
Instead, what we can do is create an index over the relevant values and then query that for the N most relevant values,
```
from langchain_chroma import Chromafrom langchain_openai import OpenAIEmbeddingsembeddings = OpenAIEmbeddings(model="text-embedding-3-small")vectorstore = Chroma.from_texts(names, embeddings, collection_name="author_names")
```

**API Reference:**OpenAIEmbeddings
```
defselect_names(question):  _docs = vectorstore.similarity_search(question, k=10)  _names =[d.page_content for d in _docs]return", ".join(_names)
```

```
create_prompt ={"question": RunnablePassthrough(),"authors": select_names,}| base_prompt
```

```
query_analyzer_select = create_prompt | structured_llm
```

```
create_prompt.invoke("what are books by jess knight")
```

```
ChatPromptValue(messages=[SystemMessage(content='Generate a relevant search query for a library system.\n\n`author` attribute MUST be one of:\n\nJennifer Knight, Jill Knight, John Knight, Dr. Jeffrey Knight, Christopher Knight, Andrea Knight, Brandy Knight, Jennifer Keller, Becky Chambers, Sarah Knapp\n\nDo NOT hallucinate author name!'), HumanMessage(content='what are books by jess knight')])
```

```
query_analyzer_select.invoke("what are books about aliens by jess knight")
```

```
Search(query='books about aliens', author='Jennifer Knight')
```

### Replace after selection​
Another method is to let the LLM fill in whatever value, but then convert that value to a valid value. This can actually be done with the Pydantic class itself!
```
classSearch(BaseModel):  query:str  author:str@model_validator(mode="before")@classmethoddefdouble(cls, values:dict)->dict:    author = values["author"]    closest_valid_author = vectorstore.similarity_search(author, k=1)[0].page_content    values["author"]= closest_valid_authorreturn values
```

```
system ="""Generate a relevant search query for a library system"""prompt = ChatPromptTemplate.from_messages([("system", system),("human","{question}"),])corrective_structure_llm = llm.with_structured_output(Search)corrective_query_analyzer =({"question": RunnablePassthrough()}| prompt | corrective_structure_llm)
```

```
corrective_query_analyzer.invoke("what are books about aliens by jes knight")
```

```
Search(query='aliens', author='John Knight')
```

```
# TODO: show trigram similarity
```

#### Was this page helpful?
  * Setup
  * Query Analysis
    * Add in all values
    * Find and all relevant values
    * Replace after selection


