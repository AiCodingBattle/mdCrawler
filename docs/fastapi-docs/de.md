Zum Inhalt 
# FastAPI¶
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_FastAPI Framework, hochperformant, leicht zu erlernen, schnell zu programmieren, einsatzbereit_
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master) ![Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ![Package-Version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package) ![Unterstützte Python-Versionen](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
**Dokumentation** : https://fastapi.tiangolo.com
**Quellcode** : https://github.com/fastapi/fastapi
FastAPI ist ein modernes, schnelles (hoch performantes) Webframework zur Erstellung von APIs mit Python auf Basis von Standard-Python-Typhinweisen.
Seine Schlüssel-Merkmale sind:
  * **Schnell** : Sehr hohe Leistung, auf Augenhöhe mit **NodeJS** und **Go** (Dank Starlette und Pydantic). Eines der schnellsten verfügbaren Python-Frameworks.
  * **Schnell zu programmieren** : Erhöhen Sie die Geschwindigkeit bei der Entwicklung von Funktionen um etwa 200 % bis 300 %. *
  * **Weniger Bugs** : Verringern Sie die von Menschen (Entwicklern) verursachten Fehler um etwa 40 %. *
  * **Intuitiv** : Exzellente Editor-Unterstützung. Code-Vervollständigung überall. Weniger Debuggen.
  * **Einfach** : So konzipiert, dass es einfach zu benutzen und zu erlernen ist. Weniger Zeit für das Lesen der Dokumentation.
  * **Kurz** : Minimieren Sie die Verdoppelung von Code. Mehrere Funktionen aus jeder Parameterdeklaration. Weniger Bugs.
  * **Robust** : Erhalten Sie produktionsreifen Code. Mit automatischer, interaktiver Dokumentation.
  * **Standards-basiert** : Basierend auf (und vollständig kompatibel mit) den offenen Standards für APIs: OpenAPI (früher bekannt als Swagger) und JSON Schema.


* Schätzung auf Basis von Tests in einem internen Entwicklungsteam, das Produktionsanwendungen erstellt.
## Sponsoren¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Andere Sponsoren
## Meinungen¶
„ _[...] Ich verwende**FastAPI** heutzutage sehr oft. [...] Ich habe tatsächlich vor, es für alle **ML-Dienste meines Teams bei Microsoft** zu verwenden. Einige davon werden in das Kernprodukt **Windows** und einige **Office** -Produkte integriert._“
Kabir Khan - **Microsoft** (Ref)
„ _Wir haben die**FastAPI** -Bibliothek genommen, um einen **REST** -Server zu erstellen, der abgefragt werden kann, um **Vorhersagen** zu erhalten. [für Ludwig]_“
Piero Molino, Yaroslav Dudin, und Sai Sumanth Miryala - **Uber** (Ref)
„ _**Netflix** freut sich, die Open-Source-Veröffentlichung unseres **Krisenmanagement** -Orchestrierung-Frameworks bekannt zu geben: **Dispatch**! [erstellt mit **FastAPI**]_“
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** (Ref)
„ _Ich bin überglücklich mit**FastAPI**. Es macht so viel Spaß!_“
Brian Okken - **Host desPython Bytes Podcast** (Ref)
„ _Ehrlich, was Du gebaut hast, sieht super solide und poliert aus. In vielerlei Hinsicht ist es so, wie ich**Hug** haben wollte – es ist wirklich inspirierend, jemanden so etwas bauen zu sehen._“
Timothy Crosley - **Autor vonHug** (Ref)
„ _Wenn Sie ein**modernes Framework** zum Erstellen von REST-APIs erlernen möchten, schauen Sie sich **FastAPI** an. [...] Es ist schnell, einfach zu verwenden und leicht zu erlernen [...]_“
„ _Wir haben zu**FastAPI** für unsere **APIs** gewechselt [...] Ich denke, es wird Ihnen gefallen [...]_“
Ines Montani - Matthew Honnibal - **Gründer vonExplosion AI - Autoren von spaCy** (Ref) - (Ref)
„ _Falls irgendjemand eine Produktions-Python-API erstellen möchte, kann ich**FastAPI** wärmstens empfehlen. Es ist **wunderschön konzipiert** , **einfach zu verwenden** und **hoch skalierbar** ; es ist zu einer **Schlüsselkomponente** in unserer API-First-Entwicklungsstrategie geworden und treibt viele Automatisierungen und Dienste an, wie etwa unseren virtuellen TAC-Ingenieur._“
Deon Pillsbury - **Cisco** (Ref)
## **Typer** , das FastAPI der CLIs¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
Wenn Sie eine CLI-Anwendung für das Terminal erstellen, anstelle einer Web-API, schauen Sie sich **Typer** an.
**Typer** ist die kleine Schwester von FastAPI. Und es soll das **FastAPI der CLIs** sein. ⌨️ 🚀
## Anforderungen¶
FastAPI steht auf den Schultern von Giganten:
  * Starlette für die Webanteile.
  * Pydantic für die Datenanteile.


## Installation¶
```

fast →pip install fastapirestart ↻

```

Sie benötigen außerdem einen ASGI-Server. Für die Produktumgebung beispielsweise Uvicorn oder Hypercorn.
```

fast →pip install "uvicorn[standard]"restart ↻

```

## Beispiel¶
### Erstellung¶
  * Erstellen Sie eine Datei `main.py` mit:


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

Oder verwenden Sie `async def` ...
Wenn Ihr Code `async` / `await` verwendet, benutzen Sie `async def`:
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

**Anmerkung** :
Wenn Sie das nicht kennen, schauen Sie sich den Abschnitt _„In Eile?“_ über `async` und `await` in der Dokumentation an.
### Starten¶
Führen Sie den Server aus:
```

fast →uvicorn main:app --reloadINFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [28720]INFO:   Started server process [28722]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

Was macht der Befehl `uvicorn main:app --reload` ...
Der Befehl `uvicorn main:app` bezieht sich auf:
  * `main`: die Datei `main.py` (das Python-„Modul“).
  * `app`: das Objekt, das innerhalb von `main.py` mit der Zeile `app = FastAPI()` erzeugt wurde.
  * `--reload`: lässt den Server nach Codeänderungen neu starten. Tun Sie das nur während der Entwicklung.


### Testen¶
Öffnen Sie Ihren Browser unter http://127.0.0.1:8000/items/5?q=somequery.
Sie erhalten die JSON-Response:
```
{"item_id":5,"q":"somequery"}

```

Damit haben Sie bereits eine API erstellt, welche:
  * HTTP-Anfragen auf den _Pfaden_ `/` und `/items/{item_id}` entgegennimmt.
  * Beide _Pfade_ erhalten `GET` _Operationen_ (auch bekannt als HTTP _Methoden_).
  * Der _Pfad_ `/items/{item_id}` hat einen _Pfadparameter_ `item_id`, der ein `int` sein sollte.
  * Der _Pfad_ `/items/{item_id}` hat einen optionalen `str` _Query Parameter_ `q`.


### Interaktive API-Dokumentation¶
Gehen Sie nun auf http://127.0.0.1:8000/docs.
Sie sehen die automatische interaktive API-Dokumentation (bereitgestellt von Swagger UI):
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Alternative API-Dokumentation¶
Gehen Sie jetzt auf http://127.0.0.1:8000/redoc.
Sie sehen die alternative automatische Dokumentation (bereitgestellt von ReDoc):
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Beispiel Aktualisierung¶
Ändern Sie jetzt die Datei `main.py`, um den Body einer `PUT`-Anfrage zu empfangen.
Deklarieren Sie den Body mithilfe von Standard-Python-Typen, dank Pydantic.
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

Der Server sollte automatisch neu geladen werden (weil Sie oben `--reload` zum Befehl `uvicorn` hinzugefügt haben).
### Aktualisierung der interaktiven API-Dokumentation¶
Gehen Sie jetzt auf http://127.0.0.1:8000/docs.
  * Die interaktive API-Dokumentation wird automatisch aktualisiert, einschließlich des neuen Bodys:


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * Klicken Sie auf die Taste „Try it out“, damit können Sie die Parameter ausfüllen und direkt mit der API interagieren:


![Swagger UI Interaktion](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Klicken Sie dann auf die Taste „Execute“, die Benutzeroberfläche wird mit Ihrer API kommunizieren, sendet die Parameter, holt die Ergebnisse und zeigt sie auf dem Bildschirm an:


![Swagger UI Interaktion](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Aktualisierung der alternativen API-Dokumentation¶
Und nun gehen Sie auf http://127.0.0.1:8000/redoc.
  * Die alternative Dokumentation wird ebenfalls den neuen Abfrageparameter und -inhalt widerspiegeln:


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### Zusammenfassung¶
Zusammengefasst deklarieren Sie **einmal** die Typen von Parametern, Body, etc. als Funktionsparameter.
Das machen Sie mit modernen Standard-Python-Typen.
Sie müssen keine neue Syntax, Methoden oder Klassen einer bestimmten Bibliothek usw. lernen.
Nur Standard-**Python+**.
Zum Beispiel für ein `int`:
```
item_id: int

```

oder für ein komplexeres `Item`-Modell:
```
item: Item

```

... und mit dieser einen Deklaration erhalten Sie:
  * Editor-Unterstützung, einschließlich:
    * Code-Vervollständigung.
    * Typprüfungen.
  * Validierung von Daten:
    * Automatische und eindeutige Fehler, wenn die Daten ungültig sind.
    * Validierung auch für tief verschachtelte JSON-Objekte.
  * Konvertierung von Eingabedaten: Aus dem Netzwerk kommend, zu Python-Daten und -Typen. Lesen von:
    * JSON.
    * Pfad-Parametern.
    * Abfrage-Parametern.
    * Cookies.
    * Header-Feldern.
    * Formularen.
    * Dateien.
  * Konvertierung von Ausgabedaten: Konvertierung von Python-Daten und -Typen zu Netzwerkdaten (als JSON):
    * Konvertieren von Python-Typen (`str`, `int`, `float`, `bool`, `list`, usw.).
    * `Datetime`-Objekte.
    * `UUID`-Objekte.
    * Datenbankmodelle.
    * ... und viele mehr.
  * Automatische interaktive API-Dokumentation, einschließlich 2 alternativer Benutzeroberflächen:
    * Swagger UI.
    * ReDoc.


Um auf das vorherige Codebeispiel zurückzukommen, **FastAPI** wird:
  * Überprüfen, dass es eine `item_id` im Pfad für `GET`- und `PUT`-Anfragen gibt.
  * Überprüfen, ob die `item_id` vom Typ `int` für `GET`- und `PUT`-Anfragen ist.
    * Falls nicht, wird dem Client ein nützlicher, eindeutiger Fehler angezeigt.
  * Prüfen, ob es einen optionalen Abfrageparameter namens `q` (wie in `http://127.0.0.1:8000/items/foo?q=somequery`) für `GET`-Anfragen gibt.
    * Da der `q`-Parameter mit `= None` deklariert ist, ist er optional.
    * Ohne das `None` wäre er erforderlich (wie der Body im Fall von `PUT`).
  * Bei `PUT`-Anfragen an `/items/{item_id}` den Body als JSON lesen:
    * Prüfen, ob er ein erforderliches Attribut `name` hat, das ein `str` sein muss.
    * Prüfen, ob er ein erforderliches Attribut `price` hat, das ein `float` sein muss.
    * Prüfen, ob er ein optionales Attribut `is_offer` hat, das ein `bool` sein muss, falls vorhanden.
    * All dies würde auch für tief verschachtelte JSON-Objekte funktionieren.
  * Automatisch von und nach JSON konvertieren.
  * Alles mit OpenAPI dokumentieren, welches verwendet werden kann von:
    * Interaktiven Dokumentationssystemen.
    * Automatisch Client-Code generierenden Systemen für viele Sprachen.
  * Zwei interaktive Dokumentation-Webschnittstellen direkt zur Verfügung stellen.


Wir haben nur an der Oberfläche gekratzt, aber Sie bekommen schon eine Vorstellung davon, wie das Ganze funktioniert.
Versuchen Sie, diese Zeile zu ändern:
```
  return {"item_name": item.name, "item_id": item_id}

```

... von:
```
    ... "item_name": item.name ...

```

... zu:
```
    ... "item_price": item.price ...

```

... und sehen Sie, wie Ihr Editor die Attribute automatisch ausfüllt und ihre Typen kennt:
![Editor Unterstützung](https://fastapi.tiangolo.com/img/vscode-completion.png)
Für ein vollständigeres Beispiel, mit weiteren Funktionen, siehe das Tutorial - Benutzerhandbuch.
**Spoiler-Alarm** : Das Tutorial - Benutzerhandbuch enthält:
  * Deklaration von **Parametern** von anderen verschiedenen Stellen wie: **Header-Felder** , **Cookies** , **Formularfelder** und **Dateien**.
  * Wie man **Validierungseinschränkungen** wie `maximum_length` oder `regex` setzt.
  * Ein sehr leistungsfähiges und einfach zu bedienendes System für **Dependency Injection**.
  * Sicherheit und Authentifizierung, einschließlich Unterstützung für **OAuth2** mit **JWT-Tokens** und **HTTP-Basic** -Authentifizierung.
  * Fortgeschrittenere (aber ebenso einfache) Techniken zur Deklaration **tief verschachtelter JSON-Modelle** (dank Pydantic).
  * **GraphQL** Integration mit Strawberry und anderen Bibliotheken.
  * Viele zusätzliche Funktionen (dank Starlette) wie:
    * **WebSockets**
    * extrem einfache Tests auf Basis von `httpx` und `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ... und mehr.


## Performanz¶
Unabhängige TechEmpower-Benchmarks zeigen **FastAPI** -Anwendungen, die unter Uvicorn laufen, als eines der schnellsten verfügbaren Python-Frameworks, nur noch hinter Starlette und Uvicorn selbst (intern von FastAPI verwendet).
Um mehr darüber zu erfahren, siehe den Abschnitt Benchmarks.
## Optionale Abhängigkeiten¶
Wird von Pydantic verwendet:
  * `email-validator` - für E-Mail-Validierung.
  * `pydantic-settings` - für die Verwaltung von Einstellungen.
  * `pydantic-extra-types` - für zusätzliche Typen, mit Pydantic zu verwenden.


Wird von Starlette verwendet:
  * `httpx` - erforderlich, wenn Sie den `TestClient` verwenden möchten.
  * `jinja2` - erforderlich, wenn Sie die Standardkonfiguration für Templates verwenden möchten.
  * `python-multipart` - erforderlich, wenn Sie Formulare mittels `request.form()` „parsen“ möchten.
  * `itsdangerous` - erforderlich für `SessionMiddleware` Unterstützung.
  * `pyyaml` - erforderlich für Starlette's `SchemaGenerator` Unterstützung (Sie brauchen das wahrscheinlich nicht mit FastAPI).
  * `ujson` - erforderlich, wenn Sie `UJSONResponse` verwenden möchten.


Wird von FastAPI / Starlette verwendet:
  * `uvicorn` - für den Server, der Ihre Anwendung lädt und serviert.
  * `orjson` - erforderlich, wenn Sie `ORJSONResponse` verwenden möchten.


Sie können diese alle mit `pip install "fastapi[all]"` installieren.
## Lizenz¶
Dieses Projekt ist unter den Bedingungen der MIT-Lizenz lizenziert.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Zurück zum Seitenanfang 
  *[Code-Vervollständigung]: auch bekannt als Autovervollständigung, Autocompletion, IntelliSense
  *[CLI]: Command Line Interface – Kommandozeilen-Schnittstelle
  *[ASGI]: Asynchronous Server Gateway Interface – Asynchrone Server-Verbindungsschnittstelle
  *[Body]: Body – Körper, Inhalt: Der eigentliche Inhalt einer Nachricht, nicht die Metadaten
  *[Konvertierung]: auch bekannt als: Serialisierung, Parsen, Marshalling
  *[Dependency Injection]: Dependency Injection – Einbringen von Abhängigkeiten: Auch bekannt als Komponenten, Ressourcen, Provider, Services, Injectables
  *[„parsen“]: Konvertieren des Strings, der aus einer HTTP-Anfrage stammt, nach Python-Daten
