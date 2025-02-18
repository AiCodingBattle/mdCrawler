Skip to content 
# `HTTPConnection` class¶
When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an `HTTPConnection` instead of a `Request` or a `WebSocket`.
You can import it from `fastapi.requests`:
```
fromfastapi.requestsimport HTTPConnection

```

##  fastapi.requests.HTTPConnection ¶
```
HTTPConnection(scope, receive=None)

```

Bases: `Mapping[str, Any]`
A base class for incoming HTTP connections, that is used to provide any functionality that is common to both `Request` and `WebSocket`.
PARAMETER | DESCRIPTION  
---|---  
`scope` |  **TYPE:** `Scope`  
`receive` |  **TYPE:** `Receive | None` **DEFAULT:** `None`  
Source code in `starlette/requests.py`
```
76
77
78
```
| ```
def__init__(self, scope: Scope, receive: Receive | None = None) -> None:
  assert scope["type"] in ("http", "websocket")
  self.scope = scope

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
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
