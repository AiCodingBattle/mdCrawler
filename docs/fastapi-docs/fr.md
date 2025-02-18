Aller au contenu 
# FastAPI¶
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_Framework FastAPI, haute performance, facile à apprendre, rapide à coder, prêt pour la production_
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master) ![Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ![Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package) ![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
**Documentation** : https://fastapi.tiangolo.com
**Code Source** : https://github.com/fastapi/fastapi
FastAPI est un framework web moderne et rapide (haute performance) pour la création d'API avec Python, basé sur les annotations de type standard de Python.
Les principales fonctionnalités sont :
  * **Rapidité** : De très hautes performances, au niveau de **NodeJS** et **Go** (grâce à Starlette et Pydantic). L'un des frameworks Python les plus rapides.
  * **Rapide à coder** : Augmente la vitesse de développement des fonctionnalités d'environ 200 % à 300 %. *
  * **Moins de bugs** : Réduit d'environ 40 % les erreurs induites par le développeur. *
  * **Intuitif** : Excellente compatibilité avec les IDE. Complétion complète. Moins de temps passé à déboguer.
  * **Facile** : Conçu pour être facile à utiliser et à apprendre. Moins de temps passé à lire la documentation.
  * **Concis** : Diminue la duplication de code. De nombreuses fonctionnalités liées à la déclaration de chaque paramètre. Moins de bugs.
  * **Robuste** : Obtenez un code prêt pour la production. Avec une documentation interactive automatique.
  * **Basé sur des normes** : Basé sur (et entièrement compatible avec) les standards ouverts pour les APIs : OpenAPI (précédemment connu sous le nom de Swagger) et JSON Schema.


* estimation basée sur des tests d'une équipe de développement interne, construisant des applications de production.
## Sponsors¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Other sponsors
## Opinions¶
"_[...] J'utilise beaucoup**FastAPI** ces derniers temps. [...] Je prévois de l'utiliser dans mon équipe pour tous les **services de ML chez Microsoft**. Certains d'entre eux seront intégrés dans le coeur de **Windows** et dans certains produits **Office**._"
Kabir Khan - **Microsoft** (ref)
"_Nous avons adopté la bibliothèque**FastAPI** pour créer un serveur **REST** qui peut être interrogé pour obtenir des **prédictions**. [pour Ludwig]_"
Piero Molino, Yaroslav Dudin et Sai Sumanth Miryala - **Uber** (ref)
"_**Netflix** a le plaisir d'annoncer la sortie en open-source de notre framework d'orchestration de **gestion de crise** : **Dispatch** ! [construit avec **FastAPI**]_"
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** (ref)
"_Je suis très enthousiaste à propos de**FastAPI**. C'est un bonheur !_"
Brian Okken - **Auteur du podcastPython Bytes** (ref)
"_Honnêtement, ce que vous avez construit a l'air super solide et élégant. A bien des égards, c'est comme ça que je voulais que**Hug** soit - c'est vraiment inspirant de voir quelqu'un construire ça._"
Timothy Crosley - **Créateur deHug** (ref)
"_Si vous cherchez à apprendre un**framework moderne** pour créer des APIs REST, regardez **FastAPI** [...] C'est rapide, facile à utiliser et à apprendre [...]_"
"_Nous sommes passés à**FastAPI** pour nos **APIs** [...] Je pense que vous l'aimerez [...]_"
Ines Montani - Matthew Honnibal - **Fondateurs deExplosion AI - Créateurs de spaCy** (ref) - (ref)
"_Si quelqu'un cherche à construire une API Python de production, je recommande vivement**FastAPI**. Il est **bien conçu** , **simple à utiliser** et **très évolutif**. Il est devenu un **composant clé** dans notre stratégie de développement API first et il est à l'origine de nombreux automatismes et services tels que notre ingénieur virtuel TAC._"
Deon Pillsbury - **Cisco** (ref)
## **Typer** , le FastAPI des CLI¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
Si vous souhaitez construire une application CLI utilisable dans un terminal au lieu d'une API web, regardez **Typer**.
**Typer** est le petit frère de FastAPI. Et il est destiné à être le **FastAPI des CLI**. ⌨️ 🚀
## Prérequis¶
FastAPI repose sur les épaules de géants :
  * Starlette pour les parties web.
  * Pydantic pour les parties données.


## Installation¶
```

fast →pip install fastapirestart ↻

```

Vous aurez également besoin d'un serveur ASGI pour la production tel que Uvicorn ou Hypercorn.
```

fast →pip install "uvicorn[standard]"restart ↻

```

## Exemple¶
### Créez¶
  * Créez un fichier `main.py` avec :


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

Ou utilisez `async def` ...
Si votre code utilise `async` / `await`, utilisez `async def` :
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

**Note**
Si vous n'êtes pas familier avec cette notion, consultez la section _"Vous êtes pressés ?"_ à propos de `async` et `await` dans la documentation.
### Lancez¶
Lancez le serveur avec :
```

fast →uvicorn main:app --reloadINFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [28720]INFO:   Started server process [28722]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

À propos de la commande `uvicorn main:app --reload` ...
La commande `uvicorn main:app` fait référence à :
  * `main` : le fichier `main.py` (le "module" Python).
  * `app` : l'objet créé à l'intérieur de `main.py` avec la ligne `app = FastAPI()`.
  * `--reload` : fait redémarrer le serveur après des changements de code. À n'utiliser que pour le développement.


### Vérifiez¶
Ouvrez votre navigateur à l'adresse http://127.0.0.1:8000/items/5?q=somequery.
Vous obtenez alors cette réponse JSON :
```
{"item_id":5,"q":"somequery"}

```

Vous venez de créer une API qui :
  * Reçoit les requêtes HTTP pour les _chemins_ `/` et `/items/{item_id}`.
  * Les deux _chemins_ acceptent des _opérations_ `GET` (également connu sous le nom de _méthodes_ HTTP).
  * Le _chemin_ `/items/{item_id}` a un _paramètre_ `item_id` qui doit être un `int`.
  * Le _chemin_ `/items/{item_id}` a un _paramètre de requête_ optionnel `q` de type `str`.


### Documentation API interactive¶
Maintenant, rendez-vous sur http://127.0.0.1:8000/docs.
Vous verrez la documentation interactive automatique de l'API (fournie par Swagger UI) :
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Documentation API alternative¶
Et maintenant, rendez-vous sur http://127.0.0.1:8000/redoc.
Vous verrez la documentation interactive automatique de l'API (fournie par ReDoc) :
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Exemple plus poussé¶
Maintenant, modifiez le fichier `main.py` pour recevoir le corps d'une requête `PUT`.
Déclarez ce corps en utilisant les types Python standards, grâce à Pydantic.
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

Le serveur se recharge normalement automatiquement (car vous avez pensé à `--reload` dans la commande `uvicorn` ci-dessus).
### Plus loin avec la documentation API interactive¶
Maintenant, rendez-vous sur http://127.0.0.1:8000/docs.
  * La documentation interactive de l'API sera automatiquement mise à jour, y compris le nouveau corps de la requête :


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * Cliquez sur le bouton "Try it out", il vous permet de renseigner les paramètres et d'interagir directement avec l'API :


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Cliquez ensuite sur le bouton "Execute", l'interface utilisateur communiquera avec votre API, enverra les paramètres, obtiendra les résultats et les affichera à l'écran :


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Plus loin avec la documentation API alternative¶
Et maintenant, rendez-vous sur http://127.0.0.1:8000/redoc.
  * La documentation alternative reflétera également le nouveau paramètre de requête et le nouveau corps :


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### En résumé¶
En résumé, vous déclarez **une fois** les types de paramètres, le corps de la requête, etc. en tant que paramètres de fonction.
Vous faites cela avec les types Python standard modernes.
Vous n'avez pas à apprendre une nouvelle syntaxe, les méthodes ou les classes d'une bibliothèque spécifique, etc.
Juste du **Python** standard.
Par exemple, pour un `int`:
```
item_id: int

```

ou pour un modèle `Item` plus complexe :
```
item: Item

```

... et avec cette déclaration unique, vous obtenez :
  * Une assistance dans votre IDE, notamment :
    * la complétion.
    * la vérification des types.
  * La validation des données :
    * des erreurs automatiques et claires lorsque les données ne sont pas valides.
    * une validation même pour les objets JSON profondément imbriqués.
  * Une conversion des données d'entrée : venant du réseau et allant vers les données et types de Python, permettant de lire :
    * le JSON.
    * les paramètres du chemin.
    * les paramètres de la requête.
    * les cookies.
    * les en-têtes.
    * les formulaires.
    * les fichiers.
  * La conversion des données de sortie : conversion des données et types Python en données réseau (au format JSON), permettant de convertir :
    * les types Python (`str`, `int`, `float`, `bool`, `list`, etc).
    * les objets `datetime`.
    * les objets `UUID`.
    * les modèles de base de données.
    * ... et beaucoup plus.
  * La documentation API interactive automatique, avec 2 interfaces utilisateur au choix :
    * Swagger UI.
    * ReDoc.


Pour revenir à l'exemple de code précédent, **FastAPI** permet de :
  * Valider que `item_id` existe dans le chemin des requêtes `GET` et `PUT`.
  * Valider que `item_id` est de type `int` pour les requêtes `GET` et `PUT`.
    * Si ce n'est pas le cas, le client voit une erreur utile et claire.
  * Vérifier qu'il existe un paramètre de requête facultatif nommé `q` (comme dans `http://127.0.0.1:8000/items/foo?q=somequery`) pour les requêtes `GET`.
    * Puisque le paramètre `q` est déclaré avec `= None`, il est facultatif.
    * Sans le `None`, il serait nécessaire (comme l'est le corps de la requête dans le cas du `PUT`).
  * Pour les requêtes `PUT` vers `/items/{item_id}`, de lire le corps en JSON :
    * Vérifier qu'il a un attribut obligatoire `name` qui devrait être un `str`.
    * Vérifier qu'il a un attribut obligatoire `prix` qui doit être un `float`.
    * Vérifier qu'il a un attribut facultatif `is_offer`, qui devrait être un `bool`, s'il est présent.
    * Tout cela fonctionnerait également pour les objets JSON profondément imbriqués.
  * Convertir de et vers JSON automatiquement.
  * Documenter tout avec OpenAPI, qui peut être utilisé par :
    * Les systèmes de documentation interactifs.
    * Les systèmes de génération automatique de code client, pour de nombreuses langues.
  * Fournir directement 2 interfaces web de documentation interactive.


Nous n'avons fait qu'effleurer la surface, mais vous avez déjà une idée de la façon dont tout cela fonctionne.
Essayez de changer la ligne contenant :
```
  return {"item_name": item.name, "item_id": item_id}

```

... de :
```
    ... "item_name": item.name ...

```

... vers :
```
    ... "item_price": item.price ...

```

... et voyez comment votre éditeur complétera automatiquement les attributs et connaîtra leurs types :
![compatibilité IDE](https://fastapi.tiangolo.com/img/vscode-completion.png)
Pour un exemple plus complet comprenant plus de fonctionnalités, voir le Tutoriel - Guide utilisateur.
**Spoiler alert** : le tutoriel - guide utilisateur inclut :
  * Déclaration de **paramètres** provenant d'autres endroits différents comme : **en-têtes.**, **cookies** , **champs de formulaire** et **fichiers**.
  * L'utilisation de **contraintes de validation** comme `maximum_length` ou `regex`.
  * Un **système d'injection de dépendance** très puissant et facile à utiliser .
  * Sécurité et authentification, y compris la prise en charge de **OAuth2** avec les **jetons JWT** et l'authentification **HTTP Basic**.
  * Des techniques plus avancées (mais tout aussi faciles) pour déclarer les **modèles JSON profondément imbriqués** (grâce à Pydantic).
  * Intégration de **GraphQL** avec Strawberry et d'autres bibliothèques.
  * D'obtenir de nombreuses fonctionnalités supplémentaires (grâce à Starlette) comme :
    * **WebSockets**
    * de tester le code très facilement avec `requests` et `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ... et plus encore.


## Performance¶
Les benchmarks TechEmpower indépendants montrent que les applications **FastAPI** s'exécutant sous Uvicorn sont  parmi les frameworks existants en Python les plus rapides , juste derrière Starlette et Uvicorn (utilisés en interne par FastAPI). (*)
Pour en savoir plus, consultez la section Benchmarks.
## Dépendances facultatives¶
Utilisées par Pydantic:
  * `email-validator` - pour la validation des adresses email.


Utilisées par Starlette :
  * `requests` - Obligatoire si vous souhaitez utiliser `TestClient`.
  * `jinja2` - Obligatoire si vous souhaitez utiliser la configuration de template par défaut.
  * `python-multipart` - Obligatoire si vous souhaitez supporter le "décodage" de formulaire avec `request.form()`.
  * `itsdangerous` - Obligatoire pour la prise en charge de `SessionMiddleware`.
  * `pyyaml` - Obligatoire pour le support `SchemaGenerator` de Starlette (vous n'en avez probablement pas besoin avec FastAPI).


Utilisées par FastAPI / Starlette :
  * `uvicorn` - Pour le serveur qui charge et sert votre application.
  * `orjson` - Obligatoire si vous voulez utiliser `ORJSONResponse`.
  * `ujson` - Obligatoire si vous souhaitez utiliser `UJSONResponse`.


Vous pouvez tout installer avec `pip install fastapi[all]`.
## Licence¶
Ce projet est soumis aux termes de la licence MIT.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Retour en haut de la page 
  *[Complétion]: également connu sous le nom d'auto-complétion, autocomplétion, IntelliSense
  *[CLI]: Command Line Interface
  *[ CLI]: Command Line Interface
  *[JSON]: JavaScript Object Notation
  *[paramètre]: en anglais : path parameter
  *[paramètre de requête]: en anglais : query param
  *[le corps]: en anglais : body
  *[Une conversion]: aussi connu sous le nom de : serialization, parsing, marshalling
  *[les paramètres du chemin]: en anglais : path parameters
  *[les paramètres de la requête]: en anglais : query parameters
  *[les en-têtes]: en anglais : headers
  *[les formulaires]: en anglais : forms
  *[les fichiers]: en anglais : files
  *[La conversion]: aussi connu sous le nom de : serialization, parsing, marshalling
  *[en-têtes]: en anglais : headers
  *[système d'injection de dépendance]: aussi connu sous le nom de composants, ressources, fournisseurs, services, injectables
  *[ JWT]: JSON Web Tokens
  *[ JSON]: JavaScript Object Notation
  *[CORS]: Cross-Origin Resource Sharing
  *["décodage"]: convertit la chaine de caractère d'une requête HTTP en donnée Python
