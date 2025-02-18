Skip to content 
# Dependencies - `Depends()` and `Security()`¶
## `Depends()`¶
Dependencies are handled mainly with the special function `Depends()` that takes a callable.
Here is the reference for it and its parameters.
You can import it directly from `fastapi`:
```
fromfastapiimport Depends

```

##  fastapi.Depends ¶
```
Depends(dependency=None, *, use_cache=True)

```

Declare a FastAPI dependency.
It takes a single "dependable" callable (like a function).
Don't call it directly, FastAPI will call it for you.
Read more about it in the FastAPI docs for Dependencies.
**Example**
```
fromtypingimport Annotated
fromfastapiimport Depends, FastAPI
app = FastAPI()
async defcommon_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
  return {"q": q, "skip": skip, "limit": limit}
@app.get("/items/")
async defread_items(commons: Annotated[dict, Depends(common_parameters)]):
  return commons

```

PARAMETER | DESCRIPTION  
---|---  
`dependency` |  A "dependable" callable (like a function). Don't call it directly, FastAPI will call it for you, just pass the object directly. **TYPE:** `Optional[Callable[..., Any]]` **DEFAULT:** `None`  
`use_cache` |  By default, after a dependency is called the first time in a request, if the dependency is declared again for the rest of the request (for example if the dependency is needed by several dependencies), the value will be re-used for the rest of the request. Set `use_cache` to `False` to disable this behavior and ensure the dependency is called again (if declared more than once) in the same request. **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/param_functions.py`
```
2220
2221
2222
2223
2224
2225
2226
2227
2228
2229
2230
2231
2232
2233
2234
2235
2236
2237
2238
2239
2240
2241
2242
2243
2244
2245
2246
2247
2248
2249
2250
2251
2252
2253
2254
2255
2256
2257
2258
2259
2260
2261
2262
2263
2264
2265
2266
2267
2268
2269
2270
2271
2272
2273
2274
2275
2276
2277
```
| ```
defDepends( # noqa: N802
  dependency: Annotated[
    Optional[Callable[..., Any]],
    Doc(
"""
      A "dependable" callable (like a function).
      Don't call it directly, FastAPI will call it for you, just pass the object
      directly.
      """
    ),
  ] = None,
  *,
  use_cache: Annotated[
    bool,
    Doc(
"""
      By default, after a dependency is called the first time in a request, if
      the dependency is declared again for the rest of the request (for example
      if the dependency is needed by several dependencies), the value will be
      re-used for the rest of the request.
      Set `use_cache` to `False` to disable this behavior and ensure the
      dependency is called again (if declared more than once) in the same request.
      """
    ),
  ] = True,
) -> Any:
"""
  Declare a FastAPI dependency.
  It takes a single "dependable" callable (like a function).
  Don't call it directly, FastAPI will call it for you.
  Read more about it in the
  [FastAPI docs for Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/).
  **Example**
  ```python
  from typing import Annotated
  from fastapi import Depends, FastAPI
  app = FastAPI()
  async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}
  @app.get("/items/")
  async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
  ```
  """
  return params.Depends(dependency=dependency, use_cache=use_cache)

```
  
---|---  
## `Security()`¶
For many scenarios, you can handle security (authorization, authentication, etc.) with dependencies, using `Depends()`.
But when you want to also declare OAuth2 scopes, you can use `Security()` instead of `Depends()`.
You can import `Security()` directly from `fastapi`:
```
fromfastapiimport Security

```

##  fastapi.Security ¶
```
Security(dependency=None, *, scopes=None, use_cache=True)

```

Declare a FastAPI Security dependency.
The only difference with a regular dependency is that it can declare OAuth2 scopes that will be integrated with OpenAPI and the automatic UI docs (by default at `/docs`).
It takes a single "dependable" callable (like a function).
Don't call it directly, FastAPI will call it for you.
Read more about it in the FastAPI docs for Security and in the FastAPI docs for OAuth2 scopes.
**Example**
```
fromtypingimport Annotated
fromfastapiimport Security, FastAPI
from.dbimport User
from.securityimport get_current_active_user
app = FastAPI()
@app.get("/users/me/items/")
async defread_own_items(
  current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])]
):
  return [{"item_id": "Foo", "owner": current_user.username}]

```

PARAMETER | DESCRIPTION  
---|---  
`dependency` |  A "dependable" callable (like a function). Don't call it directly, FastAPI will call it for you, just pass the object directly. **TYPE:** `Optional[Callable[..., Any]]` **DEFAULT:** `None`  
`scopes` |  OAuth2 scopes required for the _path operation_ that uses this Security dependency. The term "scope" comes from the OAuth2 specification, it seems to be intentionally vague and interpretable. It normally refers to permissions, in cases to roles. These scopes are integrated with OpenAPI (and the API docs at `/docs`). So they are visible in the OpenAPI specification. ) **TYPE:** `Optional[Sequence[str]]` **DEFAULT:** `None`  
`use_cache` |  By default, after a dependency is called the first time in a request, if the dependency is declared again for the rest of the request (for example if the dependency is needed by several dependencies), the value will be re-used for the rest of the request. Set `use_cache` to `False` to disable this behavior and ensure the dependency is called again (if declared more than once) in the same request. **TYPE:** `bool` **DEFAULT:** `True`  
Source code in `fastapi/param_functions.py`
```
2280
2281
2282
2283
2284
2285
2286
2287
2288
2289
2290
2291
2292
2293
2294
2295
2296
2297
2298
2299
2300
2301
2302
2303
2304
2305
2306
2307
2308
2309
2310
2311
2312
2313
2314
2315
2316
2317
2318
2319
2320
2321
2322
2323
2324
2325
2326
2327
2328
2329
2330
2331
2332
2333
2334
2335
2336
2337
2338
2339
2340
2341
2342
2343
2344
2345
2346
2347
2348
2349
2350
2351
2352
2353
2354
2355
2356
2357
2358
2359
2360
```
| ```
defSecurity( # noqa: N802
  dependency: Annotated[
    Optional[Callable[..., Any]],
    Doc(
"""
      A "dependable" callable (like a function).
      Don't call it directly, FastAPI will call it for you, just pass the object
      directly.
      """
    ),
  ] = None,
  *,
  scopes: Annotated[
    Optional[Sequence[str]],
    Doc(
"""
      OAuth2 scopes required for the *path operation* that uses this Security
      dependency.
      The term "scope" comes from the OAuth2 specification, it seems to be
      intentionally vague and interpretable. It normally refers to permissions,
      in cases to roles.
      These scopes are integrated with OpenAPI (and the API docs at `/docs`).
      So they are visible in the OpenAPI specification.
      )
      """
    ),
  ] = None,
  use_cache: Annotated[
    bool,
    Doc(
"""
      By default, after a dependency is called the first time in a request, if
      the dependency is declared again for the rest of the request (for example
      if the dependency is needed by several dependencies), the value will be
      re-used for the rest of the request.
      Set `use_cache` to `False` to disable this behavior and ensure the
      dependency is called again (if declared more than once) in the same request.
      """
    ),
  ] = True,
) -> Any:
"""
  Declare a FastAPI Security dependency.
  The only difference with a regular dependency is that it can declare OAuth2
  scopes that will be integrated with OpenAPI and the automatic UI docs (by default
  at `/docs`).
  It takes a single "dependable" callable (like a function).
  Don't call it directly, FastAPI will call it for you.
  Read more about it in the
  [FastAPI docs for Security](https://fastapi.tiangolo.com/tutorial/security/) and
  in the
  [FastAPI docs for OAuth2 scopes](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/).
  **Example**
  ```python
  from typing import Annotated
  from fastapi import Security, FastAPI
  from .db import User
  from .security import get_current_active_user
  app = FastAPI()
  @app.get("/users/me/items/")
  async def read_own_items(
    current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])]
  ):
    return [{"item_id": "Foo", "owner": current_user.username}]
  ```
  """
  return params.Security(dependency=dependency, scopes=scopes, use_cache=use_cache)

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
