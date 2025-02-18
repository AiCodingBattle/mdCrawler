Skip to content 
# Custom Docs UI Static Assets (Self-Hosting)¶
The API docs use **Swagger UI** and **ReDoc** , and each of those need some JavaScript and CSS files.
By default, those files are served from a CDN.
But it's possible to customize it, you can set a specific CDN, or serve the files yourself.
## Custom CDN for JavaScript and CSS¶
Let's say that you want to use a different CDN, for example you want to use `https://unpkg.com/`.
This could be useful if for example you live in a country that restricts some URLs.
### Disable the automatic docs¶
The first step is to disable the automatic docs, as by default, those use the default CDN.
To disable them, set their URLs to `None` when creating your `FastAPI` app:
Python 3.8+
```
fromfastapiimport FastAPI
fromfastapi.openapi.docsimport (
  get_redoc_html,
  get_swagger_ui_html,
  get_swagger_ui_oauth2_redirect_html,
)
app = FastAPI(docs_url=None, redoc_url=None)
@app.get("/docs", include_in_schema=False)
async defcustom_swagger_ui_html():
  return get_swagger_ui_html(
    openapi_url=app.openapi_url,
    title=app.title + " - Swagger UI",
    oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
    swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
    swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
  )
@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async defswagger_ui_redirect():
  return get_swagger_ui_oauth2_redirect_html()
@app.get("/redoc", include_in_schema=False)
async defredoc_html():
  return get_redoc_html(
    openapi_url=app.openapi_url,
    title=app.title + " - ReDoc",
    redoc_js_url="https://unpkg.com/redoc@next/bundles/redoc.standalone.js",
  )
@app.get("/users/{username}")
async defread_user(username: str):
  return {"message": f"Hello {username}"}

```

### Include the custom docs¶
Now you can create the _path operations_ for the custom docs.
You can reuse FastAPI's internal functions to create the HTML pages for the docs, and pass them the needed arguments:
  * `openapi_url`: the URL where the HTML page for the docs can get the OpenAPI schema for your API. You can use here the attribute `app.openapi_url`.
  * `title`: the title of your API.
  * `oauth2_redirect_url`: you can use `app.swagger_ui_oauth2_redirect_url` here to use the default.
  * `swagger_js_url`: the URL where the HTML for your Swagger UI docs can get the **JavaScript** file. This is the custom CDN URL.
  * `swagger_css_url`: the URL where the HTML for your Swagger UI docs can get the **CSS** file. This is the custom CDN URL.


And similarly for ReDoc...
Python 3.8+
```
fromfastapiimport FastAPI
fromfastapi.openapi.docsimport (
  get_redoc_html,
  get_swagger_ui_html,
  get_swagger_ui_oauth2_redirect_html,
)
app = FastAPI(docs_url=None, redoc_url=None)
@app.get("/docs", include_in_schema=False)
async defcustom_swagger_ui_html():
  return get_swagger_ui_html(
    openapi_url=app.openapi_url,
    title=app.title + " - Swagger UI",
    oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
    swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
    swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
  )
@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async defswagger_ui_redirect():
  return get_swagger_ui_oauth2_redirect_html()
@app.get("/redoc", include_in_schema=False)
async defredoc_html():
  return get_redoc_html(
    openapi_url=app.openapi_url,
    title=app.title + " - ReDoc",
    redoc_js_url="https://unpkg.com/redoc@next/bundles/redoc.standalone.js",
  )
@app.get("/users/{username}")
async defread_user(username: str):
  return {"message": f"Hello {username}"}

```

Tip
The _path operation_ for `swagger_ui_redirect` is a helper for when you use OAuth2.
If you integrate your API with an OAuth2 provider, you will be able to authenticate and come back to the API docs with the acquired credentials. And interact with it using the real OAuth2 authentication.
Swagger UI will handle it behind the scenes for you, but it needs this "redirect" helper.
### Create a _path operation_ to test it¶
Now, to be able to test that everything works, create a _path operation_ :
Python 3.8+
```
fromfastapiimport FastAPI
fromfastapi.openapi.docsimport (
  get_redoc_html,
  get_swagger_ui_html,
  get_swagger_ui_oauth2_redirect_html,
)
app = FastAPI(docs_url=None, redoc_url=None)
@app.get("/docs", include_in_schema=False)
async defcustom_swagger_ui_html():
  return get_swagger_ui_html(
    openapi_url=app.openapi_url,
    title=app.title + " - Swagger UI",
    oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
    swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
    swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
  )
@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async defswagger_ui_redirect():
  return get_swagger_ui_oauth2_redirect_html()
@app.get("/redoc", include_in_schema=False)
async defredoc_html():
  return get_redoc_html(
    openapi_url=app.openapi_url,
    title=app.title + " - ReDoc",
    redoc_js_url="https://unpkg.com/redoc@next/bundles/redoc.standalone.js",
  )
@app.get("/users/{username}")
async defread_user(username: str):
  return {"message": f"Hello {username}"}

```

### Test it¶
Now, you should be able to go to your docs at http://127.0.0.1:8000/docs, and reload the page, it will load those assets from the new CDN.
## Self-hosting JavaScript and CSS for docs¶
Self-hosting the JavaScript and CSS could be useful if, for example, you need your app to keep working even while offline, without open Internet access, or in a local network.
Here you'll see how to serve those files yourself, in the same FastAPI app, and configure the docs to use them.
### Project file structure¶
Let's say your project file structure looks like this:
```
.
├── app
│  ├── __init__.py
│  ├── main.py

```

Now create a directory to store those static files.
Your new file structure could look like this:
```
.
├── app
│   ├── __init__.py
│   ├── main.py
└── static/

```

### Download the files¶
Download the static files needed for the docs and put them on that `static/` directory.
You can probably right-click each link and select an option similar to `Save link as...`.
**Swagger UI** uses the files:
  * `swagger-ui-bundle.js`
  * `swagger-ui.css`


And **ReDoc** uses the file:
  * `redoc.standalone.js`


After that, your file structure could look like:
```
.
├── app
│   ├── __init__.py
│   ├── main.py
└── static
  ├── redoc.standalone.js
  ├── swagger-ui-bundle.js
  └── swagger-ui.css

```

### Serve the static files¶
  * Import `StaticFiles`.
  * "Mount" a `StaticFiles()` instance in a specific path.


Python 3.8+
```
fromfastapiimport FastAPI
fromfastapi.openapi.docsimport (
  get_redoc_html,
  get_swagger_ui_html,
  get_swagger_ui_oauth2_redirect_html,
)
fromfastapi.staticfilesimport StaticFiles
app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/docs", include_in_schema=False)
async defcustom_swagger_ui_html():
  return get_swagger_ui_html(
    openapi_url=app.openapi_url,
    title=app.title + " - Swagger UI",
    oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
    swagger_js_url="/static/swagger-ui-bundle.js",
    swagger_css_url="/static/swagger-ui.css",
  )
@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async defswagger_ui_redirect():
  return get_swagger_ui_oauth2_redirect_html()
@app.get("/redoc", include_in_schema=False)
async defredoc_html():
  return get_redoc_html(
    openapi_url=app.openapi_url,
    title=app.title + " - ReDoc",
    redoc_js_url="/static/redoc.standalone.js",
  )
@app.get("/users/{username}")
async defread_user(username: str):
  return {"message": f"Hello {username}"}

```

### Test the static files¶
Start your application and go to http://127.0.0.1:8000/static/redoc.standalone.js.
You should see a very long JavaScript file for **ReDoc**.
It could start with something like:
```
/*!
 * ReDoc - OpenAPI/Swagger-generated API Reference Documentation
 * -------------------------------------------------------------
 *  Version: "2.0.0-rc.18"
 *  Repo: https://github.com/Redocly/redoc
 */
!function(e,t){"object"==typeofexports&&"object"==typeofm
...

```

That confirms that you are being able to serve static files from your app, and that you placed the static files for the docs in the correct place.
Now we can configure the app to use those static files for the docs.
### Disable the automatic docs for static files¶
The same as when using a custom CDN, the first step is to disable the automatic docs, as those use the CDN by default.
To disable them, set their URLs to `None` when creating your `FastAPI` app:
Python 3.8+
```
fromfastapiimport FastAPI
fromfastapi.openapi.docsimport (
  get_redoc_html,
  get_swagger_ui_html,
  get_swagger_ui_oauth2_redirect_html,
)
fromfastapi.staticfilesimport StaticFiles
app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/docs", include_in_schema=False)
async defcustom_swagger_ui_html():
  return get_swagger_ui_html(
    openapi_url=app.openapi_url,
    title=app.title + " - Swagger UI",
    oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
    swagger_js_url="/static/swagger-ui-bundle.js",
    swagger_css_url="/static/swagger-ui.css",
  )
@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async defswagger_ui_redirect():
  return get_swagger_ui_oauth2_redirect_html()
@app.get("/redoc", include_in_schema=False)
async defredoc_html():
  return get_redoc_html(
    openapi_url=app.openapi_url,
    title=app.title + " - ReDoc",
    redoc_js_url="/static/redoc.standalone.js",
  )
@app.get("/users/{username}")
async defread_user(username: str):
  return {"message": f"Hello {username}"}

```

### Include the custom docs for static files¶
And the same way as with a custom CDN, now you can create the _path operations_ for the custom docs.
Again, you can reuse FastAPI's internal functions to create the HTML pages for the docs, and pass them the needed arguments:
  * `openapi_url`: the URL where the HTML page for the docs can get the OpenAPI schema for your API. You can use here the attribute `app.openapi_url`.
  * `title`: the title of your API.
  * `oauth2_redirect_url`: you can use `app.swagger_ui_oauth2_redirect_url` here to use the default.
  * `swagger_js_url`: the URL where the HTML for your Swagger UI docs can get the **JavaScript** file. **This is the one that your own app is now serving**.
  * `swagger_css_url`: the URL where the HTML for your Swagger UI docs can get the **CSS** file. **This is the one that your own app is now serving**.


And similarly for ReDoc...
Python 3.8+
```
fromfastapiimport FastAPI
fromfastapi.openapi.docsimport (
  get_redoc_html,
  get_swagger_ui_html,
  get_swagger_ui_oauth2_redirect_html,
)
fromfastapi.staticfilesimport StaticFiles
app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/docs", include_in_schema=False)
async defcustom_swagger_ui_html():
  return get_swagger_ui_html(
    openapi_url=app.openapi_url,
    title=app.title + " - Swagger UI",
    oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
    swagger_js_url="/static/swagger-ui-bundle.js",
    swagger_css_url="/static/swagger-ui.css",
  )
@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async defswagger_ui_redirect():
  return get_swagger_ui_oauth2_redirect_html()
@app.get("/redoc", include_in_schema=False)
async defredoc_html():
  return get_redoc_html(
    openapi_url=app.openapi_url,
    title=app.title + " - ReDoc",
    redoc_js_url="/static/redoc.standalone.js",
  )
@app.get("/users/{username}")
async defread_user(username: str):
  return {"message": f"Hello {username}"}

```

Tip
The _path operation_ for `swagger_ui_redirect` is a helper for when you use OAuth2.
If you integrate your API with an OAuth2 provider, you will be able to authenticate and come back to the API docs with the acquired credentials. And interact with it using the real OAuth2 authentication.
Swagger UI will handle it behind the scenes for you, but it needs this "redirect" helper.
### Create a _path operation_ to test static files¶
Now, to be able to test that everything works, create a _path operation_ :
Python 3.8+
```
fromfastapiimport FastAPI
fromfastapi.openapi.docsimport (
  get_redoc_html,
  get_swagger_ui_html,
  get_swagger_ui_oauth2_redirect_html,
)
fromfastapi.staticfilesimport StaticFiles
app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/docs", include_in_schema=False)
async defcustom_swagger_ui_html():
  return get_swagger_ui_html(
    openapi_url=app.openapi_url,
    title=app.title + " - Swagger UI",
    oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
    swagger_js_url="/static/swagger-ui-bundle.js",
    swagger_css_url="/static/swagger-ui.css",
  )
@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async defswagger_ui_redirect():
  return get_swagger_ui_oauth2_redirect_html()
@app.get("/redoc", include_in_schema=False)
async defredoc_html():
  return get_redoc_html(
    openapi_url=app.openapi_url,
    title=app.title + " - ReDoc",
    redoc_js_url="/static/redoc.standalone.js",
  )
@app.get("/users/{username}")
async defread_user(username: str):
  return {"message": f"Hello {username}"}

```

### Test Static Files UI¶
Now, you should be able to disconnect your WiFi, go to your docs at http://127.0.0.1:8000/docs, and reload the page.
And even without Internet, you would be able to see the docs for your API and interact with it.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
  *[CDN]: Content Delivery Network
