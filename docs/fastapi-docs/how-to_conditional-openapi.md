Skip to content 
# Conditional OpenAPI¶
If you needed to, you could use settings and environment variables to configure OpenAPI conditionally depending on the environment, and even disable it entirely.
## About security, APIs, and docs¶
Hiding your documentation user interfaces in production _shouldn't_ be the way to protect your API.
That doesn't add any extra security to your API, the _path operations_ will still be available where they are.
If there's a security flaw in your code, it will still exist.
Hiding the documentation just makes it more difficult to understand how to interact with your API, and could make it more difficult for you to debug it in production. It could be considered simply a form of Security through obscurity.
If you want to secure your API, there are several better things you can do, for example:
  * Make sure you have well defined Pydantic models for your request bodies and responses.
  * Configure any required permissions and roles using dependencies.
  * Never store plaintext passwords, only password hashes.
  * Implement and use well-known cryptographic tools, like Passlib and JWT tokens, etc.
  * Add more granular permission controls with OAuth2 scopes where needed.
  * ...etc.


Nevertheless, you might have a very specific use case where you really need to disable the API docs for some environment (e.g. for production) or depending on configurations from environment variables.
## Conditional OpenAPI from settings and env vars¶
You can easily use the same Pydantic settings to configure your generated OpenAPI and the docs UIs.
For example:
Python 3.8+
```
fromfastapiimport FastAPI
frompydantic_settingsimport BaseSettings
classSettings(BaseSettings):
  openapi_url: str = "/openapi.json"
settings = Settings()
app = FastAPI(openapi_url=settings.openapi_url)
@app.get("/")
defroot():
  return {"message": "Hello World"}

```

Here we declare the setting `openapi_url` with the same default of `"/openapi.json"`.
And then we use it when creating the `FastAPI` app.
Then you could disable OpenAPI (including the UI docs) by setting the environment variable `OPENAPI_URL` to the empty string, like:
```

fast →OPENAPI_URL= uvicorn main:appINFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)restart ↻

```

Then if you go to the URLs at `/openapi.json`, `/docs`, or `/redoc` you will just get a `404 Not Found` error like:
```
{
"detail":"Not Found"
}

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
