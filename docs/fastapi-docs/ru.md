Перейти к содержанию 
# FastAPI¶
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_Готовый к внедрению высокопроизводительный фреймворк, простой в изучении и разработке._
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master) ![Coverage](https://img.shields.io/codecov/c/github/fastapi/fastapi?color=%2334D058) ![Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package) ![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
**Документация** : https://fastapi.tiangolo.com
**Исходный код** : https://github.com/fastapi/fastapi
FastAPI — это современный, быстрый (высокопроизводительный) веб-фреймворк для создания API используя Python, в основе которого лежит стандартная аннотация типов Python.
Ключевые особенности:
  * **Скорость** : Очень высокая производительность, на уровне **NodeJS** и **Go** (благодаря Starlette и Pydantic). Один из самых быстрых фреймворков Python.
  * **Быстрота разработки** : Увеличьте скорость разработки примерно на 200–300%. *
  * **Меньше ошибок** : Сократите примерно на 40% количество ошибок, вызванных человеком (разработчиком). *
  * **Интуитивно понятный** : Отличная поддержка редактора. Автозавершение везде. Меньше времени на отладку.
  * **Лёгкость** : Разработан так, чтобы его было легко использовать и осваивать. Меньше времени на чтение документации.
  * **Краткость** : Сведите к минимуму дублирование кода. Каждый объявленный параметр - определяет несколько функций. Меньше ошибок.
  * **Надежность** : Получите готовый к работе код. С автоматической интерактивной документацией.
  * **На основе стандартов** : Основан на открытых стандартах API и полностью совместим с ними: OpenAPI (ранее известном как Swagger) и JSON Schema.


* оценка на основе тестов внутренней команды разработчиков, создающих производственные приложения.
## Спонсоры¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Другие спонсоры
## Отзывы¶
"_В последнее время я много где использую**FastAPI**. [...] На самом деле я планирую использовать его для всех **сервисов машинного обучения моей команды в Microsoft**. Некоторые из них интегрируются в основной продукт **Windows** , а некоторые — в продукты **Office**._"
Kabir Khan - **Microsoft** (ref)
"_Мы использовали библиотеку**FastAPI** для создания сервера **REST** , к которому можно делать запросы для получения **прогнозов**. [для Ludwig]_"
Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber** (ref)
"_**Netflix** рада объявить о выпуске опенсорсного фреймворка для оркестровки **антикризисного управления** : **Dispatch**! [создана с помощью **FastAPI**]_"
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** (ref)
"_Я в полном восторге от**FastAPI**. Это так весело!_"
Brian Okken - **Python Bytes podcast host** (ref)
"_Честно говоря, то, что вы создали, выглядит очень солидно и отполировано. Во многих смыслах я хотел, чтобы**Hug** был именно таким — это действительно вдохновляет, когда кто-то создаёт такое._"
Timothy Crosley - **Hug creator** (ref)
"_Если вы хотите изучить какой-нибудь**современный фреймворк** для создания REST API, ознакомьтесь с **FastAPI** [...] Он быстрый, лёгкий и простой в изучении [...]_"
"_Мы перешли на**FastAPI** для наших **API** [...] Я думаю, вам тоже понравится [...]_"
Ines Montani - Matthew Honnibal - **Explosion AI founders - spaCy creators** (ref) - (ref)
## **Typer** , интерфейс командной строки для FastAPI¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
Если вы создаете приложение CLI для использования в терминале вместо веб-API, ознакомьтесь с **Typer**.
**Typer** — младший брат FastAPI. И он предназначен для использования в качестве **интерфейса командной строки для FastAPI**. ⌨️ 🚀
## Зависимости¶
FastAPI стоит на плечах гигантов:
  * Starlette для части связанной с вебом.
  * Pydantic для части связанной с данными.


## Установка¶
```

fast →pip install fastapirestart ↻

```

Вам также понадобится сервер ASGI для производства, такой как Uvicorn или Hypercorn.
```

fast →pip install "uvicorn[standard]"restart ↻

```

## Пример¶
### Создание¶
  * Создайте файл `main.py` со следующим содержимым:


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

Или используйте `async def`...
Если ваш код использует `async` / `await`, используйте `async def`:
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

**Примечание** :
Если вы не знаете, проверьте раздел _"Торопитесь?"_ в документации об `async` и `await`.
### Запуск¶
Запустите сервер с помощью:
```

fast →uvicorn main:app --reloadINFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [28720]INFO:   Started server process [28722]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

О команде `uvicorn main:app --reload`...
Команда `uvicorn main:app` относится к:
  * `main`: файл `main.py` (модуль Python).
  * `app`: объект, созданный внутри `main.py` с помощью строки `app = FastAPI()`.
  * `--reload`: перезапуск сервера после изменения кода. Делайте это только во время разработки.


### Проверка¶
Откройте браузер на http://127.0.0.1:8000/items/5?q=somequery.
Вы увидите следующий JSON ответ:
```
{"item_id":5,"q":"somequery"}

```

Вы уже создали API, который:
  * Получает HTTP-запросы по _путям_ `/` и `/items/{item_id}`.
  * И первый и второй _путь_ используют `GET` _операции_ (также известные как HTTP _методы_).
  * _путь_ `/items/{item_id}` имеет _параметр пути_ `item_id`, который должен быть `int`.
  * _путь_ `/items/{item_id}` имеет необязательный `str` _параметр запроса_ `q`.


### Интерактивная документация по API¶
Перейдите на http://127.0.0.1:8000/docs.
Вы увидите автоматическую интерактивную документацию API (предоставленную Swagger UI):
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Альтернативная документация по API¶
А теперь перейдите на http://127.0.0.1:8000/redoc.
Вы увидите альтернативную автоматическую документацию (предоставленную ReDoc):
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Пример обновления¶
Теперь измените файл `main.py`, чтобы получить тело ответа из `PUT` запроса.
Объявите тело, используя стандартную типизацию Python, спасибо Pydantic.
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

Сервер должен перезагрузиться автоматически (потому что вы добавили `--reload` к команде `uvicorn` выше).
### Интерактивное обновление документации API¶
Перейдите на http://127.0.0.1:8000/docs.
  * Интерактивная документация API будет автоматически обновляться, включая новое тело:


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * Нажмите на кнопку "Try it out", это позволит вам заполнить параметры и напрямую взаимодействовать с API:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Затем нажмите кнопку "Execute", пользовательский интерфейс свяжется с вашим API, отправит параметры, получит результаты и отобразит их на экране:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Альтернативное обновление документации API¶
А теперь перейдите на http://127.0.0.1:8000/redoc.
  * Альтернативная документация также будет отражать новый параметр и тело запроса:


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### Подведём итоги¶
Таким образом, вы объявляете **один раз** типы параметров, тело и т. д. в качестве параметров функции.
Вы делаете это используя стандартную современную типизацию Python.
Вам не нужно изучать новый синтаксис, методы или классы конкретной библиотеки и т. д.
Только стандартный **Python**.
Например, для `int`:
```
item_id: int

```

или для более сложной модели `Item`:
```
item: Item

```

... и с этим единственным объявлением вы получаете:
  * Поддержка редактора, в том числе:
    * Автозавершение.
    * Проверка типов.
  * Валидация данных:
    * Автоматические и четкие ошибки, когда данные недействительны.
    * Проверка даже для глубоко вложенных объектов JSON.
  * Преобразование входных данных: поступающие из сети в объекты Python с соблюдением типов. Чтение из:
    * JSON.
    * Параметров пути.
    * Параметров запроса.
    * Cookies.
    * Заголовков.
    * Форм.
    * Файлов.
  * Преобразование выходных данных: преобразование объектов Python в данные передаваемые по сети интернет (такие как JSON):
    * Преобразование типов Python (`str`, `int`, `float`, `bool`, `list`, и т.д.).
    * Объекты `datetime`.
    * Объекты `UUID`.
    * Модели баз данных.
    * ...и многое другое.
  * Автоматическая интерактивная документация по API, включая 2 альтернативных пользовательских интерфейса:
    * Swagger UI.
    * ReDoc.


Возвращаясь к предыдущему примеру кода, **FastAPI** будет:
  * Проверять наличие `item_id` в пути для запросов `GET` и `PUT`.
  * Проверять, что `item_id` имеет тип `int` для запросов `GET` и `PUT`.
    * Если это не так, клиент увидит полезную чёткую ошибку.
  * Проверять, есть ли необязательный параметр запроса с именем `q` (например, `http://127.0.0.1:8000/items/foo?q=somequery`) для `GET` запросов.
    * Поскольку параметр `q` объявлен с `= None`, он является необязательным.
    * Без `None` он был бы необходим (как тело в случае с `PUT`).
  * Для `PUT` запросов к `/items/{item_id}` читать тело как JSON:
    * Проверять, что у него есть обязательный атрибут `name`, который должен быть `str`.
    * Проверять, что у него есть обязательный атрибут `price`, который должен быть `float`.
    * Проверять, что у него есть необязательный атрибут `is_offer`, который должен быть `bool`, если он присутствует.
    * Все это также будет работать для глубоко вложенных объектов JSON.
  * Преобразовывать из и в JSON автоматически.
  * Документировать с помощью OpenAPI все, что может быть использовано:
    * Системы интерактивной документации.
    * Системы автоматической генерации клиентского кода для многих языков.
  * Обеспечит 2 интерактивных веб-интерфейса документации напрямую.


Мы только немного копнули поверхность, но вы уже поняли, как все это работает.
Попробуйте изменить строку с помощью:
```
  return {"item_name": item.name, "item_id": item_id}

```

...из:
```
    ... "item_name": item.name ...

```

...в:
```
    ... "item_price": item.price ...

```

... и посмотрите, как ваш редактор будет автоматически заполнять атрибуты и узнавать их типы:
![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)
Более полный пример с дополнительными функциями см. в Учебное руководство - Руководство пользователя.
**Осторожно, спойлер** : руководство пользователя включает в себя:
  * Объявление **параметров** из других мест, таких как: **заголовки** , **cookies** , **поля формы** и **файлы**.
  * Как установить **ограничительные проверки** такие как `maximum_length` или `regex`.
  * Очень мощная и простая в использовании система **внедрения зависимостей**.
  * Безопасность и аутентификация, включая поддержку **OAuth2** с **токенами JWT** и **HTTP Basic** аутентификацию.
  * Более продвинутые (но столь же простые) методы объявления **глубоко вложенных моделей JSON** (спасибо Pydantic).
  * **GraphQL** интеграция с Strawberry и другими библиотеками.
  * Множество дополнительных функций (благодаря Starlette), таких как:
    * **Веб-сокеты**
    * очень простые тесты на основе HTTPX и `pytest`
    * **CORS**
    * **Cookie сеансы(сессии)**
    * ...и многое другое.


## Производительность¶
Независимые тесты TechEmpower показывают приложения **FastAPI** , работающие под управлением Uvicorn, как один из самых быстрых доступных фреймворков Python, уступающий только самим Starlette и Uvicorn (используемых внутри FastAPI). (*)
Чтобы узнать больше об этом, см. раздел Тесты производительности.
## Необязательные зависимости¶
Используется Pydantic:
  * `email-validator` - для проверки электронной почты.


Используется Starlette:
  * `HTTPX` - Обязательно, если вы хотите использовать `TestClient`.
  * `jinja2` - Обязательно, если вы хотите использовать конфигурацию шаблона по умолчанию.
  * `python-multipart` - Обязательно, если вы хотите поддерживать форму "парсинга" с помощью `request.form()`.
  * `itsdangerous` - Обязательно, для поддержки `SessionMiddleware`.
  * `pyyaml` - Обязательно, для поддержки `SchemaGenerator` Starlette (возможно, вам это не нужно с FastAPI).


Используется FastAPI / Starlette:
  * `uvicorn` - сервер, который загружает и обслуживает ваше приложение.
  * `orjson` - Обязательно, если вы хотите использовать `ORJSONResponse`.
  * `ujson` - Обязательно, если вы хотите использовать `UJSONResponse`.


Вы можете установить все это с помощью `pip install "fastapi[all]"`.
## Лицензия¶
Этот проект распространяется на условиях лицензии MIT.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
К началу 
  *[Автозавершение]: также известное как автозаполнение, автодополнение, IntelliSense
  *[CLI]: Интерфейс командной строки
  *[Преобразование]: также известный как: сериализация, синтаксический анализ, маршалинг
  *[внедрения зависимостей]: также известная как компоненты, ресурсы, провайдеры, сервисы, инъекции
  *["парсинга"]: преобразование строки, полученной из HTTP-запроса, в данные Python
