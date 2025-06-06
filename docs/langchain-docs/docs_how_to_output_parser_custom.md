Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
In some situations you may want to implement a custom parser to structure the model output into a custom format.
There are two ways to implement a custom parser:
  1. Using `RunnableLambda` or `RunnableGenerator` in LCEL -- we strongly recommend this for most use cases
  2. By inheriting from one of the base classes for out parsing -- this is the hard way of doing things


The difference between the two approaches are mostly superficial and are mainly in terms of which callbacks are triggered (e.g., `on_chain_start` vs. `on_parser_start`), and how a runnable lambda vs. a parser might be visualized in a tracing platform like LangSmith.
## Runnable Lambdas and Generators​
The recommended way to parse is using **runnable lambdas** and **runnable generators**!
Here, we will make a simple parse that inverts the case of the output from the model.
For example, if the model outputs: "Meow", the parser will produce "mEOW".
```
from typing import Iterablefrom langchain_anthropic.chat_models import ChatAnthropicfrom langchain_core.messages import AIMessage, AIMessageChunkmodel = ChatAnthropic(model_name="claude-2.1")defparse(ai_message: AIMessage)->str:"""Parse the AI message."""return ai_message.content.swapcase()chain = model | parsechain.invoke("hello")
```

**API Reference:**ChatAnthropic | AIMessage | AIMessageChunk
```
'hELLO!'
```

tip
LCEL automatically upgrades the function `parse` to `RunnableLambda(parse)` when composed using a `|` syntax.
If you don't like that you can manually import `RunnableLambda` and then run`parse = RunnableLambda(parse)`.
Does streaming work?
```
for chunk in chain.stream("tell me about yourself in one sentence"):print(chunk, end="|", flush=True)
```

```
i'M cLAUDE, AN ai ASSISTANT CREATED BY aNTHROPIC TO BE HELPFUL, HARMLESS, AND HONEST.|
```

No, it doesn't because the parser aggregates the input before parsing the output.
If we want to implement a streaming parser, we can have the parser accept an iterable over the input instead and yield the results as they're available.
```
from langchain_core.runnables import RunnableGeneratordefstreaming_parse(chunks: Iterable[AIMessageChunk])-> Iterable[str]:for chunk in chunks:yield chunk.content.swapcase()streaming_parse = RunnableGenerator(streaming_parse)
```

**API Reference:**RunnableGenerator
important
Please wrap the streaming parser in `RunnableGenerator` as we may stop automatically upgrading it with the `|` syntax.
```
chain = model | streaming_parsechain.invoke("hello")
```

```
'hELLO!'
```

Let's confirm that streaming works!
```
for chunk in chain.stream("tell me about yourself in one sentence"):print(chunk, end="|", flush=True)
```

```
i|'M| cLAUDE|,| AN| ai| ASSISTANT| CREATED| BY| aN|THROP|IC| TO| BE| HELPFUL|,| HARMLESS|,| AND| HONEST|.|
```

## Inheriting from Parsing Base Classes​
Another approach to implement a parser is by inheriting from `BaseOutputParser`, `BaseGenerationOutputParser` or another one of the base parsers depending on what you need to do.
In general, we **do not** recommend this approach for most use cases as it results in more code to write without significant benefits.
The simplest kind of output parser extends the `BaseOutputParser` class and must implement the following methods:
  * `parse`: takes the string output from the model and parses it
  * (optional) `_type`: identifies the name of the parser.


When the output from the chat model or LLM is malformed, the can throw an `OutputParserException` to indicate that parsing fails because of bad input. Using this exception allows code that utilizes the parser to handle the exceptions in a consistent manner.
Parsers are Runnables! 🏃
Because `BaseOutputParser` implements the `Runnable` interface, any custom parser you will create this way will become valid LangChain Runnables and will benefit from automatic async support, batch interface, logging support etc.
### Simple Parser​
Here's a simple parser that can parse a **string** representation of a boolean (e.g., `YES` or `NO`) and convert it into the corresponding `boolean` type.
```
from langchain_core.exceptions import OutputParserExceptionfrom langchain_core.output_parsers import BaseOutputParser# The [bool] desribes a parameterization of a generic.# It's basically indicating what the return type of parse is# in this case the return type is either True or FalseclassBooleanOutputParser(BaseOutputParser[bool]):"""Custom boolean parser."""  true_val:str="YES"  false_val:str="NO"defparse(self, text:str)->bool:    cleaned_text = text.strip().upper()if cleaned_text notin(self.true_val.upper(), self.false_val.upper()):raise OutputParserException(f"BooleanOutputParser expected output value to either be "f"{self.true_val} or {self.false_val} (case-insensitive). "f"Received {cleaned_text}.")return cleaned_text == self.true_val.upper()@propertydef_type(self)->str:return"boolean_output_parser"
```

**API Reference:**OutputParserException | BaseOutputParser
```
parser = BooleanOutputParser()parser.invoke("YES")
```

```
True
```

```
try:  parser.invoke("MEOW")except Exception as e:print(f"Triggered an exception of type: {type(e)}")
```

```
Triggered an exception of type: <class 'langchain_core.exceptions.OutputParserException'>
```

Let's test changing the parameterization
```
parser = BooleanOutputParser(true_val="OKAY")parser.invoke("OKAY")
```

```
True
```

Let's confirm that other LCEL methods are present
```
parser.batch(["OKAY","NO"])
```

```
[True, False]
```

```
await parser.abatch(["OKAY","NO"])
```

```
[True, False]
```

```
from langchain_anthropic.chat_models import ChatAnthropicanthropic = ChatAnthropic(model_name="claude-2.1")anthropic.invoke("say OKAY or NO")
```

**API Reference:**ChatAnthropic
```
AIMessage(content='OKAY')
```

Let's test that our parser works!
```
chain = anthropic | parserchain.invoke("say OKAY or NO")
```

```
True
```

note
The parser will work with either the output from an LLM (a string) or the output from a chat model (an `AIMessage`)!
### Parsing Raw Model Outputs​
Sometimes there is additional metadata on the model output that is important besides the raw text. One example of this is tool calling, where arguments intended to be passed to called functions are returned in a separate property. If you need this finer-grained control, you can instead subclass the `BaseGenerationOutputParser` class.
This class requires a single method `parse_result`. This method takes raw model output (e.g., list of `Generation` or `ChatGeneration`) and returns the parsed output.
Supporting both `Generation` and `ChatGeneration` allows the parser to work with both regular LLMs as well as with Chat Models.
```
from typing import Listfrom langchain_core.exceptions import OutputParserExceptionfrom langchain_core.messages import AIMessagefrom langchain_core.output_parsers import BaseGenerationOutputParserfrom langchain_core.outputs import ChatGeneration, GenerationclassStrInvertCase(BaseGenerationOutputParser[str]):"""An example parser that inverts the case of the characters in the message.  This is an example parse shown just for demonstration purposes and to keep  the example as simple as possible.  """defparse_result(self, result: List[Generation],*, partial:bool=False)->str:"""Parse a list of model Generations into a specific format.    Args:      result: A list of Generations to be parsed. The Generations are assumed        to be different candidate outputs for a single model input.        Many parsers assume that only a single generation is passed it in.        We will assert for that      partial: Whether to allow partial results. This is used for parsers           that support streaming    """iflen(result)!=1:raise NotImplementedError("This output parser can only be used with a single generation.")    generation = result[0]ifnotisinstance(generation, ChatGeneration):# Say that this one only works with chat generationsraise OutputParserException("This output parser can only be used with a chat generation.")return generation.message.content.swapcase()chain = anthropic | StrInvertCase()
```

**API Reference:**OutputParserException | AIMessage | BaseGenerationOutputParser | ChatGeneration | Generation
Let's the new parser! It should be inverting the output from the model.
```
chain.invoke("Tell me a short sentence about yourself")
```

```
'hELLO! mY NAME IS cLAUDE.'
```

#### Was this page helpful?
  * Runnable Lambdas and Generators
  * Inheriting from Parsing Base Classes
    * Simple Parser
    * Parsing Raw Model Outputs


