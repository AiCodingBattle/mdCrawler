Skip to content 
# Including WSGI - Flask, Django, others¶
You can mount WSGI applications as you saw with Sub Applications - Mounts, Behind a Proxy.
For that, you can use the `WSGIMiddleware` and use it to wrap your WSGI application, for example, Flask, Django, etc.
## Using `WSGIMiddleware`¶
You need to import `WSGIMiddleware`.
Then wrap the WSGI (e.g. Flask) app with the middleware.
And then mount that under a path.
Python 3.8+
```
fromfastapiimport FastAPI
fromfastapi.middleware.wsgiimport WSGIMiddleware
fromflaskimport Flask, request
frommarkupsafeimport escape
flask_app = Flask(__name__)
@flask_app.route("/")
defflask_main():
  name = request.args.get("name", "World")
  return f"Hello, {escape(name)} from Flask!"
app = FastAPI()
@app.get("/v2")
defread_main():
  return {"message": "Hello World"}
app.mount("/v1", WSGIMiddleware(flask_app))

```

## Check it¶
Now, every request under the path `/v1/` will be handled by the Flask application.
And the rest will be handled by **FastAPI**.
If you run it and go to http://localhost:8000/v1/ you will see the response from Flask:
```
Hello, World from Flask!

```

And if you go to http://localhost:8000/v2 you will see the response from FastAPI:
```
{
"message":"Hello World"
}

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
