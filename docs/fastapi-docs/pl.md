Przejdź do treści 
# FastAPI¶
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_FastAPI to szybki, prosty w nauce i gotowy do użycia w produkcji framework_
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg) ![Coverage](https://img.shields.io/codecov/c/github/fastapi/fastapi?color=%2334D058) ![Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)
**Dokumentacja** : https://fastapi.tiangolo.com
**Kod żródłowy** : https://github.com/fastapi/fastapi
FastAPI to nowoczesny, wydajny framework webowy do budowania API z użyciem Pythona bazujący na standardowym typowaniu Pythona.
Kluczowe cechy:
  * **Wydajność** : FastAPI jest bardzo wydajny, na równi z **NodeJS** oraz **Go** (dzięki Starlette i Pydantic). Jeden z najszybszych dostępnych frameworków Pythonowych.
  * **Szybkość kodowania** : Przyśpiesza szybkość pisania nowych funkcjonalności o około 200% do 300%. *
  * **Mniejsza ilość błędów** : Zmniejsza ilość ludzkich (dewelopera) błędy o około 40%. *
  * **Intuicyjność** : Wspaniałe wsparcie dla edytorów kodu. Dostępne wszędzie automatyczne uzupełnianie kodu. Krótszy czas debugowania.
  * **Łatwość** : Zaprojektowany by być prosty i łatwy do nauczenia. Mniej czasu spędzonego na czytanie dokumentacji.
  * **Kompaktowość** : Minimalizacja powtarzającego się kodu. Wiele funkcjonalności dla każdej deklaracji parametru. Mniej błędów.
  * **Solidność** : Kod gotowy dla środowiska produkcyjnego. Wraz z automatyczną interaktywną dokumentacją.
  * **Bazujący na standardach** : Oparty na (i w pełni kompatybilny z) otwartych standardach API: OpenAPI (wcześniej znane jako Swagger) oraz JSON Schema.


* oszacowania bazowane na testach wykonanych przez wewnętrzny zespół deweloperów, budujących aplikacie używane na środowisku produkcyjnym.
## Sponsorzy¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Inni sponsorzy
## Opinie¶
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
## **Typer** , FastAPI aplikacji konsolowych¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
Jeżeli tworzysz aplikacje CLI, która ma być używana w terminalu zamiast API, sprawdź **Typer**.
**Typer** to młodsze rodzeństwo FastAPI. Jego celem jest pozostanie **FastAPI aplikacji konsolowych** . ⌨️ 🚀
## Wymagania¶
FastAPI oparty jest na:
  * Starlette dla części webowej.
  * Pydantic dla części obsługujących dane.


## Instalacja¶
```

fast →pip install fastapirestart ↻

```

Na serwerze produkcyjnym będziesz także potrzebował serwera ASGI, np. Uvicorn lub Hypercorn.
```

fast →pip install "uvicorn[standard]"restart ↻

```

## Przykład¶
### Stwórz¶
  * Utwórz plik o nazwie `main.py` z:


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

Albo użyj `async def`...
Jeżeli twój kod korzysta z `async` / `await`, użyj `async def`:
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

**Przypis** :
Jeżeli nie znasz, sprawdź sekcję _"In a hurry?"_ o `async` i `await` w dokumentacji.
### Uruchom¶
Uruchom serwer używając:
```

fast →uvicorn main:app --reloadINFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [28720]INFO:   Started server process [28722]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

O komendzie `uvicorn main:app --reload`...
Komenda `uvicorn main:app` odnosi się do:
  * `main`: plik `main.py` ("moduł" w Pythonie).
  * `app`: obiekt stworzony w `main.py` w lini `app = FastAPI()`.
  * `--reload`: spraw by serwer resetował się po każdej zmianie w kodzie. Używaj tego tylko w środowisku deweloperskim.


### Wypróbuj¶
Otwórz link http://127.0.0.1:8000/items/5?q=somequery w przeglądarce.
Zobaczysz następującą odpowiedź JSON:
```
{"item_id":5,"q":"somequery"}

```

Właśnie stworzyłeś API które:
  * Otrzymuje żądania HTTP w _ścieżce_ `/` i `/items/{item_id}`.
  * Obie _ścieżki_ używają _operacji_ `GET` (znane także jako _metody_ HTTP).
  * _Ścieżka_ `/items/{item_id}` ma _parametr ścieżki_ `item_id` który powinien być obiektem typu `int`.
  * _Ścieżka_ `/items/{item_id}` ma opcjonalny _parametr zapytania_ typu `str` o nazwie `q`.


### Interaktywna dokumentacja API¶
Otwórz teraz stronę http://127.0.0.1:8000/docs.
Zobaczysz automatyczną interaktywną dokumentację API (dostarczoną z pomocą Swagger UI):
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Alternatywna dokumentacja API¶
Otwórz teraz http://127.0.0.1:8000/redoc.
Zobaczysz alternatywną, lecz wciąż automatyczną dokumentację (wygenerowaną z pomocą ReDoc):
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Aktualizacja przykładu¶
Zmodyfikuj teraz plik `main.py`, aby otrzmywał treść (body) żądania `PUT`.
Zadeklaruj treść żądania, używając standardowych typów w Pythonie dzięki Pydantic.
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

Serwer powinien przeładować się automatycznie (ponieważ dodałeś `--reload` do komendy `uvicorn` powyżej).
### Zaktualizowana interaktywna dokumentacja API¶
Wejdź teraz na http://127.0.0.1:8000/docs.
  * Interaktywna dokumentacja API zaktualizuje sie automatycznie, także z nową treścią żądania (body):


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * Kliknij przycisk "Try it out" (wypróbuj), pozwoli Ci to wypełnić parametry i bezpośrednio użyć API:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Kliknij potem przycisk "Execute" (wykonaj), interfejs użytkownika połączy się z API, wyśle parametry, otrzyma odpowiedź i wyświetli ją na ekranie:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Zaktualizowana alternatywna dokumentacja API¶
Otwórz teraz http://127.0.0.1:8000/redoc.
  * Alternatywna dokumentacja również pokaże zaktualizowane parametry i treść żądania (body):


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### Podsumowanie¶
Podsumowując, musiałeś zadeklarować typy parametrów, treści żądania (body) itp. tylko **raz** , i są one dostępne jako parametry funkcji.
Robisz to tak samo jak ze standardowymi typami w Pythonie.
Nie musisz sie uczyć żadnej nowej składni, metod lub klas ze specyficznych bibliotek itp.
Po prostu standardowy **Python**.
Na przykład, dla danych typu `int`:
```
item_id: int

```

albo dla bardziej złożonego obiektu `Item`:
```
item: Item

```

...i z pojedyńczą deklaracją otrzymujesz:
  * Wsparcie edytorów kodu, wliczając:
    * Auto-uzupełnianie.
    * Sprawdzanie typów.
  * Walidacja danych:
    * Automatyczne i przejrzyste błędy gdy dane są niepoprawne.
    * Walidacja nawet dla głęboko zagnieżdżonych obiektów JSON.
  * Konwersja danych wejściowych: przychodzących z sieci na Pythonowe typy. Pozwala na przetwarzanie danych:
    * JSON.
    * Parametrów ścieżki.
    * Parametrów zapytania.
    * Dane cookies.
    * Dane nagłówków (headers).
    * Formularze.
    * Pliki.
  * Konwersja danych wyjściowych: wychodzących z Pythona do sieci (jako JSON):
    * Przetwarzanie Pythonowych typów (`str`, `int`, `float`, `bool`, `list`, itp).
    * Obiekty `datetime`.
    * Obiekty `UUID`.
    * Modele baz danych.
    * ...i wiele więcej.
  * Automatyczne interaktywne dokumentacje API, wliczając 2 alternatywne interfejsy użytkownika:
    * Swagger UI.
    * ReDoc.


Wracając do poprzedniego przykładu, **FastAPI** :
  * Potwierdzi, że w ścieżce jest `item_id` dla żądań `GET` i `PUT`.
  * Potwierdzi, że `item_id` jest typu `int` dla żądań `GET` i `PUT`.
    * Jeżeli nie jest, odbiorca zobaczy przydatną, przejrzystą wiadomość z błędem.
  * Sprawdzi czy w ścieżce jest opcjonalny parametr zapytania `q` (np. `http://127.0.0.1:8000/items/foo?q=somequery`) dla żądania `GET`.
    * Jako że parametr `q` jest zadeklarowany jako `= None`, jest on opcjonalny.
    * Gdyby tego `None` nie było, parametr ten byłby wymagany (tak jak treść żądania w żądaniu `PUT`).
  * Dla żądania `PUT` z ścieżką `/items/{item_id}`, odczyta treść żądania jako JSON:
    * Sprawdzi czy posiada wymagany atrybut `name`, który powinien być typu `str`.
    * Sprawdzi czy posiada wymagany atrybut `price`, który musi być typu `float`.
    * Sprawdzi czy posiada opcjonalny atrybut `is_offer`, który (jeżeli obecny) powinien być typu `bool`.
    * To wszystko będzie również działać dla głęboko zagnieżdżonych obiektów JSON.
  * Automatycznie konwertuje z i do JSON.
  * Dokumentuje wszystko w OpenAPI, które może być używane przez:
    * Interaktywne systemy dokumentacji.
    * Systemy automatycznego generowania kodu klienckiego, dla wielu języków.
  * Dostarczy bezpośrednio 2 interaktywne dokumentacje webowe.


To dopiero początek, ale już masz mniej-więcej pojęcie jak to wszystko działa.
Spróbuj zmienić linijkę:
```
  return {"item_name": item.name, "item_id": item_id}

```

...z:
```
    ... "item_name": item.name ...

```

...na:
```
    ... "item_price": item.price ...

```

...i zobacz jak edytor kodu automatycznie uzupełni atrybuty i będzie znał ich typy:
![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)
Dla bardziej kompletnych przykładów posiadających więcej funkcjonalności, zobacz Tutorial - User Guide.
**Uwaga Spoiler** : tutorial - user guide zawiera:
  * Deklaracje **parametrów** z innych miejsc takich jak: **nagłówki** , **pliki cookies** , **formularze** i **pliki**.
  * Jak ustawić **ograniczenia walidacyjne** takie jak `maksymalna długość` lub `regex`.
  * Potężny i łatwy w użyciu system **Dependency Injection**.
  * Zabezpieczenia i autentykacja, wliczając wsparcie dla **OAuth2** z **tokenami JWT** oraz autoryzacją **HTTP Basic**.
  * Bardziej zaawansowane (ale równie proste) techniki deklarowania **głęboko zagnieżdżonych modeli JSON** (dzięki Pydantic).
  * Wiele dodatkowych funkcji (dzięki Starlette) takie jak:
    * **WebSockety**
    * **GraphQL**
    * bardzo proste testy bazujące na HTTPX oraz `pytest`
    * **CORS**
    * **Sesje cookie**
    * ...i więcej.


## Wydajność¶
Niezależne benchmarki TechEmpower pokazują, że **FastAPI** (uruchomiony na serwerze Uvicorn) jest jednym z najszybszych dostępnych Pythonowych frameworków, zaraz po Starlette i Uvicorn (używanymi wewnątrznie przez FastAPI). (*)
Aby dowiedzieć się o tym więcej, zobacz sekcję Benchmarks.
## Opcjonalne zależności¶
Używane przez Pydantic:
  * `email-validator` - dla walidacji adresów email.


Używane przez Starlette:
  * `httpx` - Wymagane jeżeli chcesz korzystać z `TestClient`.
  * `aiofiles` - Wymagane jeżeli chcesz korzystać z `FileResponse` albo `StaticFiles`.
  * `jinja2` - Wymagane jeżeli chcesz używać domyślnej konfiguracji szablonów.
  * `python-multipart` - Wymagane jeżelich chcesz wsparcie "parsowania" formularzy, używając `request.form()`.
  * `itsdangerous` - Wymagany dla wsparcia `SessionMiddleware`.
  * `pyyaml` - Wymagane dla wsparcia `SchemaGenerator` z Starlette (z FastAPI prawdopodobnie tego nie potrzebujesz).
  * `graphene` - Wymagane dla wsparcia `GraphQLApp`.


Używane przez FastAPI / Starlette:
  * `uvicorn` - jako serwer, który ładuje i obsługuje Twoją aplikację.
  * `orjson` - Wymagane jeżeli chcesz używać `ORJSONResponse`.
  * `ujson` - Wymagane jeżeli chcesz korzystać z `UJSONResponse`.


Możesz zainstalować wszystkie te aplikacje przy pomocy `pip install fastapi[all]`.
## Licencja¶
Ten projekt jest na licencji MIT.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Powrót do góry 
  *[automatyczne uzupełnianie]: znane jako auto-complete, autocompletion, IntelliSense
  *[CLI]: aplikacja z interfejsem konsolowym
  *[Konwersja]: znane również jako: serializacja, przetwarzanie, marshalling
  *[Dependency Injection]: znane jako komponenty, resources, providers, services, injectables
  *["parsowania"]: przetwarzania stringa którzy przychodzi z żądaniem HTTP na dane używane przez Pythona
