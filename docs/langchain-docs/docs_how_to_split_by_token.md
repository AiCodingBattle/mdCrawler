Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Language models have a token limit. You should not exceed the token limit. When you split your text into chunks it is therefore a good idea to count the number of tokens. There are many tokenizers. When you count tokens in your text you should use the same tokenizer as used in the language model.
## tiktoken​
note
tiktoken is a fast `BPE` tokenizer created by `OpenAI`.
We can use `tiktoken` to estimate tokens used. It will probably be more accurate for the OpenAI models.
  1. How the text is split: by character passed in.
  2. How the chunk size is measured: by `tiktoken` tokenizer.


CharacterTextSplitter, RecursiveCharacterTextSplitter, and TokenTextSplitter can be used with `tiktoken` directly.
```
%pip install --upgrade --quiet langchain-text-splitters tiktoken
```

```
from langchain_text_splitters import CharacterTextSplitter# This is a long document we can split up.withopen("state_of_the_union.txt")as f:  state_of_the_union = f.read()
```

**API Reference:**CharacterTextSplitter
To split with a CharacterTextSplitter and then merge chunks with `tiktoken`, use its `.from_tiktoken_encoder()` method. Note that splits from this method can be larger than the chunk size measured by the `tiktoken` tokenizer.
The `.from_tiktoken_encoder()` method takes either `encoding_name` as an argument (e.g. `cl100k_base`), or the `model_name` (e.g. `gpt-4`). All additional arguments like `chunk_size`, `chunk_overlap`, and `separators` are used to instantiate `CharacterTextSplitter`:
```
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(  encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0)texts = text_splitter.split_text(state_of_the_union)
```

```
print(texts[0])
```

```
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans. Last year COVID-19 kept us apart. This year we are finally together again. Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. With a duty to one another to the American people to the Constitution.
```

To implement a hard constraint on the chunk size, we can use `RecursiveCharacterTextSplitter.from_tiktoken_encoder`, where each split will be recursively split if it has a larger size:
```
from langchain_text_splitters import RecursiveCharacterTextSplittertext_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(  model_name="gpt-4",  chunk_size=100,  chunk_overlap=0,)
```

**API Reference:**RecursiveCharacterTextSplitter
We can also load a `TokenTextSplitter` splitter, which works with `tiktoken` directly and will ensure each split is smaller than chunk size.
```
from langchain_text_splitters import TokenTextSplittertext_splitter = TokenTextSplitter(chunk_size=10, chunk_overlap=0)texts = text_splitter.split_text(state_of_the_union)print(texts[0])
```

**API Reference:**TokenTextSplitter
```
Madam Speaker, Madam Vice President, our
```

Some written languages (e.g. Chinese and Japanese) have characters which encode to 2 or more tokens. Using the `TokenTextSplitter` directly can split the tokens for a character between two chunks causing malformed Unicode characters. Use `RecursiveCharacterTextSplitter.from_tiktoken_encoder` or `CharacterTextSplitter.from_tiktoken_encoder` to ensure chunks contain valid Unicode strings.
## spaCy​
note
spaCy is an open-source software library for advanced natural language processing, written in the programming languages Python and Cython.
LangChain implements splitters based on the spaCy tokenizer.
  1. How the text is split: by `spaCy` tokenizer.
  2. How the chunk size is measured: by number of characters.


```
%pip install --upgrade --quiet spacy
```

```
# This is a long document we can split up.withopen("state_of_the_union.txt")as f:  state_of_the_union = f.read()
```

```
from langchain_text_splitters import SpacyTextSplittertext_splitter = SpacyTextSplitter(chunk_size=1000)texts = text_splitter.split_text(state_of_the_union)print(texts[0])
```

**API Reference:**SpacyTextSplitter
```
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman.Members of Congress and the Cabinet.Justices of the Supreme Court.My fellow Americans. Last year COVID-19 kept us apart.This year we are finally together again. Tonight, we meet as Democrats Republicans and Independents.But most importantly as Americans. With a duty to one another to the American people to the Constitution. And with an unwavering resolve that freedom will always triumph over tyranny. Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways.But he badly miscalculated. He thought he could roll into Ukraine and the world would roll over.Instead he met a wall of strength he never imagined. He met the Ukrainian people. From President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world.
```

## SentenceTransformers​
The SentenceTransformersTokenTextSplitter is a specialized text splitter for use with the sentence-transformer models. The default behaviour is to split the text into chunks that fit the token window of the sentence transformer model that you would like to use.
To split text and constrain token counts according to the sentence-transformers tokenizer, instantiate a `SentenceTransformersTokenTextSplitter`. You can optionally specify:
  * `chunk_overlap`: integer count of token overlap;
  * `model_name`: sentence-transformer model name, defaulting to `"sentence-transformers/all-mpnet-base-v2"`;
  * `tokens_per_chunk`: desired token count per chunk.


```
from langchain_text_splitters import SentenceTransformersTokenTextSplittersplitter = SentenceTransformersTokenTextSplitter(chunk_overlap=0)text ="Lorem "count_start_and_stop_tokens =2text_token_count = splitter.count_tokens(text=text)- count_start_and_stop_tokensprint(text_token_count)
```

**API Reference:**SentenceTransformersTokenTextSplitter
```
2
```

```
token_multiplier = splitter.maximum_tokens_per_chunk // text_token_count +1# `text_to_split` does not fit in a single chunktext_to_split = text * token_multiplierprint(f"tokens in text to split: {splitter.count_tokens(text=text_to_split)}")
```

```
tokens in text to split: 514
```

```
text_chunks = splitter.split_text(text=text_to_split)print(text_chunks[1])
```

```
lorem
```

## NLTK​
note
The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in the Python programming language.
Rather than just splitting on "\n\n", we can use `NLTK` to split based on NLTK tokenizers.
  1. How the text is split: by `NLTK` tokenizer.
  2. How the chunk size is measured: by number of characters.


```
# pip install nltk
```

```
# This is a long document we can split up.withopen("state_of_the_union.txt")as f:  state_of_the_union = f.read()
```

```
from langchain_text_splitters import NLTKTextSplittertext_splitter = NLTKTextSplitter(chunk_size=1000)
```

**API Reference:**NLTKTextSplitter
```
texts = text_splitter.split_text(state_of_the_union)print(texts[0])
```

```
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman.Members of Congress and the Cabinet.Justices of the Supreme Court.My fellow Americans.Last year COVID-19 kept us apart.This year we are finally together again.Tonight, we meet as Democrats Republicans and Independents.But most importantly as Americans.With a duty to one another to the American people to the Constitution.And with an unwavering resolve that freedom will always triumph over tyranny.Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways.But he badly miscalculated.He thought he could roll into Ukraine and the world would roll over.Instead he met a wall of strength he never imagined.He met the Ukrainian people.From President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world.Groups of citizens blocking tanks with their bodies.
```

## KoNLPY​
note
KoNLPy: Korean NLP in Python is is a Python package for natural language processing (NLP) of the Korean language.
Token splitting involves the segmentation of text into smaller, more manageable units called tokens. These tokens are often words, phrases, symbols, or other meaningful elements crucial for further processing and analysis. In languages like English, token splitting typically involves separating words by spaces and punctuation marks. The effectiveness of token splitting largely depends on the tokenizer's understanding of the language structure, ensuring the generation of meaningful tokens. Since tokenizers designed for the English language are not equipped to understand the unique semantic structures of other languages, such as Korean, they cannot be effectively used for Korean language processing.
### Token splitting for Korean with KoNLPy's Kkma Analyzer​
In case of Korean text, KoNLPY includes at morphological analyzer called `Kkma` (Korean Knowledge Morpheme Analyzer). `Kkma` provides detailed morphological analysis of Korean text. It breaks down sentences into words and words into their respective morphemes, identifying parts of speech for each token. It can segment a block of text into individual sentences, which is particularly useful for processing long texts.
### Usage Considerations​
While `Kkma` is renowned for its detailed analysis, it is important to note that this precision may impact processing speed. Thus, `Kkma` is best suited for applications where analytical depth is prioritized over rapid text processing.
```
# pip install konlpy
```

```
# This is a long Korean document that we want to split up into its component sentences.withopen("./your_korean_doc.txt")as f:  korean_document = f.read()
```

```
from langchain_text_splitters import KonlpyTextSplittertext_splitter = KonlpyTextSplitter()
```

**API Reference:**KonlpyTextSplitter
```
texts = text_splitter.split_text(korean_document)# The sentences are split with "\n\n" characters.print(texts[0])
```

```
춘향전 옛날에 남원에 이 도령이라는 벼슬아치 아들이 있었다.그의 외모는 빛나는 달처럼 잘생겼고, 그의 학식과 기예는 남보다 뛰어났다.한편, 이 마을에는 춘향이라는 절세 가인이 살고 있었다.춘 향의 아름다움은 꽃과 같아 마을 사람들 로부터 많은 사랑을 받았다.어느 봄날, 도령은 친구들과 놀러 나갔다가 춘 향을 만 나 첫 눈에 반하고 말았다.두 사람은 서로 사랑하게 되었고, 이내 비밀스러운 사랑의 맹세를 나누었다.하지만 좋은 날들은 오래가지 않았다.도령의 아버지가 다른 곳으로 전근을 가게 되어 도령도 떠나 야만 했다.이별의 아픔 속에서도, 두 사람은 재회를 기약하며 서로를 믿고 기다리기로 했다.그러나 새로 부임한 관아의 사또가 춘 향의 아름다움에 욕심을 내 어 그녀에게 강요를 시작했다.춘 향 은 도령에 대한 자신의 사랑을 지키기 위해, 사또의 요구를 단호히 거절했다.이에 분노한 사또는 춘 향을 감옥에 가두고 혹독한 형벌을 내렸다.이야기는 이 도령이 고위 관직에 오른 후, 춘 향을 구해 내는 것으로 끝난다.두 사람은 오랜 시련 끝에 다시 만나게 되고, 그들의 사랑은 온 세상에 전해 지며 후세에까지 이어진다.- 춘향전 (The Tale of Chunhyang)
```

## Hugging Face tokenizer​
Hugging Face has many tokenizers.
We use Hugging Face tokenizer, the GPT2TokenizerFast to count the text length in tokens.
  1. How the text is split: by character passed in.
  2. How the chunk size is measured: by number of tokens calculated by the `Hugging Face` tokenizer.


```
from transformers import GPT2TokenizerFasttokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
```

```
# This is a long document we can split up.withopen("state_of_the_union.txt")as f:  state_of_the_union = f.read()from langchain_text_splitters import CharacterTextSplitter
```

**API Reference:**CharacterTextSplitter
```
text_splitter = CharacterTextSplitter.from_huggingface_tokenizer(  tokenizer, chunk_size=100, chunk_overlap=0)texts = text_splitter.split_text(state_of_the_union)
```

```
print(texts[0])
```

```
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans. Last year COVID-19 kept us apart. This year we are finally together again. Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. With a duty to one another to the American people to the Constitution.
```

#### Was this page helpful?
  * tiktoken
  * spaCy
  * SentenceTransformers
  * NLTK
  * KoNLPY
    * Token splitting for Korean with KoNLPy's Kkma Analyzer
    * Usage Considerations
  * Hugging Face tokenizer


