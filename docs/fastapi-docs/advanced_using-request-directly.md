Skip to content 
# Using the Request Directly¶
Up to now, you have been declaring the parts of the request that you need with their types.
Taking data from:
  * The path as parameters.
  * Headers.
  * Cookies.
  * etc.


And by doing so, **FastAPI** is validating that data, converting it and generating documentation for your API automatically.
But there are situations where you might need to access the `Request` object directly.
## Details about the `Request` object¶
As **FastAPI** is actually **Starlette** underneath, with a layer of several tools on top, you can use Starlette's `Request` object directly when you need to.
It would also mean that if you get data from the `Request` object directly (for example, read the body) it won't be validated, converted or documented (with OpenAPI, for the automatic API user interface) by FastAPI.
Although any other parameter declared normally (for example, the body with a Pydantic model) would still be validated, converted, annotated, etc.
But there are specific cases where it's useful to get the `Request` object.
## Use the `Request` object directly¶
Let's imagine you want to get the client's IP address/host inside of your _path operation function_.
For that you need to access the request directly.
Python 3.8+
```
fromfastapiimport FastAPI, Request
app = FastAPI()
@app.get("/items/{item_id}")
defread_root(item_id: str, request: Request):
  client_host = request.client.host
  return {"client_host": client_host, "item_id": item_id}

```

By declaring a _path operation function_ parameter with the type being the `Request` **FastAPI** will know to pass the `Request` in that parameter.
Tip
Note that in this case, we are declaring a path parameter beside the request parameter.
So, the path parameter will be extracted, validated, converted to the specified type and annotated with OpenAPI.
The same way, you can declare any other parameter as normally, and additionally, get the `Request` too.
## `Request` documentation¶
You can read more details about the `Request` object in the official Starlette documentation site.
Technical Details
You could also use `from starlette.requests import Request`.
**FastAPI** provides it directly just as a convenience for you, the developer. But it comes directly from Starlette.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
