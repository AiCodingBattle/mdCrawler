Skip to content 
# OpenAPI Callbacks¶
You could create an API with a _path operation_ that could trigger a request to an _external API_ created by someone else (probably the same developer that would be _using_ your API).
The process that happens when your API app calls the _external API_ is named a "callback". Because the software that the external developer wrote sends a request to your API and then your API _calls back_ , sending a request to an _external API_ (that was probably created by the same developer).
In this case, you could want to document how that external API _should_ look like. What _path operation_ it should have, what body it should expect, what response it should return, etc.
## An app with callbacks¶
Let's see all this with an example.
Imagine you develop an app that allows creating invoices.
These invoices will have an `id`, `title` (optional), `customer`, and `total`.
The user of your API (an external developer) will create an invoice in your API with a POST request.
Then your API will (let's imagine):
  * Send the invoice to some customer of the external developer.
  * Collect the money.
  * Send a notification back to the API user (the external developer).
    * This will be done by sending a POST request (from _your API_) to some _external API_ provided by that external developer (this is the "callback").


## The normal **FastAPI** app¶
Let's first see how the normal API app would look like before adding the callback.
It will have a _path operation_ that will receive an `Invoice` body, and a query parameter `callback_url` that will contain the URL for the callback.
This part is pretty normal, most of the code is probably already familiar to you:
Python 3.8+
```
fromtypingimport Union
fromfastapiimport APIRouter, FastAPI
frompydanticimport BaseModel, HttpUrl
app = FastAPI()
classInvoice(BaseModel):
  id: str
  title: Union[str, None] = None
  customer: str
  total: float
classInvoiceEvent(BaseModel):
  description: str
  paid: bool
classInvoiceEventReceived(BaseModel):
  ok: bool
invoices_callback_router = APIRouter()
@invoices_callback_router.post(
  "{$callback_url}/invoices/{$request.body.id}", response_model=InvoiceEventReceived
)
definvoice_notification(body: InvoiceEvent):
  pass
@app.post("/invoices/", callbacks=invoices_callback_router.routes)
defcreate_invoice(invoice: Invoice, callback_url: Union[HttpUrl, None] = None):
"""
  Create an invoice.
  This will (let's imagine) let the API user (some external developer) create an
  invoice.
  And this path operation will:
  * Send the invoice to the client.
  * Collect the money from the client.
  * Send a notification back to the API user (the external developer), as a callback.
    * At this point is that the API will somehow send a POST request to the
      external API with the notification of the invoice event
      (e.g. "payment successful").
  """
  # Send the invoice, collect the money, send the notification (the callback)
  return {"msg": "Invoice received"}

```

Tip
The `callback_url` query parameter uses a Pydantic Url type.
The only new thing is the `callbacks=invoices_callback_router.routes` as an argument to the _path operation decorator_. We'll see what that is next.
## Documenting the callback¶
The actual callback code will depend heavily on your own API app.
And it will probably vary a lot from one app to the next.
It could be just one or two lines of code, like:
```
callback_url = "https://example.com/api/v1/invoices/events/"
httpx.post(callback_url, json={"description": "Invoice paid", "paid": True})

```

But possibly the most important part of the callback is making sure that your API user (the external developer) implements the _external API_ correctly, according to the data that _your API_ is going to send in the request body of the callback, etc.
So, what we will do next is add the code to document how that _external API_ should look like to receive the callback from _your API_.
That documentation will show up in the Swagger UI at `/docs` in your API, and it will let external developers know how to build the _external API_.
This example doesn't implement the callback itself (that could be just a line of code), only the documentation part.
Tip
The actual callback is just an HTTP request.
When implementing the callback yourself, you could use something like HTTPX or Requests.
## Write the callback documentation code¶
This code won't be executed in your app, we only need it to _document_ how that _external API_ should look like.
But, you already know how to easily create automatic documentation for an API with **FastAPI**.
So we are going to use that same knowledge to document how the _external API_ should look like... by creating the _path operation(s)_ that the external API should implement (the ones your API will call).
Tip
When writing the code to document a callback, it might be useful to imagine that you are that _external developer_. And that you are currently implementing the _external API_ , not _your API_.
Temporarily adopting this point of view (of the _external developer_) can help you feel like it's more obvious where to put the parameters, the Pydantic model for the body, for the response, etc. for that _external API_.
### Create a callback `APIRouter`¶
First create a new `APIRouter` that will contain one or more callbacks.
Python 3.8+
```
fromtypingimport Union
fromfastapiimport APIRouter, FastAPI
frompydanticimport BaseModel, HttpUrl
app = FastAPI()
classInvoice(BaseModel):
  id: str
  title: Union[str, None] = None
  customer: str
  total: float
classInvoiceEvent(BaseModel):
  description: str
  paid: bool
classInvoiceEventReceived(BaseModel):
  ok: bool
invoices_callback_router = APIRouter()
@invoices_callback_router.post(
  "{$callback_url}/invoices/{$request.body.id}", response_model=InvoiceEventReceived
)
definvoice_notification(body: InvoiceEvent):
  pass
@app.post("/invoices/", callbacks=invoices_callback_router.routes)
defcreate_invoice(invoice: Invoice, callback_url: Union[HttpUrl, None] = None):
"""
  Create an invoice.
  This will (let's imagine) let the API user (some external developer) create an
  invoice.
  And this path operation will:
  * Send the invoice to the client.
  * Collect the money from the client.
  * Send a notification back to the API user (the external developer), as a callback.
    * At this point is that the API will somehow send a POST request to the
      external API with the notification of the invoice event
      (e.g. "payment successful").
  """
  # Send the invoice, collect the money, send the notification (the callback)
  return {"msg": "Invoice received"}

```

### Create the callback _path operation_¶
To create the callback _path operation_ use the same `APIRouter` you created above.
It should look just like a normal FastAPI _path operation_ :
  * It should probably have a declaration of the body it should receive, e.g. `body: InvoiceEvent`.
  * And it could also have a declaration of the response it should return, e.g. `response_model=InvoiceEventReceived`.


Python 3.8+
```
fromtypingimport Union
fromfastapiimport APIRouter, FastAPI
frompydanticimport BaseModel, HttpUrl
app = FastAPI()
classInvoice(BaseModel):
  id: str
  title: Union[str, None] = None
  customer: str
  total: float
classInvoiceEvent(BaseModel):
  description: str
  paid: bool
classInvoiceEventReceived(BaseModel):
  ok: bool
invoices_callback_router = APIRouter()
@invoices_callback_router.post(
  "{$callback_url}/invoices/{$request.body.id}", response_model=InvoiceEventReceived
)
definvoice_notification(body: InvoiceEvent):
  pass
@app.post("/invoices/", callbacks=invoices_callback_router.routes)
defcreate_invoice(invoice: Invoice, callback_url: Union[HttpUrl, None] = None):
"""
  Create an invoice.
  This will (let's imagine) let the API user (some external developer) create an
  invoice.
  And this path operation will:
  * Send the invoice to the client.
  * Collect the money from the client.
  * Send a notification back to the API user (the external developer), as a callback.
    * At this point is that the API will somehow send a POST request to the
      external API with the notification of the invoice event
      (e.g. "payment successful").
  """
  # Send the invoice, collect the money, send the notification (the callback)
  return {"msg": "Invoice received"}

```

There are 2 main differences from a normal _path operation_ :
  * It doesn't need to have any actual code, because your app will never call this code. It's only used to document the _external API_. So, the function could just have `pass`.
  * The _path_ can contain an OpenAPI 3 expression (see more below) where it can use variables with parameters and parts of the original request sent to _your API_.


### The callback path expression¶
The callback _path_ can have an OpenAPI 3 expression that can contain parts of the original request sent to _your API_.
In this case, it's the `str`:
```
"{$callback_url}/invoices/{$request.body.id}"

```

So, if your API user (the external developer) sends a request to _your API_ to:
```
https://yourapi.com/invoices/?callback_url=https://www.external.org/events

```

with a JSON body of:
```
{
"id":"2expen51ve",
"customer":"Mr. Richie Rich",
"total":"9999"
}

```

then _your API_ will process the invoice, and at some point later, send a callback request to the `callback_url` (the _external API_):
```
https://www.external.org/events/invoices/2expen51ve

```

with a JSON body containing something like:
```
{
"description":"Payment celebration",
"paid":true
}

```

and it would expect a response from that _external API_ with a JSON body like:
```
{
"ok":true
}

```

Tip
Notice how the callback URL used contains the URL received as a query parameter in `callback_url` (`https://www.external.org/events`) and also the invoice `id` from inside of the JSON body (`2expen51ve`).
### Add the callback router¶
At this point you have the _callback path operation(s)_ needed (the one(s) that the _external developer_ should implement in the _external API_) in the callback router you created above.
Now use the parameter `callbacks` in _your API's path operation decorator_ to pass the attribute `.routes` (that's actually just a `list` of routes/_path operations_) from that callback router:
Python 3.8+
```
fromtypingimport Union
fromfastapiimport APIRouter, FastAPI
frompydanticimport BaseModel, HttpUrl
app = FastAPI()
classInvoice(BaseModel):
  id: str
  title: Union[str, None] = None
  customer: str
  total: float
classInvoiceEvent(BaseModel):
  description: str
  paid: bool
classInvoiceEventReceived(BaseModel):
  ok: bool
invoices_callback_router = APIRouter()
@invoices_callback_router.post(
  "{$callback_url}/invoices/{$request.body.id}", response_model=InvoiceEventReceived
)
definvoice_notification(body: InvoiceEvent):
  pass
@app.post("/invoices/", callbacks=invoices_callback_router.routes)
defcreate_invoice(invoice: Invoice, callback_url: Union[HttpUrl, None] = None):
"""
  Create an invoice.
  This will (let's imagine) let the API user (some external developer) create an
  invoice.
  And this path operation will:
  * Send the invoice to the client.
  * Collect the money from the client.
  * Send a notification back to the API user (the external developer), as a callback.
    * At this point is that the API will somehow send a POST request to the
      external API with the notification of the invoice event
      (e.g. "payment successful").
  """
  # Send the invoice, collect the money, send the notification (the callback)
  return {"msg": "Invoice received"}

```

Tip
Notice that you are not passing the router itself (`invoices_callback_router`) to `callback=`, but the attribute `.routes`, as in `invoices_callback_router.routes`.
### Check the docs¶
Now you can start your app and go to http://127.0.0.1:8000/docs.
You will see your docs including a "Callbacks" section for your _path operation_ that shows how the _external API_ should look like:
![](https://fastapi.tiangolo.com/img/tutorial/openapi-callbacks/image01.png)
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
