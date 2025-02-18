Skip to content 
# Additional Status Codes¶
By default, **FastAPI** will return the responses using a `JSONResponse`, putting the content you return from your _path operation_ inside of that `JSONResponse`.
It will use the default status code or the one you set in your _path operation_.
## Additional status codes¶
If you want to return additional status codes apart from the main one, you can do that by returning a `Response` directly, like a `JSONResponse`, and set the additional status code directly.
For example, let's say that you want to have a _path operation_ that allows to update items, and returns HTTP status codes of 200 "OK" when successful.
But you also want it to accept new items. And when the items didn't exist before, it creates them, and returns an HTTP status code of 201 "Created".
To achieve that, import `JSONResponse`, and return your content there directly, setting the `status_code` that you want:
Python 3.10+
```
fromtypingimport Annotated
fromfastapiimport Body, FastAPI, status
fromfastapi.responsesimport JSONResponse
app = FastAPI()
items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}
@app.put("/items/{item_id}")
async defupsert_item(
  item_id: str,
  name: Annotated[str | None, Body()] = None,
  size: Annotated[int | None, Body()] = None,
):
  if item_id in items:
    item = items[item_id]
    item["name"] = name
    item["size"] = size
    return item
  else:
    item = {"name": name, "size": size}
    items[item_id] = item
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)

```

🤓 Other versions and variants
Python 3.9+Python 3.8+Python 3.10+ - non-AnnotatedPython 3.8+ - non-Annotated
```
fromtypingimport Annotated, Union
fromfastapiimport Body, FastAPI, status
fromfastapi.responsesimport JSONResponse
app = FastAPI()
items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}
@app.put("/items/{item_id}")
async defupsert_item(
  item_id: str,
  name: Annotated[Union[str, None], Body()] = None,
  size: Annotated[Union[int, None], Body()] = None,
):
  if item_id in items:
    item = items[item_id]
    item["name"] = name
    item["size"] = size
    return item
  else:
    item = {"name": name, "size": size}
    items[item_id] = item
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)

```

```
fromtypingimport Union
fromfastapiimport Body, FastAPI, status
fromfastapi.responsesimport JSONResponse
fromtyping_extensionsimport Annotated
app = FastAPI()
items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}
@app.put("/items/{item_id}")
async defupsert_item(
  item_id: str,
  name: Annotated[Union[str, None], Body()] = None,
  size: Annotated[Union[int, None], Body()] = None,
):
  if item_id in items:
    item = items[item_id]
    item["name"] = name
    item["size"] = size
    return item
  else:
    item = {"name": name, "size": size}
    items[item_id] = item
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)

```

Tip
Prefer to use the `Annotated` version if possible.
```
fromfastapiimport Body, FastAPI, status
fromfastapi.responsesimport JSONResponse
app = FastAPI()
items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}
@app.put("/items/{item_id}")
async defupsert_item(
  item_id: str,
  name: str | None = Body(default=None),
  size: int | None = Body(default=None),
):
  if item_id in items:
    item = items[item_id]
    item["name"] = name
    item["size"] = size
    return item
  else:
    item = {"name": name, "size": size}
    items[item_id] = item
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)

```

Tip
Prefer to use the `Annotated` version if possible.
```
fromtypingimport Union
fromfastapiimport Body, FastAPI, status
fromfastapi.responsesimport JSONResponse
app = FastAPI()
items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}
@app.put("/items/{item_id}")
async defupsert_item(
  item_id: str,
  name: Union[str, None] = Body(default=None),
  size: Union[int, None] = Body(default=None),
):
  if item_id in items:
    item = items[item_id]
    item["name"] = name
    item["size"] = size
    return item
  else:
    item = {"name": name, "size": size}
    items[item_id] = item
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)

```

Warning
When you return a `Response` directly, like in the example above, it will be returned directly.
It won't be serialized with a model, etc.
Make sure it has the data you want it to have, and that the values are valid JSON (if you are using `JSONResponse`).
Technical Details
You could also use `from starlette.responses import JSONResponse`.
**FastAPI** provides the same `starlette.responses` as `fastapi.responses` just as a convenience for you, the developer. But most of the available responses come directly from Starlette. The same with `status`.
## OpenAPI and API docs¶
If you return additional status codes and responses directly, they won't be included in the OpenAPI schema (the API docs), because FastAPI doesn't have a way to know beforehand what you are going to return.
But you can document that in your code, using: Additional Responses.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
