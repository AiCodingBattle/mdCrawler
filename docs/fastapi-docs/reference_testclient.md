Skip to content 
# Test Client - `TestClient`¶
You can use the `TestClient` class to test FastAPI applications without creating an actual HTTP and socket connection, just communicating directly with the FastAPI code.
Read more about it in the FastAPI docs for Testing.
You can import it directly from `fastapi.testclient`:
```
fromfastapi.testclientimport TestClient

```

##  fastapi.testclient.TestClient ¶
```
TestClient(
  app,
  base_url="http://testserver",
  raise_server_exceptions=True,
  root_path="",
  backend="asyncio",
  backend_options=None,
  cookies=None,
  headers=None,
  follow_redirects=True,
  client=("testclient", 50000),
)

```

Bases: `Client`
PARAMETER | DESCRIPTION  
---|---  
`app` |  **TYPE:** `ASGIApp`  
`base_url` |  **TYPE:** `str` **DEFAULT:** `'http://testserver'`  
`raise_server_exceptions` |  **TYPE:** `bool` **DEFAULT:** `True`  
`root_path` |  **TYPE:** `str` **DEFAULT:** `''`  
`backend` |  **TYPE:** `Literal['asyncio', 'trio']` **DEFAULT:** `'asyncio'`  
`backend_options` |  **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`  
`cookies` |  **TYPE:** `CookieTypes | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `dict[str, str] | None` **DEFAULT:** `None`  
`follow_redirects` |  **TYPE:** `bool` **DEFAULT:** `True`  
`client` |  **TYPE:** `tuple[str, int]` **DEFAULT:** `('testclient', 50000)`  
Source code in `starlette/testclient.py`
```
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
402
```
| ```
def__init__(
  self,
  app: ASGIApp,
  base_url: str = "http://testserver",
  raise_server_exceptions: bool = True,
  root_path: str = "",
  backend: typing.Literal["asyncio", "trio"] = "asyncio",
  backend_options: dict[str, typing.Any] | None = None,
  cookies: httpx._types.CookieTypes | None = None,
  headers: dict[str, str] | None = None,
  follow_redirects: bool = True,
  client: tuple[str, int] = ("testclient", 50000),
) -> None:
  self.async_backend = _AsyncBackend(backend=backend, backend_options=backend_options or {})
  if _is_asgi3(app):
    asgi_app = app
  else:
    app = typing.cast(ASGI2App, app) # type: ignore[assignment]
    asgi_app = _WrapASGI2(app) # type: ignore[arg-type]
  self.app = asgi_app
  self.app_state: dict[str, typing.Any] = {}
  transport = _TestClientTransport(
    self.app,
    portal_factory=self._portal_factory,
    raise_server_exceptions=raise_server_exceptions,
    root_path=root_path,
    app_state=self.app_state,
    client=client,
  )
  if headers is None:
    headers = {}
  headers.setdefault("user-agent", "testclient")
  super().__init__(
    base_url=base_url,
    headers=headers,
    transport=transport,
    follow_redirects=follow_redirects,
    cookies=cookies,
  )

```
  
---|---  
###  headers `property` `writable` ¶
```
headers

```

HTTP headers to include when sending requests.
###  follow_redirects `instance-attribute` ¶
```
follow_redirects = follow_redirects

```

###  max_redirects `instance-attribute` ¶
```
max_redirects = max_redirects

```

###  is_closed `property` ¶
```
is_closed

```

Check if the client being closed
###  trust_env `property` ¶
```
trust_env

```

###  timeout `property` `writable` ¶
```
timeout

```

###  event_hooks `property` `writable` ¶
```
event_hooks

```

###  auth `property` `writable` ¶
```
auth

```

Authentication class used when none is passed at the request-level.
See also Authentication.
###  base_url `property` `writable` ¶
```
base_url

```

Base URL to use when sending requests with relative URLs.
###  cookies `property` `writable` ¶
```
cookies

```

Cookie values to include when sending requests.
###  params `property` `writable` ¶
```
params

```

Query parameters to include in the URL when sending requests.
###  task `instance-attribute` ¶
```
task

```

###  portal `class-attribute` `instance-attribute` ¶
```
portal = None

```

###  async_backend `instance-attribute` ¶
```
async_backend = _AsyncBackend(
  backend=backend, backend_options=backend_options or {}
)

```

###  app `instance-attribute` ¶
```
app = asgi_app

```

###  app_state `instance-attribute` ¶
```
app_state = {}

```

###  build_request ¶
```
build_request(
  method,
  url,
  *,
  content=None,
  data=None,
  files=None,
  json=None,
  params=None,
  headers=None,
  cookies=None,
  timeout=USE_CLIENT_DEFAULT,
  extensions=None
)

```

Build and return a request instance.
  * The `params`, `headers` and `cookies` arguments are merged with any values set on the client.
  * The `url` argument is merged with any `base_url` set on the client.


See also: Request instances
PARAMETER | DESCRIPTION  
---|---  
`method` |  **TYPE:** `str`  
`url` |  **TYPE:** `URL | str`  
`content` |  **TYPE:** `RequestContent | None` **DEFAULT:** `None`  
`data` |  **TYPE:** `RequestData | None` **DEFAULT:** `None`  
`files` |  **TYPE:** `RequestFiles | None` **DEFAULT:** `None`  
`json` |  **TYPE:** `Any | None` **DEFAULT:** `None`  
`params` |  **TYPE:** `QueryParamTypes | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `HeaderTypes | None` **DEFAULT:** `None`  
`cookies` |  **TYPE:** `CookieTypes | None` **DEFAULT:** `None`  
`timeout` |  **TYPE:** `TimeoutTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`extensions` |  **TYPE:** `RequestExtensions | None` **DEFAULT:** `None`  
Source code in `httpx/_client.py`
```
320
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
```
| ```
defbuild_request(
  self,
  method: str,
  url: URL | str,
  *,
  content: RequestContent | None = None,
  data: RequestData | None = None,
  files: RequestFiles | None = None,
  json: typing.Any | None = None,
  params: QueryParamTypes | None = None,
  headers: HeaderTypes | None = None,
  cookies: CookieTypes | None = None,
  timeout: TimeoutTypes | UseClientDefault = USE_CLIENT_DEFAULT,
  extensions: RequestExtensions | None = None,
) -> Request:
"""
  Build and return a request instance.
  * The `params`, `headers` and `cookies` arguments
  are merged with any values set on the client.
  * The `url` argument is merged with any `base_url` set on the client.
  See also: [Request instances][0]
  [0]: /advanced/clients/#request-instances
  """
  url = self._merge_url(url)
  headers = self._merge_headers(headers)
  cookies = self._merge_cookies(cookies)
  params = self._merge_queryparams(params)
  extensions = {} if extensions is None else extensions
  if "timeout" not in extensions:
    timeout = (
      self.timeout
      if isinstance(timeout, UseClientDefault)
      else Timeout(timeout)
    )
    extensions = dict(**extensions, timeout=timeout.as_dict())
  return Request(
    method,
    url,
    content=content,
    data=data,
    files=files,
    json=json,
    params=params,
    headers=headers,
    cookies=cookies,
    extensions=extensions,
  )

```
  
---|---  
###  stream ¶
```
stream(
  method,
  url,
  *,
  content=None,
  data=None,
  files=None,
  json=None,
  params=None,
  headers=None,
  cookies=None,
  auth=USE_CLIENT_DEFAULT,
  follow_redirects=USE_CLIENT_DEFAULT,
  timeout=USE_CLIENT_DEFAULT,
  extensions=None
)

```

Alternative to `httpx.request()` that streams the response body instead of loading it into memory at once.
**Parameters** : See `httpx.request`.
See also: Streaming Responses
PARAMETER | DESCRIPTION  
---|---  
`method` |  **TYPE:** `str`  
`url` |  **TYPE:** `URL | str`  
`content` |  **TYPE:** `RequestContent | None` **DEFAULT:** `None`  
`data` |  **TYPE:** `RequestData | None` **DEFAULT:** `None`  
`files` |  **TYPE:** `RequestFiles | None` **DEFAULT:** `None`  
`json` |  **TYPE:** `Any | None` **DEFAULT:** `None`  
`params` |  **TYPE:** `QueryParamTypes | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `HeaderTypes | None` **DEFAULT:** `None`  
`cookies` |  **TYPE:** `CookieTypes | None` **DEFAULT:** `None`  
`auth` |  **TYPE:** `AuthTypes | UseClientDefault | None` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`follow_redirects` |  **TYPE:** `bool | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`timeout` |  **TYPE:** `TimeoutTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`extensions` |  **TYPE:** `RequestExtensions | None` **DEFAULT:** `None`  
YIELDS | DESCRIPTION  
---|---  
`Response`  
Source code in `httpx/_client.py`
```
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
```
| ```
@contextmanager
defstream(
  self,
  method: str,
  url: URL | str,
  *,
  content: RequestContent | None = None,
  data: RequestData | None = None,
  files: RequestFiles | None = None,
  json: typing.Any | None = None,
  params: QueryParamTypes | None = None,
  headers: HeaderTypes | None = None,
  cookies: CookieTypes | None = None,
  auth: AuthTypes | UseClientDefault | None = USE_CLIENT_DEFAULT,
  follow_redirects: bool | UseClientDefault = USE_CLIENT_DEFAULT,
  timeout: TimeoutTypes | UseClientDefault = USE_CLIENT_DEFAULT,
  extensions: RequestExtensions | None = None,
) -> typing.Iterator[Response]:
"""
  Alternative to `httpx.request()` that streams the response body
  instead of loading it into memory at once.
  **Parameters**: See `httpx.request`.
  See also: [Streaming Responses][0]
  [0]: /quickstart#streaming-responses
  """
  request = self.build_request(
    method=method,
    url=url,
    content=content,
    data=data,
    files=files,
    json=json,
    params=params,
    headers=headers,
    cookies=cookies,
    timeout=timeout,
    extensions=extensions,
  )
  response = self.send(
    request=request,
    auth=auth,
    follow_redirects=follow_redirects,
    stream=True,
  )
  try:
    yield response
  finally:
    response.close()

```
  
---|---  
###  send ¶
```
send(
  request,
  *,
  stream=False,
  auth=USE_CLIENT_DEFAULT,
  follow_redirects=USE_CLIENT_DEFAULT
)

```

Send a request.
The request is sent as-is, unmodified.
Typically you'll want to build one with `Client.build_request()` so that any client-level configuration is merged into the request, but passing an explicit `httpx.Request()` is supported as well.
See also: Request instances
PARAMETER | DESCRIPTION  
---|---  
`request` |  **TYPE:** `Request`  
`stream` |  **TYPE:** `bool` **DEFAULT:** `False`  
`auth` |  **TYPE:** `AuthTypes | UseClientDefault | None` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`follow_redirects` |  **TYPE:** `bool | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
Source code in `httpx/_client.py`
```
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
```
| ```
defsend(
  self,
  request: Request,
  *,
  stream: bool = False,
  auth: AuthTypes | UseClientDefault | None = USE_CLIENT_DEFAULT,
  follow_redirects: bool | UseClientDefault = USE_CLIENT_DEFAULT,
) -> Response:
"""
  Send a request.
  The request is sent as-is, unmodified.
  Typically you'll want to build one with `Client.build_request()`
  so that any client-level configuration is merged into the request,
  but passing an explicit `httpx.Request()` is supported as well.
  See also: [Request instances][0]
  [0]: /advanced/clients/#request-instances
  """
  if self._state == ClientState.CLOSED:
    raise RuntimeError("Cannot send a request, as the client has been closed.")
  self._state = ClientState.OPENED
  follow_redirects = (
    self.follow_redirects
    if isinstance(follow_redirects, UseClientDefault)
    else follow_redirects
  )
  self._set_timeout(request)
  auth = self._build_request_auth(request, auth)
  response = self._send_handling_auth(
    request,
    auth=auth,
    follow_redirects=follow_redirects,
    history=[],
  )
  try:
    if not stream:
      response.read()
    return response
  except BaseException as exc:
    response.close()
    raise exc

```
  
---|---  
###  close ¶
```
close()

```

Close transport and proxies.
Source code in `httpx/_client.py`
```
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
```
| ```
defclose(self) -> None:
"""
  Close transport and proxies.
  """
  if self._state != ClientState.CLOSED:
    self._state = ClientState.CLOSED
    self._transport.close()
    for transport in self._mounts.values():
      if transport is not None:
        transport.close()

```
  
---|---  
###  request ¶
```
request(
  method,
  url,
  *,
  content=None,
  data=None,
  files=None,
  json=None,
  params=None,
  headers=None,
  cookies=None,
  auth=USE_CLIENT_DEFAULT,
  follow_redirects=USE_CLIENT_DEFAULT,
  timeout=USE_CLIENT_DEFAULT,
  extensions=None
)

```

PARAMETER | DESCRIPTION  
---|---  
`method` |  **TYPE:** `str`  
`url` |  **TYPE:** `URLTypes`  
`content` |  **TYPE:** `RequestContent | None` **DEFAULT:** `None`  
`data` |  **TYPE:** `_RequestData | None` **DEFAULT:** `None`  
`files` |  **TYPE:** `RequestFiles | None` **DEFAULT:** `None`  
`json` |  **TYPE:** `Any` **DEFAULT:** `None`  
`params` |  **TYPE:** `QueryParamTypes | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `HeaderTypes | None` **DEFAULT:** `None`  
`cookies` |  **TYPE:** `CookieTypes | None` **DEFAULT:** `None`  
`auth` |  **TYPE:** `AuthTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`follow_redirects` |  **TYPE:** `bool | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`timeout` |  **TYPE:** `TimeoutTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`extensions` |  **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`  
Source code in `starlette/testclient.py`
```
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
```
| ```
defrequest( # type: ignore[override]
  self,
  method: str,
  url: httpx._types.URLTypes,
  *,
  content: httpx._types.RequestContent | None = None,
  data: _RequestData | None = None,
  files: httpx._types.RequestFiles | None = None,
  json: typing.Any = None,
  params: httpx._types.QueryParamTypes | None = None,
  headers: httpx._types.HeaderTypes | None = None,
  cookies: httpx._types.CookieTypes | None = None,
  auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  extensions: dict[str, typing.Any] | None = None,
) -> httpx.Response:
  url = self._merge_url(url)
  return super().request(
    method,
    url,
    content=content,
    data=data,
    files=files,
    json=json,
    params=params,
    headers=headers,
    cookies=cookies,
    auth=auth,
    follow_redirects=follow_redirects,
    timeout=timeout,
    extensions=extensions,
  )

```
  
---|---  
###  get ¶
```
get(
  url,
  *,
  params=None,
  headers=None,
  cookies=None,
  auth=USE_CLIENT_DEFAULT,
  follow_redirects=USE_CLIENT_DEFAULT,
  timeout=USE_CLIENT_DEFAULT,
  extensions=None
)

```

PARAMETER | DESCRIPTION  
---|---  
`url` |  **TYPE:** `URLTypes`  
`params` |  **TYPE:** `QueryParamTypes | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `HeaderTypes | None` **DEFAULT:** `None`  
`cookies` |  **TYPE:** `CookieTypes | None` **DEFAULT:** `None`  
`auth` |  **TYPE:** `AuthTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`follow_redirects` |  **TYPE:** `bool | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`timeout` |  **TYPE:** `TimeoutTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`extensions` |  **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`  
Source code in `starlette/testclient.py`
```
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
```
| ```
defget( # type: ignore[override]
  self,
  url: httpx._types.URLTypes,
  *,
  params: httpx._types.QueryParamTypes | None = None,
  headers: httpx._types.HeaderTypes | None = None,
  cookies: httpx._types.CookieTypes | None = None,
  auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  extensions: dict[str, typing.Any] | None = None,
) -> httpx.Response:
  return super().get(
    url,
    params=params,
    headers=headers,
    cookies=cookies,
    auth=auth,
    follow_redirects=follow_redirects,
    timeout=timeout,
    extensions=extensions,
  )

```
  
---|---  
###  options ¶
```
options(
  url,
  *,
  params=None,
  headers=None,
  cookies=None,
  auth=USE_CLIENT_DEFAULT,
  follow_redirects=USE_CLIENT_DEFAULT,
  timeout=USE_CLIENT_DEFAULT,
  extensions=None
)

```

PARAMETER | DESCRIPTION  
---|---  
`url` |  **TYPE:** `URLTypes`  
`params` |  **TYPE:** `QueryParamTypes | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `HeaderTypes | None` **DEFAULT:** `None`  
`cookies` |  **TYPE:** `CookieTypes | None` **DEFAULT:** `None`  
`auth` |  **TYPE:** `AuthTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`follow_redirects` |  **TYPE:** `bool | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`timeout` |  **TYPE:** `TimeoutTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`extensions` |  **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`  
Source code in `starlette/testclient.py`
```
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
```
| ```
defoptions( # type: ignore[override]
  self,
  url: httpx._types.URLTypes,
  *,
  params: httpx._types.QueryParamTypes | None = None,
  headers: httpx._types.HeaderTypes | None = None,
  cookies: httpx._types.CookieTypes | None = None,
  auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  extensions: dict[str, typing.Any] | None = None,
) -> httpx.Response:
  return super().options(
    url,
    params=params,
    headers=headers,
    cookies=cookies,
    auth=auth,
    follow_redirects=follow_redirects,
    timeout=timeout,
    extensions=extensions,
  )

```
  
---|---  
###  head ¶
```
head(
  url,
  *,
  params=None,
  headers=None,
  cookies=None,
  auth=USE_CLIENT_DEFAULT,
  follow_redirects=USE_CLIENT_DEFAULT,
  timeout=USE_CLIENT_DEFAULT,
  extensions=None
)

```

PARAMETER | DESCRIPTION  
---|---  
`url` |  **TYPE:** `URLTypes`  
`params` |  **TYPE:** `QueryParamTypes | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `HeaderTypes | None` **DEFAULT:** `None`  
`cookies` |  **TYPE:** `CookieTypes | None` **DEFAULT:** `None`  
`auth` |  **TYPE:** `AuthTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`follow_redirects` |  **TYPE:** `bool | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`timeout` |  **TYPE:** `TimeoutTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`extensions` |  **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`  
Source code in `starlette/testclient.py`
```
492
493
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
```
| ```
defhead( # type: ignore[override]
  self,
  url: httpx._types.URLTypes,
  *,
  params: httpx._types.QueryParamTypes | None = None,
  headers: httpx._types.HeaderTypes | None = None,
  cookies: httpx._types.CookieTypes | None = None,
  auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  extensions: dict[str, typing.Any] | None = None,
) -> httpx.Response:
  return super().head(
    url,
    params=params,
    headers=headers,
    cookies=cookies,
    auth=auth,
    follow_redirects=follow_redirects,
    timeout=timeout,
    extensions=extensions,
  )

```
  
---|---  
###  post ¶
```
post(
  url,
  *,
  content=None,
  data=None,
  files=None,
  json=None,
  params=None,
  headers=None,
  cookies=None,
  auth=USE_CLIENT_DEFAULT,
  follow_redirects=USE_CLIENT_DEFAULT,
  timeout=USE_CLIENT_DEFAULT,
  extensions=None
)

```

PARAMETER | DESCRIPTION  
---|---  
`url` |  **TYPE:** `URLTypes`  
`content` |  **TYPE:** `RequestContent | None` **DEFAULT:** `None`  
`data` |  **TYPE:** `_RequestData | None` **DEFAULT:** `None`  
`files` |  **TYPE:** `RequestFiles | None` **DEFAULT:** `None`  
`json` |  **TYPE:** `Any` **DEFAULT:** `None`  
`params` |  **TYPE:** `QueryParamTypes | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `HeaderTypes | None` **DEFAULT:** `None`  
`cookies` |  **TYPE:** `CookieTypes | None` **DEFAULT:** `None`  
`auth` |  **TYPE:** `AuthTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`follow_redirects` |  **TYPE:** `bool | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`timeout` |  **TYPE:** `TimeoutTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`extensions` |  **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`  
Source code in `starlette/testclient.py`
```
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
```
| ```
defpost( # type: ignore[override]
  self,
  url: httpx._types.URLTypes,
  *,
  content: httpx._types.RequestContent | None = None,
  data: _RequestData | None = None,
  files: httpx._types.RequestFiles | None = None,
  json: typing.Any = None,
  params: httpx._types.QueryParamTypes | None = None,
  headers: httpx._types.HeaderTypes | None = None,
  cookies: httpx._types.CookieTypes | None = None,
  auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  extensions: dict[str, typing.Any] | None = None,
) -> httpx.Response:
  return super().post(
    url,
    content=content,
    data=data,
    files=files,
    json=json,
    params=params,
    headers=headers,
    cookies=cookies,
    auth=auth,
    follow_redirects=follow_redirects,
    timeout=timeout,
    extensions=extensions,
  )

```
  
---|---  
###  put ¶
```
put(
  url,
  *,
  content=None,
  data=None,
  files=None,
  json=None,
  params=None,
  headers=None,
  cookies=None,
  auth=USE_CLIENT_DEFAULT,
  follow_redirects=USE_CLIENT_DEFAULT,
  timeout=USE_CLIENT_DEFAULT,
  extensions=None
)

```

PARAMETER | DESCRIPTION  
---|---  
`url` |  **TYPE:** `URLTypes`  
`content` |  **TYPE:** `RequestContent | None` **DEFAULT:** `None`  
`data` |  **TYPE:** `_RequestData | None` **DEFAULT:** `None`  
`files` |  **TYPE:** `RequestFiles | None` **DEFAULT:** `None`  
`json` |  **TYPE:** `Any` **DEFAULT:** `None`  
`params` |  **TYPE:** `QueryParamTypes | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `HeaderTypes | None` **DEFAULT:** `None`  
`cookies` |  **TYPE:** `CookieTypes | None` **DEFAULT:** `None`  
`auth` |  **TYPE:** `AuthTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`follow_redirects` |  **TYPE:** `bool | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`timeout` |  **TYPE:** `TimeoutTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`extensions` |  **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`  
Source code in `starlette/testclient.py`
```
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
```
| ```
defput( # type: ignore[override]
  self,
  url: httpx._types.URLTypes,
  *,
  content: httpx._types.RequestContent | None = None,
  data: _RequestData | None = None,
  files: httpx._types.RequestFiles | None = None,
  json: typing.Any = None,
  params: httpx._types.QueryParamTypes | None = None,
  headers: httpx._types.HeaderTypes | None = None,
  cookies: httpx._types.CookieTypes | None = None,
  auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  extensions: dict[str, typing.Any] | None = None,
) -> httpx.Response:
  return super().put(
    url,
    content=content,
    data=data,
    files=files,
    json=json,
    params=params,
    headers=headers,
    cookies=cookies,
    auth=auth,
    follow_redirects=follow_redirects,
    timeout=timeout,
    extensions=extensions,
  )

```
  
---|---  
###  patch ¶
```
patch(
  url,
  *,
  content=None,
  data=None,
  files=None,
  json=None,
  params=None,
  headers=None,
  cookies=None,
  auth=USE_CLIENT_DEFAULT,
  follow_redirects=USE_CLIENT_DEFAULT,
  timeout=USE_CLIENT_DEFAULT,
  extensions=None
)

```

PARAMETER | DESCRIPTION  
---|---  
`url` |  **TYPE:** `URLTypes`  
`content` |  **TYPE:** `RequestContent | None` **DEFAULT:** `None`  
`data` |  **TYPE:** `_RequestData | None` **DEFAULT:** `None`  
`files` |  **TYPE:** `RequestFiles | None` **DEFAULT:** `None`  
`json` |  **TYPE:** `Any` **DEFAULT:** `None`  
`params` |  **TYPE:** `QueryParamTypes | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `HeaderTypes | None` **DEFAULT:** `None`  
`cookies` |  **TYPE:** `CookieTypes | None` **DEFAULT:** `None`  
`auth` |  **TYPE:** `AuthTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`follow_redirects` |  **TYPE:** `bool | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`timeout` |  **TYPE:** `TimeoutTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`extensions` |  **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`  
Source code in `starlette/testclient.py`
```
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
```
| ```
defpatch( # type: ignore[override]
  self,
  url: httpx._types.URLTypes,
  *,
  content: httpx._types.RequestContent | None = None,
  data: _RequestData | None = None,
  files: httpx._types.RequestFiles | None = None,
  json: typing.Any = None,
  params: httpx._types.QueryParamTypes | None = None,
  headers: httpx._types.HeaderTypes | None = None,
  cookies: httpx._types.CookieTypes | None = None,
  auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  extensions: dict[str, typing.Any] | None = None,
) -> httpx.Response:
  return super().patch(
    url,
    content=content,
    data=data,
    files=files,
    json=json,
    params=params,
    headers=headers,
    cookies=cookies,
    auth=auth,
    follow_redirects=follow_redirects,
    timeout=timeout,
    extensions=extensions,
  )

```
  
---|---  
###  delete ¶
```
delete(
  url,
  *,
  params=None,
  headers=None,
  cookies=None,
  auth=USE_CLIENT_DEFAULT,
  follow_redirects=USE_CLIENT_DEFAULT,
  timeout=USE_CLIENT_DEFAULT,
  extensions=None
)

```

PARAMETER | DESCRIPTION  
---|---  
`url` |  **TYPE:** `URLTypes`  
`params` |  **TYPE:** `QueryParamTypes | None` **DEFAULT:** `None`  
`headers` |  **TYPE:** `HeaderTypes | None` **DEFAULT:** `None`  
`cookies` |  **TYPE:** `CookieTypes | None` **DEFAULT:** `None`  
`auth` |  **TYPE:** `AuthTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`follow_redirects` |  **TYPE:** `bool | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`timeout` |  **TYPE:** `TimeoutTypes | UseClientDefault` **DEFAULT:** `USE_CLIENT_DEFAULT`  
`extensions` |  **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`  
Source code in `starlette/testclient.py`
```
608
609
610
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
```
| ```
defdelete( # type: ignore[override]
  self,
  url: httpx._types.URLTypes,
  *,
  params: httpx._types.QueryParamTypes | None = None,
  headers: httpx._types.HeaderTypes | None = None,
  cookies: httpx._types.CookieTypes | None = None,
  auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,
  extensions: dict[str, typing.Any] | None = None,
) -> httpx.Response:
  return super().delete(
    url,
    params=params,
    headers=headers,
    cookies=cookies,
    auth=auth,
    follow_redirects=follow_redirects,
    timeout=timeout,
    extensions=extensions,
  )

```
  
---|---  
###  websocket_connect ¶
```
websocket_connect(url, subprotocols=None, **kwargs)

```

PARAMETER | DESCRIPTION  
---|---  
`url` |  **TYPE:** `str`  
`subprotocols` |  **TYPE:** `Sequence[str] | None` **DEFAULT:** `None`  
`**kwargs` |  **TYPE:** `Any` **DEFAULT:** `{}`  
Source code in `starlette/testclient.py`
```
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
```
| ```
defwebsocket_connect(
  self,
  url: str,
  subprotocols: typing.Sequence[str] | None = None,
  **kwargs: typing.Any,
) -> WebSocketTestSession:
  url = urljoin("ws://testserver", url)
  headers = kwargs.get("headers", {})
  headers.setdefault("connection", "upgrade")
  headers.setdefault("sec-websocket-key", "testserver==")
  headers.setdefault("sec-websocket-version", "13")
  if subprotocols is not None:
    headers.setdefault("sec-websocket-protocol", ", ".join(subprotocols))
  kwargs["headers"] = headers
  try:
    super().request("GET", url, **kwargs)
  except _Upgrade as exc:
    session = exc.session
  else:
    raise RuntimeError("Expected WebSocket upgrade") # pragma: no cover
  return session

```
  
---|---  
###  lifespan `async` ¶
```
lifespan()

```

Source code in `starlette/testclient.py`
```
686
687
688
689
690
691
```
| ```
async deflifespan(self) -> None:
  scope = {"type": "lifespan", "state": self.app_state}
  try:
    await self.app(scope, self.stream_receive.receive, self.stream_send.send)
  finally:
    await self.stream_send.send(None)

```
  
---|---  
###  wait_startup `async` ¶
```
wait_startup()

```

Source code in `starlette/testclient.py`
```
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
```
| ```
async defwait_startup(self) -> None:
  await self.stream_receive.send({"type": "lifespan.startup"})
  async defreceive() -> typing.Any:
    message = await self.stream_send.receive()
    if message is None:
      self.task.result()
    return message
  message = await receive()
  assert message["type"] in (
    "lifespan.startup.complete",
    "lifespan.startup.failed",
  )
  if message["type"] == "lifespan.startup.failed":
    await receive()

```
  
---|---  
###  wait_shutdown `async` ¶
```
wait_shutdown()

```

Source code in `starlette/testclient.py`
```
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
```
| ```
async defwait_shutdown(self) -> None:
  async defreceive() -> typing.Any:
    message = await self.stream_send.receive()
    if message is None:
      self.task.result()
    return message
  await self.stream_receive.send({"type": "lifespan.shutdown"})
  message = await receive()
  assert message["type"] in (
    "lifespan.shutdown.complete",
    "lifespan.shutdown.failed",
  )
  if message["type"] == "lifespan.shutdown.failed":
    await receive()

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
