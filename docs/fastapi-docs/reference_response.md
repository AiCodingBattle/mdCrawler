Skip to content 
# `Response` class¶
You can declare a parameter in a _path operation function_ or dependency to be of type `Response` and then you can set data for the response like headers or cookies.
You can also use it directly to create an instance of it and return it from your _path operations_.
You can import it directly from `fastapi`:
```
fromfastapiimport Response

```

##  fastapi.Response ¶
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
###  media_type `class-attribute` `instance-attribute` ¶
```
media_type = None

```

###  charset `class-attribute` `instance-attribute` ¶
```
charset = 'utf-8'

```

###  status_code `instance-attribute` ¶
```
status_code = status_code

```

###  background `instance-attribute` ¶
```
background = background

```

###  body `instance-attribute` ¶
```
body = render(content)

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
