Skip to content 
# Generate Clients¶
As **FastAPI** is based on the OpenAPI specification, you get automatic compatibility with many tools, including the automatic API docs (provided by Swagger UI).
One particular advantage that is not necessarily obvious is that you can **generate clients** (sometimes called **SDKs** ) for your API, for many different **programming languages**.
## OpenAPI Client Generators¶
There are many tools to generate clients from **OpenAPI**.
A common tool is OpenAPI Generator.
If you are building a **frontend** , a very interesting alternative is openapi-ts.
## Client and SDK Generators - Sponsor¶
There are also some **company-backed** Client and SDK generators based on OpenAPI (FastAPI), in some cases they can offer you **additional features** on top of high-quality generated SDKs/clients.
Some of them also ✨ **sponsor FastAPI** ✨, this ensures the continued and healthy **development** of FastAPI and its **ecosystem**.
And it shows their true commitment to FastAPI and its **community** (you), as they not only want to provide you a **good service** but also want to make sure you have a **good and healthy framework** , FastAPI. 🙇
For example, you might want to try:
  * Speakeasy
  * Stainless
  * liblab


There are also several other companies offering similar services that you can search and find online. 🤓
## Generate a TypeScript Frontend Client¶
Let's start with a simple FastAPI application:
Python 3.9+
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
app = FastAPI()
classItem(BaseModel):
  name: str
  price: float
classResponseMessage(BaseModel):
  message: str
@app.post("/items/", response_model=ResponseMessage)
async defcreate_item(item: Item):
  return {"message": "item received"}
@app.get("/items/", response_model=list[Item])
async defget_items():
  return [
    {"name": "Plumbus", "price": 3},
    {"name": "Portal Gun", "price": 9001},
  ]

```

🤓 Other versions and variants
Python 3.8+
```
fromtypingimport List
fromfastapiimport FastAPI
frompydanticimport BaseModel
app = FastAPI()
classItem(BaseModel):
  name: str
  price: float
classResponseMessage(BaseModel):
  message: str
@app.post("/items/", response_model=ResponseMessage)
async defcreate_item(item: Item):
  return {"message": "item received"}
@app.get("/items/", response_model=List[Item])
async defget_items():
  return [
    {"name": "Plumbus", "price": 3},
    {"name": "Portal Gun", "price": 9001},
  ]

```

Notice that the _path operations_ define the models they use for request payload and response payload, using the models `Item` and `ResponseMessage`.
### API Docs¶
If you go to the API docs, you will see that it has the **schemas** for the data to be sent in requests and received in responses:
![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image01.png)
You can see those schemas because they were declared with the models in the app.
That information is available in the app's **OpenAPI schema** , and then shown in the API docs (by Swagger UI).
And that same information from the models that is included in OpenAPI is what can be used to **generate the client code**.
### Generate a TypeScript Client¶
Now that we have the app with the models, we can generate the client code for the frontend.
#### Install `openapi-ts`¶
You can install `openapi-ts` in your frontend code with:
```

fast →npm install @hey-api/openapi-ts --save-devrestart ↻

```

#### Generate Client Code¶
To generate the client code you can use the command line application `openapi-ts` that would now be installed.
Because it is installed in the local project, you probably wouldn't be able to call that command directly, but you would put it on your `package.json` file.
It could look like this:
```
{
"name":"frontend-app",
"version":"1.0.0",
"description":"",
"main":"index.js",
"scripts":{
"generate-client":"openapi-ts --input http://localhost:8000/openapi.json --output ./src/client --client axios"
},
"author":"",
"license":"",
"devDependencies":{
"@hey-api/openapi-ts":"^0.27.38",
"typescript":"^4.6.2"
}
}

```

After having that NPM `generate-client` script there, you can run it with:
```

fast →npm run generate-clientfrontend-app@1.0.0 generate-client /home/user/code/frontend-app> openapi-ts --input http://localhost:8000/openapi.json --output ./src/client --client axiosrestart ↻

```

That command will generate code in `./src/client` and will use `axios` (the frontend HTTP library) internally.
### Try Out the Client Code¶
Now you can import and use the client code, it could look like this, notice that you get autocompletion for the methods:
![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image02.png)
You will also get autocompletion for the payload to send:
![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image03.png)
Tip
Notice the autocompletion for `name` and `price`, that was defined in the FastAPI application, in the `Item` model.
You will have inline errors for the data that you send:
![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image04.png)
The response object will also have autocompletion:
![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image05.png)
## FastAPI App with Tags¶
In many cases your FastAPI app will be bigger, and you will probably use tags to separate different groups of _path operations_.
For example, you could have a section for **items** and another section for **users** , and they could be separated by tags:
Python 3.9+
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
app = FastAPI()
classItem(BaseModel):
  name: str
  price: float
classResponseMessage(BaseModel):
  message: str
classUser(BaseModel):
  username: str
  email: str
@app.post("/items/", response_model=ResponseMessage, tags=["items"])
async defcreate_item(item: Item):
  return {"message": "Item received"}
@app.get("/items/", response_model=list[Item], tags=["items"])
async defget_items():
  return [
    {"name": "Plumbus", "price": 3},
    {"name": "Portal Gun", "price": 9001},
  ]
@app.post("/users/", response_model=ResponseMessage, tags=["users"])
async defcreate_user(user: User):
  return {"message": "User received"}

```

🤓 Other versions and variants
Python 3.8+
```
fromtypingimport List
fromfastapiimport FastAPI
frompydanticimport BaseModel
app = FastAPI()
classItem(BaseModel):
  name: str
  price: float
classResponseMessage(BaseModel):
  message: str
classUser(BaseModel):
  username: str
  email: str
@app.post("/items/", response_model=ResponseMessage, tags=["items"])
async defcreate_item(item: Item):
  return {"message": "Item received"}
@app.get("/items/", response_model=List[Item], tags=["items"])
async defget_items():
  return [
    {"name": "Plumbus", "price": 3},
    {"name": "Portal Gun", "price": 9001},
  ]
@app.post("/users/", response_model=ResponseMessage, tags=["users"])
async defcreate_user(user: User):
  return {"message": "User received"}

```

### Generate a TypeScript Client with Tags¶
If you generate a client for a FastAPI app using tags, it will normally also separate the client code based on the tags.
This way you will be able to have things ordered and grouped correctly for the client code:
![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image06.png)
In this case you have:
  * `ItemsService`
  * `UsersService`


### Client Method Names¶
Right now the generated method names like `createItemItemsPost` don't look very clean:
```
ItemsService.createItemItemsPost({name:"Plumbus",price:5})

```

...that's because the client generator uses the OpenAPI internal **operation ID** for each _path operation_.
OpenAPI requires that each operation ID is unique across all the _path operations_ , so FastAPI uses the **function name** , the **path** , and the **HTTP method/operation** to generate that operation ID, because that way it can make sure that the operation IDs are unique.
But I'll show you how to improve that next. 🤓
## Custom Operation IDs and Better Method Names¶
You can **modify** the way these operation IDs are **generated** to make them simpler and have **simpler method names** in the clients.
In this case you will have to ensure that each operation ID is **unique** in some other way.
For example, you could make sure that each _path operation_ has a tag, and then generate the operation ID based on the **tag** and the _path operation_ **name** (the function name).
### Custom Generate Unique ID Function¶
FastAPI uses a **unique ID** for each _path operation_ , it is used for the **operation ID** and also for the names of any needed custom models, for requests or responses.
You can customize that function. It takes an `APIRoute` and outputs a string.
For example, here it is using the first tag (you will probably have only one tag) and the _path operation_ name (the function name).
You can then pass that custom function to **FastAPI** as the `generate_unique_id_function` parameter:
Python 3.9+
```
fromfastapiimport FastAPI
fromfastapi.routingimport APIRoute
frompydanticimport BaseModel
defcustom_generate_unique_id(route: APIRoute):
  return f"{route.tags[0]}-{route.name}"
app = FastAPI(generate_unique_id_function=custom_generate_unique_id)
classItem(BaseModel):
  name: str
  price: float
classResponseMessage(BaseModel):
  message: str
classUser(BaseModel):
  username: str
  email: str
@app.post("/items/", response_model=ResponseMessage, tags=["items"])
async defcreate_item(item: Item):
  return {"message": "Item received"}
@app.get("/items/", response_model=list[Item], tags=["items"])
async defget_items():
  return [
    {"name": "Plumbus", "price": 3},
    {"name": "Portal Gun", "price": 9001},
  ]
@app.post("/users/", response_model=ResponseMessage, tags=["users"])
async defcreate_user(user: User):
  return {"message": "User received"}

```

🤓 Other versions and variants
Python 3.8+
```
fromtypingimport List
fromfastapiimport FastAPI
fromfastapi.routingimport APIRoute
frompydanticimport BaseModel
defcustom_generate_unique_id(route: APIRoute):
  return f"{route.tags[0]}-{route.name}"
app = FastAPI(generate_unique_id_function=custom_generate_unique_id)
classItem(BaseModel):
  name: str
  price: float
classResponseMessage(BaseModel):
  message: str
classUser(BaseModel):
  username: str
  email: str
@app.post("/items/", response_model=ResponseMessage, tags=["items"])
async defcreate_item(item: Item):
  return {"message": "Item received"}
@app.get("/items/", response_model=List[Item], tags=["items"])
async defget_items():
  return [
    {"name": "Plumbus", "price": 3},
    {"name": "Portal Gun", "price": 9001},
  ]
@app.post("/users/", response_model=ResponseMessage, tags=["users"])
async defcreate_user(user: User):
  return {"message": "User received"}

```

### Generate a TypeScript Client with Custom Operation IDs¶
Now if you generate the client again, you will see that it has the improved method names:
![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image07.png)
As you see, the method names now have the tag and then the function name, now they don't include information from the URL path and the HTTP operation.
### Preprocess the OpenAPI Specification for the Client Generator¶
The generated code still has some **duplicated information**.
We already know that this method is related to the **items** because that word is in the `ItemsService` (taken from the tag), but we still have the tag name prefixed in the method name too. 😕
We will probably still want to keep it for OpenAPI in general, as that will ensure that the operation IDs are **unique**.
But for the generated client we could **modify** the OpenAPI operation IDs right before generating the clients, just to make those method names nicer and **cleaner**.
We could download the OpenAPI JSON to a file `openapi.json` and then we could **remove that prefixed tag** with a script like this:
Python 3.8+Node.js
```
importjson
frompathlibimport Path
file_path = Path("./openapi.json")
openapi_content = json.loads(file_path.read_text())
for path_data in openapi_content["paths"].values():
  for operation in path_data.values():
    tag = operation["tags"][0]
    operation_id = operation["operationId"]
    to_remove = f"{tag}-"
    new_operation_id = operation_id[len(to_remove) :]
    operation["operationId"] = new_operation_id
file_path.write_text(json.dumps(openapi_content))

```

```
import*asfsfrom'fs'
asyncfunctionmodifyOpenAPIFile(filePath){
try{
constdata=awaitfs.promises.readFile(filePath)
constopenapiContent=JSON.parse(data)
constpaths=openapiContent.paths
for(constpathKeyofObject.keys(paths)){
constpathData=paths[pathKey]
for(constmethodofObject.keys(pathData)){
constoperation=pathData[method]
if(operation.tags&&operation.tags.length>0){
consttag=operation.tags[0]
constoperationId=operation.operationId
consttoRemove=`${tag}-`
if(operationId.startsWith(toRemove)){
constnewOperationId=operationId.substring(toRemove.length)
operation.operationId=newOperationId
}
}
}
}
awaitfs.promises.writeFile(
filePath,
JSON.stringify(openapiContent,null,2),
)
console.log('File successfully modified')
}catch(err){
console.error('Error:',err)
}
}
constfilePath='./openapi.json'
modifyOpenAPIFile(filePath)

```

With that, the operation IDs would be renamed from things like `items-get_items` to just `get_items`, that way the client generator can generate simpler method names.
### Generate a TypeScript Client with the Preprocessed OpenAPI¶
Now as the end result is in a file `openapi.json`, you would modify the `package.json` to use that local file, for example:
```
{
"name":"frontend-app",
"version":"1.0.0",
"description":"",
"main":"index.js",
"scripts":{
"generate-client":"openapi-ts --input ./openapi.json --output ./src/client --client axios"
},
"author":"",
"license":"",
"devDependencies":{
"@hey-api/openapi-ts":"^0.27.38",
"typescript":"^4.6.2"
}
}

```

After generating the new client, you would now have **clean method names** , with all the **autocompletion** , **inline errors** , etc:
![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image08.png)
## Benefits¶
When using the automatically generated clients you would get **autocompletion** for:
  * Methods.
  * Request payloads in the body, query parameters, etc.
  * Response payloads.


You would also have **inline errors** for everything.
And whenever you update the backend code, and **regenerate** the frontend, it would have any new _path operations_ available as methods, the old ones removed, and any other change would be reflected on the generated code. 🤓
This also means that if something changed it will be **reflected** on the client code automatically. And if you **build** the client it will error out if you have any **mismatch** in the data used.
So, you would **detect many errors** very early in the development cycle instead of having to wait for the errors to show up to your final users in production and then trying to debug where the problem is. ✨
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
  *[**SDKs**]: Software Development Kits
