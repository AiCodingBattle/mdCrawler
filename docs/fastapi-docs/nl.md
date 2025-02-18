Ga naar inhoud 
# FastAPI¶
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_FastAPI framework, zeer goede prestaties, eenvoudig te leren, snel te programmeren, klaar voor productie_
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master) ![Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ![Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package) ![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
**Documentatie** : https://fastapi.tiangolo.com
**Broncode** : https://github.com/tiangolo/fastapi
FastAPI is een modern, snel (zeer goede prestaties), web framework voor het bouwen van API's in Python, gebruikmakend van standaard Python type-hints.
De belangrijkste kenmerken zijn:
  * **Snel** : Zeer goede prestaties, vergelijkbaar met **NodeJS** en **Go** (dankzij Starlette en Pydantic). Een van de snelste beschikbare Python frameworks.
  * **Snel te programmeren** : Verhoog de snelheid om functionaliteit te ontwikkelen met ongeveer 200% tot 300%. *
  * **Minder bugs** : Verminder ongeveer 40% van de door mensen (ontwikkelaars) veroorzaakte fouten. *
  * **Intuïtief** : Buitengewoon goede ondersteuning voor editors. Overal automische code aanvulling. Minder tijd kwijt aan debuggen.
  * **Eenvoudig** : Ontworpen om gemakkelijk te gebruiken en te leren. Minder tijd nodig om documentatie te lezen.
  * **Kort** : Minimaliseer codeduplicatie. Elke parameterdeclaratie ondersteunt meerdere functionaliteiten. Minder bugs.
  * **Robust** : Code gereed voor productie. Met automatische interactieve documentatie.
  * **Standards-based** : Gebaseerd op (en volledig verenigbaar met) open standaarden voor API's: OpenAPI (voorheen bekend als Swagger) en JSON Schema.


* schatting op basis van testen met een intern ontwikkelteam en bouwen van productieapplicaties.
## Sponsors¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Overige sponsoren
## Meningen¶
"_[...] Ik gebruik**FastAPI** heel vaak tegenwoordig. [...] Ik ben van plan om het te gebruiken voor alle **ML-services van mijn team bij Microsoft**. Sommige van deze worden geïntegreerd in het kernproduct van **Windows** en sommige **Office** -producten._"
Kabir Khan - **Microsoft** (ref)
"_We hebben de**FastAPI** library gebruikt om een **REST** server te maken die bevraagd kan worden om **voorspellingen** te maken. [voor Ludwig]_"
Piero Molino, Yaroslav Dudin en Sai Sumanth Miryala - **Uber** (ref)
"_**Netflix** is verheugd om een open-source release aan te kondigen van ons **crisismanagement** -orkestratieframework: **Dispatch**! [gebouwd met **FastAPI**]_"
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** (ref)
"_Ik ben super enthousiast over**FastAPI**. Het is zo leuk!_"
Brian Okken - **Python Bytes podcast presentator** (ref)
"_Wat je hebt gebouwd ziet er echt super solide en gepolijst uit. In veel opzichten is het wat ik wilde dat**Hug** kon zijn - het is echt inspirerend om iemand dit te zien bouwen._"
Timothy Crosley - **Hug creator** (ref)
"Wie geïnteresseerd is in een **modern framework** voor het bouwen van REST API's, bekijkt best eens **FastAPI** [...] Het is snel, gebruiksvriendelijk en gemakkelijk te leren [...]_"
"_We zijn overgestapt naar**FastAPI** voor onze **API's** [...] Het gaat jou vast ook bevallen [...]_"
Ines Montani - Matthew Honnibal - **Explosion AI oprichters - spaCy ontwikkelaars** (ref) - (ref)
"_Wie een Python API wil bouwen voor productie, kan ik ten stelligste**FastAPI** aanraden. Het is **prachtig ontworpen** , **eenvoudig te gebruiken** en **gemakkelijk schaalbaar** , het is een **cruciale component** geworden in onze strategie om API's centraal te zetten, en het vereenvoudigt automatisering en diensten zoals onze Virtual TAC Engineer._"
Deon Pillsbury - **Cisco** (ref)
## **Typer** , de FastAPI van CLIs¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
Als je een CLI-app bouwt die in de terminal moet worden gebruikt in plaats van een web-API, gebruik dan **Typer**.
**Typer** is het kleine broertje van FastAPI. En het is bedoeld als de **FastAPI van CLI's**. ️
## Vereisten¶
FastAPI staat op de schouders van reuzen:
  * Starlette voor de webonderdelen.
  * Pydantic voor de datadelen.


## Installatie¶
```

fast →pip install "fastapi[standard]"restart ↻

```

**Opmerking** : Zet `"fastapi[standard]"` tussen aanhalingstekens om ervoor te zorgen dat het werkt in alle terminals.
## Voorbeeld¶
### Creëer het¶
  * Maak het bestand `main.py` aan met daarin:


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

Of maak gebruik van `async def`...
Als je code gebruik maakt van `async` / `await`, gebruik dan `async def`:
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

**Opmerking** :
Als je het niet weet, kijk dan in het gedeelte _"Heb je haast?"_ over `async` en `await` in de documentatie.
### Voer het uit¶
Run de server met:
```

fast →fastapi dev main.py ╭────────── FastAPI CLI - Development mode ───────────╮ │                           │ │ Serving at: http://127.0.0.1:8000         │ │                           │ │ API docs: http://127.0.0.1:8000/docs        │ │                           │ │ Running in development mode, for production use:  │ │                           │ │ fastapi run                    │ │                           │ ╰─────────────────────────────────────────────────────╯INFO:   Will watch for changes in these directories: ['/home/user/code/awesomeapp']INFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [2248755] using WatchFilesINFO:   Started server process [2248757]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

Over het commando `fastapi dev main.py`...
Het commando `fastapi dev` leest het `main.py` bestand, detecteert de **FastAPI** app, en start een server met Uvicorn.
Standaard zal dit commando `fastapi dev` starten met "auto-reload" geactiveerd voor ontwikkeling op het lokale systeem.
Je kan hier meer over lezen in de FastAPI CLI documentatie.
### Controleer het¶
Open je browser op http://127.0.0.1:8000/items/5?q=somequery.
Je zult een JSON response zien:
```
{"item_id":5,"q":"somequery"}

```

Je hebt een API gemaakt die:
  * HTTP verzoeken kan ontvangen op de _paden_ `/` en `/items/{item_id}`.
  * Beide _paden_ hebben `GET` _operaties_ (ook bekend als HTTP _methoden_).
  * Het _pad_ `/items/{item_id}` heeft een _pad parameter_ `item_id` dat een `int` moet zijn.
  * Het _pad_ `/items/{item_id}` heeft een optionele `str` _query parameter_ `q`.


### Interactieve API documentatie¶
Ga naar http://127.0.0.1:8000/docs.
Je ziet de automatische interactieve API documentatie (verstrekt door Swagger UI):
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Alternatieve API documentatie¶
Ga vervolgens naar http://127.0.0.1:8000/redoc.
Je ziet de automatische interactieve API documentatie (verstrekt door ReDoc):
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Voorbeeld upgrade¶
Pas nu het bestand `main.py` aan om de body van een `PUT` request te ontvangen.
Dankzij Pydantic kunnen we de body declareren met standaard Python types.
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

De `fastapi dev` server zou automatisch moeten herladen.
### Interactieve API documentatie upgrade¶
Ga nu naar http://127.0.0.1:8000/docs.
  * De interactieve API-documentatie wordt automatisch bijgewerkt, inclusief de nieuwe body:


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * Klik op de knop "Try it out", hiermee kan je de parameters invullen en direct met de API interacteren:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Klik vervolgens op de knop "Execute", de gebruikersinterface zal communiceren met jouw API, de parameters verzenden, de resultaten ophalen en deze op het scherm tonen:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Alternatieve API documentatie upgrade¶
Ga vervolgens naar http://127.0.0.1:8000/redoc.
  * De alternatieve documentatie zal ook de nieuwe queryparameter en body weergeven:


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### Samenvatting¶
Samengevat declareer je **eenmalig** de types van parameters, body, etc. als functieparameters.
Dat doe je met standaard moderne Python types.
Je hoeft geen nieuwe syntax te leren, de methods of klassen van een specifieke bibliotheek, etc.
Gewoon standaard **Python**.
Bijvoorbeeld, voor een `int`:
```
item_id: int

```

of voor een complexer `Item` model:
```
item: Item

```

...en met die ene verklaring krijg je:
  * Editor ondersteuning, inclusief:
    * Code aanvulling.
    * Type validatie.
  * Validatie van data:
    * Automatische en duidelijke foutboodschappen wanneer de data ongeldig is.
    * Validatie zelfs voor diep geneste JSON objecten.
  * Conversie van invoergegevens: afkomstig van het netwerk naar Python-data en -types. Zoals:
    * JSON.
    * Pad parameters.
    * Query parameters.
    * Cookies.
    * Headers.
    * Formulieren.
    * Bestanden.
  * Conversie van uitvoergegevens: converstie van Python-data en -types naar netwerkgegevens (zoals JSON):
    * Converteer Python types (`str`, `int`, `float`, `bool`, `list`, etc).
    * `datetime` objecten.
    * `UUID` objecten.
    * Database modellen.
    * ...en nog veel meer.
  * Automatische interactieve API-documentatie, inclusief 2 alternatieve gebruikersinterfaces:
    * Swagger UI.
    * ReDoc.


Terugkomend op het vorige code voorbeeld, **FastAPI** zal:
  * Valideren dat er een `item_id` bestaat in het pad voor `GET` en `PUT` verzoeken.
  * Valideren dat het `item_id` van het type `int` is voor `GET` en `PUT` verzoeken.
    * Wanneer dat niet het geval is, krijgt de cliënt een nuttige, duidelijke foutmelding.
  * Controleren of er een optionele query parameter is met de naam `q` (zoals in `http://127.0.0.1:8000/items/foo?q=somequery`) voor `GET` verzoeken.
    * Aangezien de `q` parameter werd gedeclareerd met `= None`, is deze optioneel.
    * Zonder de `None` declaratie zou deze verplicht zijn (net als bij de body in het geval met `PUT`).
  * Voor `PUT` verzoeken naar `/items/{item_id}`, lees de body als JSON:
    * Controleer of het een verplicht attribuut `naam` heeft en dat dat een `str` is.
    * Controleer of het een verplicht attribuut `price` heeft en dat dat een`float` is.
    * Controleer of het een optioneel attribuut `is_offer` heeft, dat een `bool` is wanneer het aanwezig is.
    * Dit alles werkt ook voor diep geneste JSON objecten.
  * Converteer automatisch van en naar JSON.
  * Documenteer alles met OpenAPI, dat gebruikt kan worden door:
    * Interactieve documentatiesystemen.
    * Automatische client code generatie systemen, voor vele talen.
  * Biedt 2 interactieve documentatie-webinterfaces aan.


Dit was nog maar een snel overzicht, maar je zou nu toch al een idee moeten hebben over hoe het allemaal werkt.
Probeer deze regel te veranderen:
```
  return {"item_name": item.name, "item_id": item_id}

```

...van:
```
    ... "item_name": item.name ...

```

...naar:
```
    ... "item_price": item.price ...

```

...en zie hoe je editor de attributen automatisch invult en hun types herkent:
![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)
Voor een vollediger voorbeeld met meer mogelijkheden, zie de Tutorial - Gebruikershandleiding.
**Spoiler alert** : de tutorial - gebruikershandleiding bevat:
  * Declaratie van **parameters** op andere plaatsen zoals: **headers** , **cookies** , **formuliervelden** en **bestanden**.
  * Hoe stel je **validatie restricties** in zoals `maximum_length` of een `regex`.
  * Een zeer krachtig en eenvoudig te gebruiken **Dependency Injection** systeem.
  * Beveiliging en authenticatie, inclusief ondersteuning voor **OAuth2** met **JWT-tokens** en **HTTP Basic** auth.
  * Meer geavanceerde (maar even eenvoudige) technieken voor het declareren van **diep geneste JSON modellen** (dankzij Pydantic).
  * **GraphQL** integratie met Strawberry en andere packages.
  * Veel extra functies (dankzij Starlette) zoals:
    * **WebSockets**
    * uiterst gemakkelijke tests gebaseerd op HTTPX en `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...en meer.


## Prestaties¶
Onafhankelijke TechEmpower benchmarks tonen **FastAPI** applicaties draaiend onder Uvicorn aan als een van de snelste Python frameworks beschikbaar, alleen onder Starlette en Uvicorn zelf (intern gebruikt door FastAPI). (*)
Zie de sectie Benchmarks om hier meer over te lezen.
## Afhankelijkheden¶
FastAPI maakt gebruik van Pydantic en Starlette.
### `standard` Afhankelijkheden¶
Wanneer je FastAPI installeert met `pip install "fastapi[standard]"`, worden de volgende `standard` optionele afhankelijkheden geïnstalleerd:
Gebruikt door Pydantic:
  * `email_validator` - voor email validatie.


Gebruikt door Starlette:
  * `httpx` - Vereist indien je de `TestClient` wil gebruiken.
  * `jinja2` - Vereist als je de standaard templateconfiguratie wil gebruiken.
  * `python-multipart` - Vereist indien je "parsen" van formulieren wil ondersteunen met `requests.form()`.


Gebruikt door FastAPI / Starlette:
  * `uvicorn` - voor de server die jouw applicatie laadt en bedient.
  * `fastapi-cli` - om het `fastapi` commando te voorzien.


### Zonder `standard` Afhankelijkheden¶
Indien je de optionele `standard` afhankelijkheden niet wenst te installeren, kan je installeren met `pip install fastapi` in plaats van `pip install "fastapi[standard]"`.
### Bijkomende Optionele Afhankelijkheden¶
Er zijn nog een aantal bijkomende afhankelijkheden die je eventueel kan installeren.
Bijkomende optionele afhankelijkheden voor Pydantic:
  * `pydantic-settings` - voor het beheren van settings.
  * `pydantic-extra-types` - voor extra data types die gebruikt kunnen worden met Pydantic.


Bijkomende optionele afhankelijkheden voor FastAPI:
  * `orjson` - Vereist indien je `ORJSONResponse` wil gebruiken.
  * `ujson` - Vereist indien je `UJSONResponse` wil gebruiken.


## Licentie¶
Dit project is gelicenseerd onder de voorwaarden van de MIT licentie.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Terug naar boven 
  *[Overal automische code aanvulling]: ook bekend als automatisch aanvullen, automatisch aanvullen, IntelliSense
  *[CLI]: Command Line Interface
  *[Conversie]: ook bekend als: serialisatie, parsing, marshalling
  *[Dependency Injection]: ook bekend als componenten, middelen, verstrekkers, diensten, injectables
  *["parsen"]: het omzetten van de string die uit een HTTP verzoek komt in Python data
