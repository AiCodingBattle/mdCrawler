Ir para o conteúdo 
# FastAPI¶
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_Framework FastAPI, alta performance, fácil de aprender, fácil de codar, pronto para produção_
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master) ![Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ![Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package) ![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
**Documentação** : https://fastapi.tiangolo.com
**Código fonte** : https://github.com/fastapi/fastapi
FastAPI é um moderno e rápido (alta performance) _framework web_ para construção de APIs com Python, baseado nos _type hints_ padrões do Python.
Os recursos chave são:
  * **Rápido** : alta performance, equivalente a **NodeJS** e **Go** (graças ao Starlette e Pydantic). Um dos frameworks mais rápidos disponíveis.
  * **Rápido para codar** : Aumenta a velocidade para desenvolver recursos entre 200% a 300%. *
  * **Poucos bugs** : Reduz cerca de 40% de erros induzidos por humanos (desenvolvedores). *
  * **Intuitivo** : Grande suporte a _IDEs_. _Auto-Complete_ em todos os lugares. Menos tempo debugando.
  * **Fácil** : Projetado para ser fácil de aprender e usar. Menos tempo lendo documentação.
  * **Enxuto** : Minimize duplicação de código. Múltiplos recursos para cada declaração de parâmetro. Menos bugs.
  * **Robusto** : Tenha código pronto para produção. E com documentação interativa automática.
  * **Baseado em padrões** : Baseado em (e totalmente compatível com) os padrões abertos para APIs: OpenAPI (anteriormente conhecido como Swagger) e _JSON Schema_.


* estimativas baseadas em testes realizados com equipe interna de desenvolvimento, construindo aplicações em produção.
## Patrocinadores Ouro¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Outros patrocinadores
## Opiniões¶
"_[...] Estou usando**FastAPI** muito esses dias. [...] Estou na verdade planejando utilizar ele em todos os times de **serviços _Machine Learning_ na Microsoft**. Alguns deles estão sendo integrados no _core_ do produto **Windows** e alguns produtos **Office**._"
Kabir Khan - **Microsoft** (ref)
"_Nós adotamos a biblioteca**FastAPI** para iniciar um servidor **REST** que pode ser consultado para obter **previsões**. [para o Ludwig]_"
Piero Molino, Yaroslav Dudin, e Sai Sumanth Miryala - **Uber** (ref)
"_A**Netflix** tem o prazer de anunciar o lançamento open-source do nosso framework de orquestração de **gerenciamento de crises** : **Dispatch**! [criado com **FastAPI**]_"
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** (ref)
"_Estou extremamente entusiasmado com o**FastAPI**. É tão divertido!_"
Brian Okken - **Python Bytes podcaster** (ref)
"_Honestamente, o que você construiu parece super sólido e rebuscado. De muitas formas, eu queria que o**Hug** fosse assim - é realmente inspirador ver alguém que construiu ele._"
Timothy Crosley - **criador doHug** (ref)
"_Se você está procurando aprender um** _framework_ moderno** para construir aplicações _REST_ , dê uma olhada no **FastAPI** [...] É rápido, fácil de usar e fácil de aprender [...]_"
"_Nós trocamos nossas**APIs** por **FastAPI** [...] Acredito que vocês gostarão dele [...]_"
Ines Montani - Matthew Honnibal - **fundadores daExplosion AI - criadores da spaCy** (ref) - (ref)
"_Se alguém estiver procurando construir uma API Python para produção, eu recomendaria fortemente o**FastAPI**. Ele é **lindamente projetado** , **simples de usar** e **altamente escalável**. Ele se tornou um **componente chave** para a nossa estratégia API first de desenvolvimento e está impulsionando diversas automações e serviços, como o nosso Virtual TAC Engineer._"
Deon Pillsbury - **Cisco** (ref)
## **Typer** , o FastAPI das interfaces de linhas de comando¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
Se você estiver construindo uma aplicação _CLI_ para ser utilizada em um terminal ao invés de uma aplicação web, dê uma olhada no **Typer**.
**Typer** é o irmão menor do FastAPI. E seu propósito é ser o **FastAPI das _CLIs_**. ⌨️ 🚀
## Requisitos¶
FastAPI está nos ombros de gigantes:
  * Starlette para as partes web.
  * Pydantic para a parte de dados.


## Instalação¶
Crie e ative um ambiente virtual, e então instale o FastAPI:
```

fast →pip install "fastapi[standard]"restart ↻

```

**Nota** : Certifique-se de que você colocou `"fastapi[standard]"` com aspas, para garantir que funcione em todos os terminais.
## Exemplo¶
### Crie¶
  * Crie um arquivo `main.py` com:


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

Ou use `async def`...
Se seu código utiliza `async` / `await`, use `async def`:
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
Se você não sabe, verifique a seção _"Com pressa?"_ sobre `async` e `await` nas docs.
### Rode¶
Rode o servidor com:
```

fast →fastapi dev main.py ╭────────── FastAPI CLI - Development mode ───────────╮ │                           │ │ Serving at: http://127.0.0.1:8000         │ │                           │ │ API docs: http://127.0.0.1:8000/docs        │ │                           │ │ Running in development mode, for production use:  │ │                           │ │ fastapi run                    │ │                           │ ╰─────────────────────────────────────────────────────╯INFO:   Will watch for changes in these directories: ['/home/user/code/awesomeapp']INFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [2248755] using WatchFilesINFO:   Started server process [2248757]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

Sobre o comando `fastapi dev main.py`...
O comando `fastapi dev` lê o seu arquivo `main.py`, identifica o aplicativo **FastAPI** nele, e inicia um servidor usando o Uvicorn.
Por padrão, o `fastapi dev` iniciará com _auto-reload_ habilitado para desenvolvimento local.
Você pode ler mais sobre isso na documentação do FastAPI CLI.
### Verifique¶
Abra seu navegador em http://127.0.0.1:8000/items/5?q=somequery.
Você verá a resposta JSON como:
```
{"item_id":5,"q":"somequery"}

```

Você acabou de criar uma API que:
  * Recebe requisições HTTP nas _rotas_ `/` e `/items/{item_id}`.
  * Ambas _rotas_ fazem _operações_ `GET` (também conhecido como _métodos_ HTTP).
  * A _rota_ `/items/{item_id}` tem um _parâmetro de rota_ `item_id` que deve ser um `int`.
  * A _rota_ `/items/{item_id}` tem um _parâmetro query_ `q` `str` opcional.


### Documentação Interativa da API¶
Agora vá para http://127.0.0.1:8000/docs.
Você verá a documentação automática interativa da API (fornecida por Swagger UI):
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Documentação Alternativa da API¶
E agora, vá para http://127.0.0.1:8000/redoc.
Você verá a documentação automática alternativa (fornecida por ReDoc):
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Evoluindo o Exemplo¶
Agora modifique o arquivo `main.py` para receber um corpo para uma requisição `PUT`.
Declare o corpo utilizando tipos padrão Python, graças ao Pydantic.
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

O servidor `fastapi dev` deverá recarregar automaticamente.
### Evoluindo a Documentação Interativa da API¶
Agora vá para http://127.0.0.1:8000/docs.
  * A documentação interativa da API será automaticamente atualizada, incluindo o novo corpo:


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * Clique no botão "Try it out", ele permitirá que você preencha os parâmetros e interaja diretamente com a API:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Então clique no botão "Execute", a interface do usuário irá se comunicar com a API, enviar os parâmetros, pegar os resultados e mostrá-los na tela:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Evoluindo a Documentação Alternativa da API¶
E agora, vá para http://127.0.0.1:8000/redoc.
  * A documentação alternativa também irá refletir o novo parâmetro da _query_ e o corpo:


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### Recapitulando¶
Resumindo, você declara **uma vez** os tipos dos parâmetros, corpo etc. como parâmetros de função.
Você faz isso com os tipos padrão do Python moderno.
Você não terá que aprender uma nova sintaxe, métodos ou classes de uma biblioteca específica etc.
Apenas **Python** padrão.
Por exemplo, para um `int`:
```
item_id: int

```

ou para um modelo mais complexo, `Item`:
```
item: Item

```

...e com essa única declaração você tem:
  * Suporte ao Editor, incluindo:
    * Completação.
    * Verificação de tipos.
  * Validação de dados:
    * Erros automáticos e claros quando o dado é inválido.
    * Validação até para objetos JSON profundamente aninhados.
  * Conversão de dados de entrada: vindo da rede para dados e tipos Python. Consegue ler:
    * JSON.
    * Parâmetros de rota.
    * Parâmetros de _query_ .
    * _Cookies_.
    * Cabeçalhos.
    * Formulários.
    * Arquivos.
  * Conversão de dados de saída de tipos e dados Python para dados de rede (como JSON):
    * Converte tipos Python (`str`, `int`, `float`, `bool`, `list` etc).
    * Objetos `datetime`.
    * Objetos `UUID`.
    * Modelos de Banco de Dados.
    * ...e muito mais.
  * Documentação interativa automática da API, incluindo 2 alternativas de interface de usuário:
    * Swagger UI.
    * ReDoc.


Voltando ao código do exemplo anterior, **FastAPI** irá:
  * Validar que existe um `item_id` na rota para requisições `GET` e `PUT`.
  * Validar que `item_id` é do tipo `int` para requisições `GET` e `PUT`.
    * Se não é validado, o cliente verá um útil, claro erro.
  * Verificar se existe um parâmetro de _query_ opcional nomeado como `q` (como em `http://127.0.0.1:8000/items/foo?q=somequery`) para requisições `GET`.
    * Como o parâmetro `q` é declarado com `= None`, ele é opcional.
    * Sem o `None` ele poderia ser obrigatório (como o corpo no caso de `PUT`).
  * Para requisições `PUT` para `/items/{item_id}`, lerá o corpo como JSON e:
    * Verifica que tem um atributo obrigatório `name` que deve ser `str`.
    * Verifica que tem um atributo obrigatório `price` que deve ser `float`.
    * Verifica que tem an atributo opcional `is_offer`, que deve ser `bool`, se presente.
    * Tudo isso também funciona para objetos JSON profundamente aninhados.
  * Converter de e para JSON automaticamente.
  * Documentar tudo com OpenAPI, que poderá ser usado por:
    * Sistemas de documentação interativos.
    * Sistemas de clientes de geração de código automáticos, para muitas linguagens.
  * Fornecer diretamente 2 interfaces _web_ de documentação interativa.


Nós apenas arranhamos a superfície, mas você já tem idéia de como tudo funciona.
Experimente mudar a seguinte linha:
```
  return {"item_name": item.name, "item_id": item_id}

```

...de:
```
    ... "item_name": item.name ...

```

...para:
```
    ... "item_price": item.price ...

```

...e veja como seu editor irá auto-completar os atributos e saberá os tipos:
![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)
Para um exemplo mais completo incluindo mais recursos, veja Tutorial - Guia do Usuário.
**Alerta de Spoiler** : o tutorial - guia do usuário inclui:
  * Declaração de **parâmetetros** de diferentes lugares como: **cabeçalhos** , **cookies** , **campos de formulários** e **arquivos**.
  * Como configurar **Limitações de Validação** como `maximum_length` ou `regex`.
  * Um poderoso e fácil de usar sistema de **Injeção de Dependência**.
  * Segurança e autenticação, incluindo suporte para **OAuth2** com autenticação **JWT tokens** e **HTTP Basic**.
  * Técnicas mais avançadas (mas igualmente fáceis) para declaração de **modelos JSON profundamente aninhados** (graças ao Pydantic).
  * Integrações **GraphQL** com o Strawberry e outras bibliotecas.
  * Muitos recursos extras (graças ao Starlette) como:
    * **WebSockets**
    * testes extrememamente fáceis baseados em HTTPX e `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...e mais.


## Performance¶
Testes de performance da _Independent TechEmpower_ mostram aplicações **FastAPI** rodando sob Uvicorn como um dos _frameworks_ Python mais rápidos disponíveis, somente atrás de Starlette e Uvicorn (utilizados internamente pelo FastAPI). (*)
Para entender mais sobre performance, veja a seção Comparações.
## Dependências¶
O FastAPI depende do Pydantic e do Starlette.
### Dependências `standard`¶
Quando você instala o FastAPI com `pip install "fastapi[standard]"`, ele vêm com o grupo `standard` (padrão) de dependências opcionais:
Utilizado pelo Pydantic:
  * `email-validator` - para validação de email.


Utilizado pelo Starlette:
  * `httpx` - Obrigatório caso você queira utilizar o `TestClient`.
  * `jinja2` - Obrigatório se você quer utilizar a configuração padrão de templates.
  * `python-multipart` - Obrigatório se você deseja suporte a "parsing" de formulário, com `request.form()`.


Utilizado pelo FastAPI / Starlette:
  * `uvicorn` - para o servidor que carrega e serve a sua aplicação. Isto inclui `uvicorn[standard]`, que inclui algumas dependências (e.g. `uvloop`) necessárias para servir em alta performance.
  * `fastapi-cli` - que disponibiliza o comando `fastapi`.


### Sem as dependências `standard`¶
Se você não deseja incluir as dependências opcionais `standard`, você pode instalar utilizando `pip install fastapi` ao invés de `pip install "fastapi[standard]"`.
### Dpendências opcionais adicionais¶
Existem algumas dependências adicionais que você pode querer instalar.
Dependências opcionais adicionais do Pydantic:
  * `pydantic-settings` - para gerenciamento de configurações.
  * `pydantic-extra-types` - tipos extras para serem utilizados com o Pydantic.


Dependências opcionais adicionais do FastAPI:
  * `orjson` - Obrigatório se você deseja utilizar o `ORJSONResponse`.
  * `ujson` - Obrigatório se você deseja utilizar o `UJSONResponse`.


## Licença¶
Esse projeto é licenciado sob os termos da licença MIT.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Voltar ao topo 
  *[_Auto-Complete_]: também conhecido como _auto-complete_, _autocompletion_, _IntelliSense_
  *[_CLI_]: Command Line Interface
  *[Conversão]: também conhecido como: serialization, parsing, marshalling
  *[Injeção de Dependência]: também conhecido como componentes, recursos, fornecedores, serviços, injetáveis
  *["parsing"]: converting the string that comes from an HTTP request into Python data
