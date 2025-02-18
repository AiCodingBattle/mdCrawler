Skip to content 
# Background Tasks - `BackgroundTasks`¶
You can declare a parameter in a _path operation function_ or dependency function with the type `BackgroundTasks`, and then you can use it to schedule the execution of background tasks after the response is sent.
You can import it directly from `fastapi`:
```
fromfastapiimport BackgroundTasks

```

##  fastapi.BackgroundTasks ¶
```
BackgroundTasks(tasks=None)

```

Bases: `BackgroundTasks`
A collection of background tasks that will be called after a response has been sent to the client.
Read more about it in the FastAPI docs for Background Tasks.
#### Example¶
```
fromfastapiimport BackgroundTasks, FastAPI
app = FastAPI()
defwrite_notification(email: str, message=""):
  with open("log.txt", mode="w") as email_file:
    content = f"notification for {email}: {message}"
    email_file.write(content)
@app.post("/send-notification/{email}")
async defsend_notification(email: str, background_tasks: BackgroundTasks):
  background_tasks.add_task(write_notification, email, message="some notification")
  return {"message": "Notification sent in the background"}

```

PARAMETER | DESCRIPTION  
---|---  
`tasks` |  **TYPE:** `Sequence[BackgroundTask] | None` **DEFAULT:** `None`  
Source code in `starlette/background.py`
```
32
33
```
| ```
def__init__(self, tasks: typing.Sequence[BackgroundTask] | None = None):
  self.tasks = list(tasks) if tasks else []

```
  
---|---  
###  func `instance-attribute` ¶
```
func = func

```

###  args `instance-attribute` ¶
```
args = args

```

###  kwargs `instance-attribute` ¶
```
kwargs = kwargs

```

###  is_async `instance-attribute` ¶
```
is_async = is_async_callable(func)

```

###  tasks `instance-attribute` ¶
```
tasks = list(tasks) if tasks else []

```

###  add_task ¶
```
add_task(func, *args, **kwargs)

```

Add a function to be called in the background after the response is sent.
Read more about it in the FastAPI docs for Background Tasks.
PARAMETER | DESCRIPTION  
---|---  
`func` |  The function to call after the response is sent. It can be a regular `def` function or an `async def` function. **TYPE:** `Callable[P, Any]`  
`*args` |  **TYPE:** `args` **DEFAULT:** `()`  
`**kwargs` |  **TYPE:** `kwargs` **DEFAULT:** `{}`  
Source code in `fastapi/background.py`
```
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
```
| ```
defadd_task(
  self,
  func: Annotated[
    Callable[P, Any],
    Doc(
"""
      The function to call after the response is sent.
      It can be a regular `def` function or an `async def` function.
      """
    ),
  ],
  *args: P.args,
  **kwargs: P.kwargs,
) -> None:
"""
  Add a function to be called in the background after the response is sent.
  Read more about it in the
  [FastAPI docs for Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/).
  """
  return super().add_task(func, *args, **kwargs)

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
