Skip to content 
# Cookie Parameters¶
You can define Cookie parameters the same way you define `Query` and `Path` parameters.
## Import `Cookie`¶
First import `Cookie`:
Python 3.10+
```
fromtypingimport Annotated
fromfastapiimport Cookie, FastAPI
app = FastAPI()
@app.get("/items/")
async defread_items(ads_id: Annotated[str | None, Cookie()] = None):
  return {"ads_id": ads_id}

```

🤓 Other versions and variants
Python 3.9+Python 3.8+Python 3.10+ - non-AnnotatedPython 3.8+ - non-Annotated
```
fromtypingimport Annotated, Union
fromfastapiimport Cookie, FastAPI
app = FastAPI()
@app.get("/items/")
async defread_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
  return {"ads_id": ads_id}

```

```
fromtypingimport Union
fromfastapiimport Cookie, FastAPI
fromtyping_extensionsimport Annotated
app = FastAPI()
@app.get("/items/")
async defread_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
  return {"ads_id": ads_id}

```

Tip
Prefer to use the `Annotated` version if possible.
```
fromfastapiimport Cookie, FastAPI
app = FastAPI()
@app.get("/items/")
async defread_items(ads_id: str | None = Cookie(default=None)):
  return {"ads_id": ads_id}

```

Tip
Prefer to use the `Annotated` version if possible.
```
fromtypingimport Union
fromfastapiimport Cookie, FastAPI
app = FastAPI()
@app.get("/items/")
async defread_items(ads_id: Union[str, None] = Cookie(default=None)):
  return {"ads_id": ads_id}

```

## Declare `Cookie` parameters¶
Then declare the cookie parameters using the same structure as with `Path` and `Query`.
You can define the default value as well as all the extra validation or annotation parameters:
Python 3.10+
```
fromtypingimport Annotated
fromfastapiimport Cookie, FastAPI
app = FastAPI()
@app.get("/items/")
async defread_items(ads_id: Annotated[str | None, Cookie()] = None):
  return {"ads_id": ads_id}

```

🤓 Other versions and variants
Python 3.9+Python 3.8+Python 3.10+ - non-AnnotatedPython 3.8+ - non-Annotated
```
fromtypingimport Annotated, Union
fromfastapiimport Cookie, FastAPI
app = FastAPI()
@app.get("/items/")
async defread_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
  return {"ads_id": ads_id}

```

```
fromtypingimport Union
fromfastapiimport Cookie, FastAPI
fromtyping_extensionsimport Annotated
app = FastAPI()
@app.get("/items/")
async defread_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
  return {"ads_id": ads_id}

```

Tip
Prefer to use the `Annotated` version if possible.
```
fromfastapiimport Cookie, FastAPI
app = FastAPI()
@app.get("/items/")
async defread_items(ads_id: str | None = Cookie(default=None)):
  return {"ads_id": ads_id}

```

Tip
Prefer to use the `Annotated` version if possible.
```
fromtypingimport Union
fromfastapiimport Cookie, FastAPI
app = FastAPI()
@app.get("/items/")
async defread_items(ads_id: Union[str, None] = Cookie(default=None)):
  return {"ads_id": ads_id}

```

Technical Details
`Cookie` is a "sister" class of `Path` and `Query`. It also inherits from the same common `Param` class.
But remember that when you import `Query`, `Path`, `Cookie` and others from `fastapi`, those are actually functions that return special classes.
Info
To declare cookies, you need to use `Cookie`, because otherwise the parameters would be interpreted as query parameters.
## Recap¶
Declare cookies with `Cookie`, using the same common pattern as `Query` and `Path`.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
