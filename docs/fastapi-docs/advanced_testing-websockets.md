Skip to content 
# Testing WebSockets¶
You can use the same `TestClient` to test WebSockets.
For this, you use the `TestClient` in a `with` statement, connecting to the WebSocket:
Python 3.8+
```
fromfastapiimport FastAPI
fromfastapi.testclientimport TestClient
fromfastapi.websocketsimport WebSocket
app = FastAPI()
@app.get("/")
async defread_main():
  return {"msg": "Hello World"}
@app.websocket("/ws")
async defwebsocket(websocket: WebSocket):
  await websocket.accept()
  await websocket.send_json({"msg": "Hello WebSocket"})
  await websocket.close()
deftest_read_main():
  client = TestClient(app)
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"msg": "Hello World"}
deftest_websocket():
  client = TestClient(app)
  with client.websocket_connect("/ws") as websocket:
    data = websocket.receive_json()
    assert data == {"msg": "Hello WebSocket"}

```

Note
For more details, check Starlette's documentation for testing WebSockets.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Back to top 
