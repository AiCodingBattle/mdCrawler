コンテンツにスキップ 
# FastAPI¶
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_FastAPI framework, high performance, easy to learn, fast to code, ready for production_
![Build Status](https://travis-ci.com/fastapi/fastapi.svg?branch=master) ![Coverage](https://img.shields.io/codecov/c/github/fastapi/fastapi) ![Package version](https://badge.fury.io/py/fastapi.svg)
**ドキュメント** : https://fastapi.tiangolo.com
**ソースコード** : https://github.com/fastapi/fastapi
FastAPI は、Pythonの標準である型ヒントに基づいてPython 以降でAPI を構築するための、モダンで、高速(高パフォーマンス)な、Web フレームワークです。
主な特徴:
  * **高速** : **NodeJS** や **Go** 並みのとても高いパフォーマンス (Starlette と Pydantic のおかげです)。 最も高速な Python フレームワークの一つです.
  * **高速なコーディング** : 開発速度を約 200%~300%向上させます。 *
  * **少ないバグ** : 開発者起因のヒューマンエラーを約 40％削減します。 *
  * **直感的** : 素晴らしいエディタのサポートや オートコンプリート。 デバッグ時間を削減します。
  * **簡単** : 簡単に利用、習得できるようにデザインされています。ドキュメントを読む時間を削減します。
  * **短い** : コードの重複を最小限にしています。各パラメータからの複数の機能。少ないバグ。
  * **堅牢性** : 自動対話ドキュメントを使用して、本番環境で使用できるコードを取得します。
  * **Standards-based** : API のオープンスタンダードに基づいており、完全に互換性があります: OpenAPI (以前は Swagger として知られていました) や JSON スキーマ.


* 本番アプリケーションを構築している開発チームのテストによる見積もり。
## Sponsors¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Other sponsors
## 評価¶
"_[...] 最近**FastAPI** を使っています。 [...] 実際に私のチームの全ての **Microsoft の機械学習サービス** で使用する予定です。 そのうちのいくつかのコアな**Windows** 製品と**Office** 製品に統合されつつあります。_"
Kabir Khan - **Microsoft** (ref)
"_FastAPIライブラリを採用し、クエリで**予測値** を取得できる**REST** サーバを構築しました。 [for Ludwig]_"
Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber** (ref)
"_**Netflix** は、**危機管理** オーケストレーションフレームワーク、**Dispatch** のオープンソースリリースを発表できることをうれしく思います。 [built with **FastAPI**]_"
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** (ref)
"_私は**FastAPI** にワクワクしています。 めちゃくちゃ楽しいです！_"
Brian Okken - **Python Bytes podcast host** (ref)
"_正直、超堅実で洗練されているように見えます。いろんな意味で、それは私がハグしたかったものです。_ "
Timothy Crosley - **Hug creator** (ref)
"_REST API を構築するための**モダンなフレームワーク** を学びたい方は、**FastAPI** [...] をチェックしてみてください。 [...] 高速で, 使用、習得が簡単です。[...]_"
"_私たちの**API** は**FastAPI** に切り替えました。[...] きっと気に入ると思います。 [...]_"
Ines Montani - Matthew Honnibal - **Explosion AI founders - spaCy creators** (ref) - (ref)
## **Typer** , the FastAPI of CLIs¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
もし Web API の代わりにターミナルで使用するCLIアプリを構築する場合は、**Typer**を確認してください。
**Typer** は FastAPI の弟分です。そして、**CLI 版 の FastAPI** を意味しています。
## 必要条件¶
FastAPI は巨人の肩の上に立っています。
  * Web の部分はStarlette
  * データの部分はPydantic


## インストール¶
```

fast →pip install fastapirestart ↻

```

本番環境では、Uvicorn または、 Hypercornのような、 ASGI サーバーが必要になります。
```

fast →pip install "uvicorn[standard]"restart ↻

```

## アプリケーション例¶
### アプリケーションの作成¶
  * `main.py` を作成し、以下のコードを入力します:


```
fromfastapiimport FastAPI
app = FastAPI()
@app.get("/")
defread_root():
  return {"Hello": "World"}
@app.get("/items/{item_id}")
defread_item(item_id: int, q: str = None):
  return {"item_id": item_id, "q": q}

```

または`async def`を使います...
`async` / `await`を使用するときは、 `async def`を使います:
```
fromfastapiimport FastAPI
app = FastAPI()
@app.get("/")
async defread_root():
  return {"Hello": "World"}
@app.get("/items/{item_id}")
async defread_item(item_id: int, q: str = None):
  return {"item_id": item_id, "q": q}

```

**注** :
わからない場合は、ドキュメントの`async` と `await`にある"In a hurry?"セクションをチェックしてください。
### 実行¶
以下のコマンドでサーバーを起動します:
```

fast →uvicorn main:app --reloadINFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [28720]INFO:   Started server process [28722]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

`uvicorn main:app --reload`コマンドについて
`uvicorn main:app`コマンドは以下の項目を参照します:
  * `main`: `main.py`ファイル (Python "モジュール")
  * `app`: `main.py` の`app = FastAPI()`の行で生成されたオブジェクト
  * `--reload`: コードを変更したらサーバーを再起動します。このオプションは開発環境でのみ使用します


### 動作確認¶
ブラウザからhttp://127.0.0.1:8000/items/5?q=somequeryを開きます。
以下の JSON のレスポンスが確認できます:
```
{"item_id":5,"q":"somequery"}

```

もうすでに以下の API が作成されています:
  * `/` と `/items/{item_id}`のパスで HTTP リクエストを受けます。
  * どちらのパスも `GET` _操作_ を取ります。(HTTP メソッドとしても知られています。)
  * `/items/{item_id}` パスのパスパラメータ `item_id` は `int` でなければなりません。
  * パス `/items/{item_id}` はオプションの `str` クエリパラメータ `q` を持ちます。


### 自動対話型の API ドキュメント¶
http://127.0.0.1:8000/docsにアクセスしてみてください。
自動対話型の API ドキュメントが表示されます。 (Swagger UIが提供しています。):
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### 代替の API ドキュメント¶
http://127.0.0.1:8000/redocにアクセスしてみてください。
代替の自動ドキュメントが表示されます。(ReDocが提供しています。):
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## アップグレード例¶
`PUT`リクエストからボディを受け取るために`main.py`を修正しましょう。
Pydantic によって、Python の標準的な型を使ってボディを宣言します。
```
fromfastapiimport FastAPI
frompydanticimport BaseModel
app = FastAPI()
classItem(BaseModel):
  name: str
  price: float
  is_offer: bool = None
@app.get("/")
defread_root():
  return {"Hello": "World"}
@app.get("/items/{item_id}")
defread_item(item_id: int, q: str = None):
  return {"item_id": item_id, "q": q}
@app.put("/items/{item_id}")
defupdate_item(item_id: int, item: Item):
  return {"item_name": item.name, "item_id": item_id}

```

サーバーは自動でリロードされます。(上述の`uvicorn`コマンドで`--reload`オプションを追加しているからです。)
### 自動対話型の API ドキュメントのアップグレード¶
http://127.0.0.1:8000/docsにアクセスしましょう。
  * 自動対話型の API ドキュメントが新しいボディも含めて自動でアップデートされます:


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * "Try it out"ボタンをクリックしてください。パラメータを入力して API と直接やりとりすることができます:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * それから、"Execute" ボタンをクリックしてください。 ユーザーインターフェースは API と通信し、パラメータを送信し、結果を取得して画面に表示します:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### 代替の API ドキュメントのアップグレード¶
http://127.0.0.1:8000/redocにアクセスしましょう。
  * 代替の API ドキュメントにも新しいクエリパラメータやボディが反映されます。


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### まとめ¶
要約すると、関数のパラメータとして、パラメータやボディ などの型を**一度だけ** 宣言します。
標準的な最新の Python の型を使っています。
新しい構文や特定のライブラリのメソッドやクラスなどを覚える必要はありません。
単なる標準的な**3.8 以降の Python** です。
例えば、`int`の場合:
```
item_id: int

```

または、より複雑な`Item`モデルの場合:
```
item: Item

```

...そして、この一度の宣言で、以下のようになります:
  * 以下を含むエディタサポート:
  * 補完
  * タイプチェック
  * データの検証:
  * データが無効な場合に自動でエラーをクリアします。
  * 深い入れ子になった JSON オブジェクトでも検証が可能です。
  * 入力データの変換: ネットワークから Python のデータや型に変換してから読み取ります:
  * JSON.
  * パスパラメータ
  * クエリパラメータ
  * クッキー
  * ヘッダー
  * フォーム
  * ファイル
  * 出力データの変換: Python のデータや型からネットワークデータへ変換します (JSON として):
  * Convert Python types (`str`, `int`, `float`, `bool`, `list`, etc).
  * `datetime` オブジェクト
  * `UUID` オブジェクト
  * データベースモデル
  * ...などなど
  * 2 つの代替ユーザーインターフェースを含む自動インタラクティブ API ドキュメント:
  * Swagger UI.
  * ReDoc.


コード例に戻りましょう、**FastAPI** は次のようになります:
  * `GET`および`PUT`リクエストのパスに`item_id` があることを検証します。
  * `item_id`が`GET`および`PUT`リクエストに対して`int` 型であることを検証します。
  * そうでない場合は、クライアントは有用で明確なエラーが表示されます。
  * `GET` リクエストに対してオプションのクエリパラメータ `q` (`http://127.0.0.1:8000/items/foo?q=somequery` のように) が存在するかどうかを調べます。
  * パラメータ `q` は `= None` で宣言されているので、オプションです。
  * `None`がなければ必須になります（`PUT`の場合のボディと同様です）。
  * `PUT` リクエストを `/items/{item_id}` に送信する場合は、ボディを JSON として読み込みます:
  * 必須の属性 `name` を確認してください。 それは `str` であるべきです。
  * 必須の属性 `price` を確認してください。それは `float` でなければならないです。
  * オプションの属性 `is_offer` を確認してください。値がある場合は、`bool` であるべきです。
  * これらはすべて、深くネストされた JSON オブジェクトに対しても動作します。
  * JSON から JSON に自動的に変換します。
  * OpenAPIですべてを文書化し、以下を使用することができます:
  * 対話的なドキュメントシステム。
  * 多くの言語に対応した自動クライアントコード生成システム。
  * 2 つの対話的なドキュメントのWebインターフェイスを直接提供します。


まだ表面的な部分に触れただけですが、もう全ての仕組みは分かっているはずです。
以下の行を変更してみてください:
```
  return {"item_name": item.name, "item_id": item_id}

```

...以下を:
```
    ... "item_name": item.name ...

```

...以下のように:
```
    ... "item_price": item.price ...

```

...そして、エディタが属性を自動補完し、そのタイプを知る方法を確認してください。:
![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)
より多くの機能を含む、より完全な例については、チュートリアル - ユーザーガイドをご覧ください。
**ネタバレ注意** : チュートリアル - ユーザーガイドは以下の情報が含まれています:
  * **ヘッダー** 、**クッキー** 、**フォームフィールド** 、**ファイル** などの他の場所からの **パラメータ** 宣言。
  * `maximum_length`や`regex`のような**検証や制約** を設定する方法。
  * 非常に強力で使いやすい **依存性注入** システム。
  * **JWT トークン** を用いた **OAuth2** や **HTTP Basic 認証** のサポートを含む、セキュリティと認証。
  * **深くネストされた JSON モデル** を宣言するためのより高度な（しかし同様に簡単な）技術（Pydantic のおかげです）。
  * 以下のようなたくさんのおまけ機能(Starlette のおかげです):
  * **WebSockets**
  * **GraphQL**
  * `httpx` や `pytest`をもとにした極限に簡単なテスト
  * **CORS**
  * **クッキーセッション**
  * ...などなど。


## パフォーマンス¶
独立した TechEmpower のベンチマークでは、Uvicorn で動作する**FastAPI** アプリケーションが、Python フレームワークの中で最も高速なものの 1 つであり、Starlette と Uvicorn（FastAPI で内部的に使用されています）にのみ下回っていると示されています。
詳細はベンチマークセクションをご覧ください。
## オプションの依存関係¶
Pydantic によって使用されるもの:
  * `email-validator` - E メールの検証


Starlette によって使用されるもの:
  * `httpx` - `TestClient`を使用するために必要です。
  * `jinja2` - デフォルトのテンプレート設定を使用する場合は必要です。
  * `python-multipart` - "parsing"`request.form()`からの変換をサポートしたい場合は必要です。
  * `itsdangerous` - `SessionMiddleware` サポートのためには必要です。
  * `pyyaml` - Starlette の `SchemaGenerator` サポートのために必要です。 (FastAPI では必要ないでしょう。)
  * `graphene` - `GraphQLApp` サポートのためには必要です。


FastAPI / Starlette に使用されるもの:
  * `uvicorn` - アプリケーションをロードしてサーブするサーバーのため。
  * `orjson` - `ORJSONResponse`を使用したい場合は必要です。
  * `ujson` - `UJSONResponse`を使用する場合は必須です。


これらは全て `pip install fastapi[all]`でインストールできます。
## ライセンス¶
このプロジェクトは MIT ライセンスです。
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
ページトップへ戻る 
  *[オートコンプリート。]: also known as auto-complete, autocompletion, IntelliSense
  *[CLI]: Command Line Interface
  *[変換]: also known as: serialization, parsing, marshalling
  *[**依存性注入**]: also known as components, resources, providers, services, injectables
  *["parsing"]: converting the string that comes from an HTTP request into Python data
