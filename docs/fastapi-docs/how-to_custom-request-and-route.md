Skip to content 
# Custom Request and APIRoute class¶
In some cases, you may want to override the logic used by the `Request` and `APIRoute` classes.
In particular, this may be a good alternative to logic in a middleware.
For example, if you want to read or manipulate the request body before it is processed by your application.
Danger
This is an "advanced" feature.
If you are just starting with **FastAPI** you might want to skip this section.
## Use cases¶
Some use cases include:
  * Converting non-JSON request bodies to JSON (e.g. `msgpack`).
  * Decompressing gzip-compressed request bodies.
  * Automatically logging all request bodies.


## Handling custom request body encodings¶
Let's see how to make use of a custom `Request` subclass to decompress gzip requests.
And an `APIRoute` subclass to use that custom request class.
### Create a custom `GzipRequest` class¶
Tip
This is a toy example to demonstrate how it works, if you need Gzip support, you can use the provided `GzipMiddleware`.
First, we create a `GzipRequest` class, which will overwrite the `Request.body()` method to decompress the body in the presence of an appropriate header.
If there's no `gzip` in the header, it will not try to decompress the body.
That way, the same route class can handle gzip compressed or uncompressed requests.
Python 3.8+
```
importgzip
fromtypingimport Callable, List
fromfastapiimport Body, FastAPI, Request, Response
fromfastapi.routingimport APIRoute
classGzipRequest(Request):
  async defbody(self) -> bytes:
    if not hasattr(self, "_body"):
      body = await super().body()
      if "gzip" in self.headers.getlist("Content-Encoding"):
        body = gzip.decompress(body)
      self._body = body
    return self._body
classGzipRoute(APIRoute):
  defget_route_handler(self) -> Callable:
    original_route_handler = super().get_route_handler()
    async defcustom_route_handler(request: Request) -> Response:
      request = GzipRequest(request.scope, request.receive)
      return await original_route_handler(request)
    return custom_route_handler
app = FastAPI()
app.router.route_class = GzipRoute
@app.post("/sum")
async defsum_numbers(numbers: List[int] = Body()):
  return {"sum": sum(numbers)}

```

### Create a custom `GzipRoute` class¶
Next, we create a custom subclass of `fastapi.routing.APIRoute` that will make use of the `GzipRequest`.
This time, it will overwrite the method `APIRoute.get_route_handler()`.
This method returns a function. And that function is what will receive a request and return a response.
Here we use it to create a `GzipRequest` from the original request.
Python 3.8+
```
importgzip
fromtypingimport Callable, List
fromfastapiimport Body, FastAPI, Request, Response
fromfastapi.routingimport APIRoute
classGzipRequest(Request):
  async defbody(self) -> bytes:
    if not hasattr(self, "_body"):
      body = await super().body()
      if "gzip" in self.headers.getlist("Content-Encoding"):
        body = gzip.decompress(body)
      self._body = body
    return self._body
classGzipRoute(APIRoute):
  defget_route_handler(self) -> Callable:
    original_route_handler = super().get_route_handler()
    async defcustom_route_handler(request: Request) -> Response:
      request = GzipRequest(request.scope, request.receive)
      return await original_route_handler(request)
    return custom_route_handler
app = FastAPI()
app.router.route_class = GzipRoute
@app.post("/sum")
async defsum_numbers(numbers: List[int] = Body()):
  return {"sum": sum(numbers)}

```

Technical Details
A `Request` has a `request.scope` attribute, that's just a Python `dict` containing the metadata related to the request.
A `Request` also has a `request.receive`, that's a function to "receive" the body of the request.
The `scope` `dict` and `receive` function are both part of the ASGI specification.
And those two things, `scope` and `receive`, are what is needed to create a new `Request` instance.
To learn more about the `Request` check Starlette's docs about Requests.
The only thing the function returned by `GzipRequest.get_route_handler` does differently is convert the `Request` to a `GzipRequest`.
Doing this, our `GzipRequest` will take care of decompressing the data (if necessary) before passing it to our _path operations_.
After that, all of the processing logic is the same.
But because of our changes in `GzipRequest.body`, the request body will be automatically decompressed when it is loaded by **FastAPI** when needed.
## Accessing the request body in an exception handler¶
Tip
To solve this same problem, it's probably a lot easier to use the `body` in a custom handler for `RequestValidationError` (Handling Errors).
But this example is still valid and it shows how to interact with the internal components.
We can also use this same approach to access the request body in an exception handler.
All we need to do is handle the request inside a `try`/`except` block:
Python 3.8+
```
fromtypingimport Callable, List
fromfastapiimport Body, FastAPI, HTTPException, Request, Response
fromfastapi.exceptionsimport RequestValidationError
fromfastapi.routingimport APIRoute
classValidationErrorLoggingRoute(APIRoute):
  defget_route_handler(self) -> Callable:
    original_route_handler = super().get_route_handler()
    async defcustom_route_handler(request: Request) -> Response:
      try:
        return await original_route_handler(request)
      except RequestValidationError as exc:
        body = await request.body()
        detail = {"errors": exc.errors(), "body": body.decode()}
        raise HTTPException(status_code=422, detail=detail)
    return custom_route_handler
app = FastAPI()
app.router.route_class = ValidationErrorLoggingRoute
@app.post("/")
async defsum_numbers(numbers: List[int] = Body()):
  return sum(numbers)

```

If an exception occurs, the`Request` instance will still be in scope, so we can read and make use of the request body when handling the error:
Python 3.8+
```
fromtypingimport Callable, List
fromfastapiimport Body, FastAPI, HTTPException, Request, Response
fromfastapi.exceptionsimport RequestValidationError
fromfastapi.routingimport APIRoute
classValidationErrorLoggingRoute(APIRoute):
  defget_route_handler(self) -> Callable:
    original_route_handler = super().get_route_handler()
    async defcustom_route_handler(request: Request) -> Response:
      try:
        return await original_route_handler(request)
      except RequestValidationError as exc:
        body = await request.body()
        detail = {"errors": exc.errors(), "body": body.decode()}
        raise HTTPException(status_code=422, detail=detail)
    return custom_route_handler
app = FastAPI()
app.router.route_class = ValidationErrorLoggingRoute
@app.post("/")
async defsum_numbers(numbers: List[int] = Body()):
  return sum(numbers)

```

## Custom `APIRoute` class in a router¶
You can also set the `route_class` parameter of an `APIRouter`:
Python 3.8+
```
importtime
fromtypingimport Callable
fromfastapiimport APIRouter, FastAPI, Request, Response
fromfastapi.routingimport APIRoute
classTimedRoute(APIRoute):
  defget_route_handler(self) -> Callable:
    original_route_handler = super().get_route_handler()
    async defcustom_route_handler(request: Request) -> Response:
      before = time.time()
      response: Response = await original_route_handler(request)
      duration = time.time() - before
      response.headers["X-Response-Time"] = str(duration)
      print(f"route duration: {duration}")
      print(f"route response: {response}")
      print(f"route response headers: {response.headers}")
      return response
    return custom_route_handler
app = FastAPI()
router = APIRouter(route_class=TimedRoute)
@app.get("/")
async defnot_timed():
  return {"message": "Not timed"}
@router.get("/timed")
async deftimed():
  return {"message": "It's the time of my life"}
app.include_router(router)

```

In this example, the _path operations_ under the `router` will use the custom `TimedRoute` class, and will have an extra `X-Response-Time` header in the response with the time it took to generate the response:
Python 3.8+
```
importtime
fromtypingimport Callable
fromfastapiimport APIRouter, FastAPI, Request, Response
fromfastapi.routingimport APIRoute
classTimedRoute(APIRoute):
  defget_route_handler(self) -> Callable:
    original_route_handler = super().get_route_handler()
    async defcustom_route_handler(request: Request) -> Response:
      before = time.time()
      response: Response = await original_route_handler(request)
      duration = time.time() - before
      response.headers["X-Response-Time"] = str(duration)
      print(f"route duration: {duration}")
      print(f"route response: {response}")
      print(f"route response headers: {response.headers}")
      return response
    return custom_route_handler
app = FastAPI()
router = APIRouter(route_class=TimedRoute)
@app.get("/")
async defnot_timed():
  return {"message": "Not timed"}
@router.get("/timed")
async deftimed():
  return {"message": "It's the time of my life"}
app.include_router(router)

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
