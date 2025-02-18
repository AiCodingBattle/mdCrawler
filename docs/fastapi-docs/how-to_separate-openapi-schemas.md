Skip to content 
# Separate OpenAPI Schemas for Input and Output or Not¶
When using **Pydantic v2** , the generated OpenAPI is a bit more exact and **correct** than before. 😎
In fact, in some cases, it will even have **two JSON Schemas** in OpenAPI for the same Pydantic model, for input and output, depending on if they have **default values**.
Let's see how that works and how to change it if you need to do that.
## Pydantic Models for Input and Output¶
Let's say you have a Pydantic model with default values, like this one:
Python 3.10+
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: str | None = None
# Code below omitted 👇

```

👀 Full file preview
Python 3.10+
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: str | None = None
app = FastAPI()
@app.post("/items/")
defcreate_item(item: Item):
  return item
@app.get("/items/")
defread_items() -> list[Item]:
  return [
    Item(
      name="Portal Gun",
      description="Device to travel through the multi-rick-verse",
    ),
    Item(name="Plumbus"),
  ]

```

🤓 Other versions and variants
Python 3.9+Python 3.8+
```
fromtypingimport Optional
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: Optional[str] = None
app = FastAPI()
@app.post("/items/")
defcreate_item(item: Item):
  return item
@app.get("/items/")
defread_items() -> list[Item]:
  return [
    Item(
      name="Portal Gun",
      description="Device to travel through the multi-rick-verse",
    ),
    Item(name="Plumbus"),
  ]

```

```
fromtypingimport List, Union
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: Union[str, None] = None
app = FastAPI()
@app.post("/items/")
defcreate_item(item: Item):
  return item
@app.get("/items/")
defread_items() -> List[Item]:
  return [
    Item(
      name="Portal Gun",
      description="Device to travel through the multi-rick-verse",
    ),
    Item(name="Plumbus"),
  ]

```

### Model for Input¶
If you use this model as an input like here:
Python 3.10+
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: str | None = None
app = FastAPI()
@app.post("/items/")
defcreate_item(item: Item):
  return item
# Code below omitted 👇

```

👀 Full file preview
Python 3.10+
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: str | None = None
app = FastAPI()
@app.post("/items/")
defcreate_item(item: Item):
  return item
@app.get("/items/")
defread_items() -> list[Item]:
  return [
    Item(
      name="Portal Gun",
      description="Device to travel through the multi-rick-verse",
    ),
    Item(name="Plumbus"),
  ]

```

🤓 Other versions and variants
Python 3.9+Python 3.8+
```
fromtypingimport Optional
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: Optional[str] = None
app = FastAPI()
@app.post("/items/")
defcreate_item(item: Item):
  return item
@app.get("/items/")
defread_items() -> list[Item]:
  return [
    Item(
      name="Portal Gun",
      description="Device to travel through the multi-rick-verse",
    ),
    Item(name="Plumbus"),
  ]

```

```
fromtypingimport List, Union
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: Union[str, None] = None
app = FastAPI()
@app.post("/items/")
defcreate_item(item: Item):
  return item
@app.get("/items/")
defread_items() -> List[Item]:
  return [
    Item(
      name="Portal Gun",
      description="Device to travel through the multi-rick-verse",
    ),
    Item(name="Plumbus"),
  ]

```

...then the `description` field will **not be required**. Because it has a default value of `None`.
### Input Model in Docs¶
You can confirm that in the docs, the `description` field doesn't have a **red asterisk** , it's not marked as required:
![](https://fastapi.tiangolo.com/img/tutorial/separate-openapi-schemas/image01.png)
### Model for Output¶
But if you use the same model as an output, like here:
Python 3.10+
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: str | None = None
app = FastAPI()
@app.post("/items/")
defcreate_item(item: Item):
  return item
@app.get("/items/")
defread_items() -> list[Item]:
  return [
    Item(
      name="Portal Gun",
      description="Device to travel through the multi-rick-verse",
    ),
    Item(name="Plumbus"),
  ]

```

🤓 Other versions and variants
Python 3.9+Python 3.8+
```
fromtypingimport Optional
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: Optional[str] = None
app = FastAPI()
@app.post("/items/")
defcreate_item(item: Item):
  return item
@app.get("/items/")
defread_items() -> list[Item]:
  return [
    Item(
      name="Portal Gun",
      description="Device to travel through the multi-rick-verse",
    ),
    Item(name="Plumbus"),
  ]

```

```
fromtypingimport List, Union
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: Union[str, None] = None
app = FastAPI()
@app.post("/items/")
defcreate_item(item: Item):
  return item
@app.get("/items/")
defread_items() -> List[Item]:
  return [
    Item(
      name="Portal Gun",
      description="Device to travel through the multi-rick-verse",
    ),
    Item(name="Plumbus"),
  ]

```

...then because `description` has a default value, if you **don't return anything** for that field, it will still have that **default value**.
### Model for Output Response Data¶
If you interact with the docs and check the response, even though the code didn't add anything in one of the `description` fields, the JSON response contains the default value (`null`):
![](https://fastapi.tiangolo.com/img/tutorial/separate-openapi-schemas/image02.png)
This means that it will **always have a value** , it's just that sometimes the value could be `None` (or `null` in JSON).
That means that, clients using your API don't have to check if the value exists or not, they can **assume the field will always be there** , but just that in some cases it will have the default value of `None`.
The way to describe this in OpenAPI, is to mark that field as **required** , because it will always be there.
Because of that, the JSON Schema for a model can be different depending on if it's used for **input or output** :
  * for **input** the `description` will **not be required**
  * for **output** it will be **required** (and possibly `None`, or in JSON terms, `null`)


### Model for Output in Docs¶
You can check the output model in the docs too, **both** `name` and `description` are marked as **required** with a **red asterisk** :
![](https://fastapi.tiangolo.com/img/tutorial/separate-openapi-schemas/image03.png)
### Model for Input and Output in Docs¶
And if you check all the available Schemas (JSON Schemas) in OpenAPI, you will see that there are two, one `Item-Input` and one `Item-Output`.
For `Item-Input`, `description` is **not required** , it doesn't have a red asterisk.
But for `Item-Output`, `description` is **required** , it has a red asterisk.
![](https://fastapi.tiangolo.com/img/tutorial/separate-openapi-schemas/image04.png)
With this feature from **Pydantic v2** , your API documentation is more **precise** , and if you have autogenerated clients and SDKs, they will be more precise too, with a better **developer experience** and consistency. 🎉
## Do not Separate Schemas¶
Now, there are some cases where you might want to have the **same schema for input and output**.
Probably the main use case for this is if you already have some autogenerated client code/SDKs and you don't want to update all the autogenerated client code/SDKs yet, you probably will want to do it at some point, but maybe not right now.
In that case, you can disable this feature in **FastAPI** , with the parameter `separate_input_output_schemas=False`.
Info
Support for `separate_input_output_schemas` was added in FastAPI `0.102.0`. 🤓
Python 3.10+
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: str | None = None
app = FastAPI(separate_input_output_schemas=False)
@app.post("/items/")
defcreate_item(item: Item):
  return item
@app.get("/items/")
defread_items() -> list[Item]:
  return [
    Item(
      name="Portal Gun",
      description="Device to travel through the multi-rick-verse",
    ),
    Item(name="Plumbus"),
  ]

```

🤓 Other versions and variants
Python 3.9+Python 3.8+
```
fromtypingimport Optional
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: Optional[str] = None
app = FastAPI(separate_input_output_schemas=False)
@app.post("/items/")
defcreate_item(item: Item):
  return item
@app.get("/items/")
defread_items() -> list[Item]:
  return [
    Item(
      name="Portal Gun",
      description="Device to travel through the multi-rick-verse",
    ),
    Item(name="Plumbus"),
  ]

```

```
fromtypingimport List, Union
fromfastapiimport FastAPI
frompydanticimport BaseModel
classItem(BaseModel):
  name: str
  description: Union[str, None] = None
app = FastAPI(separate_input_output_schemas=False)
@app.post("/items/")
defcreate_item(item: Item):
  return item
@app.get("/items/")
defread_items() -> List[Item]:
  return [
    Item(
      name="Portal Gun",
      description="Device to travel through the multi-rick-verse",
    ),
    Item(name="Plumbus"),
  ]

```

### Same Schema for Input and Output Models in Docs¶
And now there will be one single schema for input and output for the model, only `Item`, and it will have `description` as **not required** :
![](https://fastapi.tiangolo.com/img/tutorial/separate-openapi-schemas/image05.png)
This is the same behavior as in Pydantic v1. 🤓
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
