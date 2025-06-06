Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Prompt templates
  * Example selectors
  * Chat models
  * Vectorstores


This guide covers how to prompt a chat model with example inputs and outputs. Providing the model with a few such examples is called few-shotting, and is a simple yet powerful way to guide generation and in some cases drastically improve model performance.
There does not appear to be solid consensus on how best to do few-shot prompting, and the optimal prompt compilation will likely vary by model. Because of this, we provide few-shot prompt templates like the FewShotChatMessagePromptTemplate as a flexible starting point, and you can modify or replace them as you see fit.
The goal of few-shot prompt templates are to dynamically select examples based on an input, and then format the examples in a final prompt to provide for the model.
**Note:** The following code examples are for chat models only, since `FewShotChatMessagePromptTemplates` are designed to output formatted chat messages rather than pure strings. For similar few-shot prompt examples for pure string templates compatible with completion models (LLMs), see the few-shot prompt templates guide.
## Fixed Examples​
The most basic (and common) few-shot prompting technique is to use fixed prompt examples. This way you can select a chain, evaluate it, and avoid worrying about additional moving parts in production.
The basic components of the template are:
  * `examples`: A list of dictionary examples to include in the final prompt.
  * `example_prompt`: converts each example into 1 or more messages through its `format_messages` method. A common example would be to convert each example into one human message and one AI message response, or a human message followed by a function call message.


Below is a simple demonstration. First, define the examples you'd like to include. Let's give the LLM an unfamiliar mathematical operator, denoted by the "🦜" emoji:
```
%pip install -qU langchain langchain-openai langchain-chromaimport osfrom getpass import getpassif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()
```

If we try to ask the model what the result of this expression is, it will fail:
```
from langchain_openai import ChatOpenAImodel = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)model.invoke("What is 2 🦜 9?")
```

**API Reference:**ChatOpenAI
```
AIMessage(content='The expression "2 🦜 9" is not a standard mathematical operation or equation. It appears to be a combination of the number 2 and the parrot emoji 🦜 followed by the number 9. It does not have a specific mathematical meaning.', response_metadata={'token_usage': {'completion_tokens': 54, 'prompt_tokens': 17, 'total_tokens': 71}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-aad12dda-5c47-4a1e-9949-6fe94e03242a-0', usage_metadata={'input_tokens': 17, 'output_tokens': 54, 'total_tokens': 71})
```

Now let's see what happens if we give the LLM some examples to work with. We'll define some below:
```
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplateexamples =[{"input":"2 🦜 2","output":"4"},{"input":"2 🦜 3","output":"5"},]
```

**API Reference:**ChatPromptTemplate | FewShotChatMessagePromptTemplate
Next, assemble them into the few-shot prompt template.
```
# This is a prompt template used to format each individual example.example_prompt = ChatPromptTemplate.from_messages([("human","{input}"),("ai","{output}"),])few_shot_prompt = FewShotChatMessagePromptTemplate(  example_prompt=example_prompt,  examples=examples,)print(few_shot_prompt.invoke({}).to_messages())
```

```
[HumanMessage(content='2 🦜 2'), AIMessage(content='4'), HumanMessage(content='2 🦜 3'), AIMessage(content='5')]
```

Finally, we assemble the final prompt as shown below, passing `few_shot_prompt` directly into the `from_messages` factory method, and use it with a model:
```
final_prompt = ChatPromptTemplate.from_messages([("system","You are a wondrous wizard of math."),    few_shot_prompt,("human","{input}"),])
```

And now let's ask the model the initial question and see how it does:
```
from langchain_openai import ChatOpenAIchain = final_prompt | modelchain.invoke({"input":"What is 2 🦜 9?"})
```

**API Reference:**ChatOpenAI
```
AIMessage(content='11', response_metadata={'token_usage': {'completion_tokens': 1, 'prompt_tokens': 60, 'total_tokens': 61}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-5ec4e051-262f-408e-ad00-3f2ebeb561c3-0', usage_metadata={'input_tokens': 60, 'output_tokens': 1, 'total_tokens': 61})
```

And we can see that the model has now inferred that the parrot emoji means addition from the given few-shot examples!
## Dynamic few-shot prompting​
Sometimes you may want to select only a few examples from your overall set to show based on the input. For this, you can replace the `examples` passed into `FewShotChatMessagePromptTemplate` with an `example_selector`. The other components remain the same as above! Our dynamic few-shot prompt template would look like:
  * `example_selector`: responsible for selecting few-shot examples (and the order in which they are returned) for a given input. These implement the BaseExampleSelector interface. A common example is the vectorstore-backed SemanticSimilarityExampleSelector
  * `example_prompt`: convert each example into 1 or more messages through its `format_messages` method. A common example would be to convert each example into one human message and one AI message response, or a human message followed by a function call message.


These once again can be composed with other messages and chat templates to assemble your final prompt.
Let's walk through an example with the `SemanticSimilarityExampleSelector`. Since this implementation uses a vectorstore to select examples based on semantic similarity, we will want to first populate the store. Since the basic idea here is that we want to search for and return examples most similar to the text input, we embed the `values` of our prompt examples rather than considering the keys:
```
from langchain_chroma import Chromafrom langchain_core.example_selectors import SemanticSimilarityExampleSelectorfrom langchain_openai import OpenAIEmbeddingsexamples =[{"input":"2 🦜 2","output":"4"},{"input":"2 🦜 3","output":"5"},{"input":"2 🦜 4","output":"6"},{"input":"What did the cow say to the moon?","output":"nothing at all"},{"input":"Write me a poem about the moon","output":"One for the moon, and one for me, who are we to talk about the moon?",},]to_vectorize =[" ".join(example.values())for example in examples]embeddings = OpenAIEmbeddings()vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=examples)
```

**API Reference:**SemanticSimilarityExampleSelector | OpenAIEmbeddings
### Create the `example_selector`​
With a vectorstore created, we can create the `example_selector`. Here we will call it in isolation, and set `k` on it to only fetch the two example closest to the input.
```
example_selector = SemanticSimilarityExampleSelector(  vectorstore=vectorstore,  k=2,)# The prompt template will load examples by passing the input do the `select_examples` methodexample_selector.select_examples({"input":"horse"})
```

```
[{'input': 'What did the cow say to the moon?', 'output': 'nothing at all'}, {'input': '2 🦜 4', 'output': '6'}]
```

### Create prompt template​
We now assemble the prompt template, using the `example_selector` created above.
```
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate# Define the few-shot prompt.few_shot_prompt = FewShotChatMessagePromptTemplate(# The input variables select the values to pass to the example_selector  input_variables=["input"],  example_selector=example_selector,# Define how each example will be formatted.# In this case, each example will become 2 messages:# 1 human, and 1 AI  example_prompt=ChatPromptTemplate.from_messages([("human","{input}"),("ai","{output}")]),)print(few_shot_prompt.invoke(input="What's 3 🦜 3?").to_messages())
```

**API Reference:**ChatPromptTemplate | FewShotChatMessagePromptTemplate
```
[HumanMessage(content='2 🦜 3'), AIMessage(content='5'), HumanMessage(content='2 🦜 4'), AIMessage(content='6')]
```

And we can pass this few-shot chat message prompt template into another chat prompt template:
```
final_prompt = ChatPromptTemplate.from_messages([("system","You are a wondrous wizard of math."),    few_shot_prompt,("human","{input}"),])print(few_shot_prompt.invoke(input="What's 3 🦜 3?"))
```

```
messages=[HumanMessage(content='2 🦜 3'), AIMessage(content='5'), HumanMessage(content='2 🦜 4'), AIMessage(content='6')]
```

### Use with an chat model​
Finally, you can connect your model to the few-shot prompt.
```
chain = final_prompt | ChatOpenAI(model="gpt-4o-mini", temperature=0.0)chain.invoke({"input":"What's 3 🦜 3?"})
```

```
AIMessage(content='6', response_metadata={'token_usage': {'completion_tokens': 1, 'prompt_tokens': 60, 'total_tokens': 61}, 'model_name': 'gpt-4o-mini', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-d1863e5e-17cd-4e9d-bf7a-b9f118747a65-0', usage_metadata={'input_tokens': 60, 'output_tokens': 1, 'total_tokens': 61})
```

## Next steps​
You've now learned how to add few-shot examples to your chat prompts.
Next, check out the other how-to guides on prompt templates in this section, the related how-to guide on few shotting with text completion models, or the other example selector how-to guides.
#### Was this page helpful?
  * Fixed Examples
  * Dynamic few-shot prompting
    * Create the `example_selector`
    * Create prompt template
    * Use with an chat model
  * Next steps


