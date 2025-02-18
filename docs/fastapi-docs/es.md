Saltar a contenido 
# FastAPI¶
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_FastAPI framework, alto rendimiento, fácil de aprender, rápido de programar, listo para producción_
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master) ![Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ![Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package) ![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
**Documentación** : https://fastapi.tiangolo.com
**Código Fuente** : https://github.com/fastapi/fastapi
FastAPI es un framework web moderno, rápido (de alto rendimiento), para construir APIs con Python basado en las anotaciones de tipos estándar de Python.
Las características clave son:
  * **Rápido** : Muy alto rendimiento, a la par con **NodeJS** y **Go** (gracias a Starlette y Pydantic). Uno de los frameworks Python más rápidos disponibles.
  * **Rápido de programar** : Aumenta la velocidad para desarrollar funcionalidades en aproximadamente un 200% a 300%. *
  * **Menos bugs** : Reduce en aproximadamente un 40% los errores inducidos por humanos (desarrolladores). *
  * **Intuitivo** : Gran soporte para editores. Autocompletado en todas partes. Menos tiempo depurando.
  * **Fácil** : Diseñado para ser fácil de usar y aprender. Menos tiempo leyendo documentación.
  * **Corto** : Minimiza la duplicación de código. Múltiples funcionalidades desde cada declaración de parámetro. Menos bugs.
  * **Robusto** : Obtén código listo para producción. Con documentación interactiva automática.
  * **Basado en estándares** : Basado (y completamente compatible) con los estándares abiertos para APIs: OpenAPI (anteriormente conocido como Swagger) y JSON Schema.


* estimación basada en pruebas con un equipo de desarrollo interno, construyendo aplicaciones de producción.
## Sponsors¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Otros sponsors
## Opiniones¶
"_[...] Estoy usando**FastAPI** un montón estos días. [...] De hecho, estoy planeando usarlo para todos los servicios de **ML de mi equipo en Microsoft**. Algunos de ellos se están integrando en el núcleo del producto **Windows** y algunos productos de **Office**._"
Kabir Khan - **Microsoft** (ref)
"_Adoptamos el paquete**FastAPI** para crear un servidor **REST** que pueda ser consultado para obtener **predicciones**. [para Ludwig]_"
Piero Molino, Yaroslav Dudin, y Sai Sumanth Miryala - **Uber** (ref)
"_**Netflix** se complace en anunciar el lanzamiento de código abierto de nuestro framework de orquestación de **gestión de crisis** : **Dispatch**! [construido con **FastAPI**]_"
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** (ref)
"_Estoy súper emocionado con**FastAPI**. ¡Es tan divertido!_"
Brian Okken - **host del podcast Python Bytes** (ref)
"_Honestamente, lo que has construido parece súper sólido y pulido. En muchos aspectos, es lo que quería que**Hug** fuera; es realmente inspirador ver a alguien construir eso._"
Timothy Crosley - **creador de Hug** (ref)
"_Si estás buscando aprender un**framework moderno** para construir APIs REST, échale un vistazo a **FastAPI** [...] Es rápido, fácil de usar y fácil de aprender [...]_"
"_Nos hemos cambiado a**FastAPI** para nuestras **APIs** [...] Creo que te gustará [...]_"
Ines Montani - Matthew Honnibal - **fundadores de Explosion AI - creadores de spaCy** (ref) - (ref)
"_Si alguien está buscando construir una API de Python para producción, altamente recomendaría**FastAPI**. Está **hermosamente diseñado** , es **simple de usar** y **altamente escalable** , se ha convertido en un **componente clave** en nuestra estrategia de desarrollo API primero y está impulsando muchas automatizaciones y servicios como nuestro Ingeniero Virtual TAC._"
Deon Pillsbury - **Cisco** (ref)
## **Typer** , el FastAPI de las CLIs¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
Si estás construyendo una aplicación de CLI para ser usada en el terminal en lugar de una API web, revisa **Typer**.
**Typer** es el hermano pequeño de FastAPI. Y está destinado a ser el **FastAPI de las CLIs**. ⌨️ 🚀
## Requisitos¶
FastAPI se apoya en hombros de gigantes:
  * Starlette para las partes web.
  * Pydantic para las partes de datos.


## Instalación¶
Crea y activa un entorno virtual y luego instala FastAPI:
```

fast →pip install "fastapi[standard]"restart ↻

```

**Nota** : Asegúrate de poner `"fastapi[standard]"` entre comillas para asegurar que funcione en todas las terminales.
## Ejemplo¶
### Créalo¶
  * Crea un archivo `main.py` con:


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

O usa `async def`...
Si tu código usa `async` / `await`, usa `async def`:
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

**Nota** :
Si no lo sabes, revisa la sección _"¿Con prisa?"_ sobre `async` y `await` en la documentación.
### Córrelo¶
Corre el servidor con:
```

fast →fastapi dev main.py ╭────────── FastAPI CLI - Development mode ───────────╮ │                           │ │ Serving at: http://127.0.0.1:8000         │ │                           │ │ API docs: http://127.0.0.1:8000/docs        │ │                           │ │ Running in development mode, for production use:  │ │                           │ │ fastapi run                    │ │                           │ ╰─────────────────────────────────────────────────────╯INFO:   Will watch for changes in these directories: ['/home/user/code/awesomeapp']INFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [2248755] using WatchFilesINFO:   Started server process [2248757]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

Acerca del comando `fastapi dev main.py`...
El comando `fastapi dev` lee tu archivo `main.py`, detecta la app **FastAPI** en él y arranca un servidor usando Uvicorn.
Por defecto, `fastapi dev` comenzará con auto-recarga habilitada para el desarrollo local.
Puedes leer más sobre esto en la documentación del CLI de FastAPI.
### Revísalo¶
Abre tu navegador en http://127.0.0.1:8000/items/5?q=somequery.
Verás el response JSON como:
```
{"item_id":5,"q":"somequery"}

```

Ya creaste una API que:
  * Recibe requests HTTP en los _paths_ `/` y `/items/{item_id}`.
  * Ambos _paths_ toman _operaciones_ `GET` (también conocidas como métodos HTTP).
  * El _path_ `/items/{item_id}` tiene un _parámetro de path_ `item_id` que debe ser un `int`.
  * El _path_ `/items/{item_id}` tiene un _parámetro de query_ `q` opcional que es un `str`.


### Documentación interactiva de la API¶
Ahora ve a http://127.0.0.1:8000/docs.
Verás la documentación interactiva automática de la API (proporcionada por Swagger UI):
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Documentación de API Alternativa¶
Y ahora, ve a http://127.0.0.1:8000/redoc.
Verás la documentación alternativa automática (proporcionada por ReDoc):
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Actualización del Ejemplo¶
Ahora modifica el archivo `main.py` para recibir un body desde un request `PUT`.
Declara el body usando tipos estándar de Python, gracias a Pydantic.
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

El servidor `fastapi dev` debería recargarse automáticamente.
### Actualización de la Documentación Interactiva de la API¶
Ahora ve a http://127.0.0.1:8000/docs.
  * La documentación interactiva de la API se actualizará automáticamente, incluyendo el nuevo body:


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * Haz clic en el botón "Try it out", te permite llenar los parámetros e interactuar directamente con la API:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Luego haz clic en el botón "Execute", la interfaz de usuario se comunicará con tu API, enviará los parámetros, obtendrá los resultados y los mostrará en la pantalla:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Actualización de la Documentación Alternativa de la API¶
Y ahora, ve a http://127.0.0.1:8000/redoc.
  * La documentación alternativa también reflejará el nuevo parámetro de query y body:


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### Resumen¶
En resumen, declaras **una vez** los tipos de parámetros, body, etc. como parámetros de función.
Lo haces con tipos estándar modernos de Python.
No tienes que aprender una nueva sintaxis, los métodos o clases de un paquete específico, etc.
Solo **Python** estándar.
Por ejemplo, para un `int`:
```
item_id: int

```

o para un modelo `Item` más complejo:
```
item: Item

```

...y con esa única declaración obtienes:
  * Soporte para editores, incluyendo:
    * Autocompletado.
    * Chequeo de tipos.
  * Validación de datos:
    * Errores automáticos y claros cuando los datos son inválidos.
    * Validación incluso para objetos JSON profundamente anidados.
  * Conversión de datos de entrada: de la red a los datos y tipos de Python. Leyendo desde:
    * JSON.
    * Parámetros de path.
    * Parámetros de query.
    * Cookies.
    * Headers.
    * Forms.
    * Archivos.
  * Conversión de datos de salida: convirtiendo de datos y tipos de Python a datos de red (como JSON):
    * Convertir tipos de Python (`str`, `int`, `float`, `bool`, `list`, etc).
    * Objetos `datetime`.
    * Objetos `UUID`.
    * Modelos de base de datos.
    * ...y muchos más.
  * Documentación interactiva automática de la API, incluyendo 2 interfaces de usuario alternativas:
    * Swagger UI.
    * ReDoc.


Volviendo al ejemplo de código anterior, **FastAPI** :
  * Validará que haya un `item_id` en el path para requests `GET` y `PUT`.
  * Validará que el `item_id` sea del tipo `int` para requests `GET` y `PUT`.
    * Si no lo es, el cliente verá un error útil y claro.
  * Comprobará si hay un parámetro de query opcional llamado `q` (como en `http://127.0.0.1:8000/items/foo?q=somequery`) para requests `GET`.
    * Como el parámetro `q` está declarado con `= None`, es opcional.
    * Sin el `None` sería requerido (como lo es el body en el caso con `PUT`).
  * Para requests `PUT` a `/items/{item_id}`, leerá el body como JSON:
    * Comprobará que tiene un atributo requerido `name` que debe ser un `str`.
    * Comprobará que tiene un atributo requerido `price` que debe ser un `float`.
    * Comprobará que tiene un atributo opcional `is_offer`, que debe ser un `bool`, si está presente.
    * Todo esto también funcionaría para objetos JSON profundamente anidados.
  * Convertirá de y a JSON automáticamente.
  * Documentará todo con OpenAPI, que puede ser usado por:
    * Sistemas de documentación interactiva.
    * Sistemas de generación automática de código cliente, para muchos lenguajes.
  * Proporcionará 2 interfaces web de documentación interactiva directamente.


Solo tocamos los conceptos básicos, pero ya te haces una idea de cómo funciona todo.
Intenta cambiar la línea con:
```
  return {"item_name": item.name, "item_id": item_id}

```

...desde:
```
    ... "item_name": item.name ...

```

...a:
```
    ... "item_price": item.price ...

```

...y observa cómo tu editor autocompleta los atributos y conoce sus tipos:
![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)
Para un ejemplo más completo incluyendo más funcionalidades, ve al Tutorial - Guía del Usuario.
**Alerta de spoilers** : el tutorial - guía del usuario incluye:
  * Declaración de **parámetros** desde otros lugares diferentes como: **headers** , **cookies** , **campos de formulario** y **archivos**.
  * Cómo establecer **restricciones de validación** como `maximum_length` o `regex`.
  * Un sistema de **Inyección de Dependencias** muy poderoso y fácil de usar.
  * Seguridad y autenticación, incluyendo soporte para **OAuth2** con **tokens JWT** y autenticación **HTTP Basic**.
  * Técnicas más avanzadas (pero igualmente fáciles) para declarar **modelos JSON profundamente anidados** (gracias a Pydantic).
  * Integración con **GraphQL** usando Strawberry y otros paquetes.
  * Muchas funcionalidades extra (gracias a Starlette) como:
    * **WebSockets**
    * pruebas extremadamente fáciles basadas en HTTPX y `pytest`
    * **CORS**
    * **Sesiones de Cookies**
    * ...y más.


## Rendimiento¶
Benchmarks independientes de TechEmpower muestran aplicaciones **FastAPI** ejecutándose bajo Uvicorn como uno de los frameworks Python más rápidos disponibles, solo por debajo de Starlette y Uvicorn (usados internamente por FastAPI). (*)
Para entender más sobre esto, ve la sección Benchmarks.
## Dependencias¶
FastAPI depende de Pydantic y Starlette.
### Dependencias `standard`¶
Cuando instalas FastAPI con `pip install "fastapi[standard]"` viene con el grupo `standard` de dependencias opcionales:
Usadas por Pydantic:
  * `email-validator` - para validación de correos electrónicos.


Usadas por Starlette:
  * `httpx` - Requerido si deseas usar el `TestClient`.
  * `jinja2` - Requerido si deseas usar la configuración de plantilla predeterminada.
  * `python-multipart` - Requerido si deseas soportar "parsing" de forms, con `request.form()`.


Usadas por FastAPI / Starlette:
  * `uvicorn` - para el servidor que carga y sirve tu aplicación. Esto incluye `uvicorn[standard]`, que incluye algunas dependencias (por ejemplo, `uvloop`) necesarias para servir con alto rendimiento.
  * `fastapi-cli` - para proporcionar el comando `fastapi`.


### Sin Dependencias `standard`¶
Si no deseas incluir las dependencias opcionales `standard`, puedes instalar con `pip install fastapi` en lugar de `pip install "fastapi[standard]"`.
### Dependencias Opcionales Adicionales¶
Existen algunas dependencias adicionales que podrías querer instalar.
Dependencias opcionales adicionales de Pydantic:
  * `pydantic-settings` - para la gestión de configuraciones.
  * `pydantic-extra-types` - para tipos extra para ser usados con Pydantic.


Dependencias opcionales adicionales de FastAPI:
  * `orjson` - Requerido si deseas usar `ORJSONResponse`.
  * `ujson` - Requerido si deseas usar `UJSONResponse`.


## Licencia¶
Este proyecto tiene licencia bajo los términos de la licencia MIT.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Volver al principio 
  *[Autocompletado]: también conocido como autocompletado, IntelliSense
  *[CLI]: Interfaz de Línea de Comandos
  *[Conversión]: también conocido como: serialización, parsing, marshalling
  *[Inyección de Dependencias]: también conocido como componentes, recursos, proveedores, servicios, inyectables
  *["parsing"]: convertir el string que viene de un request HTTP en datos de Python
