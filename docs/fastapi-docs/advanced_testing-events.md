Skip to content 
# Testing Events: startup - shutdown¶
When you need your event handlers (`startup` and `shutdown`) to run in your tests, you can use the `TestClient` with a `with` statement:
Python 3.8+
```
fromfastapiimport FastAPI
fromfastapi.testclientimport TestClient
app = FastAPI()
items = {}
@app.on_event("startup")
async defstartup_event():
  items["foo"] = {"name": "Fighters"}
  items["bar"] = {"name": "Tenders"}
@app.get("/items/{item_id}")
async defread_items(item_id: str):
  return items[item_id]
deftest_read_items():
  with TestClient(app) as client:
    response = client.get("/items/foo")
    assert response.status_code == 200
    assert response.json() == {"name": "Fighters"}

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
