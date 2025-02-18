Skip to content 
# OpenAPI Webhooks¶
There are cases where you want to tell your API **users** that your app could call _their_ app (sending a request) with some data, normally to **notify** of some type of **event**.
This means that instead of the normal process of your users sending requests to your API, it's **your API** (or your app) that could **send requests to their system** (to their API, their app).
This is normally called a **webhook**.
## Webhooks steps¶
The process normally is that **you define** in your code what is the message that you will send, the **body of the request**.
You also define in some way at which **moments** your app will send those requests or events.
And **your users** define in some way (for example in a web dashboard somewhere) the **URL** where your app should send those requests.
All the **logic** about how to register the URLs for webhooks and the code to actually send those requests is up to you. You write it however you want to in **your own code**.
## Documenting webhooks with **FastAPI** and OpenAPI¶
With **FastAPI** , using OpenAPI, you can define the names of these webhooks, the types of HTTP operations that your app can send (e.g. `POST`, `PUT`, etc.) and the request **bodies** that your app would send.
This can make it a lot easier for your users to **implement their APIs** to receive your **webhook** requests, they might even be able to autogenerate some of their own API code.
Info
Webhooks are available in OpenAPI 3.1.0 and above, supported by FastAPI `0.99.0` and above.
## An app with webhooks¶
When you create a **FastAPI** application, there is a `webhooks` attribute that you can use to define _webhooks_ , the same way you would define _path operations_ , for example with `@app.webhooks.post()`.
Python 3.8+
```
fromdatetimeimport datetime
fromfastapiimport FastAPI
frompydanticimport BaseModel
app = FastAPI()
classSubscription(BaseModel):
  username: str
  monthly_fee: float
  start_date: datetime
@app.webhooks.post("new-subscription")
defnew_subscription(body: Subscription):
"""
  When a new user subscribes to your service we'll send you a POST request with this
  data to the URL that you register for the event `new-subscription` in the dashboard.
  """
@app.get("/users/")
defread_users():
  return ["Rick", "Morty"]

```

The webhooks that you define will end up in the **OpenAPI** schema and the automatic **docs UI**.
Info
The `app.webhooks` object is actually just an `APIRouter`, the same type you would use when structuring your app with multiple files.
Notice that with webhooks you are actually not declaring a _path_ (like `/items/`), the text you pass there is just an **identifier** of the webhook (the name of the event), for example in `@app.webhooks.post("new-subscription")`, the webhook name is `new-subscription`.
This is because it is expected that **your users** would define the actual **URL path** where they want to receive the webhook request in some other way (e.g. a web dashboard).
### Check the docs¶
Now you can start your app and go to http://127.0.0.1:8000/docs.
You will see your docs have the normal _path operations_ and now also some **webhooks** :
![](https://fastapi.tiangolo.com/img/tutorial/openapi-webhooks/image01.png)
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
