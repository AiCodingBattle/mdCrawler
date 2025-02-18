Skip to content 
# GraphQL¶
As **FastAPI** is based on the **ASGI** standard, it's very easy to integrate any **GraphQL** library also compatible with ASGI.
You can combine normal FastAPI _path operations_ with GraphQL on the same application.
Tip
**GraphQL** solves some very specific use cases.
It has **advantages** and **disadvantages** when compared to common **web APIs**.
Make sure you evaluate if the **benefits** for your use case compensate the **drawbacks**. 🤓
## GraphQL Libraries¶
Here are some of the **GraphQL** libraries that have **ASGI** support. You could use them with **FastAPI** :
  * Strawberry 🍓
    * With docs for FastAPI
  * Ariadne
    * With docs for FastAPI
  * Tartiflette
    * With Tartiflette ASGI to provide ASGI integration
  * Graphene
    * With starlette-graphene3


## GraphQL with Strawberry¶
If you need or want to work with **GraphQL** , **Strawberry** is the **recommended** library as it has the design closest to **FastAPI's** design, it's all based on **type annotations**.
Depending on your use case, you might prefer to use a different library, but if you asked me, I would probably suggest you try **Strawberry**.
Here's a small preview of how you could integrate Strawberry with FastAPI:
Python 3.8+
```
importstrawberry
fromfastapiimport FastAPI
fromstrawberry.fastapiimport GraphQLRouter
@strawberry.type
classUser:
  name: str
  age: int
@strawberry.type
classQuery:
  @strawberry.field
  defuser(self) -> User:
    return User(name="Patrick", age=100)
schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

```

You can learn more about Strawberry in the Strawberry documentation.
And also the docs about Strawberry with FastAPI.
## Older `GraphQLApp` from Starlette¶
Previous versions of Starlette included a `GraphQLApp` class to integrate with Graphene.
It was deprecated from Starlette, but if you have code that used it, you can easily **migrate** to starlette-graphene3, that covers the same use case and has an **almost identical interface**.
Tip
If you need GraphQL, I still would recommend you check out Strawberry, as it's based on type annotations instead of custom classes and types.
## Learn More¶
You can learn more about **GraphQL** in the official GraphQL documentation.
You can also read more about each those libraries described above in their links.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
