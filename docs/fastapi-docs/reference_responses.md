Skip to content 
# Custom Response Classes - File, HTML, Redirect, Streaming, etc.¶
There are several custom response classes you can use to create an instance and return them directly from your _path operations_.
Read more about it in the FastAPI docs for Custom Response - HTML, Stream, File, others.
You can import them directly from `fastapi.responses`:
```
fromfastapi.responsesimport (
  FileResponse,
  HTMLResponse,
  JSONResponse,
  ORJSONResponse,
  PlainTextResponse,
  RedirectResponse,
  Response,
  StreamingResponse,
  UJSONResponse,
)

```

## FastAPI Responses¶
There are a couple of custom FastAPI response classes, you can use them to optimize JSON performance.
##  fastapi.responses.UJSONResponse ¶
```
UJSONResponse(
  content,
  status_code=200,
  headers=None,
  media_type=None,
  background=None,
)

```

Bases: `JSONResponse`
JSON response using the high-performance ujson library to serialize data to JSON.
Read more about it in the FastAPI docs for Custom Response - HTML, Stream, File, others.
PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any`  
`status_code` |  **TYPE:** `int` **DEFAULT:** `200`  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
`media_type` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`background` |  **TYPE:** `BackgroundTask | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
173
174
175
176
177
178
179
180
181
```
| ```
def__init__(
  self,
  content: typing.Any,
  status_code: int = 200,
  headers: typing.Mapping[str, str] | None = None,
  media_type: str | None = None,
  background: BackgroundTask | None = None,
) -> None:
  super().__init__(content, status_code, headers, media_type, background)

```
  
---|---  
###  charset `class-attribute` `instance-attribute` ¶
```
charset = 'utf-8'

```

###  status_code `instance-attribute` ¶
```
status_code = status_code

```

###  media_type `class-attribute` `instance-attribute` ¶
```
media_type = 'application/json'

```

###  body `instance-attribute` ¶
```
body = render(content)

```

###  background `instance-attribute` ¶
```
background = background

```

###  headers `property` ¶
```
headers

```

###  render ¶
```
render(content)

```

PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any`  
Source code in `fastapi/responses.py`
```
31
32
33
```
| ```
defrender(self, content: Any) -> bytes:
  assert ujson is not None, "ujson must be installed to use UJSONResponse"
  return ujson.dumps(content, ensure_ascii=False).encode("utf-8")

```
  
---|---  
###  init_headers ¶
```
init_headers(headers=None)

```

PARAMETER | DESCRIPTION  
---|---  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
```
| ```
definit_headers(self, headers: typing.Mapping[str, str] | None = None) -> None:
  if headers is None:
    raw_headers: list[tuple[bytes, bytes]] = []
    populate_content_length = True
    populate_content_type = True
  else:
    raw_headers = [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]
    keys = [h[0] for h in raw_headers]
    populate_content_length = b"content-length" not in keys
    populate_content_type = b"content-type" not in keys
  body = getattr(self, "body", None)
  if (
    body is not None
    and populate_content_length
    and not (self.status_code < 200 or self.status_code in (204, 304))
  ):
    content_length = str(len(body))
    raw_headers.append((b"content-length", content_length.encode("latin-1")))
  content_type = self.media_type
  if content_type is not None and populate_content_type:
    if content_type.startswith("text/") and "charset=" not in content_type.lower():
      content_type += "; charset=" + self.charset
    raw_headers.append((b"content-type", content_type.encode("latin-1")))
  self.raw_headers = raw_headers

```
  
---|---  
###  set_cookie ¶
```
set_cookie(
  key,
  value="",
  max_age=None,
  expires=None,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`value` |  **TYPE:** `str` **DEFAULT:** `''`  
`max_age` |  **TYPE:** `int | None` **DEFAULT:** `None`  
`expires` |  **TYPE:** `datetime | str | int | None` **DEFAULT:** `None`  
`path` |  **TYPE:** `str | None` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
 88
 89
 90
 91
 92
 93
 94
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
112
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
```
| ```
defset_cookie(
  self,
  key: str,
  value: str = "",
  max_age: int | None = None,
  expires: datetime | str | int | None = None,
  path: str | None = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  cookie: http.cookies.BaseCookie[str] = http.cookies.SimpleCookie()
  cookie[key] = value
  if max_age is not None:
    cookie[key]["max-age"] = max_age
  if expires is not None:
    if isinstance(expires, datetime):
      cookie[key]["expires"] = format_datetime(expires, usegmt=True)
    else:
      cookie[key]["expires"] = expires
  if path is not None:
    cookie[key]["path"] = path
  if domain is not None:
    cookie[key]["domain"] = domain
  if secure:
    cookie[key]["secure"] = True
  if httponly:
    cookie[key]["httponly"] = True
  if samesite is not None:
    assert samesite.lower() in [
      "strict",
      "lax",
      "none",
    ], "samesite must be either 'strict', 'lax' or 'none'"
    cookie[key]["samesite"] = samesite
  cookie_val = cookie.output(header="").strip()
  self.raw_headers.append((b"set-cookie", cookie_val.encode("latin-1")))

```
  
---|---  
###  delete_cookie ¶
```
delete_cookie(
  key,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`path` |  **TYPE:** `str` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
```
| ```
defdelete_cookie(
  self,
  key: str,
  path: str = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  self.set_cookie(
    key,
    max_age=0,
    expires=0,
    path=path,
    domain=domain,
    secure=secure,
    httponly=httponly,
    samesite=samesite,
  )

```
  
---|---  
##  fastapi.responses.ORJSONResponse ¶
```
ORJSONResponse(
  content,
  status_code=200,
  headers=None,
  media_type=None,
  background=None,
)

```

Bases: `JSONResponse`
JSON response using the high-performance orjson library to serialize data to JSON.
Read more about it in the FastAPI docs for Custom Response - HTML, Stream, File, others.
PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any`  
`status_code` |  **TYPE:** `int` **DEFAULT:** `200`  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
`media_type` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`background` |  **TYPE:** `BackgroundTask | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
173
174
175
176
177
178
179
180
181
```
| ```
def__init__(
  self,
  content: typing.Any,
  status_code: int = 200,
  headers: typing.Mapping[str, str] | None = None,
  media_type: str | None = None,
  background: BackgroundTask | None = None,
) -> None:
  super().__init__(content, status_code, headers, media_type, background)

```
  
---|---  
###  charset `class-attribute` `instance-attribute` ¶
```
charset = 'utf-8'

```

###  status_code `instance-attribute` ¶
```
status_code = status_code

```

###  media_type `class-attribute` `instance-attribute` ¶
```
media_type = 'application/json'

```

###  body `instance-attribute` ¶
```
body = render(content)

```

###  background `instance-attribute` ¶
```
background = background

```

###  headers `property` ¶
```
headers

```

###  render ¶
```
render(content)

```

PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any`  
Source code in `fastapi/responses.py`
```
44
45
46
47
48
```
| ```
defrender(self, content: Any) -> bytes:
  assert orjson is not None, "orjson must be installed to use ORJSONResponse"
  return orjson.dumps(
    content, option=orjson.OPT_NON_STR_KEYS | orjson.OPT_SERIALIZE_NUMPY
  )

```
  
---|---  
###  init_headers ¶
```
init_headers(headers=None)

```

PARAMETER | DESCRIPTION  
---|---  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
```
| ```
definit_headers(self, headers: typing.Mapping[str, str] | None = None) -> None:
  if headers is None:
    raw_headers: list[tuple[bytes, bytes]] = []
    populate_content_length = True
    populate_content_type = True
  else:
    raw_headers = [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]
    keys = [h[0] for h in raw_headers]
    populate_content_length = b"content-length" not in keys
    populate_content_type = b"content-type" not in keys
  body = getattr(self, "body", None)
  if (
    body is not None
    and populate_content_length
    and not (self.status_code < 200 or self.status_code in (204, 304))
  ):
    content_length = str(len(body))
    raw_headers.append((b"content-length", content_length.encode("latin-1")))
  content_type = self.media_type
  if content_type is not None and populate_content_type:
    if content_type.startswith("text/") and "charset=" not in content_type.lower():
      content_type += "; charset=" + self.charset
    raw_headers.append((b"content-type", content_type.encode("latin-1")))
  self.raw_headers = raw_headers

```
  
---|---  
###  set_cookie ¶
```
set_cookie(
  key,
  value="",
  max_age=None,
  expires=None,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`value` |  **TYPE:** `str` **DEFAULT:** `''`  
`max_age` |  **TYPE:** `int | None` **DEFAULT:** `None`  
`expires` |  **TYPE:** `datetime | str | int | None` **DEFAULT:** `None`  
`path` |  **TYPE:** `str | None` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
 88
 89
 90
 91
 92
 93
 94
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
112
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
```
| ```
defset_cookie(
  self,
  key: str,
  value: str = "",
  max_age: int | None = None,
  expires: datetime | str | int | None = None,
  path: str | None = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  cookie: http.cookies.BaseCookie[str] = http.cookies.SimpleCookie()
  cookie[key] = value
  if max_age is not None:
    cookie[key]["max-age"] = max_age
  if expires is not None:
    if isinstance(expires, datetime):
      cookie[key]["expires"] = format_datetime(expires, usegmt=True)
    else:
      cookie[key]["expires"] = expires
  if path is not None:
    cookie[key]["path"] = path
  if domain is not None:
    cookie[key]["domain"] = domain
  if secure:
    cookie[key]["secure"] = True
  if httponly:
    cookie[key]["httponly"] = True
  if samesite is not None:
    assert samesite.lower() in [
      "strict",
      "lax",
      "none",
    ], "samesite must be either 'strict', 'lax' or 'none'"
    cookie[key]["samesite"] = samesite
  cookie_val = cookie.output(header="").strip()
  self.raw_headers.append((b"set-cookie", cookie_val.encode("latin-1")))

```
  
---|---  
###  delete_cookie ¶
```
delete_cookie(
  key,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`path` |  **TYPE:** `str` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
```
| ```
defdelete_cookie(
  self,
  key: str,
  path: str = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  self.set_cookie(
    key,
    max_age=0,
    expires=0,
    path=path,
    domain=domain,
    secure=secure,
    httponly=httponly,
    samesite=samesite,
  )

```
  
---|---  
## Starlette Responses¶
##  fastapi.responses.FileResponse ¶
```
FileResponse(
  path,
  status_code=200,
  headers=None,
  media_type=None,
  background=None,
  filename=None,
  stat_result=None,
  method=None,
  content_disposition_type="attachment",
)

```

Bases: `Response`
PARAMETER | DESCRIPTION  
---|---  
`path` |  **TYPE:** `str | PathLike[str]`  
`status_code` |  **TYPE:** `int` **DEFAULT:** `200`  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
`media_type` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`background` |  **TYPE:** `BackgroundTask | None` **DEFAULT:** `None`  
`filename` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`stat_result` |  **TYPE:** `stat_result | None` **DEFAULT:** `None`  
`method` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`content_disposition_type` |  **TYPE:** `str` **DEFAULT:** `'attachment'`  
Source code in `starlette/responses.py`
```
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
```
| ```
def__init__(
  self,
  path: str | os.PathLike[str],
  status_code: int = 200,
  headers: typing.Mapping[str, str] | None = None,
  media_type: str | None = None,
  background: BackgroundTask | None = None,
  filename: str | None = None,
  stat_result: os.stat_result | None = None,
  method: str | None = None,
  content_disposition_type: str = "attachment",
) -> None:
  self.path = path
  self.status_code = status_code
  self.filename = filename
  if method is not None:
    warnings.warn(
      "The 'method' parameter is not used, and it will be removed.",
      DeprecationWarning,
    )
  if media_type is None:
    media_type = guess_type(filename or path)[0] or "text/plain"
  self.media_type = media_type
  self.background = background
  self.init_headers(headers)
  self.headers.setdefault("accept-ranges", "bytes")
  if self.filename is not None:
    content_disposition_filename = quote(self.filename)
    if content_disposition_filename != self.filename:
      content_disposition = f"{content_disposition_type}; filename*=utf-8''{content_disposition_filename}"
    else:
      content_disposition = f'{content_disposition_type}; filename="{self.filename}"'
    self.headers.setdefault("content-disposition", content_disposition)
  self.stat_result = stat_result
  if stat_result is not None:
    self.set_stat_headers(stat_result)

```
  
---|---  
###  chunk_size `class-attribute` `instance-attribute` ¶
```
chunk_size = 64 * 1024

```

###  charset `class-attribute` `instance-attribute` ¶
```
charset = 'utf-8'

```

###  status_code `instance-attribute` ¶
```
status_code = status_code

```

###  media_type `instance-attribute` ¶
```
media_type = media_type

```

###  body `instance-attribute` ¶
```
body = render(content)

```

###  background `instance-attribute` ¶
```
background = background

```

###  headers `property` ¶
```
headers

```

###  render ¶
```
render(content)

```

PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any`  
Source code in `starlette/responses.py`
```
47
48
49
50
51
52
```
| ```
defrender(self, content: typing.Any) -> bytes | memoryview:
  if content is None:
    return b""
  if isinstance(content, (bytes, memoryview)):
    return content
  return content.encode(self.charset) # type: ignore

```
  
---|---  
###  init_headers ¶
```
init_headers(headers=None)

```

PARAMETER | DESCRIPTION  
---|---  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
```
| ```
definit_headers(self, headers: typing.Mapping[str, str] | None = None) -> None:
  if headers is None:
    raw_headers: list[tuple[bytes, bytes]] = []
    populate_content_length = True
    populate_content_type = True
  else:
    raw_headers = [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]
    keys = [h[0] for h in raw_headers]
    populate_content_length = b"content-length" not in keys
    populate_content_type = b"content-type" not in keys
  body = getattr(self, "body", None)
  if (
    body is not None
    and populate_content_length
    and not (self.status_code < 200 or self.status_code in (204, 304))
  ):
    content_length = str(len(body))
    raw_headers.append((b"content-length", content_length.encode("latin-1")))
  content_type = self.media_type
  if content_type is not None and populate_content_type:
    if content_type.startswith("text/") and "charset=" not in content_type.lower():
      content_type += "; charset=" + self.charset
    raw_headers.append((b"content-type", content_type.encode("latin-1")))
  self.raw_headers = raw_headers

```
  
---|---  
###  set_cookie ¶
```
set_cookie(
  key,
  value="",
  max_age=None,
  expires=None,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`value` |  **TYPE:** `str` **DEFAULT:** `''`  
`max_age` |  **TYPE:** `int | None` **DEFAULT:** `None`  
`expires` |  **TYPE:** `datetime | str | int | None` **DEFAULT:** `None`  
`path` |  **TYPE:** `str | None` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
 88
 89
 90
 91
 92
 93
 94
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
112
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
```
| ```
defset_cookie(
  self,
  key: str,
  value: str = "",
  max_age: int | None = None,
  expires: datetime | str | int | None = None,
  path: str | None = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  cookie: http.cookies.BaseCookie[str] = http.cookies.SimpleCookie()
  cookie[key] = value
  if max_age is not None:
    cookie[key]["max-age"] = max_age
  if expires is not None:
    if isinstance(expires, datetime):
      cookie[key]["expires"] = format_datetime(expires, usegmt=True)
    else:
      cookie[key]["expires"] = expires
  if path is not None:
    cookie[key]["path"] = path
  if domain is not None:
    cookie[key]["domain"] = domain
  if secure:
    cookie[key]["secure"] = True
  if httponly:
    cookie[key]["httponly"] = True
  if samesite is not None:
    assert samesite.lower() in [
      "strict",
      "lax",
      "none",
    ], "samesite must be either 'strict', 'lax' or 'none'"
    cookie[key]["samesite"] = samesite
  cookie_val = cookie.output(header="").strip()
  self.raw_headers.append((b"set-cookie", cookie_val.encode("latin-1")))

```
  
---|---  
###  delete_cookie ¶
```
delete_cookie(
  key,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`path` |  **TYPE:** `str` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
```
| ```
defdelete_cookie(
  self,
  key: str,
  path: str = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  self.set_cookie(
    key,
    max_age=0,
    expires=0,
    path=path,
    domain=domain,
    secure=secure,
    httponly=httponly,
    samesite=samesite,
  )

```
  
---|---  
##  fastapi.responses.HTMLResponse ¶
```
HTMLResponse(
  content=None,
  status_code=200,
  headers=None,
  media_type=None,
  background=None,
)

```

Bases: `Response`
PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any` **DEFAULT:** `None`  
`status_code` |  **TYPE:** `int` **DEFAULT:** `200`  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
`media_type` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`background` |  **TYPE:** `BackgroundTask | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
32
33
34
35
36
37
38
39
40
41
42
43
44
45
```
| ```
def__init__(
  self,
  content: typing.Any = None,
  status_code: int = 200,
  headers: typing.Mapping[str, str] | None = None,
  media_type: str | None = None,
  background: BackgroundTask | None = None,
) -> None:
  self.status_code = status_code
  if media_type is not None:
    self.media_type = media_type
  self.background = background
  self.body = self.render(content)
  self.init_headers(headers)

```
  
---|---  
###  charset `class-attribute` `instance-attribute` ¶
```
charset = 'utf-8'

```

###  status_code `instance-attribute` ¶
```
status_code = status_code

```

###  media_type `class-attribute` `instance-attribute` ¶
```
media_type = 'text/html'

```

###  body `instance-attribute` ¶
```
body = render(content)

```

###  background `instance-attribute` ¶
```
background = background

```

###  headers `property` ¶
```
headers

```

###  render ¶
```
render(content)

```

PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any`  
Source code in `starlette/responses.py`
```
47
48
49
50
51
52
```
| ```
defrender(self, content: typing.Any) -> bytes | memoryview:
  if content is None:
    return b""
  if isinstance(content, (bytes, memoryview)):
    return content
  return content.encode(self.charset) # type: ignore

```
  
---|---  
###  init_headers ¶
```
init_headers(headers=None)

```

PARAMETER | DESCRIPTION  
---|---  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
```
| ```
definit_headers(self, headers: typing.Mapping[str, str] | None = None) -> None:
  if headers is None:
    raw_headers: list[tuple[bytes, bytes]] = []
    populate_content_length = True
    populate_content_type = True
  else:
    raw_headers = [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]
    keys = [h[0] for h in raw_headers]
    populate_content_length = b"content-length" not in keys
    populate_content_type = b"content-type" not in keys
  body = getattr(self, "body", None)
  if (
    body is not None
    and populate_content_length
    and not (self.status_code < 200 or self.status_code in (204, 304))
  ):
    content_length = str(len(body))
    raw_headers.append((b"content-length", content_length.encode("latin-1")))
  content_type = self.media_type
  if content_type is not None and populate_content_type:
    if content_type.startswith("text/") and "charset=" not in content_type.lower():
      content_type += "; charset=" + self.charset
    raw_headers.append((b"content-type", content_type.encode("latin-1")))
  self.raw_headers = raw_headers

```
  
---|---  
###  set_cookie ¶
```
set_cookie(
  key,
  value="",
  max_age=None,
  expires=None,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`value` |  **TYPE:** `str` **DEFAULT:** `''`  
`max_age` |  **TYPE:** `int | None` **DEFAULT:** `None`  
`expires` |  **TYPE:** `datetime | str | int | None` **DEFAULT:** `None`  
`path` |  **TYPE:** `str | None` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
 88
 89
 90
 91
 92
 93
 94
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
112
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
```
| ```
defset_cookie(
  self,
  key: str,
  value: str = "",
  max_age: int | None = None,
  expires: datetime | str | int | None = None,
  path: str | None = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  cookie: http.cookies.BaseCookie[str] = http.cookies.SimpleCookie()
  cookie[key] = value
  if max_age is not None:
    cookie[key]["max-age"] = max_age
  if expires is not None:
    if isinstance(expires, datetime):
      cookie[key]["expires"] = format_datetime(expires, usegmt=True)
    else:
      cookie[key]["expires"] = expires
  if path is not None:
    cookie[key]["path"] = path
  if domain is not None:
    cookie[key]["domain"] = domain
  if secure:
    cookie[key]["secure"] = True
  if httponly:
    cookie[key]["httponly"] = True
  if samesite is not None:
    assert samesite.lower() in [
      "strict",
      "lax",
      "none",
    ], "samesite must be either 'strict', 'lax' or 'none'"
    cookie[key]["samesite"] = samesite
  cookie_val = cookie.output(header="").strip()
  self.raw_headers.append((b"set-cookie", cookie_val.encode("latin-1")))

```
  
---|---  
###  delete_cookie ¶
```
delete_cookie(
  key,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`path` |  **TYPE:** `str` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
```
| ```
defdelete_cookie(
  self,
  key: str,
  path: str = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  self.set_cookie(
    key,
    max_age=0,
    expires=0,
    path=path,
    domain=domain,
    secure=secure,
    httponly=httponly,
    samesite=samesite,
  )

```
  
---|---  
##  fastapi.responses.JSONResponse ¶
```
JSONResponse(
  content,
  status_code=200,
  headers=None,
  media_type=None,
  background=None,
)

```

Bases: `Response`
PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any`  
`status_code` |  **TYPE:** `int` **DEFAULT:** `200`  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
`media_type` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`background` |  **TYPE:** `BackgroundTask | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
173
174
175
176
177
178
179
180
181
```
| ```
def__init__(
  self,
  content: typing.Any,
  status_code: int = 200,
  headers: typing.Mapping[str, str] | None = None,
  media_type: str | None = None,
  background: BackgroundTask | None = None,
) -> None:
  super().__init__(content, status_code, headers, media_type, background)

```
  
---|---  
###  charset `class-attribute` `instance-attribute` ¶
```
charset = 'utf-8'

```

###  status_code `instance-attribute` ¶
```
status_code = status_code

```

###  media_type `class-attribute` `instance-attribute` ¶
```
media_type = 'application/json'

```

###  body `instance-attribute` ¶
```
body = render(content)

```

###  background `instance-attribute` ¶
```
background = background

```

###  headers `property` ¶
```
headers

```

###  render ¶
```
render(content)

```

PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any`  
Source code in `starlette/responses.py`
```
183
184
185
186
187
188
189
190
```
| ```
defrender(self, content: typing.Any) -> bytes:
  return json.dumps(
    content,
    ensure_ascii=False,
    allow_nan=False,
    indent=None,
    separators=(",", ":"),
  ).encode("utf-8")

```
  
---|---  
###  init_headers ¶
```
init_headers(headers=None)

```

PARAMETER | DESCRIPTION  
---|---  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
```
| ```
definit_headers(self, headers: typing.Mapping[str, str] | None = None) -> None:
  if headers is None:
    raw_headers: list[tuple[bytes, bytes]] = []
    populate_content_length = True
    populate_content_type = True
  else:
    raw_headers = [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]
    keys = [h[0] for h in raw_headers]
    populate_content_length = b"content-length" not in keys
    populate_content_type = b"content-type" not in keys
  body = getattr(self, "body", None)
  if (
    body is not None
    and populate_content_length
    and not (self.status_code < 200 or self.status_code in (204, 304))
  ):
    content_length = str(len(body))
    raw_headers.append((b"content-length", content_length.encode("latin-1")))
  content_type = self.media_type
  if content_type is not None and populate_content_type:
    if content_type.startswith("text/") and "charset=" not in content_type.lower():
      content_type += "; charset=" + self.charset
    raw_headers.append((b"content-type", content_type.encode("latin-1")))
  self.raw_headers = raw_headers

```
  
---|---  
###  set_cookie ¶
```
set_cookie(
  key,
  value="",
  max_age=None,
  expires=None,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`value` |  **TYPE:** `str` **DEFAULT:** `''`  
`max_age` |  **TYPE:** `int | None` **DEFAULT:** `None`  
`expires` |  **TYPE:** `datetime | str | int | None` **DEFAULT:** `None`  
`path` |  **TYPE:** `str | None` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
 88
 89
 90
 91
 92
 93
 94
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
112
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
```
| ```
defset_cookie(
  self,
  key: str,
  value: str = "",
  max_age: int | None = None,
  expires: datetime | str | int | None = None,
  path: str | None = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  cookie: http.cookies.BaseCookie[str] = http.cookies.SimpleCookie()
  cookie[key] = value
  if max_age is not None:
    cookie[key]["max-age"] = max_age
  if expires is not None:
    if isinstance(expires, datetime):
      cookie[key]["expires"] = format_datetime(expires, usegmt=True)
    else:
      cookie[key]["expires"] = expires
  if path is not None:
    cookie[key]["path"] = path
  if domain is not None:
    cookie[key]["domain"] = domain
  if secure:
    cookie[key]["secure"] = True
  if httponly:
    cookie[key]["httponly"] = True
  if samesite is not None:
    assert samesite.lower() in [
      "strict",
      "lax",
      "none",
    ], "samesite must be either 'strict', 'lax' or 'none'"
    cookie[key]["samesite"] = samesite
  cookie_val = cookie.output(header="").strip()
  self.raw_headers.append((b"set-cookie", cookie_val.encode("latin-1")))

```
  
---|---  
###  delete_cookie ¶
```
delete_cookie(
  key,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`path` |  **TYPE:** `str` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
```
| ```
defdelete_cookie(
  self,
  key: str,
  path: str = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  self.set_cookie(
    key,
    max_age=0,
    expires=0,
    path=path,
    domain=domain,
    secure=secure,
    httponly=httponly,
    samesite=samesite,
  )

```
  
---|---  
##  fastapi.responses.PlainTextResponse ¶
```
PlainTextResponse(
  content=None,
  status_code=200,
  headers=None,
  media_type=None,
  background=None,
)

```

Bases: `Response`
PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any` **DEFAULT:** `None`  
`status_code` |  **TYPE:** `int` **DEFAULT:** `200`  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
`media_type` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`background` |  **TYPE:** `BackgroundTask | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
32
33
34
35
36
37
38
39
40
41
42
43
44
45
```
| ```
def__init__(
  self,
  content: typing.Any = None,
  status_code: int = 200,
  headers: typing.Mapping[str, str] | None = None,
  media_type: str | None = None,
  background: BackgroundTask | None = None,
) -> None:
  self.status_code = status_code
  if media_type is not None:
    self.media_type = media_type
  self.background = background
  self.body = self.render(content)
  self.init_headers(headers)

```
  
---|---  
###  charset `class-attribute` `instance-attribute` ¶
```
charset = 'utf-8'

```

###  status_code `instance-attribute` ¶
```
status_code = status_code

```

###  media_type `class-attribute` `instance-attribute` ¶
```
media_type = 'text/plain'

```

###  body `instance-attribute` ¶
```
body = render(content)

```

###  background `instance-attribute` ¶
```
background = background

```

###  headers `property` ¶
```
headers

```

###  render ¶
```
render(content)

```

PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any`  
Source code in `starlette/responses.py`
```
47
48
49
50
51
52
```
| ```
defrender(self, content: typing.Any) -> bytes | memoryview:
  if content is None:
    return b""
  if isinstance(content, (bytes, memoryview)):
    return content
  return content.encode(self.charset) # type: ignore

```
  
---|---  
###  init_headers ¶
```
init_headers(headers=None)

```

PARAMETER | DESCRIPTION  
---|---  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
```
| ```
definit_headers(self, headers: typing.Mapping[str, str] | None = None) -> None:
  if headers is None:
    raw_headers: list[tuple[bytes, bytes]] = []
    populate_content_length = True
    populate_content_type = True
  else:
    raw_headers = [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]
    keys = [h[0] for h in raw_headers]
    populate_content_length = b"content-length" not in keys
    populate_content_type = b"content-type" not in keys
  body = getattr(self, "body", None)
  if (
    body is not None
    and populate_content_length
    and not (self.status_code < 200 or self.status_code in (204, 304))
  ):
    content_length = str(len(body))
    raw_headers.append((b"content-length", content_length.encode("latin-1")))
  content_type = self.media_type
  if content_type is not None and populate_content_type:
    if content_type.startswith("text/") and "charset=" not in content_type.lower():
      content_type += "; charset=" + self.charset
    raw_headers.append((b"content-type", content_type.encode("latin-1")))
  self.raw_headers = raw_headers

```
  
---|---  
###  set_cookie ¶
```
set_cookie(
  key,
  value="",
  max_age=None,
  expires=None,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`value` |  **TYPE:** `str` **DEFAULT:** `''`  
`max_age` |  **TYPE:** `int | None` **DEFAULT:** `None`  
`expires` |  **TYPE:** `datetime | str | int | None` **DEFAULT:** `None`  
`path` |  **TYPE:** `str | None` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
 88
 89
 90
 91
 92
 93
 94
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
112
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
```
| ```
defset_cookie(
  self,
  key: str,
  value: str = "",
  max_age: int | None = None,
  expires: datetime | str | int | None = None,
  path: str | None = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  cookie: http.cookies.BaseCookie[str] = http.cookies.SimpleCookie()
  cookie[key] = value
  if max_age is not None:
    cookie[key]["max-age"] = max_age
  if expires is not None:
    if isinstance(expires, datetime):
      cookie[key]["expires"] = format_datetime(expires, usegmt=True)
    else:
      cookie[key]["expires"] = expires
  if path is not None:
    cookie[key]["path"] = path
  if domain is not None:
    cookie[key]["domain"] = domain
  if secure:
    cookie[key]["secure"] = True
  if httponly:
    cookie[key]["httponly"] = True
  if samesite is not None:
    assert samesite.lower() in [
      "strict",
      "lax",
      "none",
    ], "samesite must be either 'strict', 'lax' or 'none'"
    cookie[key]["samesite"] = samesite
  cookie_val = cookie.output(header="").strip()
  self.raw_headers.append((b"set-cookie", cookie_val.encode("latin-1")))

```
  
---|---  
###  delete_cookie ¶
```
delete_cookie(
  key,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`path` |  **TYPE:** `str` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
```
| ```
defdelete_cookie(
  self,
  key: str,
  path: str = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  self.set_cookie(
    key,
    max_age=0,
    expires=0,
    path=path,
    domain=domain,
    secure=secure,
    httponly=httponly,
    samesite=samesite,
  )

```
  
---|---  
##  fastapi.responses.RedirectResponse ¶
```
RedirectResponse(
  url, status_code=307, headers=None, background=None
)

```

Bases: `Response`
PARAMETER | DESCRIPTION  
---|---  
`url` |  **TYPE:** `str | URL`  
`status_code` |  **TYPE:** `int` **DEFAULT:** `307`  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
`background` |  **TYPE:** `BackgroundTask | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
194
195
196
197
198
199
200
201
202
```
| ```
def__init__(
  self,
  url: str | URL,
  status_code: int = 307,
  headers: typing.Mapping[str, str] | None = None,
  background: BackgroundTask | None = None,
) -> None:
  super().__init__(content=b"", status_code=status_code, headers=headers, background=background)
  self.headers["location"] = quote(str(url), safe=":/%#?=@[]!$&'()*+,;")

```
  
---|---  
###  charset `class-attribute` `instance-attribute` ¶
```
charset = 'utf-8'

```

###  status_code `instance-attribute` ¶
```
status_code = status_code

```

###  media_type `class-attribute` `instance-attribute` ¶
```
media_type = None

```

###  body `instance-attribute` ¶
```
body = render(content)

```

###  background `instance-attribute` ¶
```
background = background

```

###  headers `property` ¶
```
headers

```

###  render ¶
```
render(content)

```

PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any`  
Source code in `starlette/responses.py`
```
47
48
49
50
51
52
```
| ```
defrender(self, content: typing.Any) -> bytes | memoryview:
  if content is None:
    return b""
  if isinstance(content, (bytes, memoryview)):
    return content
  return content.encode(self.charset) # type: ignore

```
  
---|---  
###  init_headers ¶
```
init_headers(headers=None)

```

PARAMETER | DESCRIPTION  
---|---  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
```
| ```
definit_headers(self, headers: typing.Mapping[str, str] | None = None) -> None:
  if headers is None:
    raw_headers: list[tuple[bytes, bytes]] = []
    populate_content_length = True
    populate_content_type = True
  else:
    raw_headers = [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]
    keys = [h[0] for h in raw_headers]
    populate_content_length = b"content-length" not in keys
    populate_content_type = b"content-type" not in keys
  body = getattr(self, "body", None)
  if (
    body is not None
    and populate_content_length
    and not (self.status_code < 200 or self.status_code in (204, 304))
  ):
    content_length = str(len(body))
    raw_headers.append((b"content-length", content_length.encode("latin-1")))
  content_type = self.media_type
  if content_type is not None and populate_content_type:
    if content_type.startswith("text/") and "charset=" not in content_type.lower():
      content_type += "; charset=" + self.charset
    raw_headers.append((b"content-type", content_type.encode("latin-1")))
  self.raw_headers = raw_headers

```
  
---|---  
###  set_cookie ¶
```
set_cookie(
  key,
  value="",
  max_age=None,
  expires=None,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`value` |  **TYPE:** `str` **DEFAULT:** `''`  
`max_age` |  **TYPE:** `int | None` **DEFAULT:** `None`  
`expires` |  **TYPE:** `datetime | str | int | None` **DEFAULT:** `None`  
`path` |  **TYPE:** `str | None` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
 88
 89
 90
 91
 92
 93
 94
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
112
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
```
| ```
defset_cookie(
  self,
  key: str,
  value: str = "",
  max_age: int | None = None,
  expires: datetime | str | int | None = None,
  path: str | None = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  cookie: http.cookies.BaseCookie[str] = http.cookies.SimpleCookie()
  cookie[key] = value
  if max_age is not None:
    cookie[key]["max-age"] = max_age
  if expires is not None:
    if isinstance(expires, datetime):
      cookie[key]["expires"] = format_datetime(expires, usegmt=True)
    else:
      cookie[key]["expires"] = expires
  if path is not None:
    cookie[key]["path"] = path
  if domain is not None:
    cookie[key]["domain"] = domain
  if secure:
    cookie[key]["secure"] = True
  if httponly:
    cookie[key]["httponly"] = True
  if samesite is not None:
    assert samesite.lower() in [
      "strict",
      "lax",
      "none",
    ], "samesite must be either 'strict', 'lax' or 'none'"
    cookie[key]["samesite"] = samesite
  cookie_val = cookie.output(header="").strip()
  self.raw_headers.append((b"set-cookie", cookie_val.encode("latin-1")))

```
  
---|---  
###  delete_cookie ¶
```
delete_cookie(
  key,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`path` |  **TYPE:** `str` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
```
| ```
defdelete_cookie(
  self,
  key: str,
  path: str = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  self.set_cookie(
    key,
    max_age=0,
    expires=0,
    path=path,
    domain=domain,
    secure=secure,
    httponly=httponly,
    samesite=samesite,
  )

```
  
---|---  
##  fastapi.responses.Response ¶
```
Response(
  content=None,
  status_code=200,
  headers=None,
  media_type=None,
  background=None,
)

```

PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any` **DEFAULT:** `None`  
`status_code` |  **TYPE:** `int` **DEFAULT:** `200`  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
`media_type` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`background` |  **TYPE:** `BackgroundTask | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
32
33
34
35
36
37
38
39
40
41
42
43
44
45
```
| ```
def__init__(
  self,
  content: typing.Any = None,
  status_code: int = 200,
  headers: typing.Mapping[str, str] | None = None,
  media_type: str | None = None,
  background: BackgroundTask | None = None,
) -> None:
  self.status_code = status_code
  if media_type is not None:
    self.media_type = media_type
  self.background = background
  self.body = self.render(content)
  self.init_headers(headers)

```
  
---|---  
###  charset `class-attribute` `instance-attribute` ¶
```
charset = 'utf-8'

```

###  status_code `instance-attribute` ¶
```
status_code = status_code

```

###  media_type `class-attribute` `instance-attribute` ¶
```
media_type = None

```

###  body `instance-attribute` ¶
```
body = render(content)

```

###  background `instance-attribute` ¶
```
background = background

```

###  headers `property` ¶
```
headers

```

###  render ¶
```
render(content)

```

PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any`  
Source code in `starlette/responses.py`
```
47
48
49
50
51
52
```
| ```
defrender(self, content: typing.Any) -> bytes | memoryview:
  if content is None:
    return b""
  if isinstance(content, (bytes, memoryview)):
    return content
  return content.encode(self.charset) # type: ignore

```
  
---|---  
###  init_headers ¶
```
init_headers(headers=None)

```

PARAMETER | DESCRIPTION  
---|---  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
```
| ```
definit_headers(self, headers: typing.Mapping[str, str] | None = None) -> None:
  if headers is None:
    raw_headers: list[tuple[bytes, bytes]] = []
    populate_content_length = True
    populate_content_type = True
  else:
    raw_headers = [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]
    keys = [h[0] for h in raw_headers]
    populate_content_length = b"content-length" not in keys
    populate_content_type = b"content-type" not in keys
  body = getattr(self, "body", None)
  if (
    body is not None
    and populate_content_length
    and not (self.status_code < 200 or self.status_code in (204, 304))
  ):
    content_length = str(len(body))
    raw_headers.append((b"content-length", content_length.encode("latin-1")))
  content_type = self.media_type
  if content_type is not None and populate_content_type:
    if content_type.startswith("text/") and "charset=" not in content_type.lower():
      content_type += "; charset=" + self.charset
    raw_headers.append((b"content-type", content_type.encode("latin-1")))
  self.raw_headers = raw_headers

```
  
---|---  
###  set_cookie ¶
```
set_cookie(
  key,
  value="",
  max_age=None,
  expires=None,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`value` |  **TYPE:** `str` **DEFAULT:** `''`  
`max_age` |  **TYPE:** `int | None` **DEFAULT:** `None`  
`expires` |  **TYPE:** `datetime | str | int | None` **DEFAULT:** `None`  
`path` |  **TYPE:** `str | None` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
 88
 89
 90
 91
 92
 93
 94
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
112
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
```
| ```
defset_cookie(
  self,
  key: str,
  value: str = "",
  max_age: int | None = None,
  expires: datetime | str | int | None = None,
  path: str | None = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  cookie: http.cookies.BaseCookie[str] = http.cookies.SimpleCookie()
  cookie[key] = value
  if max_age is not None:
    cookie[key]["max-age"] = max_age
  if expires is not None:
    if isinstance(expires, datetime):
      cookie[key]["expires"] = format_datetime(expires, usegmt=True)
    else:
      cookie[key]["expires"] = expires
  if path is not None:
    cookie[key]["path"] = path
  if domain is not None:
    cookie[key]["domain"] = domain
  if secure:
    cookie[key]["secure"] = True
  if httponly:
    cookie[key]["httponly"] = True
  if samesite is not None:
    assert samesite.lower() in [
      "strict",
      "lax",
      "none",
    ], "samesite must be either 'strict', 'lax' or 'none'"
    cookie[key]["samesite"] = samesite
  cookie_val = cookie.output(header="").strip()
  self.raw_headers.append((b"set-cookie", cookie_val.encode("latin-1")))

```
  
---|---  
###  delete_cookie ¶
```
delete_cookie(
  key,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`path` |  **TYPE:** `str` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
```
| ```
defdelete_cookie(
  self,
  key: str,
  path: str = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  self.set_cookie(
    key,
    max_age=0,
    expires=0,
    path=path,
    domain=domain,
    secure=secure,
    httponly=httponly,
    samesite=samesite,
  )

```
  
---|---  
##  fastapi.responses.StreamingResponse ¶
```
StreamingResponse(
  content,
  status_code=200,
  headers=None,
  media_type=None,
  background=None,
)

```

Bases: `Response`
PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `ContentStream`  
`status_code` |  **TYPE:** `int` **DEFAULT:** `200`  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
`media_type` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`background` |  **TYPE:** `BackgroundTask | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
```
| ```
def__init__(
  self,
  content: ContentStream,
  status_code: int = 200,
  headers: typing.Mapping[str, str] | None = None,
  media_type: str | None = None,
  background: BackgroundTask | None = None,
) -> None:
  if isinstance(content, typing.AsyncIterable):
    self.body_iterator = content
  else:
    self.body_iterator = iterate_in_threadpool(content)
  self.status_code = status_code
  self.media_type = self.media_type if media_type is None else media_type
  self.background = background
  self.init_headers(headers)

```
  
---|---  
###  body_iterator `instance-attribute` ¶
```
body_iterator

```

###  charset `class-attribute` `instance-attribute` ¶
```
charset = 'utf-8'

```

###  status_code `instance-attribute` ¶
```
status_code = status_code

```

###  media_type `instance-attribute` ¶
```
media_type = (
  media_type if media_type is None else media_type
)

```

###  body `instance-attribute` ¶
```
body = render(content)

```

###  background `instance-attribute` ¶
```
background = background

```

###  headers `property` ¶
```
headers

```

###  render ¶
```
render(content)

```

PARAMETER | DESCRIPTION  
---|---  
`content` |  **TYPE:** `Any`  
Source code in `starlette/responses.py`
```
47
48
49
50
51
52
```
| ```
defrender(self, content: typing.Any) -> bytes | memoryview:
  if content is None:
    return b""
  if isinstance(content, (bytes, memoryview)):
    return content
  return content.encode(self.charset) # type: ignore

```
  
---|---  
###  init_headers ¶
```
init_headers(headers=None)

```

PARAMETER | DESCRIPTION  
---|---  
`headers` |  **TYPE:** `Mapping[str, str] | None` **DEFAULT:** `None`  
Source code in `starlette/responses.py`
```
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
```
| ```
definit_headers(self, headers: typing.Mapping[str, str] | None = None) -> None:
  if headers is None:
    raw_headers: list[tuple[bytes, bytes]] = []
    populate_content_length = True
    populate_content_type = True
  else:
    raw_headers = [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]
    keys = [h[0] for h in raw_headers]
    populate_content_length = b"content-length" not in keys
    populate_content_type = b"content-type" not in keys
  body = getattr(self, "body", None)
  if (
    body is not None
    and populate_content_length
    and not (self.status_code < 200 or self.status_code in (204, 304))
  ):
    content_length = str(len(body))
    raw_headers.append((b"content-length", content_length.encode("latin-1")))
  content_type = self.media_type
  if content_type is not None and populate_content_type:
    if content_type.startswith("text/") and "charset=" not in content_type.lower():
      content_type += "; charset=" + self.charset
    raw_headers.append((b"content-type", content_type.encode("latin-1")))
  self.raw_headers = raw_headers

```
  
---|---  
###  set_cookie ¶
```
set_cookie(
  key,
  value="",
  max_age=None,
  expires=None,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`value` |  **TYPE:** `str` **DEFAULT:** `''`  
`max_age` |  **TYPE:** `int | None` **DEFAULT:** `None`  
`expires` |  **TYPE:** `datetime | str | int | None` **DEFAULT:** `None`  
`path` |  **TYPE:** `str | None` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
 88
 89
 90
 91
 92
 93
 94
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
112
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
```
| ```
defset_cookie(
  self,
  key: str,
  value: str = "",
  max_age: int | None = None,
  expires: datetime | str | int | None = None,
  path: str | None = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  cookie: http.cookies.BaseCookie[str] = http.cookies.SimpleCookie()
  cookie[key] = value
  if max_age is not None:
    cookie[key]["max-age"] = max_age
  if expires is not None:
    if isinstance(expires, datetime):
      cookie[key]["expires"] = format_datetime(expires, usegmt=True)
    else:
      cookie[key]["expires"] = expires
  if path is not None:
    cookie[key]["path"] = path
  if domain is not None:
    cookie[key]["domain"] = domain
  if secure:
    cookie[key]["secure"] = True
  if httponly:
    cookie[key]["httponly"] = True
  if samesite is not None:
    assert samesite.lower() in [
      "strict",
      "lax",
      "none",
    ], "samesite must be either 'strict', 'lax' or 'none'"
    cookie[key]["samesite"] = samesite
  cookie_val = cookie.output(header="").strip()
  self.raw_headers.append((b"set-cookie", cookie_val.encode("latin-1")))

```
  
---|---  
###  delete_cookie ¶
```
delete_cookie(
  key,
  path="/",
  domain=None,
  secure=False,
  httponly=False,
  samesite="lax",
)

```

PARAMETER | DESCRIPTION  
---|---  
`key` |  **TYPE:** `str`  
`path` |  **TYPE:** `str` **DEFAULT:** `'/'`  
`domain` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`secure` |  **TYPE:** `bool` **DEFAULT:** `False`  
`httponly` |  **TYPE:** `bool` **DEFAULT:** `False`  
`samesite` |  **TYPE:** `Literal['lax', 'strict', 'none'] | None` **DEFAULT:** `'lax'`  
Source code in `starlette/responses.py`
```
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
```
| ```
defdelete_cookie(
  self,
  key: str,
  path: str = "/",
  domain: str | None = None,
  secure: bool = False,
  httponly: bool = False,
  samesite: typing.Literal["lax", "strict", "none"] | None = "lax",
) -> None:
  self.set_cookie(
    key,
    max_age=0,
    expires=0,
    path=path,
    domain=domain,
    secure=secure,
    httponly=httponly,
    samesite=samesite,
  )

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
