Skip to content 
# WebSockets¶
When defining WebSockets, you normally declare a parameter of type `WebSocket` and with it you can read data from the client and send data to it.
It is provided directly by Starlette, but you can import it from `fastapi`:
```
fromfastapiimport WebSocket

```

Tip
When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an `HTTPConnection` instead of a `Request` or a `WebSocket`.
##  fastapi.WebSocket ¶
```
WebSocket(scope, receive, send)

```

Bases: `HTTPConnection`
PARAMETER | DESCRIPTION  
---|---  
`scope` |  **TYPE:** `Scope`  
`receive` |  **TYPE:** `Receive`  
`send` |  **TYPE:** `Send`  
Source code in `starlette/websockets.py`
```
26
27
28
29
30
31
32
```
| ```
def__init__(self, scope: Scope, receive: Receive, send: Send) -> None:
  super().__init__(scope)
  assert scope["type"] == "websocket"
  self._receive = receive
  self._send = send
  self.client_state = WebSocketState.CONNECTING
  self.application_state = WebSocketState.CONNECTING

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

###  state `property` ¶
```
state

```

###  client_state `instance-attribute` ¶
```
client_state = CONNECTING

```

###  application_state `instance-attribute` ¶
```
application_state = CONNECTING

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
###  receive `async` ¶
```
receive()

```

Receive ASGI websocket messages, ensuring valid state transitions.
Source code in `starlette/websockets.py`
```
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
```
| ```
async defreceive(self) -> Message:
"""
  Receive ASGI websocket messages, ensuring valid state transitions.
  """
  if self.client_state == WebSocketState.CONNECTING:
    message = await self._receive()
    message_type = message["type"]
    if message_type != "websocket.connect":
      raise RuntimeError(f'Expected ASGI message "websocket.connect", but got {message_type!r}')
    self.client_state = WebSocketState.CONNECTED
    return message
  elif self.client_state == WebSocketState.CONNECTED:
    message = await self._receive()
    message_type = message["type"]
    if message_type not in {"websocket.receive", "websocket.disconnect"}:
      raise RuntimeError(
        f'Expected ASGI message "websocket.receive" or "websocket.disconnect", but got {message_type!r}'
      )
    if message_type == "websocket.disconnect":
      self.client_state = WebSocketState.DISCONNECTED
    return message
  else:
    raise RuntimeError('Cannot call "receive" once a disconnect message has been received.')

```
  
---|---  
###  send `async` ¶
```
send(message)

```

Send ASGI websocket messages, ensuring valid state transitions.
PARAMETER | DESCRIPTION  
---|---  
`message` |  **TYPE:** `Message`  
Source code in `starlette/websockets.py`
```
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
94
95
96
97
```
| ```
async defsend(self, message: Message) -> None:
"""
  Send ASGI websocket messages, ensuring valid state transitions.
  """
  if self.application_state == WebSocketState.CONNECTING:
    message_type = message["type"]
    if message_type not in {"websocket.accept", "websocket.close", "websocket.http.response.start"}:
      raise RuntimeError(
        'Expected ASGI message "websocket.accept", "websocket.close" or "websocket.http.response.start", '
        f"but got {message_type!r}"
      )
    if message_type == "websocket.close":
      self.application_state = WebSocketState.DISCONNECTED
    elif message_type == "websocket.http.response.start":
      self.application_state = WebSocketState.RESPONSE
    else:
      self.application_state = WebSocketState.CONNECTED
    await self._send(message)
  elif self.application_state == WebSocketState.CONNECTED:
    message_type = message["type"]
    if message_type not in {"websocket.send", "websocket.close"}:
      raise RuntimeError(
        f'Expected ASGI message "websocket.send" or "websocket.close", but got {message_type!r}'
      )
    if message_type == "websocket.close":
      self.application_state = WebSocketState.DISCONNECTED
    try:
      await self._send(message)
    except OSError:
      self.application_state = WebSocketState.DISCONNECTED
      raise WebSocketDisconnect(code=1006)
  elif self.application_state == WebSocketState.RESPONSE:
    message_type = message["type"]
    if message_type != "websocket.http.response.body":
      raise RuntimeError(f'Expected ASGI message "websocket.http.response.body", but got {message_type!r}')
    if not message.get("more_body", False):
      self.application_state = WebSocketState.DISCONNECTED
    await self._send(message)
  else:
    raise RuntimeError('Cannot call "send" once a close message has been sent.')

```
  
---|---  
###  accept `async` ¶
```
accept(subprotocol=None, headers=None)

```

PARAMETER | DESCRIPTION  
---|---  
`subprotocol` |  **TYPE:** `str | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `Iterable[tuple[bytes, bytes]] | None` **DEFAULT:** `None`  
Source code in `starlette/websockets.py`
```
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
```
| ```
async defaccept(
  self,
  subprotocol: str | None = None,
  headers: typing.Iterable[tuple[bytes, bytes]] | None = None,
) -> None:
  headers = headers or []
  if self.client_state == WebSocketState.CONNECTING: # pragma: no branch
    # If we haven't yet seen the 'connect' message, then wait for it first.
    await self.receive()
  await self.send({"type": "websocket.accept", "subprotocol": subprotocol, "headers": headers})

```
  
---|---  
###  receive_text `async` ¶
```
receive_text()

```

Source code in `starlette/websockets.py`
```
115
116
117
118
119
120
```
| ```
async defreceive_text(self) -> str:
  if self.application_state != WebSocketState.CONNECTED:
    raise RuntimeError('WebSocket is not connected. Need to call "accept" first.')
  message = await self.receive()
  self._raise_on_disconnect(message)
  return typing.cast(str, message["text"])

```
  
---|---  
###  receive_bytes `async` ¶
```
receive_bytes()

```

Source code in `starlette/websockets.py`
```
122
123
124
125
126
127
```
| ```
async defreceive_bytes(self) -> bytes:
  if self.application_state != WebSocketState.CONNECTED:
    raise RuntimeError('WebSocket is not connected. Need to call "accept" first.')
  message = await self.receive()
  self._raise_on_disconnect(message)
  return typing.cast(bytes, message["bytes"])

```
  
---|---  
###  receive_json `async` ¶
```
receive_json(mode='text')

```

PARAMETER | DESCRIPTION  
---|---  
`mode` |  **TYPE:** `str` **DEFAULT:** `'text'`  
Source code in `starlette/websockets.py`
```
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
```
| ```
async defreceive_json(self, mode: str = "text") -> typing.Any:
  if mode not in {"text", "binary"}:
    raise RuntimeError('The "mode" argument should be "text" or "binary".')
  if self.application_state != WebSocketState.CONNECTED:
    raise RuntimeError('WebSocket is not connected. Need to call "accept" first.')
  message = await self.receive()
  self._raise_on_disconnect(message)
  if mode == "text":
    text = message["text"]
  else:
    text = message["bytes"].decode("utf-8")
  return json.loads(text)

```
  
---|---  
###  iter_text `async` ¶
```
iter_text()

```

Source code in `starlette/websockets.py`
```
143
144
145
146
147
148
```
| ```
async defiter_text(self) -> typing.AsyncIterator[str]:
  try:
    while True:
      yield await self.receive_text()
  except WebSocketDisconnect:
    pass

```
  
---|---  
###  iter_bytes `async` ¶
```
iter_bytes()

```

Source code in `starlette/websockets.py`
```
150
151
152
153
154
155
```
| ```
async defiter_bytes(self) -> typing.AsyncIterator[bytes]:
  try:
    while True:
      yield await self.receive_bytes()
  except WebSocketDisconnect:
    pass

```
  
---|---  
###  iter_json `async` ¶
```
iter_json()

```

Source code in `starlette/websockets.py`
```
157
158
159
160
161
162
```
| ```
async defiter_json(self) -> typing.AsyncIterator[typing.Any]:
  try:
    while True:
      yield await self.receive_json()
  except WebSocketDisconnect:
    pass

```
  
---|---  
###  send_text `async` ¶
```
send_text(data)

```

PARAMETER | DESCRIPTION  
---|---  
`data` |  **TYPE:** `str`  
Source code in `starlette/websockets.py`
```
164
165
```
| ```
async defsend_text(self, data: str) -> None:
  await self.send({"type": "websocket.send", "text": data})

```
  
---|---  
###  send_bytes `async` ¶
```
send_bytes(data)

```

PARAMETER | DESCRIPTION  
---|---  
`data` |  **TYPE:** `bytes`  
Source code in `starlette/websockets.py`
```
167
168
```
| ```
async defsend_bytes(self, data: bytes) -> None:
  await self.send({"type": "websocket.send", "bytes": data})

```
  
---|---  
###  send_json `async` ¶
```
send_json(data, mode='text')

```

PARAMETER | DESCRIPTION  
---|---  
`data` |  **TYPE:** `Any`  
`mode` |  **TYPE:** `str` **DEFAULT:** `'text'`  
Source code in `starlette/websockets.py`
```
170
171
172
173
174
175
176
177
```
| ```
async defsend_json(self, data: typing.Any, mode: str = "text") -> None:
  if mode not in {"text", "binary"}:
    raise RuntimeError('The "mode" argument should be "text" or "binary".')
  text = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
  if mode == "text":
    await self.send({"type": "websocket.send", "text": text})
  else:
    await self.send({"type": "websocket.send", "bytes": text.encode("utf-8")})

```
  
---|---  
###  close `async` ¶
```
close(code=1000, reason=None)

```

PARAMETER | DESCRIPTION  
---|---  
`code` |  **TYPE:** `int` **DEFAULT:** `1000`  
`reason` |  **TYPE:** `str | None` **DEFAULT:** `None`  
Source code in `starlette/websockets.py`
```
179
180
```
| ```
async defclose(self, code: int = 1000, reason: str | None = None) -> None:
  await self.send({"type": "websocket.close", "code": code, "reason": reason or ""})

```
  
---|---  
When a client disconnects, a `WebSocketDisconnect` exception is raised, you can catch it.
You can import it directly form `fastapi`:
```
fromfastapiimport WebSocketDisconnect

```

##  fastapi.WebSocketDisconnect ¶
```
WebSocketDisconnect(code=1000, reason=None)

```

Bases: `Exception`
PARAMETER | DESCRIPTION  
---|---  
`code` |  **TYPE:** `int` **DEFAULT:** `1000`  
`reason` |  **TYPE:** `str | None` **DEFAULT:** `None`  
Source code in `starlette/websockets.py`
```
20
21
22
```
| ```
def__init__(self, code: int = 1000, reason: str | None = None) -> None:
  self.code = code
  self.reason = reason or ""

```
  
---|---  
###  code `instance-attribute` ¶
```
code = code

```

###  reason `instance-attribute` ¶
```
reason = reason or ''

```

## WebSockets - additional classes¶
Additional classes for handling WebSockets.
Provided directly by Starlette, but you can import it from `fastapi`:
```
fromfastapi.websocketsimport WebSocketDisconnect, WebSocketState

```

##  fastapi.websockets.WebSocketDisconnect ¶
```
WebSocketDisconnect(code=1000, reason=None)

```

Bases: `Exception`
PARAMETER | DESCRIPTION  
---|---  
`code` |  **TYPE:** `int` **DEFAULT:** `1000`  
`reason` |  **TYPE:** `str | None` **DEFAULT:** `None`  
Source code in `starlette/websockets.py`
```
20
21
22
```
| ```
def__init__(self, code: int = 1000, reason: str | None = None) -> None:
  self.code = code
  self.reason = reason or ""

```
  
---|---  
###  code `instance-attribute` ¶
```
code = code

```

###  reason `instance-attribute` ¶
```
reason = reason or ''

```

##  fastapi.websockets.WebSocketState ¶
Bases: `Enum`
###  CONNECTING `class-attribute` `instance-attribute` ¶
```
CONNECTING = 0

```

###  CONNECTED `class-attribute` `instance-attribute` ¶
```
CONNECTED = 1

```

###  DISCONNECTED `class-attribute` `instance-attribute` ¶
```
DISCONNECTED = 2

```

###  RESPONSE `class-attribute` `instance-attribute` ¶
```
RESPONSE = 3

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
