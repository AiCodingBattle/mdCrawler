Vai al contenuto 
# FastAPI
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_FastAPI framework, alte prestazioni, facile da imparare, rapido da implementare, pronto per il rilascio in produzione_
![Build Status](https://travis-ci.com/fastapi/fastapi.svg?branch=master) ![Coverage](https://img.shields.io/codecov/c/github/fastapi/fastapi) ![Package version](https://badge.fury.io/py/fastapi.svg)
**Documentazione** : https://fastapi.tiangolo.com
**Codice Sorgente** : https://github.com/fastapi/fastapi
FastAPI è un web framework moderno e veloce (a prestazioni elevate) che serve a creare API con Python 3.6+ basato sulle annotazioni di tipo di Python.
Le sue caratteristiche principali sono:
  * **Velocità** : Prestazioni molto elevate, alla pari di **NodeJS** e **Go** (grazie a Starlette e Pydantic). Uno dei framework Python più veloci in circolazione.
  * **Veloce da programmare** : Velocizza il lavoro consentendo il rilascio di nuove funzionalità tra il 200% e il 300% più rapidamente. *
  * **Meno bug** : Riduce di circa il 40% gli errori che commettono gli sviluppatori durante la scrittura del codice. *
  * **Intuitivo** : Grande supporto per gli editor di testo con autocompletamento in ogni dove. In questo modo si può dedicare meno tempo al debugging.
  * **Facile** : Progettato per essere facile da usare e imparare. Si riduce il tempo da dedicare alla lettura della documentazione.
  * **Sintentico** : Minimizza la duplicazione di codice. Molteplici funzionalità, ognuna con la propria dichiarazione dei parametri. Meno errori.
  * **Robusto** : Crea codice pronto per la produzione con documentazione automatica interattiva.
  * **Basato sugli standard** : Basato su (e completamente compatibile con) gli open standard per le API: OpenAPI (precedentemente Swagger) e JSON Schema.


* Stima basata sull'esito di test eseguiti su codice sorgente di applicazioni rilasciate in produzione da un team interno di sviluppatori.
## Sponsor¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Altri sponsor
## Recensioni¶
"_[...] I'm using**FastAPI** a ton these days. [...] I'm actually planning to use it for all of my team's **ML services at Microsoft**. Some of them are getting integrated into the core **Windows** product and some **Office** products._"
Kabir Khan - **Microsoft** (ref)
"_We adopted the**FastAPI** library to spawn a **REST** server that can be queried to obtain **predictions**. [for Ludwig]_"
Piero Molino, Yaroslav Dudin, e Sai Sumanth Miryala - **Uber** (ref)
"_**Netflix** is pleased to announce the open-source release of our **crisis management** orchestration framework: **Dispatch**! [built with **FastAPI**]_"
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** (ref)
"_I’m over the moon excited about**FastAPI**. It’s so fun!_"
Brian Okken - **Python Bytes podcast host** (ref)
"_Honestly, what you've built looks super solid and polished. In many ways, it's what I wanted**Hug** to be - it's really inspiring to see someone build that._"
Timothy Crosley - **Hug creator** (ref)
"_If you're looking to learn one**modern framework** for building REST APIs, check out **FastAPI** [...] It's fast, easy to use and easy to learn [...]_"
"_We've switched over to**FastAPI** for our **APIs** [...] I think you'll like it [...]_"
Ines Montani - Matthew Honnibal - **Explosion AI founders - spaCy creators** (ref) - (ref)
## **Typer** , la FastAPI delle CLI¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
Se stai sviluppando un'app CLI da usare nel terminale invece che una web API, ti consigliamo **Typer**.
**Typer** è il fratello minore di FastAPI. Ed è stato ideato per essere la **FastAPI delle CLI**. ⌨️ 🚀
## Requisiti¶
Python 3.6+
FastAPI è basata su importanti librerie:
  * Starlette per le parti web.
  * Pydantic per le parti dei dati.


## Installazione¶
```

fast →pip install fastapirestart ↻

```

Per il rilascio in produzione, sarà necessario un server ASGI come Uvicorn oppure Hypercorn.
```

fast →pip install uvicorn[standard]restart ↻

```

## Esempio¶
### Crea un file¶
  * Crea un file `main.py` con:


```
fromfastapiimport FastAPI
fromtypingimport Optional
app = FastAPI()
@app.get("/")
defread_root():
  return {"Hello": "World"}
@app.get("/items/{item_id}")
defread_item(item_id: int, q: str = Optional[None]):
  return {"item_id": item_id, "q": q}

```

Oppure usa `async def`...
Se il tuo codice usa `async` / `await`, allora usa `async def`:
```
fromfastapiimport FastAPI
fromtypingimport Optional
app = FastAPI()
@app.get("/")
async defread_root():
  return {"Hello": "World"}
@app.get("/items/{item_id}")
async defread_item(item_id: int, q: Optional[str] = None):
  return {"item_id": item_id, "q": q}

```

**Nota** :
e vuoi approfondire, consulta la sezione _"In a hurry?"_ su `async` e `await` nella documentazione.
### Esegui il server¶
Puoi far partire il server così:
```

fast →uvicorn main:app --reloadINFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [28720]INFO:   Started server process [28722]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

Informazioni sul comando `uvicorn main:app --reload`...
Vediamo il comando `uvicorn main:app` in dettaglio:
  * `main`: il file `main.py` (il "modulo" Python).
  * `app`: l'oggetto creato dentro `main.py` con la riga di codice `app = FastAPI()`.
  * `--reload`: ricarica il server se vengono rilevati cambiamenti del codice. Usalo solo durante la fase di sviluppo.


### Testa l'API¶
Apri il browser all'indirizzo http://127.0.0.1:8000/items/5?q=somequery.
Vedrai la seguente risposta JSON:
```
{"item_id":5,"q":"somequery"}

```

Hai appena creato un'API che:
  * Riceve richieste HTTP sui _paths_ `/` and `/items/{item_id}`.
  * Entrambi i _paths_ accettano`GET` _operations_ (conosciuti anche come HTTP _methods_).
  * Il _path_ `/items/{item_id}` ha un _path parameter_ `item_id` che deve essere un `int`.
  * Il _path_ `/items/{item_id}` ha una `str` _query parameter_ `q`.


### Documentazione interattiva dell'API¶
Adesso vai all'indirizzo http://127.0.0.1:8000/docs.
Vedrai la documentazione interattiva dell'API (offerta da Swagger UI):
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Documentazione interattiva alternativa¶
Adesso accedi all'url http://127.0.0.1:8000/redoc.
Vedrai la documentazione interattiva dell'API (offerta da ReDoc):
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Esempio più avanzato¶
Adesso modifica il file `main.py` per ricevere un _body_ da una richiesta `PUT`.
Dichiara il _body_ usando le annotazioni di tipo standard di Python, grazie a Pydantic.
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
fromtypingimport Optional
app = FastAPI()
classItem(BaseModel):
  name: str
  price: float
  is_offer: bool = Optional[None]
@app.get("/")
defread_root():
  return {"Hello": "World"}
@app.get("/items/{item_id}")
defread_item(item_id: int, q: Optional[str] = None):
  return {"item_id": item_id, "q": q}
@app.put("/items/{item_id}")
defupdate_item(item_id: int, item: Item):
  return {"item_name": item.name, "item_id": item_id}

```

Il server dovrebbe ricaricarsi in automatico (perché hai specificato `--reload` al comando `uvicorn` lanciato precedentemente).
### Aggiornamento della documentazione interattiva¶
Adesso vai su http://127.0.0.1:8000/docs.
  * La documentazione interattiva dell'API verrà automaticamente aggiornata, includendo il nuovo _body_ :


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * Fai click sul pulsante "Try it out", che ti permette di inserire i parametri per interagire direttamente con l'API:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Successivamente, premi sul pulsante "Execute". L'interfaccia utente comunicherà con la tua API, invierà i parametri, riceverà i risultati della richiesta, e li mostrerà sullo schermo:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Aggiornamento della documentazione alternativa¶
Ora vai su http://127.0.0.1:8000/redoc.
  * Anche la documentazione alternativa dell'API mostrerà il nuovo parametro della query e il _body_ :


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### Riepilogo¶
Ricapitolando, è sufficiente dichiarare **una sola volta** i tipi dei parametri, del body, ecc. come parametri di funzioni.
Questo con le annotazioni per i tipi standard di Python.
Non c'è bisogno di imparare una nuova sintassi, metodi o classi specifici a una libreria, ecc.
È normalissimo **Python 3.6+**.
Per esempio, per un `int`:
```
item_id: int

```

o per un modello `Item` più complesso:
```
item: Item

```

...e con quella singola dichiarazione hai in cambio:
  * Supporto per gli editor di testo, incluso:
    * Autocompletamento.
    * Controllo sulle annotazioni di tipo.
  * Validazione dei dati:
    * Errori chiari e automatici quando i dati sono invalidi.
    * Validazione anche per gli oggetti JSON più complessi.
  * Conversione dei dati di input: da risorse esterne a dati e tipi di Python. È possibile leggere da:
    * JSON.
    * Path parameters.
    * Query parameters.
    * Cookies.
    * Headers.
    * Form.
    * File.
  * Conversione dei dati di output: converte dati e tipi di Python a dati per la rete (come JSON):
    * Converte i tipi di Python (`str`, `int`, `float`, `bool`, `list`, ecc).
    * Oggetti `datetime`.
    * Oggetti `UUID`.
    * Modelli del database.
    * ...e molto di più.
  * Generazione di una documentazione dell'API interattiva, con scelta dell'interfaccia grafica:
    * Swagger UI.
    * ReDoc.


Tornando al precedente esempio, **FastAPI** :
  * Validerà che esiste un `item_id` nel percorso delle richieste `GET` e `PUT`.
  * Validerà che `item_id` sia di tipo `int` per le richieste `GET` e `PUT`.
    * Se non lo è, il client vedrà un errore chiaro e utile.
  * Controllerà se ci sia un parametro opzionale chiamato `q` (per esempio `http://127.0.0.1:8000/items/foo?q=somequery`) per le richieste `GET`.
    * Siccome il parametro `q` è dichiarato con `= None`, è opzionale.
    * Senza il `None` sarebbe stato obbligatorio (come per il body della richiesta `PUT`).
  * Per le richieste `PUT` su `/items/{item_id}`, leggerà il body come JSON, questo comprende:
    * verifica che la richiesta abbia un attributo obbligatorio `name` e che sia di tipo `str`.
    * verifica che la richiesta abbia un attributo obbligatorio `price` e che sia di tipo `float`.
    * verifica che la richiesta abbia un attributo opzionale `is_offer` e che sia di tipo `bool`, se presente.
    * Tutto questo funzionerebbe anche con oggetti JSON più complessi.
  * Convertirà _da_ e _a_ JSON automaticamente.
  * Documenterà tutto con OpenAPI, che può essere usato per:
    * Sistemi di documentazione interattivi.
    * Sistemi di generazione di codice dal lato client, per molti linguaggi.
  * Fornirà 2 interfacce di documentazione dell'API interattive.


Questa è solo la punta dell'iceberg, ma dovresti avere già un'idea di come il tutto funzioni.
Prova a cambiare questa riga di codice:
```
  return {"item_name": item.name, "item_id": item_id}

```

...da:
```
    ... "item_name": item.name ...

```

...a:
```
    ... "item_price": item.price ...

```

...e osserva come il tuo editor di testo autocompleterà gli attributi e sarà in grado di riconoscere i loro tipi:
![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)
Per un esempio più completo che mostra più funzionalità del framework, consulta Tutorial - Guida Utente.
**Spoiler alert** : il tutorial - Guida Utente include:
  * Dichiarazione di **parameters** da altri posti diversi come: **headers** , **cookies** , **form fields** e **files**.
  * Come stabilire **vincoli di validazione** come `maximum_length` o `regex`.
  * Un sistema di **Dependency Injection** facile da usare e molto potente. e potente.
  * Sicurezza e autenticazione, incluso il supporto per **OAuth2** con **token JWT** e autenticazione **HTTP Basic**.
  * Tecniche più avanzate (ma ugualmente semplici) per dichiarare **modelli JSON altamente nidificati** (grazie a Pydantic).
  * E altre funzionalità (grazie a Starlette) come:
    * **WebSockets**
    * **GraphQL**
    * test molto facili basati su `requests` e `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...e altro ancora.


## Prestazioni¶
Benchmark indipendenti di TechEmpower mostrano che **FastAPI** basato su Uvicorn è uno dei framework Python più veloci in circolazione, solamente dietro a Starlette e Uvicorn (usate internamente da FastAPI). (*)
Per approfondire, consulta la sezione Benchmarks.
## Dipendenze opzionali¶
Usate da Pydantic:
  * `email-validator` - per la validazione di email.


Usate da Starlette:
  * `requests` - Richiesto se vuoi usare il `TestClient`.
  * `aiofiles` - Richiesto se vuoi usare `FileResponse` o `StaticFiles`.
  * `jinja2` - Richiesto se vuoi usare la configurazione template di default.
  * `python-multipart` - Richiesto se vuoi supportare il "parsing" con `request.form()`.
  * `itsdangerous` - Richiesto per usare `SessionMiddleware`.
  * `pyyaml` - Richiesto per il supporto dello `SchemaGenerator` di Starlette (probabilmente non ti serve con FastAPI).
  * `graphene` - Richiesto per il supporto di `GraphQLApp`.


Usate da FastAPI / Starlette:
  * `uvicorn` - per il server che carica e serve la tua applicazione.
  * `orjson` - ichiesto se vuoi usare `ORJSONResponse`.
  * `ujson` - Richiesto se vuoi usare `UJSONResponse`.


Puoi installarle tutte con `pip install fastapi[all]`.
## Licenza¶
Questo progetto è concesso in licenza in base ai termini della licenza MIT.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Torna su 
  *[autocompletamento]: anche conosciuto come auto-completamento, autocompletion, IntelliSense
  *[CLI]: Command Line Interface (interfaccia della riga di comando)
  *[HTTP _methods_]: metodi HTTP
  *[Conversione]: detta anche: serialization, parsing, marshalling
  *[Dependency Injection]: detto anche components, resources, providers, services, injectables
  *["parsing"]: convertire la stringa che proviene da una richiesta HTTP in dati Python
