Bỏ qua 
# FastAPI¶
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_FastAPI framework, hiệu năng cao, dễ học, dễ code, sẵn sàng để tạo ra sản phẩm_
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master) ![Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ![Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package) ![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
**Tài liệu** : https://fastapi.tiangolo.com
**Mã nguồn** : https://github.com/fastapi/fastapi
FastAPI là một web framework hiện đại, hiệu năng cao để xây dựng web APIs với Python dựa trên tiêu chuẩn Python type hints.
Những tính năng như:
  * **Nhanh** : Hiệu năng rất cao khi so sánh với **NodeJS** và **Go** (cảm ơn Starlette và Pydantic). Một trong những Python framework nhanh nhất.
  * **Code nhanh** : Tăng tốc độ phát triển tính năng từ 200% tới 300%. *
  * **Ít lỗi hơn** : Giảm khoảng 40% những lỗi phát sinh bởi con người (nhà phát triển). *
  * **Trực giác tốt hơn** : Được các trình soạn thảo hỗ tuyệt vời. Completion mọi nơi. Ít thời gian gỡ lỗi.
  * **Dễ dàng** : Được thiết kế để dễ dàng học và sử dụng. Ít thời gian đọc tài liệu.
  * **Ngắn** : Tối thiểu code bị trùng lặp. Nhiều tính năng được tích hợp khi định nghĩa tham số. Ít lỗi hơn.
  * **Tăng tốc** : Có được sản phẩm cùng với tài liệu (được tự động tạo) có thể tương tác.
  * **Được dựa trên các tiêu chuẩn** : Dựa trên (và hoàn toàn tương thích với) các tiêu chuẩn mở cho APIs : OpenAPI (trước đó được biết đến là Swagger) và JSON Schema.


* ước tính được dựa trên những kiểm chứng trong nhóm phát triển nội bộ, xây dựng các ứng dụng sản phẩm.
## Nhà tài trợ¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Những nhà tài trợ khác
## Ý kiến đánh giá¶
"_[...] Tôi đang sử dụng**FastAPI** vô cùng nhiều vào những ngày này. [...] Tôi thực sự đang lên kế hoạch sử dụng nó cho tất cả các nhóm **dịch vụ ML tại Microsoft**. Một vài trong số đó đang tích hợp vào sản phẩm lõi của **Window** và một vài sản phẩm cho **Office**._"
Kabir Khan - **Microsoft** (ref)
"_Chúng tôi tích hợp thư viện**FastAPI** để sinh ra một **REST** server, nó có thể được truy vấn để thu được những **dự đoán**._ [bởi Ludwid] "
Piero Molino, Yaroslav Dudin, và Sai Sumanth Miryala - **Uber** (ref)
"_**Netflix** vui mừng thông báo việc phát hành framework mã nguồn mở của chúng tôi cho _quản lí khủng hoảng_ tập trung: **Dispatch**! [xây dựng với **FastAPI**]_"
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** (ref)
"_Tôi vô cùng hào hứng về**FastAPI**. Nó rất thú vị_"
Brian Okken - **Python Bytes podcast host** (ref)
"_Thành thật, những gì bạn đã xây dựng nhìn siêu chắc chắn và bóng bẩy. Theo nhiều cách, nó là những gì tôi đã muốn Hug trở thành - thật sự truyền cảm hứng để thấy ai đó xây dựng nó._ "
Timothy Crosley - người tạo ra **Hug** (ref)
"_Nếu bạn đang tìm kiếm một**framework hiện đại** để xây dựng một REST APIs, thử xem xét **FastAPI** [...] Nó nhanh, dễ dùng và dễ học [...]_"
"_Chúng tôi đã chuyển qua**FastAPI cho **APIs** của chúng tôi [...] Tôi nghĩ bạn sẽ thích nó [...]_"
Ines Montani - Matthew Honnibal - **Explosion AI founders - spaCy creators** (ref) - (ref)
Ines Montani - Matthew Honnibal - **nhà sáng lậpExplosion AI - người tạo ra spaCy** (ref) - (ref)
"_Nếu ai đó đang tìm cách xây dựng sản phẩm API bằng Python, tôi sẽ đề xuất**FastAPI**. Nó **được thiết kế đẹp đẽ** , **sử dụng đơn giản** và **có khả năng mở rộng cao** , nó đã trở thành một **thành phần quan trọng** trong chiến lược phát triển API của chúng tôi và đang thúc đẩy nhiều dịch vụ và mảng tự động hóa như Kỹ sư TAC ảo của chúng tôi._"
Deon Pillsbury - **Cisco** (ref)
## **Typer** , giao diện dòng lệnh của FastAPI¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
Nếu bạn đang xây dựng một CLI - ứng dụng được sử dụng trong giao diện dòng lệnh, xem về **Typer**.
**Typer** là một người anh em của FastAPI. Và nó được dự định trở thành **giao diện dòng lệnh cho FastAPI**. ⌨️ 🚀
## Yêu cầu¶
FastAPI đứng trên vai những người khổng lồ:
  * Starlette cho phần web.
  * Pydantic cho phần data.


## Cài đặt¶
```

fast →pip install fastapirestart ↻

```

Bạn cũng sẽ cần một ASGI server cho production như Uvicorn hoặc Hypercorn.
```

fast →pip install "uvicorn[standard]"restart ↻

```

## Ví dụ¶
### Khởi tạo¶
  * Tạo một tệp tin `main.py` như sau:


```
fromtypingimport Union
fromfastapiimport FastAPI
app = FastAPI()
@app.get("/")
defread_root():
  return {"Hello": "World"}
@app.get("/items/{item_id}")
defread_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}

```

Hoặc sử dụng `async def`...
Nếu code của bạn sử dụng `async` / `await`, hãy sử dụng `async def`:
```
fromtypingimport Union
fromfastapiimport FastAPI
app = FastAPI()
@app.get("/")
async defread_root():
  return {"Hello": "World"}
@app.get("/items/{item_id}")
async defread_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}

```

**Lưu ý** :
Nếu bạn không biết, xem phần _"In a hurry?"_ về `async` và `await` trong tài liệu này.
### Chạy ứng dụng¶
Chạy server như sau:
```

fast →uvicorn main:app --reloadINFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [28720]INFO:   Started server process [28722]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

Về lệnh `uvicorn main:app --reload`...
Lệnh `uvicorn main:app` tham chiếu tới những thành phần sau:
  * `main`: tệp tin `main.py` (một Python "module").
  * `app`: object được tạo trong tệp tin `main.py` tại dòng `app = FastAPI()`.
  * `--reload`: chạy lại server sau khi code thay đổi. Chỉ sử dụng trong quá trình phát triển.


### Kiểm tra¶
Mở trình duyệt của bạn tại http://127.0.0.1:8000/items/5?q=somequery.
Bạn sẽ thấy một JSON response:
```
{"item_id":5,"q":"somequery"}

```

Bạn đã sẵn sàng để tạo một API như sau:
  * Nhận HTTP request với _đường dẫn_ `/` và `/items/{item_id}`.
  * Cả hai _đường dẫn_ sử dụng _toán tử_ `GET` (cũng đươc biết đến là _phương thức_ HTTP).
  * _Đường dẫn_ `/items/{item_id}` có một _tham số đường dẫn_ `item_id`, nó là một tham số kiểu `int`.
  * _Đường dẫn_ `/items/{item_id}` có một _tham số query string_ `q`, nó là một tham số tùy chọn kiểu `str`.


### Tài liệu tương tác API¶
Truy cập http://127.0.0.1:8000/docs.
Bạn sẽ thấy tài liệu tương tác API được tạo tự động (cung cấp bởi Swagger UI):
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Tài liệu API thay thế¶
Và bây giờ, hãy truy cập tới http://127.0.0.1:8000/redoc.
Bạn sẽ thấy tài liệu được thay thế (cung cấp bởi ReDoc):
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Nâng cấp ví dụ¶
Bây giờ sửa tệp tin `main.py` để nhận body từ một request `PUT`.
Định nghĩa của body sử dụng kiểu dữ liệu chuẩn của Python, cảm ơn Pydantic.
```
fromtypingimport Union
fromfastapiimport FastAPI
frompydanticimport BaseModel
app = FastAPI()
classItem(BaseModel):
  name: str
  price: float
  is_offer: Union[bool, None] = None
@app.get("/")
defread_root():
  return {"Hello": "World"}
@app.get("/items/{item_id}")
defread_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}
@app.put("/items/{item_id}")
defupdate_item(item_id: int, item: Item):
  return {"item_name": item.name, "item_id": item_id}

```

Server nên tự động chạy lại (bởi vì bạn đã thêm `--reload` trong lệnh `uvicorn` ở trên).
### Nâng cấp tài liệu API¶
Bây giờ truy cập tới http://127.0.0.1:8000/docs.
  * Tài liệu API sẽ được tự động cập nhật, bao gồm body mới:


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * Click vào nút "Try it out", nó cho phép bạn điền những tham số và tương tác trực tiếp với API:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Sau khi click vào nút "Execute", giao diện người dùng sẽ giao tiếp với API của bạn bao gồm: gửi các tham số, lấy kết quả và hiển thị chúng trên màn hình:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Nâng cấp tài liệu API thay thế¶
Và bây giờ truy cập tới http://127.0.0.1:8000/redoc.
  * Tài liệu thay thế cũng sẽ phản ánh tham số và body mới:


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### Tóm lại¶
Bạn khai báo **một lần** kiểu dữ liệu của các tham số, body, etc là các tham số của hàm số.
Bạn định nghĩa bằng cách sử dụng các kiểu dữ liệu chuẩn của Python.
Bạn không phải học một cú pháp mới, các phương thức và class của một thư viện cụ thể nào.
Chỉ cần sử dụng các chuẩn của **Python**.
Ví dụ, với một tham số kiểu `int`:
```
item_id: int

```

hoặc với một model `Item` phức tạp hơn:
```
item: Item

```

...và với định nghĩa đơn giản đó, bạn có được:
  * Sự hỗ trợ từ các trình soạn thảo, bao gồm:
    * Completion.
    * Kiểm tra kiểu dữ liệu.
  * Kiểm tra kiểu dữ liệu:
    * Tự động sinh lỗi rõ ràng khi dữ liệu không hợp lệ .
    * Kiểm tra JSON lồng nhau .
  * Chuyển đổi dữ liệu đầu vào: tới từ network sang dữ liệu kiểu Python. Đọc từ:
    * JSON.
    * Các tham số trong đường dẫn.
    * Các tham số trong query string.
    * Cookies.
    * Headers.
    * Forms.
    * Files.
  * Chuyển đổi dữ liệu đầu ra: chuyển đổi từ kiểu dữ liệu Python sang dữ liệu network (như JSON):
    * Chuyển đổi kiểu dữ liệu Python (`str`, `int`, `float`, `bool`, `list`,...).
    * `datetime` objects.
    * `UUID` objects.
    * Database models.
    * ...và nhiều hơn thế.
  * Tự động tạo tài liệu tương tác API, bao gồm 2 giao diện người dùng:
    * Swagger UI.
    * ReDoc.


Quay trở lại ví dụ trước, **FastAPI** sẽ thực hiện:
  * Kiểm tra xem có một `item_id` trong đường dẫn với các request `GET` và `PUT` không?
  * Kiểm tra xem `item_id` có phải là kiểu `int` trong các request `GET` và `PUT` không?
    * Nếu không, client sẽ thấy một lỗi rõ ràng và hữu ích.
  * Kiểm tra xem nếu có một tham số `q` trong query string (ví dụ như `http://127.0.0.1:8000/items/foo?q=somequery`) cho request `GET`.
    * Tham số `q` được định nghĩa `= None`, nó là tùy chọn.
    * Nếu không phải `None`, nó là bắt buộc (như body trong trường hợp của `PUT`).
  * Với request `PUT` tới `/items/{item_id}`, đọc body như JSON:
    * Kiểm tra xem nó có một thuộc tính bắt buộc kiểu `str` là `name` không?
    * Kiểm tra xem nó có một thuộc tính bắt buộc kiểu `float` là `price` không?
    * Kiểm tra xem nó có một thuộc tính tùy chọn là `is_offer` không? Nếu có, nó phải có kiểu `bool`.
    * Tất cả những kiểm tra này cũng được áp dụng với các JSON lồng nhau.
  * Chuyển đổi tự động các JSON object đến và JSON object đi.
  * Tài liệu hóa mọi thứ với OpenAPI, tài liệu đó có thể được sử dụng bởi:
    * Các hệ thống tài liệu có thể tương tác.
    * Hệ thống sinh code tự động, cho nhiều ngôn ngữ lập trình.
    * Cung cấp trực tiếp 2 giao diện web cho tài liệu tương tác


Chúng tôi chỉ trình bày những thứ cơ bản bên ngoài, nhưng bạn đã hiểu cách thức hoạt động của nó.
Thử thay đổi dòng này:
```
  return {"item_name": item.name, "item_id": item_id}

```

...từ:
```
    ... "item_name": item.name ...

```

...sang:
```
    ... "item_price": item.price ...

```

...và thấy trình soạn thảo của bạn nhận biết kiểu dữ liệu và gợi ý hoàn thiện các thuộc tính.
![trình soạn thảo hỗ trợ](https://fastapi.tiangolo.com/img/vscode-completion.png)
Ví dụ hoàn chỉnh bao gồm nhiều tính năng hơn, xem Tutorial - User Guide.
**Cảnh báo tiết lỗ** : Tutorial - User Guide:
  * Định nghĩa **tham số** từ các nguồn khác nhau như: **headers** , **cookies** , **form fields** và **files**.
  * Cách thiết lập **các ràng buộc cho validation** như `maximum_length` hoặc `regex`.
  * Một hệ thống **Dependency Injection vô cùng mạnh mẽ và dễ dàng sử dụng.
  * Bảo mật và xác thực, hỗ trợ **OAuth2**(với **JWT tokens**) và **HTTP Basic**.
  * Những kĩ thuật nâng cao hơn (nhưng tương đối dễ) để định nghĩa **JSON models lồng nhau** (cảm ơn Pydantic).
  * Tích hợp **GraphQL** với Strawberry và các thư viện khác.
  * Nhiều tính năng mở rộng (cảm ơn Starlette) như:
    * **WebSockets**
    * kiểm thử vô cùng dễ dàng dựa trên HTTPX và `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...và nhiều hơn thế.


## Hiệu năng¶
Independent TechEmpower benchmarks cho thấy các ứng dụng **FastAPI** chạy dưới Uvicorn là một trong những Python framework nhanh nhất, chỉ đứng sau Starlette và Uvicorn (được sử dụng bên trong FastAPI). (*)
Để hiểu rõ hơn, xem phần Benchmarks.
## Các dependency tùy chọn¶
Sử dụng bởi Pydantic:
  * `email-validator` - cho email validation.


Sử dụng Starlette:
  * `httpx` - Bắt buộc nếu bạn muốn sử dụng `TestClient`.
  * `jinja2` - Bắt buộc nếu bạn muốn sử dụng cấu hình template engine mặc định.
  * `python-multipart` - Bắt buộc nếu bạn muốn hỗ trợ "parsing", form với `request.form()`.
  * `itsdangerous` - Bắt buộc để hỗ trợ `SessionMiddleware`.
  * `pyyaml` - Bắt buộc để hỗ trợ `SchemaGenerator` cho Starlette (bạn có thể không cần nó trong FastAPI).


Sử dụng bởi FastAPI / Starlette:
  * `uvicorn` - Server để chạy ứng dụng của bạn.
  * `orjson` - Bắt buộc nếu bạn muốn sử dụng `ORJSONResponse`.
  * `ujson` - Bắt buộc nếu bạn muốn sử dụng `UJSONResponse`.


Bạn có thể cài đặt tất cả những dependency trên với `pip install "fastapi[all]"`.
## Giấy phép¶
Dự án này được cấp phép dưới những điều lệ của giấy phép MIT.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Trở lại mục lục 
  *[Completion]: như auto-complete, autocompletion, IntelliSense
  *[CLI]: Giao diện dòng lệnh
  *[Chuyển đổi]: cũng được biết tới như: serialization, parsing, marshalling
  *[Dependency Injection]: cũng được biết đến như components, resources, providers, services, injectables
  *["parsing"]: converting the string that comes from an HTTP request into Python data
