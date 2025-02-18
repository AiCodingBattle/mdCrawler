Skip to content 
# `Request` class¶
You can declare a parameter in a _path operation function_ or dependency to be of type `Request` and then you can access the raw request object directly, without any validation, etc.
You can import it directly from `fastapi`:
```
fromfastapiimport Request

```

Tip
When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an `HTTPConnection` instead of a `Request` or a `WebSocket`.
##  fastapi.Request ¶
```
Request(scope, receive=empty_receive, send=empty_send)

```

Bases: `HTTPConnection`
PARAMETER | DESCRIPTION  
---|---  
`scope` |  **TYPE:** `Scope`  
`receive` |  **TYPE:** `Receive` **DEFAULT:** `empty_receive`  
`send` |  **TYPE:** `Send` **DEFAULT:** `empty_send`  
Source code in `starlette/requests.py`
```
201
202
203
204
205
206
207
208
```
| ```
def__init__(self, scope: Scope, receive: Receive = empty_receive, send: Send = empty_send):
  super().__init__(scope)
  assert scope["type"] == "http"
  self._receive = receive
  self._send = send
  self._stream_consumed = False
  self._is_disconnected = False
  self._form = None

```
  
---|---  
###  scope `instance-attribute` ¶
```
scope = scope

```

###  app `property` ¶
```
app

```

###  url `property` ¶
```
url

```

###  base_url `property` ¶
```
base_url

```

###  headers `property` ¶
```
headers

```

###  query_params `property` ¶
```
query_params

```

###  path_params `property` ¶
```
path_params

```

###  cookies `property` ¶
```
cookies

```

###  client `property` ¶
```
client

```

###  session `property` ¶
```
session

```

###  auth `property` ¶
```
auth

```

###  user `property` ¶
```
user

```

###  state `property` ¶
```
state

```

###  method `property` ¶
```
method

```

###  receive `property` ¶
```
receive

```

###  url_for ¶
```
url_for(name, /, **path_params)

```

PARAMETER | DESCRIPTION  
---|---  
`name` |  **TYPE:** `str`  
`**path_params` |  **TYPE:** `Any` **DEFAULT:** `{}`  
Source code in `starlette/requests.py`
```
182
183
184
185
186
187
```
| ```
defurl_for(self, name: str, /, **path_params: typing.Any) -> URL:
  url_path_provider: Router | Starlette | None = self.scope.get("router") or self.scope.get("app")
  if url_path_provider is None:
    raise RuntimeError("The `url_for` method can only be used inside a Starlette application or with a router.")
  url_path = url_path_provider.url_path_for(name, **path_params)
  return url_path.make_absolute_url(base_url=self.base_url)

```
  
---|---  
###  stream `async` ¶
```
stream()

```

Source code in `starlette/requests.py`
```
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
230
231
232
233
234
235
236
```
| ```
async defstream(self) -> typing.AsyncGenerator[bytes, None]:
  if hasattr(self, "_body"):
    yield self._body
    yield b""
    return
  if self._stream_consumed:
    raise RuntimeError("Stream consumed")
  while not self._stream_consumed:
    message = await self._receive()
    if message["type"] == "http.request":
      body = message.get("body", b"")
      if not message.get("more_body", False):
        self._stream_consumed = True
      if body:
        yield body
    elif message["type"] == "http.disconnect": # pragma: no branch
      self._is_disconnected = True
      raise ClientDisconnect()
  yield b""

```
  
---|---  
###  body `async` ¶
```
body()

```

Source code in `starlette/requests.py`
```
238
239
240
241
242
243
244
```
| ```
async defbody(self) -> bytes:
  if not hasattr(self, "_body"):
    chunks: list[bytes] = []
    async for chunk in self.stream():
      chunks.append(chunk)
    self._body = b"".join(chunks)
  return self._body

```
  
---|---  
###  json `async` ¶
```
json()

```

Source code in `starlette/requests.py`
```
246
247
248
249
250
```
| ```
async defjson(self) -> typing.Any:
  if not hasattr(self, "_json"): # pragma: no branch
    body = await self.body()
    self._json = json.loads(body)
  return self._json

```
  
---|---  
###  form ¶
```
form(
  *,
  max_files=1000,
  max_fields=1000,
  max_part_size=1024 * 1024
)

```

PARAMETER | DESCRIPTION  
---|---  
`max_files` |  **TYPE:** `int | float` **DEFAULT:** `1000`  
`max_fields` |  **TYPE:** `int | float` **DEFAULT:** `1000`  
`max_part_size` |  **TYPE:** `int` **DEFAULT:** `1024 * 1024`  
Source code in `starlette/requests.py`
```
287
288
289
290
291
292
293
294
295
296
```
| ```
defform(
  self,
  *,
  max_files: int | float = 1000,
  max_fields: int | float = 1000,
  max_part_size: int = 1024 * 1024,
) -> AwaitableOrContextManager[FormData]:
  return AwaitableOrContextManagerWrapper(
    self._get_form(max_files=max_files, max_fields=max_fields, max_part_size=max_part_size)
  )

```
  
---|---  
###  close `async` ¶
```
close()

```

Source code in `starlette/requests.py`
```
298
299
300
```
| ```
async defclose(self) -> None:
  if self._form is not None: # pragma: no branch
    await self._form.close()

```
  
---|---  
###  is_disconnected `async` ¶
```
is_disconnected()

```

Source code in `starlette/requests.py`
```
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
```
| ```
async defis_disconnected(self) -> bool:
  if not self._is_disconnected:
    message: Message = {}
    # If message isn't immediately available, move on
    with anyio.CancelScope() as cs:
      cs.cancel()
      message = await self._receive()
    if message.get("type") == "http.disconnect":
      self._is_disconnected = True
  return self._is_disconnected

```
  
---|---  
###  send_push_promise `async` ¶
```
send_push_promise(path)

```

PARAMETER | DESCRIPTION  
---|---  
`path` |  **TYPE:** `str`  
Source code in `starlette/requests.py`
```
316
317
318
319
320
321
322
```
| ```
async defsend_push_promise(self, path: str) -> None:
  if "http.response.push" in self.scope.get("extensions", {}):
    raw_headers: list[tuple[bytes, bytes]] = []
    for name in SERVER_PUSH_HEADERS_TO_COPY:
      for value in self.headers.getlist(name):
        raw_headers.append((name.encode("latin-1"), value.encode("latin-1")))
    await self._send({"type": "http.response.push", "path": path, "headers": raw_headers})

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
