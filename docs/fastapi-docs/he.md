לדלג לתוכן 
# FastAPI¶
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_תשתית FastAPI, ביצועים גבוהים, קלה ללמידה, מהירה לתכנות, מוכנה לסביבת ייצור_
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master) ![Coverage](https://img.shields.io/codecov/c/github/fastapi/fastapi?color=%2334D058) ![Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package) ![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
**תיעוד** : https://fastapi.tiangolo.com
**קוד** : https://github.com/fastapi/fastapi
FastAPI היא תשתית רשת מודרנית ומהירה (ביצועים גבוהים) לבניית ממשקי תכנות יישומים (API) עם פייתון 3.6+ בהתבסס על רמזי טיפוסים סטנדרטיים.
תכונות המפתח הן:
  * **מהירה** : ביצועים גבוהים מאוד, בקנה אחד עם NodeJS ו - Go (תודות ל - Starlette ו - Pydantic). אחת מתשתיות הפייתון המהירות ביותר.
  * **מהירה לתכנות** : הגבירו את מהירות פיתוח התכונות החדשות בכ - %200 עד %300. *
  * **פחות שגיאות** : מנעו כ - %40 משגיאות אנוש (מפתחים). *
  * **אינטואיטיבית** : תמיכת עורך מעולה. השלמה בכל מקום. פחות זמן ניפוי שגיאות.
  * **קלה** : מתוכננת להיות קלה לשימוש וללמידה. פחות זמן קריאת תיעוד.
  * **קצרה** : מזערו שכפול קוד. מספר תכונות מכל הכרזת פרמטר. פחות שגיאות.
  * **חסונה** : קבלו קוד מוכן לסביבת ייצור. עם תיעוד אינטרקטיבי אוטומטי.
  * **מבוססת סטנדרטים** : מבוססת על (ותואמת לחלוטין ל -) הסטדנרטים הפתוחים לממשקי תכנות יישומים: OpenAPI (ידועים לשעבר כ - Swagger) ו - JSON Schema.


* הערכה מבוססת על בדיקות של צוות פיתוח פנימי שבונה אפליקציות בסביבת ייצור.
## נותני חסות¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
נותני חסות אחרים
## דעות¶
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
## **Typer** , ה - FastAPI של ממשקי שורת פקודה (CLI).¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
אם אתם בונים אפליקציית CLI לשימוש במסוף במקום ממשק רשת, העיפו מבט על **Typer**.
**Typer** היא אחותה הקטנה של FastAPI. ומטרתה היא להיות ה - **FastAPI של ממשקי שורת פקודה**. ⌨️ 🚀
## תלויות¶
פייתון 3.6+
FastAPI עומדת על כתפי ענקיות:
  * Starlette לחלקי הרשת.
  * Pydantic לחלקי המידע.


## התקנה¶
```

fast →pip install fastapirestart ↻

```

תצטרכו גם שרת ASGI כגון Uvicorn או Hypercorn.
```

fast →pip install "uvicorn[standard]"restart ↻

```

## דוגמא¶
### צרו אותה¶
  * צרו קובץ בשם `main.py` עם:


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

או השתמשו ב - `async def`...
אם הקוד שלכם משתמש ב - `async` / `await`, השתמשו ב - `async def`:
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

**שימו לב** :
אם אינכם יודעים, בדקו את פרק "ממהרים?" על `async` ו - `await` בתיעוד.
### הריצו אותה¶
התחילו את השרת עם:
```

fast →uvicorn main:app --reloadINFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [28720]INFO:   Started server process [28722]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

על הפקודה `uvicorn main:app --reload`...
הפקודה `uvicorn main:app` מתייחסת ל:
  * `main`: הקובץ `main.py` (מודול פייתון).
  * `app`: האובייקט שנוצר בתוך `main.py` עם השורה `app = FastAPI()`.
  * `--reload`: גרמו לשרת להתאתחל לאחר שינויים בקוד. עשו זאת רק בסביבת פיתוח.


### בדקו אותה¶
פתחו את הדפדפן שלכם בכתובת http://127.0.0.1:8000/items/5?q=somequery.
אתם תראו תגובת JSON:
```
{"item_id":5,"q":"somequery"}

```

כבר יצרתם API ש:
  * מקבל בקשות HTTP בנתיבים `/` ו - `/items/{item_id}`.
  * שני ה _נתיבים_ מקבלים _בקשות_ `GET` (ידועות גם כ _מתודות_ HTTP).
  * ה _נתיב_ `/items/{item_id}` כולל *פרמטר נתיב_ `item_id` שאמור להיות `int`.
  * ה _נתיב_ `/items/{item_id}` *פרמטר שאילתא_ אופציונלי `q`.


### תיעוד API אינטרקטיבי¶
כעת פנו לכתובת http://127.0.0.1:8000/docs.
אתם תראו את התיעוד האוטומטי (מסופק על ידי Swagger UI):
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### תיעוד אלטרנטיבי¶
כעת פנו לכתובת http://127.0.0.1:8000/redoc.
אתם תראו תיעוד אלטרנטיבי (מסופק על ידי ReDoc):
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## שדרוג לדוגמא¶
כעת ערכו את הקובץ `main.py` כך שיוכל לקבל גוף מבקשת `PUT`.
הגדירו את הגוף בעזרת רמזי טיפוסים סטנדרטיים, הודות ל - `Pydantic`.
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

השרת אמול להתאתחל אוטומטית (מאחר והוספתם `--reload` לפקודת `uvicorn` שלמעלה).
### שדרוג התיעוד האינטרקטיבי¶
כעת פנו לכתובת http://127.0.0.1:8000/docs.
  * התיעוד האוטומטי יתעדכן, כולל הגוף החדש:


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * לחצו על הכפתור "Try it out", הוא יאפשר לכם למלא את הפרמטרים ולעבוד ישירות מול ה - API.


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * אחר כך לחצו על הכפתור "Execute", האתר יתקשר עם ה - API שלכם, ישלח את הפרמטרים, ישיג את התוצאות ואז יראה אותן על המסך:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### שדרוג התיעוד האלטרנטיבי¶
כעת פנו לכתובת http://127.0.0.1:8000/redoc.
  * התיעוד האלטרנטיבי גם יראה את פרמטר השאילתא והגוף החדשים.


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### סיכום¶
לסיכום, אתם מכריזים ** פעם אחת** על טיפוסי הפרמטרים, גוף וכו' כפרמטרים לפונקציה.
אתם עושים את זה עם טיפוסי פייתון מודרניים.
אתם לא צריכים ללמוד תחביר חדש, מתודות או מחלקות של ספרייה ספיציפית, וכו'
רק **פייתון 3.6+** סטנדרטי.
לדוגמא, ל - `int`:
```
item_id: int

```

או למודל `Item` מורכב יותר:
```
item: Item

```

...ועם הכרזת הטיפוס האחת הזו אתם מקבלים:
  * תמיכת עורך, כולל:
    * השלמות.
    * בדיקת טיפוסים.
  * אימות מידע:
    * שגיאות ברורות ואטומטיות כאשר מוכנס מידע לא חוקי .
    * אימות אפילו לאובייקטי JSON מקוננים.
  * המרה של מידע קלט: המרה של מידע שמגיע מהרשת למידע וטיפוסים של פייתון. קורא מ:
    * JSON.
    * פרמטרי נתיב.
    * פרמטרי שאילתא.
    * עוגיות.
    * כותרות.
    * טפסים.
    * קבצים.
  * המרה של מידע פלט: המרה של מידע וטיפוסים מפייתון למידע רשת (כ - JSON):
    * המירו טיפוסי פייתון (`str`, `int`, `float`, `bool`, `list`, etc).
    * עצמי `datetime`.
    * עצמי `UUID`.
    * מודלי בסיסי נתונים.
    * ...ורבים אחרים.
  * תיעוד API אוטומטי ואינטרקטיבית כולל שתי אלטרנטיבות לממשק המשתמש:
    * Swagger UI.
    * ReDoc.


בחזרה לדוגמאת הקוד הקודמת, **FastAPI** ידאג:
  * לאמת שיש `item_id` בנתיב בבקשות `GET` ו - `PUT`.
  * לאמת שה - `item_id` הוא מטיפוס `int` בבקשות `GET` ו - `PUT`.
    * אם הוא לא, הלקוח יראה שגיאה ברורה ושימושית.
  * לבדוק האם קיים פרמטר שאילתא בשם `q` (קרי `http://127.0.0.1:8000/items/foo?q=somequery`) לבקשות `GET`.
    * מאחר והפרמטר `q` מוגדר עם ` = None`, הוא אופציונלי.
    * לולא ה - `None` הוא היה חובה (כמו הגוף במקרה של `PUT`).
  * לבקשות `PUT` לנתיב `/items/{item_id}`, לקרוא את גוף הבקשה כ - JSON:
    * לאמת שהוא כולל את מאפיין החובה `name` שאמור להיות מטיפוס `str`.
    * לאמת שהוא כולל את מאפיין החובה `price` שחייב להיות מטיפוס `float`.
    * לבדוק האם הוא כולל את מאפיין הרשות `is_offer` שאמור להיות מטיפוס `bool`, אם הוא נמצא.
    * כל זה יעבוד גם לאובייקט JSON מקונן.
  * להמיר מ - JSON ול- JSON אוטומטית.
  * לתעד הכל באמצעות OpenAPI, תיעוד שבו יוכלו להשתמש:
    * מערכות תיעוד אינטרקטיביות.
    * מערכות ייצור קוד אוטומטיות, להרבה שפות.
  * לספק ישירות שתי מערכות תיעוד רשתיות.


רק גרדנו את קצה הקרחון, אבל כבר יש לכם רעיון של איך הכל עובד.
נסו לשנות את השורה:
```
  return {"item_name": item.name, "item_id": item_id}

```

...מ:
```
    ... "item_name": item.name ...

```

...ל:
```
    ... "item_price": item.price ...

```

...וראו איך העורך שלכם משלים את המאפיינים ויודע את הטיפוסים שלהם:
![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)
לדוגמא יותר שלמה שכוללת עוד תכונות, ראו את המדריך - למשתמש.
**התראת ספוילרים** : המדריך - למשתמש כולל:
  * הכרזה על **פרמטרים** ממקורות אחרים ושונים כגון: **כותרות** , **עוגיות** , **טפסים** ו - **קבצים**.
  * איך לקבוע **מגבלות אימות** בעזרת `maximum_length` או `regex`.
  * דרך חזקה וקלה להשתמש ב**הזרקת תלויות**.
  * אבטחה והתאמתות, כולל תמיכה ב - **OAuth2** עם **JWT** והתאמתות **HTTP Basic**.
  * טכניקות מתקדמות (אבל קלות באותה מידה) להכרזת אובייקטי JSON מקוננים (תודות ל - Pydantic).
  * אינטרקציה עם **GraphQL** דרך Strawberry וספריות אחרות.
  * תכונות נוספות רבות (תודות ל - Starlette) כגון:
    * **WebSockets**
    * בדיקות קלות במיוחד מבוססות על `requests` ו - `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...ועוד.


## ביצועים¶
בדיקות עצמאיות של TechEmpower הראו שאפליקציות **FastAPI** שרצות תחת Uvicorn הן מתשתיות הפייתון המהירות ביותר, רק מתחת ל - Starlette ו - Uvicorn עצמן (ש - FastAPI מבוססת עליהן). (*)
כדי להבין עוד על הנושא, ראו את הפרק Benchmarks.
## תלויות אופציונליות¶
בשימוש Pydantic:
  * `email-validator` - לאימות כתובות אימייל.


בשימוש Starlette:
  * `httpx` - דרוש אם ברצונכם להשתמש ב - `TestClient`.
  * `jinja2` - דרוש אם ברצונכם להשתמש בברירת המחדל של תצורת הטמפלייטים.
  * `python-multipart` - דרוש אם ברצונכם לתמוך ב "פרסור" טפסים, באצמעות `request.form()`.
  * `itsdangerous` - דרוש אם ברצונכם להשתמש ב - `SessionMiddleware`.
  * `pyyaml` - דרוש אם ברצונכם להשתמש ב - `SchemaGenerator` של Starlette (כנראה שאתם לא צריכים את זה עם FastAPI).


בשימוש FastAPI / Starlette:
  * `uvicorn` - לשרת שטוען ומגיש את האפליקציה שלכם.
  * `orjson` - דרוש אם ברצונכם להשתמש ב - `ORJSONResponse`.
  * `ujson` - דרוש אם ברצונכם להשתמש ב - `UJSONResponse`.


תוכלו להתקין את כל אלו באמצעות `pip install "fastapi[all]"`.
## רשיון¶
הפרויקט הזה הוא תחת התנאים של רשיון MIT.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
חזרה למעלה 
  *[השלמה]: ידועה גם כהשלמה אוטומטית או IntelliSense
  *[CLI]: ממשק שורת פקודה
  *[המרה]: ידועה גם כ: פרסור, סיריאליזציה
  *[הזרקת תלויות]: ידועה גם כרכיבים, משאבים, ספקים, שירותים, מוזרקים
  *["פרסור"]: המרת המחרוזת שמגיעה מבקשת HTTP למידע פייתון
