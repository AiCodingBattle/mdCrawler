Skip to content 
# Return a Response Directly¶
When you create a **FastAPI** _path operation_ you can normally return any data from it: a `dict`, a `list`, a Pydantic model, a database model, etc.
By default, **FastAPI** would automatically convert that return value to JSON using the `jsonable_encoder` explained in JSON Compatible Encoder.
Then, behind the scenes, it would put that JSON-compatible data (e.g. a `dict`) inside of a `JSONResponse` that would be used to send the response to the client.
But you can return a `JSONResponse` directly from your _path operations_.
It might be useful, for example, to return custom headers or cookies.
## Return a `Response`¶
In fact, you can return any `Response` or any sub-class of it.
Tip
`JSONResponse` itself is a sub-class of `Response`.
And when you return a `Response`, **FastAPI** will pass it directly.
It won't do any data conversion with Pydantic models, it won't convert the contents to any type, etc.
This gives you a lot of flexibility. You can return any data type, override any data declaration or validation, etc.
## Using the `jsonable_encoder` in a `Response`¶
Because **FastAPI** doesn't make any changes to a `Response` you return, you have to make sure its contents are ready for it.
For example, you cannot put a Pydantic model in a `JSONResponse` without first converting it to a `dict` with all the data types (like `datetime`, `UUID`, etc) converted to JSON-compatible types.
For those cases, you can use the `jsonable_encoder` to convert your data before passing it to a response:
Python 3.8+
```
fromdatetimeimport datetime
fromtypingimport Union
fromfastapiimport FastAPI
fromfastapi.encodersimport jsonable_encoder
fromfastapi.responsesimport JSONResponse
frompydanticimport BaseModel
classItem(BaseModel):
  title: str
  timestamp: datetime
  description: Union[str, None] = None
app = FastAPI()
@app.put("/items/{id}")
defupdate_item(id: str, item: Item):
  json_compatible_item_data = jsonable_encoder(item)
  return JSONResponse(content=json_compatible_item_data)

```

Technical Details
You could also use `from starlette.responses import JSONResponse`.
**FastAPI** provides the same `starlette.responses` as `fastapi.responses` just as a convenience for you, the developer. But most of the available responses come directly from Starlette.
## Returning a custom `Response`¶
The example above shows all the parts you need, but it's not very useful yet, as you could have just returned the `item` directly, and **FastAPI** would put it in a `JSONResponse` for you, converting it to a `dict`, etc. All that by default.
Now, let's see how you could use that to return a custom response.
Let's say that you want to return an XML response.
You could put your XML content in a string, put that in a `Response`, and return it:
Python 3.8+
```
fromfastapiimport FastAPI, Response
app = FastAPI()
@app.get("/legacy/")
defget_legacy_data():
  data = """<?xml version="1.0"?>
  <shampoo>
  <Header>
    Apply shampoo here.
  </Header>
  <Body>
    You'll have to use soap here.
  </Body>
  </shampoo>
  """
  return Response(content=data, media_type="application/xml")

```

## Notes¶
When you return a `Response` directly its data is not validated, converted (serialized), nor documented automatically.
But you can still document it as described in Additional Responses in OpenAPI.
You can see in later sections how to use/declare these custom `Response`s while still having automatic data conversion, documentation, etc.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
