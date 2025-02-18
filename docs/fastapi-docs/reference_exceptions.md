Skip to content 
# Exceptions - `HTTPException` and `WebSocketException`¶
These are the exceptions that you can raise to show errors to the client.
When you raise an exception, as would happen with normal Python, the rest of the execution is aborted. This way you can raise these exceptions from anywhere in the code to abort a request and show the error to the client.
You can use:
  * `HTTPException`
  * `WebSocketException`


These exceptions can be imported directly from `fastapi`:
```
fromfastapiimport HTTPException, WebSocketException

```

##  fastapi.HTTPException ¶
```
HTTPException(status_code, detail=None, headers=None)

```

Bases: `HTTPException`
An HTTP exception you can raise in your own code to show errors to the client.
This is for client errors, invalid authentication, invalid data, etc. Not for server errors in your code.
Read more about it in the FastAPI docs for Handling Errors.
#### Example¶
```
fromfastapiimport FastAPI, HTTPException
app = FastAPI()
items = {"foo": "The Foo Wrestlers"}
@app.get("/items/{item_id}")
async defread_item(item_id: str):
  if item_id not in items:
    raise HTTPException(status_code=404, detail="Item not found")
  return {"item": items[item_id]}

```

PARAMETER | DESCRIPTION  
---|---  
`status_code` |  HTTP status code to send to the client. **TYPE:** `int`  
`detail` |  Any data to be sent to the client in the `detail` key of the JSON response. **TYPE:** `Any` **DEFAULT:** `None`  
`headers` |  Any headers to send to the client in the response. **TYPE:** `Optional[Dict[str, str]]` **DEFAULT:** `None`  
Source code in `fastapi/exceptions.py`
```
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
```
| ```
def__init__(
  self,
  status_code: Annotated[
    int,
    Doc(
"""
      HTTP status code to send to the client.
      """
    ),
  ],
  detail: Annotated[
    Any,
    Doc(
"""
      Any data to be sent to the client in the `detail` key of the JSON
      response.
      """
    ),
  ] = None,
  headers: Annotated[
    Optional[Dict[str, str]],
    Doc(
"""
      Any headers to send to the client in the response.
      """
    ),
  ] = None,
) -> None:
  super().__init__(status_code=status_code, detail=detail, headers=headers)

```
  
---|---  
###  status_code `instance-attribute` ¶
```
status_code = status_code

```

###  detail `instance-attribute` ¶
```
detail = detail

```

###  headers `instance-attribute` ¶
```
headers = headers

```

##  fastapi.WebSocketException ¶
```
WebSocketException(code, reason=None)

```

Bases: `WebSocketException`
A WebSocket exception you can raise in your own code to show errors to the client.
This is for client errors, invalid authentication, invalid data, etc. Not for server errors in your code.
Read more about it in the FastAPI docs for WebSockets.
#### Example¶
```
fromtypingimport Annotated
fromfastapiimport (
  Cookie,
  FastAPI,
  WebSocket,
  WebSocketException,
  status,
)
app = FastAPI()
@app.websocket("/items/{item_id}/ws")
async defwebsocket_endpoint(
  *,
  websocket: WebSocket,
  session: Annotated[str | None, Cookie()] = None,
  item_id: str,
):
  if session is None:
    raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
  await websocket.accept()
  while True:
    data = await websocket.receive_text()
    await websocket.send_text(f"Session cookie is: {session}")
    await websocket.send_text(f"Message text was: {data}, for item ID: {item_id}")

```

PARAMETER | DESCRIPTION  
---|---  
`code` |  A closing code from the valid codes defined in the specification. **TYPE:** `int`  
`reason` |  The reason to close the WebSocket connection. It is UTF-8-encoded data. The interpretation of the reason is up to the application, it is not specified by the WebSocket specification. It could contain text that could be human-readable or interpretable by the client code, etc. **TYPE:** `Union[str, None]` **DEFAULT:** `None`  
Source code in `fastapi/exceptions.py`
```
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
```
| ```
def__init__(
  self,
  code: Annotated[
    int,
    Doc(
"""
      A closing code from the
      [valid codes defined in the specification](https://datatracker.ietf.org/doc/html/rfc6455#section-7.4.1).
      """
    ),
  ],
  reason: Annotated[
    Union[str, None],
    Doc(
"""
      The reason to close the WebSocket connection.
      It is UTF-8-encoded data. The interpretation of the reason is up to the
      application, it is not specified by the WebSocket specification.
      It could contain text that could be human-readable or interpretable
      by the client code, etc.
      """
    ),
  ] = None,
) -> None:
  super().__init__(code=code, reason=reason)

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

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
