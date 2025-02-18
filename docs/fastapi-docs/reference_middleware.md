Skip to content 
# Middleware¶
There are several middlewares available provided by Starlette directly.
Read more about them in the FastAPI docs for Middleware.
##  fastapi.middleware.cors.CORSMiddleware ¶
```
CORSMiddleware(
  app,
  allow_origins=(),
  allow_methods=("GET",),
  allow_headers=(),
  allow_credentials=False,
  allow_origin_regex=None,
  expose_headers=(),
  max_age=600,
)

```

PARAMETER | DESCRIPTION  
---|---  
`app` |  **TYPE:** `ASGIApp`  
`allow_origins` |  **TYPE:** `Sequence[str]` **DEFAULT:** `()`  
`allow_methods` |  **TYPE:** `Sequence[str]` **DEFAULT:** `('GET',)`  
`allow_headers` |  **TYPE:** `Sequence[str]` **DEFAULT:** `()`  
`allow_credentials` |  **TYPE:** `bool` **DEFAULT:** `False`  
`allow_origin_regex` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`expose_headers` |  **TYPE:** `Sequence[str]` **DEFAULT:** `()`  
`max_age` |  **TYPE:** `int` **DEFAULT:** `600`  
Source code in `starlette/middleware/cors.py`
```
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
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
46
47
48
49
50
51
52
53
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
```
| ```
def__init__(
  self,
  app: ASGIApp,
  allow_origins: typing.Sequence[str] = (),
  allow_methods: typing.Sequence[str] = ("GET",),
  allow_headers: typing.Sequence[str] = (),
  allow_credentials: bool = False,
  allow_origin_regex: str | None = None,
  expose_headers: typing.Sequence[str] = (),
  max_age: int = 600,
) -> None:
  if "*" in allow_methods:
    allow_methods = ALL_METHODS
  compiled_allow_origin_regex = None
  if allow_origin_regex is not None:
    compiled_allow_origin_regex = re.compile(allow_origin_regex)
  allow_all_origins = "*" in allow_origins
  allow_all_headers = "*" in allow_headers
  preflight_explicit_allow_origin = not allow_all_origins or allow_credentials
  simple_headers = {}
  if allow_all_origins:
    simple_headers["Access-Control-Allow-Origin"] = "*"
  if allow_credentials:
    simple_headers["Access-Control-Allow-Credentials"] = "true"
  if expose_headers:
    simple_headers["Access-Control-Expose-Headers"] = ", ".join(expose_headers)
  preflight_headers = {}
  if preflight_explicit_allow_origin:
    # The origin value will be set in preflight_response() if it is allowed.
    preflight_headers["Vary"] = "Origin"
  else:
    preflight_headers["Access-Control-Allow-Origin"] = "*"
  preflight_headers.update(
    {
      "Access-Control-Allow-Methods": ", ".join(allow_methods),
      "Access-Control-Max-Age": str(max_age),
    }
  )
  allow_headers = sorted(SAFELISTED_HEADERS | set(allow_headers))
  if allow_headers and not allow_all_headers:
    preflight_headers["Access-Control-Allow-Headers"] = ", ".join(allow_headers)
  if allow_credentials:
    preflight_headers["Access-Control-Allow-Credentials"] = "true"
  self.app = app
  self.allow_origins = allow_origins
  self.allow_methods = allow_methods
  self.allow_headers = [h.lower() for h in allow_headers]
  self.allow_all_origins = allow_all_origins
  self.allow_all_headers = allow_all_headers
  self.preflight_explicit_allow_origin = preflight_explicit_allow_origin
  self.allow_origin_regex = compiled_allow_origin_regex
  self.simple_headers = simple_headers
  self.preflight_headers = preflight_headers

```
  
---|---  
###  app `instance-attribute` ¶
```
app = app

```

###  allow_origins `instance-attribute` ¶
```
allow_origins = allow_origins

```

###  allow_methods `instance-attribute` ¶
```
allow_methods = allow_methods

```

###  allow_headers `instance-attribute` ¶
```
allow_headers = [lower() for h in allow_headers]

```

###  allow_all_origins `instance-attribute` ¶
```
allow_all_origins = allow_all_origins

```

###  allow_all_headers `instance-attribute` ¶
```
allow_all_headers = allow_all_headers

```

###  preflight_explicit_allow_origin `instance-attribute` ¶
```
preflight_explicit_allow_origin = (
  preflight_explicit_allow_origin
)

```

###  allow_origin_regex `instance-attribute` ¶
```
allow_origin_regex = compiled_allow_origin_regex

```

###  simple_headers `instance-attribute` ¶
```
simple_headers = simple_headers

```

###  preflight_headers `instance-attribute` ¶
```
preflight_headers = preflight_headers

```

###  is_allowed_origin ¶
```
is_allowed_origin(origin)

```

PARAMETER | DESCRIPTION  
---|---  
`origin` |  **TYPE:** `str`  
Source code in `starlette/middleware/cors.py`
```
 95
 96
 97
 98
 99
100
101
102
```
| ```
defis_allowed_origin(self, origin: str) -> bool:
  if self.allow_all_origins:
    return True
  if self.allow_origin_regex is not None and self.allow_origin_regex.fullmatch(origin):
    return True
  return origin in self.allow_origins

```
  
---|---  
###  preflight_response ¶
```
preflight_response(request_headers)

```

PARAMETER | DESCRIPTION  
---|---  
`request_headers` |  **TYPE:** `Headers`  
Source code in `starlette/middleware/cors.py`
```
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
126
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
```
| ```
defpreflight_response(self, request_headers: Headers) -> Response:
  requested_origin = request_headers["origin"]
  requested_method = request_headers["access-control-request-method"]
  requested_headers = request_headers.get("access-control-request-headers")
  headers = dict(self.preflight_headers)
  failures = []
  if self.is_allowed_origin(origin=requested_origin):
    if self.preflight_explicit_allow_origin:
      # The "else" case is already accounted for in self.preflight_headers
      # and the value would be "*".
      headers["Access-Control-Allow-Origin"] = requested_origin
  else:
    failures.append("origin")
  if requested_method not in self.allow_methods:
    failures.append("method")
  # If we allow all headers, then we have to mirror back any requested
  # headers in the response.
  if self.allow_all_headers and requested_headers is not None:
    headers["Access-Control-Allow-Headers"] = requested_headers
  elif requested_headers is not None:
    for header in [h.lower() for h in requested_headers.split(",")]:
      if header.strip() not in self.allow_headers:
        failures.append("headers")
        break
  # We don't strictly need to use 400 responses here, since its up to
  # the browser to enforce the CORS policy, but its more informative
  # if we do.
  if failures:
    failure_text = "Disallowed CORS " + ", ".join(failures)
    return PlainTextResponse(failure_text, status_code=400, headers=headers)
  return PlainTextResponse("OK", status_code=200, headers=headers)

```
  
---|---  
###  simple_response `async` ¶
```
simple_response(scope, receive, send, request_headers)

```

PARAMETER | DESCRIPTION  
---|---  
`scope` |  **TYPE:** `Scope`  
`receive` |  **TYPE:** `Receive`  
`send` |  **TYPE:** `Send`  
`request_headers` |  **TYPE:** `Headers`  
Source code in `starlette/middleware/cors.py`
```
142
143
144
```
| ```
async defsimple_response(self, scope: Scope, receive: Receive, send: Send, request_headers: Headers) -> None:
  send = functools.partial(self.send, send=send, request_headers=request_headers)
  await self.app(scope, receive, send)

```
  
---|---  
###  send `async` ¶
```
send(message, send, request_headers)

```

PARAMETER | DESCRIPTION  
---|---  
`message` |  **TYPE:** `Message`  
`send` |  **TYPE:** `Send`  
`request_headers` |  **TYPE:** `Headers`  
Source code in `starlette/middleware/cors.py`
```
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
```
| ```
async defsend(self, message: Message, send: Send, request_headers: Headers) -> None:
  if message["type"] != "http.response.start":
    await send(message)
    return
  message.setdefault("headers", [])
  headers = MutableHeaders(scope=message)
  headers.update(self.simple_headers)
  origin = request_headers["Origin"]
  has_cookie = "cookie" in request_headers
  # If request includes any cookie headers, then we must respond
  # with the specific origin instead of '*'.
  if self.allow_all_origins and has_cookie:
    self.allow_explicit_origin(headers, origin)
  # If we only allow specific origins, then we have to mirror back
  # the Origin header in the response.
  elif not self.allow_all_origins and self.is_allowed_origin(origin=origin):
    self.allow_explicit_origin(headers, origin)
  await send(message)

```
  
---|---  
###  allow_explicit_origin `staticmethod` ¶
```
allow_explicit_origin(headers, origin)

```

PARAMETER | DESCRIPTION  
---|---  
`headers` |  **TYPE:** `MutableHeaders`  
`origin` |  **TYPE:** `str`  
Source code in `starlette/middleware/cors.py`
```
169
170
171
172
```
| ```
@staticmethod
defallow_explicit_origin(headers: MutableHeaders, origin: str) -> None:
  headers["Access-Control-Allow-Origin"] = origin
  headers.add_vary_header("Origin")

```
  
---|---  
It can be imported from `fastapi`:
```
fromfastapi.middleware.corsimport CORSMiddleware

```

##  fastapi.middleware.gzip.GZipMiddleware ¶
```
GZipMiddleware(app, minimum_size=500, compresslevel=9)

```

PARAMETER | DESCRIPTION  
---|---  
`app` |  **TYPE:** `ASGIApp`  
`minimum_size` |  **TYPE:** `int` **DEFAULT:** `500`  
`compresslevel` |  **TYPE:** `int` **DEFAULT:** `9`  
Source code in `starlette/middleware/gzip.py`
```
10
11
12
13
```
| ```
def__init__(self, app: ASGIApp, minimum_size: int = 500, compresslevel: int = 9) -> None:
  self.app = app
  self.minimum_size = minimum_size
  self.compresslevel = compresslevel

```
  
---|---  
###  app `instance-attribute` ¶
```
app = app

```

###  minimum_size `instance-attribute` ¶
```
minimum_size = minimum_size

```

###  compresslevel `instance-attribute` ¶
```
compresslevel = compresslevel

```

It can be imported from `fastapi`:
```
fromfastapi.middleware.gzipimport GZipMiddleware

```

##  fastapi.middleware.httpsredirect.HTTPSRedirectMiddleware ¶
```
HTTPSRedirectMiddleware(app)

```

PARAMETER | DESCRIPTION  
---|---  
`app` |  **TYPE:** `ASGIApp`  
Source code in `starlette/middleware/httpsredirect.py`
```
7
8
```
| ```
def__init__(self, app: ASGIApp) -> None:
  self.app = app

```
  
---|---  
###  app `instance-attribute` ¶
```
app = app

```

It can be imported from `fastapi`:
```
fromfastapi.middleware.httpsredirectimport HTTPSRedirectMiddleware

```

##  fastapi.middleware.trustedhost.TrustedHostMiddleware ¶
```
TrustedHostMiddleware(
  app, allowed_hosts=None, www_redirect=True
)

```

PARAMETER | DESCRIPTION  
---|---  
`app` |  **TYPE:** `ASGIApp`  
`allowed_hosts` |  **TYPE:** `Sequence[str] | None` **DEFAULT:** `None`  
`www_redirect` |  **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `starlette/middleware/trustedhost.py`
```
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
```
| ```
def__init__(
  self,
  app: ASGIApp,
  allowed_hosts: typing.Sequence[str] | None = None,
  www_redirect: bool = True,
) -> None:
  if allowed_hosts is None:
    allowed_hosts = ["*"]
  for pattern in allowed_hosts:
    assert "*" not in pattern[1:], ENFORCE_DOMAIN_WILDCARD
    if pattern.startswith("*") and pattern != "*":
      assert pattern.startswith("*."), ENFORCE_DOMAIN_WILDCARD
  self.app = app
  self.allowed_hosts = list(allowed_hosts)
  self.allow_any = "*" in allowed_hosts
  self.www_redirect = www_redirect

```
  
---|---  
###  app `instance-attribute` ¶
```
app = app

```

###  allowed_hosts `instance-attribute` ¶
```
allowed_hosts = list(allowed_hosts)

```

###  allow_any `instance-attribute` ¶
```
allow_any = '*' in allowed_hosts

```

###  www_redirect `instance-attribute` ¶
```
www_redirect = www_redirect

```

It can be imported from `fastapi`:
```
fromfastapi.middleware.trustedhostimport TrustedHostMiddleware

```

##  fastapi.middleware.wsgi.WSGIMiddleware ¶
```
WSGIMiddleware(app)

```

PARAMETER | DESCRIPTION  
---|---  
`app` |  **TYPE:** `Callable[..., Any]`  
Source code in `starlette/middleware/wsgi.py`
```
74
75
```
| ```
def__init__(self, app: typing.Callable[..., typing.Any]) -> None:
  self.app = app

```
  
---|---  
###  app `instance-attribute` ¶
```
app = app

```

It can be imported from `fastapi`:
```
fromfastapi.middleware.wsgiimport WSGIMiddleware

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
