Skip to content 
# `UploadFile` class¶
You can define _path operation function_ parameters to be of the type `UploadFile` to receive files from the request.
You can import it directly from `fastapi`:
```
fromfastapiimport UploadFile

```

##  fastapi.UploadFile ¶
```
UploadFile(file, *, size=None, filename=None, headers=None)

```

Bases: `UploadFile`
A file uploaded in a request.
Define it as a _path operation function_ (or dependency) parameter.
If you are using a regular `def` function, you can use the `upload_file.file` attribute to access the raw standard Python file (blocking, not async), useful and needed for non-async code.
Read more about it in the FastAPI docs for Request Files.
#### Example¶
```
fromtypingimport Annotated
fromfastapiimport FastAPI, File, UploadFile
app = FastAPI()
@app.post("/files/")
async defcreate_file(file: Annotated[bytes, File()]):
  return {"file_size": len(file)}
@app.post("/uploadfile/")
async defcreate_upload_file(file: UploadFile):
  return {"filename": file.filename}

```

PARAMETER | DESCRIPTION  
---|---  
`file` |  **TYPE:** `BinaryIO`  
`size` |  **TYPE:** `int | None` **DEFAULT:** `None`  
`filename` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `Headers | None` **DEFAULT:** `None`  
Source code in `starlette/datastructures.py`
```
414
415
416
417
418
419
420
421
422
423
424
425
```
| ```
def__init__(
  self,
  file: typing.BinaryIO,
  *,
  size: int | None = None,
  filename: str | None = None,
  headers: Headers | None = None,
) -> None:
  self.filename = filename
  self.file = file
  self.size = size
  self.headers = headers or Headers()

```
  
---|---  
###  file `instance-attribute` ¶
```
file

```

The standard Python file object (non-async).
###  filename `instance-attribute` ¶
```
filename

```

The original file name.
###  size `instance-attribute` ¶
```
size

```

The size of the file in bytes.
###  headers `instance-attribute` ¶
```
headers

```

The headers of the request.
###  content_type `instance-attribute` ¶
```
content_type

```

The content type of the request, from the headers.
###  read `async` ¶
```
read(size=-1)

```

Read some bytes from the file.
To be awaitable, compatible with async, this is run in threadpool.
PARAMETER | DESCRIPTION  
---|---  
`size` |  The number of bytes to read from the file. **TYPE:** `int` **DEFAULT:** `-1`  
Source code in `fastapi/datastructures.py`
```
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
```
| ```
async defread(
  self,
  size: Annotated[
    int,
    Doc(
"""
      The number of bytes to read from the file.
      """
    ),
  ] = -1,
) -> bytes:
"""
  Read some bytes from the file.
  To be awaitable, compatible with async, this is run in threadpool.
  """
  return await super().read(size)

```
  
---|---  
###  write `async` ¶
```
write(data)

```

Write some bytes to the file.
You normally wouldn't use this from a file you read in a request.
To be awaitable, compatible with async, this is run in threadpool.
PARAMETER | DESCRIPTION  
---|---  
`data` |  The bytes to write to the file. **TYPE:** `bytes`  
Source code in `fastapi/datastructures.py`
```
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
```
| ```
async defwrite(
  self,
  data: Annotated[
    bytes,
    Doc(
"""
      The bytes to write to the file.
      """
    ),
  ],
) -> None:
"""
  Write some bytes to the file.
  You normally wouldn't use this from a file you read in a request.
  To be awaitable, compatible with async, this is run in threadpool.
  """
  return await super().write(data)

```
  
---|---  
###  seek `async` ¶
```
seek(offset)

```

Move to a position in the file.
Any next read or write will be done from that position.
To be awaitable, compatible with async, this is run in threadpool.
PARAMETER | DESCRIPTION  
---|---  
`offset` |  The position in bytes to seek to in the file. **TYPE:** `int`  
Source code in `fastapi/datastructures.py`
```
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
```
| ```
async defseek(
  self,
  offset: Annotated[
    int,
    Doc(
"""
      The position in bytes to seek to in the file.
      """
    ),
  ],
) -> None:
"""
  Move to a position in the file.
  Any next read or write will be done from that position.
  To be awaitable, compatible with async, this is run in threadpool.
  """
  return await super().seek(offset)

```
  
---|---  
###  close `async` ¶
```
close()

```

Close the file.
To be awaitable, compatible with async, this is run in threadpool.
Source code in `fastapi/datastructures.py`
```
133
134
135
136
137
138
139
```
| ```
async defclose(self) -> None:
"""
  Close the file.
  To be awaitable, compatible with async, this is run in threadpool.
  """
  return await super().close()

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
