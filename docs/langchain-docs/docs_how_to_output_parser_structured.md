Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Language models output text. But there are times where you want to get more structured information than just text back. While some model providers support built-in ways to return structured output, not all do.
Output parsers are classes that help structure language model responses. There are two main methods an output parser must implement:
  * "Get format instructions": A method which returns a string containing instructions for how the output of a language model should be formatted.
  * "Parse": A method which takes in a string (assumed to be the response from a language model) and parses it into some structure.


And then one optional one:
  * "Parse with prompt": A method which takes in a string (assumed to be the response from a language model) and a prompt (assumed to be the prompt that generated such a response) and parses it into some structure. The prompt is largely provided in the event the OutputParser wants to retry or fix the output in some way, and needs information from the prompt to do so.


## Get started​
Below we go over the main type of output parser, the `PydanticOutputParser`.
```
from langchain_core.output_parsers import PydanticOutputParserfrom langchain_core.prompts import PromptTemplatefrom langchain_openai import OpenAIfrom pydantic import BaseModel, Field, model_validatormodel = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.0)# Define your desired data structure.classJoke(BaseModel):  setup:str= Field(description="question to set up a joke")  punchline:str= Field(description="answer to resolve the joke")# You can add custom validation logic easily with Pydantic.@model_validator(mode="before")@classmethoddefquestion_ends_with_question_mark(cls, values:dict)->dict:    setup = values.get("setup")if setup and setup[-1]!="?":raise ValueError("Badly formed question!")return values# Set up a parser + inject instructions into the prompt template.parser = PydanticOutputParser(pydantic_object=Joke)prompt = PromptTemplate(  template="Answer the user query.\n{format_instructions}\n{query}\n",  input_variables=["query"],  partial_variables={"format_instructions": parser.get_format_instructions()},)# And a query intended to prompt a language model to populate the data structure.prompt_and_model = prompt | modeloutput = prompt_and_model.invoke({"query":"Tell me a joke."})parser.invoke(output)
```

**API Reference:**PydanticOutputParser | PromptTemplate | OpenAI
```
Joke(setup='Why did the tomato turn red?', punchline='Because it saw the salad dressing!')
```

## LCEL​
Output parsers implement the Runnable interface, the basic building block of the LangChain Expression Language (LCEL). This means they support `invoke`, `ainvoke`, `stream`, `astream`, `batch`, `abatch`, `astream_log` calls.
Output parsers accept a string or `BaseMessage` as input and can return an arbitrary type.
```
parser.invoke(output)
```

```
Joke(setup='Why did the tomato turn red?', punchline='Because it saw the salad dressing!')
```

Instead of manually invoking the parser, we also could've just added it to our `Runnable` sequence:
```
chain = prompt | model | parserchain.invoke({"query":"Tell me a joke."})
```

```
Joke(setup='Why did the tomato turn red?', punchline='Because it saw the salad dressing!')
```

While all parsers support the streaming interface, only certain parsers can stream through partially parsed objects, since this is highly dependent on the output type. Parsers which cannot construct partial objects will simply yield the fully parsed output.
The `SimpleJsonOutputParser` for example can stream through partial outputs:
```
from langchain.output_parsers.json import SimpleJsonOutputParserjson_prompt = PromptTemplate.from_template("Return a JSON object with an `answer` key that answers the following question: {question}")json_parser = SimpleJsonOutputParser()json_chain = json_prompt | model | json_parser
```

**API Reference:**SimpleJsonOutputParser
```
list(json_chain.stream({"question":"Who invented the microscope?"}))
```

```
[{}, {'answer': ''}, {'answer': 'Ant'}, {'answer': 'Anton'}, {'answer': 'Antonie'}, {'answer': 'Antonie van'}, {'answer': 'Antonie van Lee'}, {'answer': 'Antonie van Leeu'}, {'answer': 'Antonie van Leeuwen'}, {'answer': 'Antonie van Leeuwenho'}, {'answer': 'Antonie van Leeuwenhoek'}]
```

Similarly,for `PydanticOutputParser`:
```
list(chain.stream({"query":"Tell me a joke."}))
```

```
[Joke(setup='Why did the tomato turn red?', punchline=''), Joke(setup='Why did the tomato turn red?', punchline='Because'), Joke(setup='Why did the tomato turn red?', punchline='Because it'), Joke(setup='Why did the tomato turn red?', punchline='Because it saw'), Joke(setup='Why did the tomato turn red?', punchline='Because it saw the'), Joke(setup='Why did the tomato turn red?', punchline='Because it saw the salad'), Joke(setup='Why did the tomato turn red?', punchline='Because it saw the salad dressing'), Joke(setup='Why did the tomato turn red?', punchline='Because it saw the salad dressing!')]
```

#### Was this page helpful?
  * Get started
  * LCEL


