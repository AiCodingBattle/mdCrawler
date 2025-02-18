Skip to content 
# Security Tools¶
When you need to declare dependencies with OAuth2 scopes you use `Security()`.
But you still need to define what is the dependable, the callable that you pass as a parameter to `Depends()` or `Security()`.
There are multiple tools that you can use to create those dependables, and they get integrated into OpenAPI so they are shown in the automatic docs UI, they can be used by automatically generated clients and SDKs, etc.
You can import them from `fastapi.security`:
```
fromfastapi.securityimport (
  APIKeyCookie,
  APIKeyHeader,
  APIKeyQuery,
  HTTPAuthorizationCredentials,
  HTTPBasic,
  HTTPBasicCredentials,
  HTTPBearer,
  HTTPDigest,
  OAuth2,
  OAuth2AuthorizationCodeBearer,
  OAuth2PasswordBearer,
  OAuth2PasswordRequestForm,
  OAuth2PasswordRequestFormStrict,
  OpenIdConnect,
  SecurityScopes,
)

```

## API Key Security Schemes¶
##  fastapi.security.APIKeyCookie ¶
```
APIKeyCookie(
  *,
  name,
  scheme_name=None,
  description=None,
  auto_error=True
)

```

Bases: `APIKeyBase`
API key authentication using a cookie.
This defines the name of the cookie that should be provided in the request with the API key and integrates that into the OpenAPI documentation. It extracts the key value sent in the cookie automatically and provides it as the dependency result. But it doesn't define how to set that cookie.
#### Usage¶
Create an instance object and use that object as the dependency in `Depends()`.
The dependency result will be a string containing the key value.
#### Example¶
```
fromfastapiimport Depends, FastAPI
fromfastapi.securityimport APIKeyCookie
app = FastAPI()
cookie_scheme = APIKeyCookie(name="session")
@app.get("/items/")
async defread_items(session: str = Depends(cookie_scheme)):
  return {"session": session}

```

PARAMETER | DESCRIPTION  
---|---  
`name` |  Cookie name. **TYPE:** `str`  
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`auto_error` |  By default, if the cookie is not provided, `APIKeyCookie` will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the cookie is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in a cookie or in an HTTP Bearer token). **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/security/api_key.py`
```
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
```
| ```
def__init__(
  self,
  *,
  name: Annotated[str, Doc("Cookie name.")],
  scheme_name: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme name.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  description: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme description.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  auto_error: Annotated[
    bool,
    Doc(
"""
      By default, if the cookie is not provided, `APIKeyCookie` will
      automatically cancel the request and send the client an error.
      If `auto_error` is set to `False`, when the cookie is not available,
      instead of erroring out, the dependency result will be `None`.
      This is useful when you want to have optional authentication.
      It is also useful when you want to have authentication that can be
      provided in one of multiple optional ways (for example, in a cookie or
      in an HTTP Bearer token).
      """
    ),
  ] = True,
):
  self.model: APIKey = APIKey(
    **{"in": APIKeyIn.cookie}, # type: ignore[arg-type]
    name=name,
    description=description,
  )
  self.scheme_name = scheme_name or self.__class__.__name__
  self.auto_error = auto_error

```
  
---|---  
###  model `instance-attribute` ¶
```
model = APIKey(
  **{"in": cookie}, name=name, description=description
)

```

###  scheme_name `instance-attribute` ¶
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` ¶
```
auto_error = auto_error

```

###  check_api_key `staticmethod` ¶
```
check_api_key(api_key, auto_error)

```

PARAMETER | DESCRIPTION  
---|---  
`api_key` |  **TYPE:** `Optional[str]`  
`auto_error` |  **TYPE:** `bool`  
Source code in `fastapi/security/api_key.py`
```
12
13
14
15
16
17
18
19
20
```
| ```
@staticmethod
defcheck_api_key(api_key: Optional[str], auto_error: bool) -> Optional[str]:
  if not api_key:
    if auto_error:
      raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
      )
    return None
  return api_key

```
  
---|---  
##  fastapi.security.APIKeyHeader ¶
```
APIKeyHeader(
  *,
  name,
  scheme_name=None,
  description=None,
  auto_error=True
)

```

Bases: `APIKeyBase`
API key authentication using a header.
This defines the name of the header that should be provided in the request with the API key and integrates that into the OpenAPI documentation. It extracts the key value sent in the header automatically and provides it as the dependency result. But it doesn't define how to send that key to the client.
#### Usage¶
Create an instance object and use that object as the dependency in `Depends()`.
The dependency result will be a string containing the key value.
#### Example¶
```
fromfastapiimport Depends, FastAPI
fromfastapi.securityimport APIKeyHeader
app = FastAPI()
header_scheme = APIKeyHeader(name="x-key")
@app.get("/items/")
async defread_items(key: str = Depends(header_scheme)):
  return {"key": key}

```

PARAMETER | DESCRIPTION  
---|---  
`name` |  Header name. **TYPE:** `str`  
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`auto_error` |  By default, if the header is not provided, `APIKeyHeader` will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the header is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in a header or in an HTTP Bearer token). **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/security/api_key.py`
```
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
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
```
| ```
def__init__(
  self,
  *,
  name: Annotated[str, Doc("Header name.")],
  scheme_name: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme name.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  description: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme description.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  auto_error: Annotated[
    bool,
    Doc(
"""
      By default, if the header is not provided, `APIKeyHeader` will
      automatically cancel the request and send the client an error.
      If `auto_error` is set to `False`, when the header is not available,
      instead of erroring out, the dependency result will be `None`.
      This is useful when you want to have optional authentication.
      It is also useful when you want to have authentication that can be
      provided in one of multiple optional ways (for example, in a header or
      in an HTTP Bearer token).
      """
    ),
  ] = True,
):
  self.model: APIKey = APIKey(
    **{"in": APIKeyIn.header}, # type: ignore[arg-type]
    name=name,
    description=description,
  )
  self.scheme_name = scheme_name or self.__class__.__name__
  self.auto_error = auto_error

```
  
---|---  
###  model `instance-attribute` ¶
```
model = APIKey(
  **{"in": header}, name=name, description=description
)

```

###  scheme_name `instance-attribute` ¶
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` ¶
```
auto_error = auto_error

```

###  check_api_key `staticmethod` ¶
```
check_api_key(api_key, auto_error)

```

PARAMETER | DESCRIPTION  
---|---  
`api_key` |  **TYPE:** `Optional[str]`  
`auto_error` |  **TYPE:** `bool`  
Source code in `fastapi/security/api_key.py`
```
12
13
14
15
16
17
18
19
20
```
| ```
@staticmethod
defcheck_api_key(api_key: Optional[str], auto_error: bool) -> Optional[str]:
  if not api_key:
    if auto_error:
      raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
      )
    return None
  return api_key

```
  
---|---  
##  fastapi.security.APIKeyQuery ¶
```
APIKeyQuery(
  *,
  name,
  scheme_name=None,
  description=None,
  auto_error=True
)

```

Bases: `APIKeyBase`
API key authentication using a query parameter.
This defines the name of the query parameter that should be provided in the request with the API key and integrates that into the OpenAPI documentation. It extracts the key value sent in the query parameter automatically and provides it as the dependency result. But it doesn't define how to send that API key to the client.
#### Usage¶
Create an instance object and use that object as the dependency in `Depends()`.
The dependency result will be a string containing the key value.
#### Example¶
```
fromfastapiimport Depends, FastAPI
fromfastapi.securityimport APIKeyQuery
app = FastAPI()
query_scheme = APIKeyQuery(name="api_key")
@app.get("/items/")
async defread_items(api_key: str = Depends(query_scheme)):
  return {"api_key": api_key}

```

PARAMETER | DESCRIPTION  
---|---  
`name` |  Query parameter name. **TYPE:** `str`  
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`auto_error` |  By default, if the query parameter is not provided, `APIKeyQuery` will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the query parameter is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in a query parameter or in an HTTP Bearer token). **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/security/api_key.py`
```
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
```
| ```
def__init__(
  self,
  *,
  name: Annotated[
    str,
    Doc("Query parameter name."),
  ],
  scheme_name: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme name.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  description: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme description.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  auto_error: Annotated[
    bool,
    Doc(
"""
      By default, if the query parameter is not provided, `APIKeyQuery` will
      automatically cancel the request and send the client an error.
      If `auto_error` is set to `False`, when the query parameter is not
      available, instead of erroring out, the dependency result will be
      `None`.
      This is useful when you want to have optional authentication.
      It is also useful when you want to have authentication that can be
      provided in one of multiple optional ways (for example, in a query
      parameter or in an HTTP Bearer token).
      """
    ),
  ] = True,
):
  self.model: APIKey = APIKey(
    **{"in": APIKeyIn.query}, # type: ignore[arg-type]
    name=name,
    description=description,
  )
  self.scheme_name = scheme_name or self.__class__.__name__
  self.auto_error = auto_error

```
  
---|---  
###  model `instance-attribute` ¶
```
model = APIKey(
  **{"in": query}, name=name, description=description
)

```

###  scheme_name `instance-attribute` ¶
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` ¶
```
auto_error = auto_error

```

###  check_api_key `staticmethod` ¶
```
check_api_key(api_key, auto_error)

```

PARAMETER | DESCRIPTION  
---|---  
`api_key` |  **TYPE:** `Optional[str]`  
`auto_error` |  **TYPE:** `bool`  
Source code in `fastapi/security/api_key.py`
```
12
13
14
15
16
17
18
19
20
```
| ```
@staticmethod
defcheck_api_key(api_key: Optional[str], auto_error: bool) -> Optional[str]:
  if not api_key:
    if auto_error:
      raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
      )
    return None
  return api_key

```
  
---|---  
## HTTP Authentication Schemes¶
##  fastapi.security.HTTPBasic ¶
```
HTTPBasic(
  *,
  scheme_name=None,
  realm=None,
  description=None,
  auto_error=True
)

```

Bases: `HTTPBase`
HTTP Basic authentication.
#### Usage¶
Create an instance object and use that object as the dependency in `Depends()`.
The dependency result will be an `HTTPBasicCredentials` object containing the `username` and the `password`.
Read more about it in the FastAPI docs for HTTP Basic Auth.
#### Example¶
```
fromtypingimport Annotated
fromfastapiimport Depends, FastAPI
fromfastapi.securityimport HTTPBasic, HTTPBasicCredentials
app = FastAPI()
security = HTTPBasic()
@app.get("/users/me")
defread_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
  return {"username": credentials.username, "password": credentials.password}

```

PARAMETER | DESCRIPTION  
---|---  
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`realm` |  HTTP Basic authentication realm. **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`auto_error` |  By default, if the HTTP Basic authentication is not provided (a header), `HTTPBasic` will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Basic authentication is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in HTTP Basic authentication or in an HTTP Bearer token). **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/security/http.py`
```
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
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
```
| ```
def__init__(
  self,
  *,
  scheme_name: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme name.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  realm: Annotated[
    Optional[str],
    Doc(
"""
      HTTP Basic authentication realm.
      """
    ),
  ] = None,
  description: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme description.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  auto_error: Annotated[
    bool,
    Doc(
"""
      By default, if the HTTP Basic authentication is not provided (a
      header), `HTTPBasic` will automatically cancel the request and send the
      client an error.
      If `auto_error` is set to `False`, when the HTTP Basic authentication
      is not available, instead of erroring out, the dependency result will
      be `None`.
      This is useful when you want to have optional authentication.
      It is also useful when you want to have authentication that can be
      provided in one of multiple optional ways (for example, in HTTP Basic
      authentication or in an HTTP Bearer token).
      """
    ),
  ] = True,
):
  self.model = HTTPBaseModel(scheme="basic", description=description)
  self.scheme_name = scheme_name or self.__class__.__name__
  self.realm = realm
  self.auto_error = auto_error

```
  
---|---  
###  model `instance-attribute` ¶
```
model = HTTPBase(scheme='basic', description=description)

```

###  scheme_name `instance-attribute` ¶
```
scheme_name = scheme_name or __name__

```

###  realm `instance-attribute` ¶
```
realm = realm

```

###  auto_error `instance-attribute` ¶
```
auto_error = auto_error

```

##  fastapi.security.HTTPBearer ¶
```
HTTPBearer(
  *,
  bearerFormat=None,
  scheme_name=None,
  description=None,
  auto_error=True
)

```

Bases: `HTTPBase`
HTTP Bearer token authentication.
#### Usage¶
Create an instance object and use that object as the dependency in `Depends()`.
The dependency result will be an `HTTPAuthorizationCredentials` object containing the `scheme` and the `credentials`.
#### Example¶
```
fromtypingimport Annotated
fromfastapiimport Depends, FastAPI
fromfastapi.securityimport HTTPAuthorizationCredentials, HTTPBearer
app = FastAPI()
security = HTTPBearer()
@app.get("/users/me")
defread_current_user(
  credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
):
  return {"scheme": credentials.scheme, "credentials": credentials.credentials}

```

PARAMETER | DESCRIPTION  
---|---  
`bearerFormat` |  Bearer token format. **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`auto_error` |  By default, if the HTTP Bearer token is not provided (in an `Authorization` header), `HTTPBearer` will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Bearer token is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in an HTTP Bearer token or in a cookie). **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/security/http.py`
```
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
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
297
298
299
```
| ```
def__init__(
  self,
  *,
  bearerFormat: Annotated[Optional[str], Doc("Bearer token format.")] = None,
  scheme_name: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme name.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  description: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme description.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  auto_error: Annotated[
    bool,
    Doc(
"""
      By default, if the HTTP Bearer token is not provided (in an
      `Authorization` header), `HTTPBearer` will automatically cancel the
      request and send the client an error.
      If `auto_error` is set to `False`, when the HTTP Bearer token
      is not available, instead of erroring out, the dependency result will
      be `None`.
      This is useful when you want to have optional authentication.
      It is also useful when you want to have authentication that can be
      provided in one of multiple optional ways (for example, in an HTTP
      Bearer token or in a cookie).
      """
    ),
  ] = True,
):
  self.model = HTTPBearerModel(bearerFormat=bearerFormat, description=description)
  self.scheme_name = scheme_name or self.__class__.__name__
  self.auto_error = auto_error

```
  
---|---  
###  model `instance-attribute` ¶
```
model = HTTPBearer(
  bearerFormat=bearerFormat, description=description
)

```

###  scheme_name `instance-attribute` ¶
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` ¶
```
auto_error = auto_error

```

##  fastapi.security.HTTPDigest ¶
```
HTTPDigest(
  *, scheme_name=None, description=None, auto_error=True
)

```

Bases: `HTTPBase`
HTTP Digest authentication.
#### Usage¶
Create an instance object and use that object as the dependency in `Depends()`.
The dependency result will be an `HTTPAuthorizationCredentials` object containing the `scheme` and the `credentials`.
#### Example¶
```
fromtypingimport Annotated
fromfastapiimport Depends, FastAPI
fromfastapi.securityimport HTTPAuthorizationCredentials, HTTPDigest
app = FastAPI()
security = HTTPDigest()
@app.get("/users/me")
defread_current_user(
  credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
):
  return {"scheme": credentials.scheme, "credentials": credentials.credentials}

```

PARAMETER | DESCRIPTION  
---|---  
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`auto_error` |  By default, if the HTTP Digest is not provided, `HTTPDigest` will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Digest is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in HTTP Digest or in a cookie). **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/security/http.py`
```
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
```
| ```
def__init__(
  self,
  *,
  scheme_name: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme name.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  description: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme description.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  auto_error: Annotated[
    bool,
    Doc(
"""
      By default, if the HTTP Digest is not provided, `HTTPDigest` will
      automatically cancel the request and send the client an error.
      If `auto_error` is set to `False`, when the HTTP Digest is not
      available, instead of erroring out, the dependency result will
      be `None`.
      This is useful when you want to have optional authentication.
      It is also useful when you want to have authentication that can be
      provided in one of multiple optional ways (for example, in HTTP
      Digest or in a cookie).
      """
    ),
  ] = True,
):
  self.model = HTTPBaseModel(scheme="digest", description=description)
  self.scheme_name = scheme_name or self.__class__.__name__
  self.auto_error = auto_error

```
  
---|---  
###  model `instance-attribute` ¶
```
model = HTTPBase(scheme='digest', description=description)

```

###  scheme_name `instance-attribute` ¶
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` ¶
```
auto_error = auto_error

```

## HTTP Credentials¶
##  fastapi.security.HTTPAuthorizationCredentials ¶
Bases: `BaseModel`
The HTTP authorization credentials in the result of using `HTTPBearer` or `HTTPDigest` in a dependency.
The HTTP authorization header value is split by the first space.
The first part is the `scheme`, the second part is the `credentials`.
For example, in an HTTP Bearer token scheme, the client will send a header like:
```
Authorization: Bearer deadbeef12346

```

In this case:
  * `scheme` will have the value `"Bearer"`
  * `credentials` will have the value `"deadbeef12346"`


###  scheme `instance-attribute` ¶
```
scheme

```

The HTTP authorization scheme extracted from the header value.
###  credentials `instance-attribute` ¶
```
credentials

```

The HTTP authorization credentials extracted from the header value.
##  fastapi.security.HTTPBasicCredentials ¶
Bases: `BaseModel`
The HTTP Basic credentials given as the result of using `HTTPBasic` in a dependency.
Read more about it in the FastAPI docs for HTTP Basic Auth.
###  username `instance-attribute` ¶
```
username

```

The HTTP Basic username.
###  password `instance-attribute` ¶
```
password

```

The HTTP Basic password.
## OAuth2 Authentication¶
##  fastapi.security.OAuth2 ¶
```
OAuth2(
  *,
  flows=OAuthFlows(),
  scheme_name=None,
  description=None,
  auto_error=True
)

```

Bases: `SecurityBase`
This is the base class for OAuth2 authentication, an instance of it would be used as a dependency. All other OAuth2 classes inherit from it and customize it for each OAuth2 flow.
You normally would not create a new class inheriting from it but use one of the existing subclasses, and maybe compose them if you want to support multiple flows.
Read more about it in the FastAPI docs for Security.
PARAMETER | DESCRIPTION  
---|---  
`flows` |  The dictionary of OAuth2 flows. **TYPE:** `Union[OAuthFlows, Dict[str, Dict[str, Any]]]` **DEFAULT:** `OAuthFlows()`  
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`auto_error` |  By default, if no HTTP Authorization header is provided, required for OAuth2 authentication, it will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Authorization header is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, with OAuth2 or in a cookie). **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/security/oauth2.py`
```
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
```
| ```
def__init__(
  self,
  *,
  flows: Annotated[
    Union[OAuthFlowsModel, Dict[str, Dict[str, Any]]],
    Doc(
"""
      The dictionary of OAuth2 flows.
      """
    ),
  ] = OAuthFlowsModel(),
  scheme_name: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme name.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  description: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme description.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  auto_error: Annotated[
    bool,
    Doc(
"""
      By default, if no HTTP Authorization header is provided, required for
      OAuth2 authentication, it will automatically cancel the request and
      send the client an error.
      If `auto_error` is set to `False`, when the HTTP Authorization header
      is not available, instead of erroring out, the dependency result will
      be `None`.
      This is useful when you want to have optional authentication.
      It is also useful when you want to have authentication that can be
      provided in one of multiple optional ways (for example, with OAuth2
      or in a cookie).
      """
    ),
  ] = True,
):
  self.model = OAuth2Model(
    flows=cast(OAuthFlowsModel, flows), description=description
  )
  self.scheme_name = scheme_name or self.__class__.__name__
  self.auto_error = auto_error

```
  
---|---  
###  model `instance-attribute` ¶
```
model = OAuth2(
  flows=cast(OAuthFlows, flows), description=description
)

```

###  scheme_name `instance-attribute` ¶
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` ¶
```
auto_error = auto_error

```

##  fastapi.security.OAuth2AuthorizationCodeBearer ¶
```
OAuth2AuthorizationCodeBearer(
  authorizationUrl,
  tokenUrl,
  refreshUrl=None,
  scheme_name=None,
  scopes=None,
  description=None,
  auto_error=True,
)

```

Bases: `OAuth2`
OAuth2 flow for authentication using a bearer token obtained with an OAuth2 code flow. An instance of it would be used as a dependency.
PARAMETER | DESCRIPTION  
---|---  
`authorizationUrl` |  **TYPE:** `str`  
`tokenUrl` |  The URL to obtain the OAuth2 token. **TYPE:** `str`  
`refreshUrl` |  The URL to refresh the token and obtain a new one. **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`scopes` |  The OAuth2 scopes that would be required by the _path operations_ that use this dependency. **TYPE:** `Optional[Dict[str, str]]` **DEFAULT:** `None`  
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`auto_error` |  By default, if no HTTP Authorization header is provided, required for OAuth2 authentication, it will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Authorization header is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, with OAuth2 or in a cookie). **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/security/oauth2.py`
```
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
```
| ```
def__init__(
  self,
  authorizationUrl: str,
  tokenUrl: Annotated[
    str,
    Doc(
"""
      The URL to obtain the OAuth2 token.
      """
    ),
  ],
  refreshUrl: Annotated[
    Optional[str],
    Doc(
"""
      The URL to refresh the token and obtain a new one.
      """
    ),
  ] = None,
  scheme_name: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme name.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  scopes: Annotated[
    Optional[Dict[str, str]],
    Doc(
"""
      The OAuth2 scopes that would be required by the *path operations* that
      use this dependency.
      """
    ),
  ] = None,
  description: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme description.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  auto_error: Annotated[
    bool,
    Doc(
"""
      By default, if no HTTP Authorization header is provided, required for
      OAuth2 authentication, it will automatically cancel the request and
      send the client an error.
      If `auto_error` is set to `False`, when the HTTP Authorization header
      is not available, instead of erroring out, the dependency result will
      be `None`.
      This is useful when you want to have optional authentication.
      It is also useful when you want to have authentication that can be
      provided in one of multiple optional ways (for example, with OAuth2
      or in a cookie).
      """
    ),
  ] = True,
):
  if not scopes:
    scopes = {}
  flows = OAuthFlowsModel(
    authorizationCode=cast(
      Any,
      {
        "authorizationUrl": authorizationUrl,
        "tokenUrl": tokenUrl,
        "refreshUrl": refreshUrl,
        "scopes": scopes,
      },
    )
  )
  super().__init__(
    flows=flows,
    scheme_name=scheme_name,
    description=description,
    auto_error=auto_error,
  )

```
  
---|---  
###  model `instance-attribute` ¶
```
model = OAuth2(
  flows=cast(OAuthFlows, flows), description=description
)

```

###  scheme_name `instance-attribute` ¶
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` ¶
```
auto_error = auto_error

```

##  fastapi.security.OAuth2PasswordBearer ¶
```
OAuth2PasswordBearer(
  tokenUrl,
  scheme_name=None,
  scopes=None,
  description=None,
  auto_error=True,
)

```

Bases: `OAuth2`
OAuth2 flow for authentication using a bearer token obtained with a password. An instance of it would be used as a dependency.
Read more about it in the FastAPI docs for Simple OAuth2 with Password and Bearer.
PARAMETER | DESCRIPTION  
---|---  
`tokenUrl` |  The URL to obtain the OAuth2 token. This would be the _path operation_ that has `OAuth2PasswordRequestForm` as a dependency. **TYPE:** `str`  
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`scopes` |  The OAuth2 scopes that would be required by the _path operations_ that use this dependency. **TYPE:** `Optional[Dict[str, str]]` **DEFAULT:** `None`  
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`auto_error` |  By default, if no HTTP Authorization header is provided, required for OAuth2 authentication, it will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Authorization header is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, with OAuth2 or in a cookie). **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/security/oauth2.py`
```
400
401
402
403
404
405
406
407
408
409
410
411
412
413
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
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
```
| ```
def__init__(
  self,
  tokenUrl: Annotated[
    str,
    Doc(
"""
      The URL to obtain the OAuth2 token. This would be the *path operation*
      that has `OAuth2PasswordRequestForm` as a dependency.
      """
    ),
  ],
  scheme_name: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme name.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  scopes: Annotated[
    Optional[Dict[str, str]],
    Doc(
"""
      The OAuth2 scopes that would be required by the *path operations* that
      use this dependency.
      """
    ),
  ] = None,
  description: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme description.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  auto_error: Annotated[
    bool,
    Doc(
"""
      By default, if no HTTP Authorization header is provided, required for
      OAuth2 authentication, it will automatically cancel the request and
      send the client an error.
      If `auto_error` is set to `False`, when the HTTP Authorization header
      is not available, instead of erroring out, the dependency result will
      be `None`.
      This is useful when you want to have optional authentication.
      It is also useful when you want to have authentication that can be
      provided in one of multiple optional ways (for example, with OAuth2
      or in a cookie).
      """
    ),
  ] = True,
):
  if not scopes:
    scopes = {}
  flows = OAuthFlowsModel(
    password=cast(Any, {"tokenUrl": tokenUrl, "scopes": scopes})
  )
  super().__init__(
    flows=flows,
    scheme_name=scheme_name,
    description=description,
    auto_error=auto_error,
  )

```
  
---|---  
###  model `instance-attribute` ¶
```
model = OAuth2(
  flows=cast(OAuthFlows, flows), description=description
)

```

###  scheme_name `instance-attribute` ¶
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` ¶
```
auto_error = auto_error

```

## OAuth2 Password Form¶
##  fastapi.security.OAuth2PasswordRequestForm ¶
```
OAuth2PasswordRequestForm(
  *,
  grant_type=None,
  username,
  password,
  scope="",
  client_id=None,
  client_secret=None
)

```

This is a dependency class to collect the `username` and `password` as form data for an OAuth2 password flow.
The OAuth2 specification dictates that for a password flow the data should be collected using form data (instead of JSON) and that it should have the specific fields `username` and `password`.
All the initialization parameters are extracted from the request.
Read more about it in the FastAPI docs for Simple OAuth2 with Password and Bearer.
#### Example¶
```
fromtypingimport Annotated
fromfastapiimport Depends, FastAPI
fromfastapi.securityimport OAuth2PasswordRequestForm
app = FastAPI()
@app.post("/login")
deflogin(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
  data = {}
  data["scopes"] = []
  for scope in form_data.scopes:
    data["scopes"].append(scope)
  if form_data.client_id:
    data["client_id"] = form_data.client_id
  if form_data.client_secret:
    data["client_secret"] = form_data.client_secret
  return data

```

Note that for OAuth2 the scope `items:read` is a single scope in an opaque string. You could have custom internal logic to separate it by colon characters (`:`) or similar, and get the two parts `items` and `read`. Many applications do that to group and organize permissions, you could do it as well in your application, just know that that it is application specific, it's not part of the specification.
PARAMETER | DESCRIPTION  
---|---  
`grant_type` |  The OAuth2 spec says it is required and MUST be the fixed string "password". Nevertheless, this dependency class is permissive and allows not passing it. If you want to enforce it, use instead the `OAuth2PasswordRequestFormStrict` dependency. **TYPE:** `Union[str, None]` **DEFAULT:** `None`  
`username` |  `username` string. The OAuth2 spec requires the exact field name `username`. **TYPE:** `str`  
`password` |  `password` string. The OAuth2 spec requires the exact field name `password". **TYPE:** `str`  
`scope` |  A single string with actually several scopes separated by spaces. Each scope is also a string. For example, a single string with: ```python "items:read items:write users:read profile openid" ```` would represent the scopes:
  * `items:read`
  * `items:write`
  * `users:read`
  * `profile`
  * `openid`

**TYPE:** `str` **DEFAULT:** `''`  
`client_id` |  If there's a `client_id`, it can be sent as part of the form fields. But the OAuth2 specification recommends sending the `client_id` and `client_secret` (if any) using HTTP Basic auth. **TYPE:** `Union[str, None]` **DEFAULT:** `None`  
`client_secret` |  If there's a `client_password` (and a `client_id`), they can be sent as part of the form fields. But the OAuth2 specification recommends sending the `client_id` and `client_secret` (if any) using HTTP Basic auth. **TYPE:** `Union[str, None]` **DEFAULT:** `None`  
Source code in `fastapi/security/oauth2.py`
```
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
141
142
143
144
145
146
147
148
149
```
| ```
def__init__(
  self,
  *,
  grant_type: Annotated[
    Union[str, None],
    Form(pattern="^password$"),
    Doc(
"""
      The OAuth2 spec says it is required and MUST be the fixed string
      "password". Nevertheless, this dependency class is permissive and
      allows not passing it. If you want to enforce it, use instead the
      `OAuth2PasswordRequestFormStrict` dependency.
      """
    ),
  ] = None,
  username: Annotated[
    str,
    Form(),
    Doc(
"""
      `username` string. The OAuth2 spec requires the exact field name
      `username`.
      """
    ),
  ],
  password: Annotated[
    str,
    Form(),
    Doc(
"""
      `password` string. The OAuth2 spec requires the exact field name
      `password".
      """
    ),
  ],
  scope: Annotated[
    str,
    Form(),
    Doc(
"""
      A single string with actually several scopes separated by spaces. Each
      scope is also a string.
      For example, a single string with:
  ```python
      "items:read items:write users:read profile openid"
  ````
      would represent the scopes:
      * `items:read`
      * `items:write`
      * `users:read`
      * `profile`
      * `openid`
      """
    ),
  ] = "",
  client_id: Annotated[
    Union[str, None],
    Form(),
    Doc(
"""
      If there's a `client_id`, it can be sent as part of the form fields.
      But the OAuth2 specification recommends sending the `client_id` and
      `client_secret` (if any) using HTTP Basic auth.
      """
    ),
  ] = None,
  client_secret: Annotated[
    Union[str, None],
    Form(),
    Doc(
"""
      If there's a `client_password` (and a `client_id`), they can be sent
      as part of the form fields. But the OAuth2 specification recommends
      sending the `client_id` and `client_secret` (if any) using HTTP Basic
      auth.
      """
    ),
  ] = None,
):
  self.grant_type = grant_type
  self.username = username
  self.password = password
  self.scopes = scope.split()
  self.client_id = client_id
  self.client_secret = client_secret

```
  
---|---  
###  grant_type `instance-attribute` ¶
```
grant_type = grant_type

```

###  username `instance-attribute` ¶
```
username = username

```

###  password `instance-attribute` ¶
```
password = password

```

###  scopes `instance-attribute` ¶
```
scopes = split()

```

###  client_id `instance-attribute` ¶
```
client_id = client_id

```

###  client_secret `instance-attribute` ¶
```
client_secret = client_secret

```

##  fastapi.security.OAuth2PasswordRequestFormStrict ¶
```
OAuth2PasswordRequestFormStrict(
  grant_type,
  username,
  password,
  scope="",
  client_id=None,
  client_secret=None,
)

```

Bases: `OAuth2PasswordRequestForm`
This is a dependency class to collect the `username` and `password` as form data for an OAuth2 password flow.
The OAuth2 specification dictates that for a password flow the data should be collected using form data (instead of JSON) and that it should have the specific fields `username` and `password`.
All the initialization parameters are extracted from the request.
The only difference between `OAuth2PasswordRequestFormStrict` and `OAuth2PasswordRequestForm` is that `OAuth2PasswordRequestFormStrict` requires the client to send the form field `grant_type` with the value `"password"`, which is required in the OAuth2 specification (it seems that for no particular reason), while for `OAuth2PasswordRequestForm` `grant_type` is optional.
Read more about it in the FastAPI docs for Simple OAuth2 with Password and Bearer.
#### Example¶
```
fromtypingimport Annotated
fromfastapiimport Depends, FastAPI
fromfastapi.securityimport OAuth2PasswordRequestForm
app = FastAPI()
@app.post("/login")
deflogin(form_data: Annotated[OAuth2PasswordRequestFormStrict, Depends()]):
  data = {}
  data["scopes"] = []
  for scope in form_data.scopes:
    data["scopes"].append(scope)
  if form_data.client_id:
    data["client_id"] = form_data.client_id
  if form_data.client_secret:
    data["client_secret"] = form_data.client_secret
  return data

```

Note that for OAuth2 the scope `items:read` is a single scope in an opaque string. You could have custom internal logic to separate it by colon characters (`:`) or similar, and get the two parts `items` and `read`. Many applications do that to group and organize permissions, you could do it as well in your application, just know that that it is application specific, it's not part of the specification.
the OAuth2 spec says it is required and MUST be the fixed string "password".
This dependency is strict about it. If you want to be permissive, use instead the OAuth2PasswordRequestForm dependency class.
username: username string. The OAuth2 spec requires the exact field name "username". password: password string. The OAuth2 spec requires the exact field name "password". scope: Optional string. Several scopes (each one a string) separated by spaces. E.g. "items:read items:write users:read profile openid" client_id: optional string. OAuth2 recommends sending the client_id and client_secret (if any) using HTTP Basic auth, as: client_id:client_secret client_secret: optional string. OAuth2 recommends sending the client_id and client_secret (if any) using HTTP Basic auth, as: client_id:client_secret
PARAMETER | DESCRIPTION  
---|---  
`grant_type` |  The OAuth2 spec says it is required and MUST be the fixed string "password". This dependency is strict about it. If you want to be permissive, use instead the `OAuth2PasswordRequestForm` dependency class. **TYPE:** `str`  
`username` |  `username` string. The OAuth2 spec requires the exact field name `username`. **TYPE:** `str`  
`password` |  `password` string. The OAuth2 spec requires the exact field name `password". **TYPE:** `str`  
`scope` |  A single string with actually several scopes separated by spaces. Each scope is also a string. For example, a single string with: ```python "items:read items:write users:read profile openid" ```` would represent the scopes:
  * `items:read`
  * `items:write`
  * `users:read`
  * `profile`
  * `openid`

**TYPE:** `str` **DEFAULT:** `''`  
`client_id` |  If there's a `client_id`, it can be sent as part of the form fields. But the OAuth2 specification recommends sending the `client_id` and `client_secret` (if any) using HTTP Basic auth. **TYPE:** `Union[str, None]` **DEFAULT:** `None`  
`client_secret` |  If there's a `client_password` (and a `client_id`), they can be sent as part of the form fields. But the OAuth2 specification recommends sending the `client_id` and `client_secret` (if any) using HTTP Basic auth. **TYPE:** `Union[str, None]` **DEFAULT:** `None`  
Source code in `fastapi/security/oauth2.py`
```
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
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
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
297
298
299
300
301
302
303
304
305
```
| ```
def__init__(
  self,
  grant_type: Annotated[
    str,
    Form(pattern="^password$"),
    Doc(
"""
      The OAuth2 spec says it is required and MUST be the fixed string
      "password". This dependency is strict about it. If you want to be
      permissive, use instead the `OAuth2PasswordRequestForm` dependency
      class.
      """
    ),
  ],
  username: Annotated[
    str,
    Form(),
    Doc(
"""
      `username` string. The OAuth2 spec requires the exact field name
      `username`.
      """
    ),
  ],
  password: Annotated[
    str,
    Form(),
    Doc(
"""
      `password` string. The OAuth2 spec requires the exact field name
      `password".
      """
    ),
  ],
  scope: Annotated[
    str,
    Form(),
    Doc(
"""
      A single string with actually several scopes separated by spaces. Each
      scope is also a string.
      For example, a single string with:
  ```python
      "items:read items:write users:read profile openid"
  ````
      would represent the scopes:
      * `items:read`
      * `items:write`
      * `users:read`
      * `profile`
      * `openid`
      """
    ),
  ] = "",
  client_id: Annotated[
    Union[str, None],
    Form(),
    Doc(
"""
      If there's a `client_id`, it can be sent as part of the form fields.
      But the OAuth2 specification recommends sending the `client_id` and
      `client_secret` (if any) using HTTP Basic auth.
      """
    ),
  ] = None,
  client_secret: Annotated[
    Union[str, None],
    Form(),
    Doc(
"""
      If there's a `client_password` (and a `client_id`), they can be sent
      as part of the form fields. But the OAuth2 specification recommends
      sending the `client_id` and `client_secret` (if any) using HTTP Basic
      auth.
      """
    ),
  ] = None,
):
  super().__init__(
    grant_type=grant_type,
    username=username,
    password=password,
    scope=scope,
    client_id=client_id,
    client_secret=client_secret,
  )

```
  
---|---  
###  grant_type `instance-attribute` ¶
```
grant_type = grant_type

```

###  username `instance-attribute` ¶
```
username = username

```

###  password `instance-attribute` ¶
```
password = password

```

###  scopes `instance-attribute` ¶
```
scopes = split()

```

###  client_id `instance-attribute` ¶
```
client_id = client_id

```

###  client_secret `instance-attribute` ¶
```
client_secret = client_secret

```

## OAuth2 Security Scopes in Dependencies¶
##  fastapi.security.SecurityScopes ¶
```
SecurityScopes(scopes=None)

```

This is a special class that you can define in a parameter in a dependency to obtain the OAuth2 scopes required by all the dependencies in the same chain.
This way, multiple dependencies can have different scopes, even when used in the same _path operation_. And with this, you can access all the scopes required in all those dependencies in a single place.
Read more about it in the FastAPI docs for OAuth2 scopes.
PARAMETER | DESCRIPTION  
---|---  
`scopes` |  This will be filled by FastAPI. **TYPE:** `Optional[List[str]]` **DEFAULT:** `None`  
Source code in `fastapi/security/oauth2.py`
```
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
```
| ```
def__init__(
  self,
  scopes: Annotated[
    Optional[List[str]],
    Doc(
"""
      This will be filled by FastAPI.
      """
    ),
  ] = None,
):
  self.scopes: Annotated[
    List[str],
    Doc(
"""
      The list of all the scopes required by dependencies.
      """
    ),
  ] = scopes or []
  self.scope_str: Annotated[
    str,
    Doc(
"""
      All the scopes required by all the dependencies in a single string
      separated by spaces, as defined in the OAuth2 specification.
      """
    ),
  ] = " ".join(self.scopes)

```
  
---|---  
###  scopes `instance-attribute` ¶
```
scopes = scopes or []

```

The list of all the scopes required by dependencies.
###  scope_str `instance-attribute` ¶
```
scope_str = join(scopes)

```

All the scopes required by all the dependencies in a single string separated by spaces, as defined in the OAuth2 specification.
## OpenID Connect¶
##  fastapi.security.OpenIdConnect ¶
```
OpenIdConnect(
  *,
  openIdConnectUrl,
  scheme_name=None,
  description=None,
  auto_error=True
)

```

Bases: `SecurityBase`
OpenID Connect authentication class. An instance of it would be used as a dependency.
PARAMETER | DESCRIPTION  
---|---  
`openIdConnectUrl` |  The OpenID Connect URL. **TYPE:** `str`  
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `Optional[str]` **DEFAULT:** `None`  
`auto_error` |  By default, if no HTTP Authorization header is provided, required for OpenID Connect authentication, it will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Authorization header is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, with OpenID Connect or in a cookie). **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/security/open_id_connect_url.py`
```
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
  *,
  openIdConnectUrl: Annotated[
    str,
    Doc(
"""
    The OpenID Connect URL.
    """
    ),
  ],
  scheme_name: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme name.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  description: Annotated[
    Optional[str],
    Doc(
"""
      Security scheme description.
      It will be included in the generated OpenAPI (e.g. visible at `/docs`).
      """
    ),
  ] = None,
  auto_error: Annotated[
    bool,
    Doc(
"""
      By default, if no HTTP Authorization header is provided, required for
      OpenID Connect authentication, it will automatically cancel the request
      and send the client an error.
      If `auto_error` is set to `False`, when the HTTP Authorization header
      is not available, instead of erroring out, the dependency result will
      be `None`.
      This is useful when you want to have optional authentication.
      It is also useful when you want to have authentication that can be
      provided in one of multiple optional ways (for example, with OpenID
      Connect or in a cookie).
      """
    ),
  ] = True,
):
  self.model = OpenIdConnectModel(
    openIdConnectUrl=openIdConnectUrl, description=description
  )
  self.scheme_name = scheme_name or self.__class__.__name__
  self.auto_error = auto_error

```
  
---|---  
###  model `instance-attribute` ¶
```
model = OpenIdConnect(
  openIdConnectUrl=openIdConnectUrl,
  description=description,
)

```

###  scheme_name `instance-attribute` ¶
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` ¶
```
auto_error = auto_error

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
