Ana içeriğe geç 
# FastAPI¶
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_FastAPI framework, yüksek performanslı, öğrenmesi oldukça kolay, kodlaması hızlı, kullanıma hazır_
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master) ![Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ![Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package) ![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
**Dokümantasyon** : https://fastapi.tiangolo.com
**Kaynak Kod** : https://github.com/fastapi/fastapi
FastAPI, Python 'nin standart tip belirteçlerine dayalı, modern ve hızlı (yüksek performanslı) API'lar oluşturmak için kullanılabilecek web framework'tür.
Temel özellikleri şunlardır:
  * **Hızlı** : Çok yüksek performanslı, **NodeJS** ve **Go** ile eşit düzeyde (Starlette ve Pydantic sayesinde). En hızlı Python framework'lerinden bir tanesidir.
  * **Kodlaması Hızlı** : Geliştirme hızını yaklaşık %200 ile %300 aralığında arttırır. *
  * **Daha az hata** : İnsan (geliştirici) kaynaklı hataları yaklaşık %40 azaltır. *
  * **Sezgisel** : Muhteşem bir editör desteği. Her yerde otomatik tamamlama. Hata ayıklama ile daha az zaman harcayacaksınız.
  * **Kolay** : Öğrenmesi ve kullanması kolay olacak şekilde tasarlandı. Doküman okuma ile daha az zaman harcayacaksınız.
  * **Kısa** : Kod tekrarı minimize edildi. Her parametre tanımlamasında birden fazla özellik ve daha az hatayla karşılaşacaksınız.
  * **Güçlü** : Otomatik ve etkileşimli dokümantasyon ile birlikte, kullanıma hazır kod elde edebilirsiniz.
  * **Standard öncelikli** : API'lar için açık standartlara dayalı (ve tamamen uyumlu); OpenAPI (eski adıyla Swagger) ve JSON Schema.


* ilgili kanılar, dahili geliştirme ekibinin geliştirdikleri ürünlere yaptıkları testlere dayanmaktadır.
## Sponsorlar¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Diğer Sponsorlar
## Görüşler¶
"_[...] Bugünlerde**FastAPI** 'ı çok fazla kullanıyorum. [...] Aslında bunu ekibimin **Microsoft'taki Machine Learning servislerinin** tamamında kullanmayı planlıyorum. Bunlardan bazıları **Windows** 'un ana ürünlerine ve **Office** ürünlerine entegre ediliyor._"
Kabir Khan - **Microsoft** (ref)
"_**FastAPI** 'ı **tahminlerimiz** 'i sorgulanabilir hale getirecek bir **REST** sunucu oluşturmak için benimsedik/kullanmaya başladık._"
Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber** (ref)
"_**Netflix** , **kriz yönetiminde** orkestrasyon yapabilmek için geliştirdiği yeni framework'ü **Dispatch** 'in, açık kaynak sürümünü paylaşmaktan gurur duyuyor. [**FastAPI** ile yapıldı.]_"
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** (ref)
"_**FastAPI** için ayın üzerindeymişcesine heyecanlıyım. Çok eğlenceli!_"
Brian Okken - **Python Bytes podcast host** (ref)
"_Dürüst olmak gerekirse, inşa ettiğiniz şey gerçekten sağlam ve profesyonel görünüyor. Birçok açıdan**Hug** 'ın olmasını istediğim şey tam da bu - böyle bir şeyi inşa eden birini görmek gerçekten ilham verici._"
Timothy Crosley - **Hug'ın Yaratıcısı** (ref)
"_Eğer REST API geliştirmek için**modern bir framework** öğrenme arayışında isen, **FastAPI** 'a bir göz at [...] Hızlı, kullanımı ve öğrenmesi kolay. [...]_"
"_**API** servislerimizi **FastAPI** 'a taşıdık [...] Sizin de beğeneceğinizi düşünüyoruz. [...]_"
Ines Montani - Matthew Honnibal - **Explosion AI kurucuları - spaCy yaratıcıları** (ref) - (ref)
"_Python ile kullanıma hazır bir API oluşturmak isteyen herhangi biri için,**FastAPI** 'ı şiddetle tavsiye ederim. **Harika tasarlanmış** , **kullanımı kolay** ve **yüksek ölçeklenebilir** , API odaklı geliştirme stratejimizin **ana bileşeni** haline geldi ve Virtual TAC Engineer gibi birçok otomasyon ve servisi yönetiyor._"
Deon Pillsbury - **Cisco** (ref)
## Komut Satırı Uygulamalarının FastAPI'ı: **Typer**¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
Eğer API yerine, terminalde kullanılmak üzere bir komut satırı uygulaması geliştiriyorsanız **Typer**'a göz atabilirsiniz.
**Typer** kısaca FastAPI'ın küçük kardeşi. Ve hedefi komut satırı uygulamalarının **FastAPI'ı** olmak. ⌨️ 🚀
## Gereksinimler¶
FastAPI iki devin omuzları üstünde duruyor:
  * Web tarafı için Starlette.
  * Data tarafı için Pydantic.


## Kurulum¶
```

fast →pip install fastapirestart ↻

```

Uygulamamızı kullanılabilir hale getirmek için Uvicorn ya da Hypercorn gibi bir ASGI sunucusuna ihtiyacımız olacak.
```

fast →pip install "uvicorn[standard]"restart ↻

```

## Örnek¶
### Kodu Oluşturalım¶
  * `main.py` adında bir dosya oluşturup içine şu kodu yapıştıralım:


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

Ya da `async def`...
Eğer kodunuzda `async` / `await` varsa, `async def` kullanalım:
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

**Not** :
Eğer bu konu hakkında bilginiz yoksa `async` ve `await` dokümantasyonundaki _"Aceleniz mi var?"_ kısmını kontrol edebilirsiniz.
### Kodu Çalıştıralım¶
Sunucuyu aşağıdaki komutla çalıştıralım:
```

fast →uvicorn main:app --reloadINFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [28720]INFO:   Started server process [28722]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

`uvicorn main:app --reload` komutuyla ilgili...
`uvicorn main:app` komutunu şu şekilde açıklayabiliriz:
  * `main`: dosya olan `main.py` (yani Python "modülü").
  * `app`: ise `main.py` dosyasının içerisinde `app = FastAPI()` satırında oluşturduğumuz `FastAPI` nesnesi.
  * `--reload`: kod değişikliklerinin ardından sunucuyu otomatik olarak yeniden başlatır. Bu parameteyi sadece geliştirme aşamasında kullanmalıyız.


### Şimdi de Kontrol Edelim¶
Tarayıcımızda şu bağlantıyı açalım http://127.0.0.1:8000/items/5?q=somequery.
Aşağıdaki gibi bir JSON yanıtıyla karşılaşacağız:
```
{"item_id":5,"q":"somequery"}

```

Az önce oluşturduğumuz API:
  * `/` ve `/items/{item_id}` _yollarına_ HTTP isteği alabilir.
  * İki _yolda_ `GET` _operasyonlarını_ (HTTP _metodları_ olarak da bilinen) kabul ediyor.
  * `/items/{item_id}` _yolu_ `item_id` adında bir _yol parametresine_ sahip ve bu parametre `int` değer almak zorundadır.
  * `/items/{item_id}` _yolu_ `q` adında bir _yol parametresine_ sahip ve bu parametre opsiyonel olmakla birlikte, `str` değer almak zorundadır.


### Etkileşimli API Dokümantasyonu¶
Şimdi http://127.0.0.1:8000/docs bağlantısını açalım.
Swagger UI tarafından sağlanan otomatik etkileşimli bir API dokümantasyonu göreceğiz:
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Alternatif API Dokümantasyonu¶
Şimdi http://127.0.0.1:8000/redoc bağlantısını açalım.
ReDoc tarafından sağlanan otomatik dokümantasyonu göreceğiz:
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Örneği Güncelleyelim¶
Şimdi `main.py` dosyasını, `PUT` isteğiyle birlikte bir gövde alacak şekilde değiştirelim.
Gövdeyi Pydantic sayesinde standart python tiplerini kullanarak tanımlayalım.
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

Sunucu otomatik olarak yeniden başlamış olmalı (çünkü yukarıda `uvicorn` komutuyla birlikte `--reload` parametresini kullandık).
### Etkileşimli API Dokümantasyonundaki Değişimi Görelim¶
Şimdi http://127.0.0.1:8000/docs bağlantısına tekrar gidelim.
  * Etkileşimli API dokümantasyonu, yeni gövdede dahil olmak üzere otomatik olarak güncellenmiş olacak:


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * "Try it out" butonuna tıklayalım, bu işlem API parametleri üzerinde değişiklik yapmamıza ve doğrudan API ile etkileşime geçmemize imkan sağlayacak:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Şimdi "Execute" butonuna tıklayalım, kullanıcı arayüzü API'ımız ile bağlantı kurup parametreleri gönderecek ve sonucu ekranımıza getirecek:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Alternatif API Dokümantasyonundaki Değişimi Görelim¶
Şimdi ise http://127.0.0.1:8000/redoc bağlantısına tekrar gidelim.
  * Alternatif dokümantasyonda yaptığımız değişiklikler ile birlikte yeni sorgu parametresi ve gövde bilgisi ile güncelemiş olacak:


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### Özet¶
Özetlemek gerekirse, parametrelerin, gövdenin, vb. veri tiplerini fonksiyon parametreleri olarak **bir kere** tanımlıyoruz.
Bu işlemi standart modern Python tipleriyle yapıyoruz.
Yeni bir sözdizimi yapısını, bir kütüphane özel metod veya sınıfları öğrenmeye gerek yoktur.
Hepsi sadece **Python** standartlarına dayalıdır.
Örnek olarak, `int` tanımlamak için:
```
item_id: int

```

ya da daha kompleks herhangi bir python modelini tanımlayabiliriz, örneğin `Item` modeli için:
```
item: Item

```

...ve sadece kısa bir parametre tipi belirterek elde ettiklerimiz:
  * Editör desteğiyle birlikte:
    * Otomatik tamamlama.
    * Tip kontrolü.
  * Veri Doğrulama:
    * Veri geçerli değilse, otomatik olarak açıklayıcı hatalar gösterir.
    * Çok derin JSON nesnelerinde bile doğrulama yapar.
  * Gelen verinin dönüşümünü aşağıdaki veri tiplerini kullanarak gerçekleştirir:
    * JSON.
    * Yol parametreleri.
    * Sorgu parametreleri.
    * Çerezler.
    * Headers.
    * Formlar.
    * Dosyalar.
  * Giden verinin dönüşümünü aşağıdaki veri tiplerini kullanarak gerçekleştirir (JSON olarak):
    * Python tiplerinin (`str`, `int`, `float`, `bool`, `list`, vb) dönüşümü.
    * `datetime` nesnesi.
    * `UUID` nesnesi.
    * Veritabanı modelleri.
    * ve çok daha fazlası...
  * 2 alternatif kullanıcı arayüzü dahil olmak üzere, otomatik etkileşimli API dokümantasyonu sağlar:
    * Swagger UI.
    * ReDoc.


Az önceki örneğe geri dönelim, **FastAPI** 'ın yapacaklarına bir bakış atalım:
  * `item_id`'nin `GET` ve `PUT` istekleri için, yolda olup olmadığının kontol edecek.
  * `item_id`'nin `GET` ve `PUT` istekleri için, tipinin `int` olduğunu doğrulayacak.
    * Eğer değilse, sebebini belirten bir hata mesajı gösterecek.
  * Opsiyonel bir `q` parametresinin `GET` isteği içinde (`http://127.0.0.1:8000/items/foo?q=somequery` gibi) olup olmadığını kontrol edecek
    * `q` parametresini `= None` ile oluşturduğumuz için, opsiyonel bir parametre olacak.
    * Eğer `None` olmasa zorunlu bir parametre olacaktı (`PUT` metodunun gövdesinde olduğu gibi).
  * `PUT` isteği için `/items/{item_id}`'nin gövdesini, JSON olarak doğrulayıp okuyacak:
    * `name` adında zorunlu bir parametre olup olmadığını ve varsa tipinin `str` olup olmadığını kontol edecek.
    * `price` adında zorunlu bir parametre olup olmadığını ve varsa tipinin `float` olup olmadığını kontol edecek.
    * `is_offer` adında opsiyonel bir parametre olup olmadığını ve varsa tipinin `float` olup olmadığını kontol edecek.
    * Bunların hepsi en derin JSON nesnelerinde bile çalışacak.
  * Verilerin JSON'a ve JSON'ın python nesnesine dönüşümü otomatik olarak yapılacak.
  * Her şeyi OpenAPI ile uyumlu bir şekilde otomatik olarak dokümanlayacak ve bunlarda aşağıdaki gibi kullanılabilecek:
    * Etkileşimli dokümantasyon sistemleri.
    * Bir çok programlama dili için otomatik istemci kodu üretim sistemleri.
  * İki ayrı etkileşimli dokümantasyon arayüzünü doğrudan sağlayacak.


Daha yeni başladık ama çalışma mantığını çoktan anlamış oldunuz.
Şimdi aşağıdaki satırı değiştirmeyi deneyin:
```
  return {"item_name": item.name, "item_id": item_id}

```

...bundan:
```
    ... "item_name": item.name ...

```

...buna:
```
    ... "item_price": item.price ...

```

...ve editörünün veri tiplerini bildiğini ve otomatik tamamladığını göreceksiniz:
![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)
Daha fazal özellik içeren, daha eksiksiz bir örnek için Öğretici - Kullanıcı Rehberi sayfasını ziyaret edebilirsin.
**Spoiler** : Öğretici - Kullanıcı rehberi şunları içerir:
  * **Parameterlerin** , **headers** , **çerezler** , **form alanları** ve **dosyalar** olarak tanımlanması.
  * `maximum_length` ya da `regex` gibi **doğrulama kısıtlamalarının** nasıl yapılabileceği.
  * Çok güçlü ve kullanımı kolay **Bağımlılık Enjeksiyonu** sistemi oluşturmayı.
  * Güvenlik ve kimlik doğrulama, **JWT tokenleri** ile **OAuth2** desteği, ve **HTTP Basic** doğrulaması.
  * İleri seviye fakat bir o kadarda basit olan **çok derin JSON modelleri** (Pydantic sayesinde).
  * **GraphQL** entegrasyonu: Strawberry ve diğer kütüphaneleri kullanarak.
  * Diğer ekstra özellikler (Starlette sayesinde):
    * **WebSocketler**
    * HTTPX ve `pytest` sayesinde aşırı kolay testler.
    * **CORS**
    * **Cookie Sessions**
    * ...ve daha fazlası.


## Performans¶
Bağımsız TechEmpower kıyaslamaları gösteriyor ki, Uvicorn ile çalıştırılan **FastAPI** uygulamaları en hızlı Python framework'lerinden birisi, sadece Starlette ve Uvicorn'dan yavaş, ki FastAPI bunların üzerine kurulu bir kütüphanedir.
Daha fazla bilgi için, bu bölüme bir göz at Kıyaslamalar.
## Opsiyonel Gereksinimler¶
Pydantic tarafında kullanılan:
  * `email-validator` - email doğrulaması için.
  * `pydantic-settings` - ayar yönetimi için.
  * `pydantic-extra-types` - Pydantic ile birlikte kullanılabilecek ek tipler için.


Starlette tarafında kullanılan:
  * `httpx` - Eğer `TestClient` yapısını kullanacaksanız gereklidir.
  * `jinja2` - Eğer varsayılan template konfigürasyonunu kullanacaksanız gereklidir.
  * `python-multipart` - Eğer `request.form()` ile form dönüşümü desteğini kullanacaksanız gereklidir.
  * `itsdangerous` - `SessionMiddleware` desteği için gerekli.
  * `pyyaml` - `SchemaGenerator` desteği için gerekli (Muhtemelen FastAPI kullanırken ihtiyacınız olmaz).


Hem FastAPI hem de Starlette tarafından kullanılan:
  * `uvicorn` - oluşturduğumuz uygulamayı servis edecek web sunucusu görevini üstlenir.
  * `orjson` - `ORJSONResponse` kullanacaksanız gereklidir.
  * `ujson` - `UJSONResponse` kullanacaksanız gerekli.


Bunların hepsini `pip install fastapi[all]` ile yükleyebilirsin.
## Lisans¶
Bu proje, MIT lisansı şartları altında lisanslanmıştır.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Başa dön 
  *[tip belirteçleri]: Tip Belirteçleri: Type Hints
  *[otomatik tamamlama]: Otomatik Tamamlama: auto-complete, autocompletion, IntelliSense
  *[komut satırı uygulaması]: Komut Satırı: Command Line Interface
  *[_yollarına_]: Adres / Yol: Path 
  *[Gövde]: Gövde: Body
  *[derin]: Derin / İç içe: Nested
  *[dönüşümünü]: Dönüşüm: serialization, parsing, marshalling olarak da biliniyor
  *[Bağımlılık Enjeksiyonu]: Bağımlılık Enjeksiyonu: components, resources, providers, services, injectables olarak da biliniyor.
  *[dönüşümü]: HTTP isteği ile gelen string veriyi Python nesnesine çevirme.
