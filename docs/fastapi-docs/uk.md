Перейти до змісту 
# FastAPI
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_Готовий до продакшину, високопродуктивний, простий у вивченні та швидкий для написання коду фреймворк_
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master) ![Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ![Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package) ![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
**Документація** : https://fastapi.tiangolo.com
**Програмний код** : https://github.com/fastapi/fastapi
FastAPI - це сучасний, швидкий (високопродуктивний), вебфреймворк для створення API за допомогою Python,в основі якого лежить стандартна анотація типів Python.
Ключові особливості:
  * **Швидкий** : Дуже висока продуктивність, на рівні з **NodeJS** та **Go** (завдяки Starlette та Pydantic). Один із найшвидших фреймворків.
  * **Швидке написання коду** : Пришвидшує розробку функціоналу приблизно на 200%-300%. *
  * **Менше помилок** : Зменшить кількість помилок спричинених людиною (розробником) на 40%. *
  * **Інтуїтивний** : Чудова підтримка редакторами коду. Доповнення всюди. Зменште час на налагодження.
  * **Простий** : Спроектований, для легкого використання та навчання. Знадобиться менше часу на читання документації.
  * **Короткий** : Зведе до мінімуму дублювання коду. Кожен оголошений параметр може виконувати кілька функцій.
  * **Надійний** : Ви матимете стабільний код готовий до продакшину з автоматичною інтерактивною документацією.
  * **Стандартизований** : Оснований та повністю сумісний з відкритими стандартами для API: OpenAPI (попередньо відомий як Swagger) та JSON Schema.


* оцінка на основі тестів внутрішньої команди розробників, створення продуктових застосунків.
## Спонсори¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Other sponsors
## Враження¶
"_[...] I'm using**FastAPI** a ton these days. [...] I'm actually planning to use it for all of my team's **ML services at Microsoft**. Some of them are getting integrated into the core **Windows** product and some **Office** products._"
Kabir Khan - **Microsoft** (ref)
"_We adopted the**FastAPI** library to spawn a **REST** server that can be queried to obtain **predictions**. [for Ludwig]_"
Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber** (ref)
"_**Netflix** is pleased to announce the open-source release of our **crisis management** orchestration framework: **Dispatch**! [built with **FastAPI**]_"
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** (ref)
"_I’m over the moon excited about**FastAPI**. It’s so fun!_"
Brian Okken - **Python Bytes podcast host** (ref)
"_Honestly, what you've built looks super solid and polished. In many ways, it's what I wanted**Hug** to be - it's really inspiring to see someone build that._"
Timothy Crosley - **Hug creator** (ref)
"_If you're looking to learn one**modern framework** for building REST APIs, check out **FastAPI** [...] It's fast, easy to use and easy to learn [...]_"
"_We've switched over to**FastAPI** for our **APIs** [...] I think you'll like it [...]_"
Ines Montani - Matthew Honnibal - **Explosion AI founders - spaCy creators** (ref) - (ref)
## **Typer** , FastAPI CLI¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
Створюючи CLI застосунок для використання в терміналі, замість веб-API зверніть увагу на **Typer**.
**Typer** є молодшим братом FastAPI. І це **FastAPI для CLI**. ⌨️ 🚀
## Вимоги¶
FastAPI стоїть на плечах гігантів:
  * Starlette для web частини.
  * Pydantic для частини даних.


## Вставновлення¶
```

fast →pip install fastapirestart ↻

```

Вам також знадобиться сервер ASGI для продакшину, наприклад Uvicorn або Hypercorn.
```

fast →pip install uvicorn[standard]restart ↻

```

## Приклад¶
### Створіть¶
  * Створіть файл `main.py` з:


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

Або використайте `async def`...
Якщо ваш код використовує `async` / `await`, скористайтеся `async def`:
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

**Примітка** :
Стикнувшись з проблемами, не зайвим буде ознайомитися з розділом _"In a hurry?"_ про `async` та `await` у документації.
### Запустіть¶
Запустіть server з:
```

fast →uvicorn main:app --reloadINFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [28720]INFO:   Started server process [28722]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

Про команди `uvicorn main:app --reload`...
Команда `uvicorn main:app` посилається на:
  * `main`: файл `main.py` ("Модуль" Python).
  * `app`: об’єкт створений усередині `main.py` рядком `app = FastAPI()`.
  * `--reload`: перезапускає сервер після зміни коду. Використовуйте виключно для розробки.


### Перевірте¶
Відкрийте браузер та введіть адресу http://127.0.0.1:8000/items/5?q=somequery.
Ви побачите у відповідь подібний JSON:
```
{"item_id":5,"q":"somequery"}

```

Ви вже створили API, який:
  * Отримує HTTP запити за _шляхами_ `/` та `/items/{item_id}`.
  * Обидва _шляхи_ приймають `GET` _операції_ (також відомі як HTTP _методи_).
  * _Шлях_ `/items/{item_id}` містить _параметр шляху_ `item_id` який має бути типу `int`.
  * _Шлях_ `/items/{item_id}` містить необовʼязковий `str` _параметр запиту_ `q`.


### Інтерактивні документації API¶
Перейдемо сюди http://127.0.0.1:8000/docs.
Ви побачите автоматичну інтерактивну API документацію (створену завдяки Swagger UI):
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Альтернативні документації API¶
Тепер перейдемо сюди http://127.0.0.1:8000/redoc.
Ви побачите альтернативну автоматичну документацію (створену завдяки ReDoc):
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Приклад оновлення¶
Тепер модифікуйте файл `main.py`, щоб отримати вміст запиту `PUT`.
Оголошуйте вміст запиту за допомогою стандартних типів Python завдяки Pydantic.
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

Сервер повинен автоматично перезавантажуватися (тому що Ви додали `--reload` до `uvicorn` команди вище).
### Оновлення інтерактивної API документації¶
Тепер перейдемо сюди http://127.0.0.1:8000/docs.
  * Інтерактивна документація API буде автоматично оновлена, включаючи новий вміст:


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * Натисніть кнопку "Try it out", це дозволить вам заповнити параметри та безпосередньо взаємодіяти з API:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Потім натисніть кнопку "Execute", інтерфейс користувача зв'яжеться з вашим API, надішле параметри, у відповідь отримає результати та покаже їх на екрані:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Оновлення альтернативної API документації¶
Зараз перейдемо http://127.0.0.1:8000/redoc.
  * Альтернативна документація також показуватиме новий параметр і вміст запиту:


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### Підсумки¶
Таким чином, Ви **один раз** оголошуєте типи параметрів, тіла тощо, як параметри функції.
Ви робите це за допомогою стандартних сучасних типів Python.
Вам не потрібно вивчати новий синтаксис, методи чи класи конкретної бібліотеки тощо.
Використовуючи стандартний **Python**.
Наприклад, для `int`:
```
item_id: int

```

або для більш складної моделі `Item`:
```
item: Item

```

...і з цим єдиним оголошенням Ви отримуєте:
  * Підтримку редактора, включаючи:
    * Варіанти заповнення.
    * Перевірку типів.
  * Перевірку даних:
    * Автоматичні та зрозумілі помилки, у разі некоректних даних.
    * Перевірка навіть для JSON з високим рівнем вкладеності.
  * Перетворення вхідних даних: з мережі до даних і типів Python. Читання з:
    * JSON.
    * Параметрів шляху.
    * Параметрів запиту.
    * Cookies.
    * Headers.
    * Forms.
    * Файлів.
  * Перетворення вихідних даних: з типів і даних Python до мережевих даних (як JSON):
    * Конвертація Python типів (`str`, `int`, `float`, `bool`, `list`, тощо).
    * `datetime` об'єкти.
    * `UUID` об'єкти.
    * Моделі бази даних.
    * ...та багато іншого.
  * Автоматичну інтерактивну документацію API, включаючи 2 альтернативні інтерфейси користувача:
    * Swagger UI.
    * ReDoc.


Повертаючись до попереднього прикладу коду, **FastAPI** :
  * Підтвердить наявність `item_id` у шляху для запитів `GET` та `PUT`.
  * Підтвердить, що `item_id` має тип `int` для запитів `GET` and `PUT`.
    * Якщо це не так, клієнт побачить корисну, зрозумілу помилку.
  * Перевірить, чи є необов'язковий параметр запиту з назвою `q` (а саме `http://127.0.0.1:8000/items/foo?q=somequery`) для запитів `GET`.
    * Оскільки параметр `q` оголошено як `= None`, він необов'язковий.
    * За відсутності `None` він був би обов'язковим (як і вміст у випадку з `PUT`).
  * Для запитів `PUT` із `/items/{item_id}`, читає вміст як JSON:
    * Перевірить, чи має обов'язковий атрибут `name` тип `str`.
    * Перевірить, чи має обов'язковий атрибут `price` тип `float`.
    * Перевірить, чи існує необов'язковий атрибут `is_offer` та чи має він тип `bool`.
    * Усе це також працюватиме для глибоко вкладених об'єктів JSON.
  * Автоматично конвертує із та в JSON.
  * Документує все за допомогою OpenAPI, який може бути використано в:
    * Інтерактивних системах документації.
    * Системах автоматичної генерації клієнтського коду для багатьох мов.
  * Надає безпосередньо 2 вебінтерфейси інтерактивної документації.


Ми лише трішки доторкнулися до коду, але Ви вже маєте уявлення про те, як все працює.
Спробуйте змінити рядок:
```
  return {"item_name": item.name, "item_id": item_id}

```

...із:
```
    ... "item_name": item.name ...

```

...на:
```
    ... "item_price": item.price ...

```

...і побачите, як ваш редактор автоматично заповнюватиме атрибути та знатиме їхні типи:
![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)
Для більш повного ознайомлення з додатковими функціями, перегляньте Туторіал - Посібник Користувача.
**Spoiler alert** : туторіал - посібник користувача містить:
  * Оголошення **параметрів** з інших місць як: **headers** , **cookies** , **form fields** та **files**.
  * Як встановити **перевірку обмежень** як `maximum_length` або `regex`.
  * Дуже потужна і проста у використанні система **Ін'єкція Залежностей**.
  * Безпека та автентифікація, включаючи підтримку **OAuth2** з **JWT tokens** та **HTTP Basic** автентифікацію.
  * Досконаліші (але однаково прості) техніки для оголошення **глибоко вкладених моделей JSON** (завдяки Pydantic).
  * Багато додаткових функцій (завдяки Starlette) як-от:
    * **WebSockets**
    * надзвичайно прості тести на основі HTTPX та `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...та більше.


## Продуктивність¶
Незалежні тести TechEmpower показують що застосунки **FastAPI** , які працюють під керуванням Uvicorn є одними з найшвидших серед доступних фреймворків в Python, поступаючись лише Starlette та Uvicorn (які внутрішньо використовуються в FastAPI). (*)
Щоб дізнатися більше про це, перегляньте розділ Benchmarks.
## Необов'язкові залежності¶
Pydantic використовує:
  * `email-validator` - для валідації електронної пошти.
  * `pydantic-settings` - для управління налаштуваннями.
  * `pydantic-extra-types` - для додаткових типів, що можуть бути використані з Pydantic.


Starlette використовує:
  * `httpx` - Необхідно, якщо Ви хочете використовувати `TestClient`.
  * `jinja2` - Необхідно, якщо Ви хочете використовувати шаблони як конфігурацію за замовчуванням.
  * `python-multipart` - Необхідно, якщо Ви хочете підтримувати "розбір" форми за допомогою `request.form()`.
  * `itsdangerous` - Необхідно для підтримки `SessionMiddleware`.
  * `pyyaml` - Необхідно для підтримки Starlette `SchemaGenerator` (ймовірно, вам це не потрібно з FastAPI).


FastAPI / Starlette використовують:
  * `uvicorn` - для сервера, який завантажує та обслуговує вашу програму.
  * `orjson` - Необхідно, якщо Ви хочете використовувати `ORJSONResponse`.
  * `ujson` - Необхідно, якщо Ви хочете використовувати `UJSONResponse`.


Ви можете встановити все це за допомогою `pip install fastapi[all]`.
## Ліцензія¶
Цей проєкт ліцензовано згідно з умовами ліцензії MIT.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Повернутись нагору 
  *[Доповнення]: Також відоме як auto-complete, autocompletion, IntelliSense.
  *[CLI]: Command Line Interface
  *[Перетворення]: також відомий як: serialization, parsing, marshalling
  *[Ін'єкція Залежностей]: також відома як: components, resources, providers, services, injectables
  *["розбір"]: перетворення рядка, який надходить із запиту HTTP, на дані Python
