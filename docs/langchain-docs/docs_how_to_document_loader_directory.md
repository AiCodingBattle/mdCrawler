Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
LangChain's DirectoryLoader implements functionality for reading files from disk into LangChain Document objects. Here we demonstrate:
  * How to load from a filesystem, including use of wildcard patterns;
  * How to use multithreading for file I/O;
  * How to use custom loader classes to parse specific file types (e.g., code);
  * How to handle errors, such as those due to decoding.


```
from langchain_community.document_loaders import DirectoryLoader
```

**API Reference:**DirectoryLoader
`DirectoryLoader` accepts a `loader_cls` kwarg, which defaults to UnstructuredLoader. Unstructured supports parsing for a number of formats, such as PDF and HTML. Here we use it to read in a markdown (.md) file.
We can use the `glob` parameter to control which files to load. Note that here it doesn't load the `.rst` file or the `.html` files.
```
loader = DirectoryLoader("../", glob="**/*.md")docs = loader.load()len(docs)
```

```
20
```

```
print(docs[0].page_content[:100])
```

```
SecurityLangChain has a large ecosystem of integrations with various external resources like local
```

## Show a progress bar​
By default a progress bar will not be shown. To show a progress bar, install the `tqdm` library (e.g. `pip install tqdm`), and set the `show_progress` parameter to `True`.
```
loader = DirectoryLoader("../", glob="**/*.md", show_progress=True)docs = loader.load()
```

```
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:00<00:00, 54.56it/s]
```

## Use multithreading​
By default the loading happens in one thread. In order to utilize several threads set the `use_multithreading` flag to true.
```
loader = DirectoryLoader("../", glob="**/*.md", use_multithreading=True)docs = loader.load()
```

## Change loader class​
By default this uses the `UnstructuredLoader` class. To customize the loader, specify the loader class in the `loader_cls` kwarg. Below we show an example using TextLoader:
```
from langchain_community.document_loaders import TextLoaderloader = DirectoryLoader("../", glob="**/*.md", loader_cls=TextLoader)docs = loader.load()
```

**API Reference:**TextLoader
```
print(docs[0].page_content[:100])
```

```
# SecurityLangChain has a large ecosystem of integrations with various external resources like loc
```

Notice that while the `UnstructuredLoader` parses Markdown headers, `TextLoader` does not.
If you need to load Python source code files, use the `PythonLoader`:
```
from langchain_community.document_loaders import PythonLoaderloader = DirectoryLoader("../../../../../", glob="**/*.py", loader_cls=PythonLoader)
```

**API Reference:**PythonLoader
## Auto-detect file encodings with TextLoader​
`DirectoryLoader` can help manage errors due to variations in file encodings. Below we will attempt to load in a collection of files, one of which includes non-UTF8 encodings.
```
path ="../../../libs/langchain/tests/unit_tests/examples/"loader = DirectoryLoader(path, glob="**/*.txt", loader_cls=TextLoader)
```

### A. Default Behavior​
By default we raise an error:
```
loader.load()
```

```
Error loading file ../../../../libs/langchain/tests/unit_tests/examples/example-non-utf8.txt
```

```
---------------------------------------------------------------------------``````outputUnicodeDecodeError            Traceback (most recent call last)``````outputFile ~/repos/langchain/libs/community/langchain_community/document_loaders/text.py:43, in TextLoader.lazy_load(self)   42   with open(self.file_path, encoding=self.encoding) as f:---> 43     text = f.read()   44 except UnicodeDecodeError as e:``````outputFile ~/.pyenv/versions/3.10.4/lib/python3.10/codecs.py:322, in BufferedIncrementalDecoder.decode(self, input, final)  321 data = self.buffer + input--> 322 (result, consumed) = self._buffer_decode(data, self.errors, final)  323 # keep undecoded input until the next call``````outputUnicodeDecodeError: 'utf-8' codec can't decode byte 0xca in position 0: invalid continuation byte``````outputThe above exception was the direct cause of the following exception:``````outputRuntimeError               Traceback (most recent call last)``````outputCell In[10], line 1----> 1 loader.load()``````outputFile ~/repos/langchain/libs/community/langchain_community/document_loaders/directory.py:117, in DirectoryLoader.load(self)  115 def load(self) -> List[Document]:  116   """Load documents."""--> 117   return list(self.lazy_load())``````outputFile ~/repos/langchain/libs/community/langchain_community/document_loaders/directory.py:182, in DirectoryLoader.lazy_load(self)  180 else:  181   for i in items:--> 182     yield from self._lazy_load_file(i, p, pbar)  184 if pbar:  185   pbar.close()``````outputFile ~/repos/langchain/libs/community/langchain_community/document_loaders/directory.py:220, in DirectoryLoader._lazy_load_file(self, item, path, pbar)  218   else:  219     logger.error(f"Error loading file {str(item)}")--> 220     raise e  221 finally:  222   if pbar:``````outputFile ~/repos/langchain/libs/community/langchain_community/document_loaders/directory.py:210, in DirectoryLoader._lazy_load_file(self, item, path, pbar)  208 loader = self.loader_cls(str(item), **self.loader_kwargs)  209 try:--> 210   for subdoc in loader.lazy_load():  211     yield subdoc  212 except NotImplementedError:``````outputFile ~/repos/langchain/libs/community/langchain_community/document_loaders/text.py:56, in TextLoader.lazy_load(self)   54         continue   55   else:---> 56     raise RuntimeError(f"Error loading {self.file_path}") from e   57 except Exception as e:   58   raise RuntimeError(f"Error loading {self.file_path}") from e``````outputRuntimeError: Error loading ../../../../libs/langchain/tests/unit_tests/examples/example-non-utf8.txt
```

The file `example-non-utf8.txt` uses a different encoding, so the `load()` function fails with a helpful message indicating which file failed decoding.
With the default behavior of `TextLoader` any failure to load any of the documents will fail the whole loading process and no documents are loaded.
### B. Silent fail​
We can pass the parameter `silent_errors` to the `DirectoryLoader` to skip the files which could not be loaded and continue the load process.
```
loader = DirectoryLoader(  path, glob="**/*.txt", loader_cls=TextLoader, silent_errors=True)docs = loader.load()
```

```
Error loading file ../../../../libs/langchain/tests/unit_tests/examples/example-non-utf8.txt: Error loading ../../../../libs/langchain/tests/unit_tests/examples/example-non-utf8.txt
```

```
doc_sources =[doc.metadata["source"]for doc in docs]doc_sources
```

```
['../../../../libs/langchain/tests/unit_tests/examples/example-utf8.txt']
```

### C. Auto detect encodings​
We can also ask `TextLoader` to auto detect the file encoding before failing, by passing the `autodetect_encoding` to the loader class.
```
text_loader_kwargs ={"autodetect_encoding":True}loader = DirectoryLoader(  path, glob="**/*.txt", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)docs = loader.load()
```

```
doc_sources =[doc.metadata["source"]for doc in docs]doc_sources
```

```
['../../../../libs/langchain/tests/unit_tests/examples/example-utf8.txt', '../../../../libs/langchain/tests/unit_tests/examples/example-non-utf8.txt']
```

#### Was this page helpful?
  * Show a progress bar
  * Use multithreading
  * Change loader class
  * Auto-detect file encodings with TextLoader
    * A. Default Behavior
    * B. Silent fail
    * C. Auto detect encodings


