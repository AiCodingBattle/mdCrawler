Lewati ke isi 
# FastAPI¶
![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
_FastAPI, framework performa tinggi, mudah dipelajari, cepat untuk coding, siap untuk pengembangan_
![Test](https://github.com/fastapi/fastapi/workflows/Test/badge.svg?event=push&branch=master) ![Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ![Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package) ![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)
**Dokumentasi** : https://fastapi.tiangolo.com
**Kode Sumber** : https://github.com/fastapi/fastapi
FastAPI adalah _framework_ _web_ moderen, cepat (performa-tinggi) untuk membangun API dengan Python berdasarkan tipe petunjuk Python.
Fitur utama FastAPI:
  * **Cepat** : Performa sangat tinggi, setara **NodeJS** dan **Go** (berkat Starlette dan Pydantic). Salah satu _framework_ Python tercepat yang ada.
  * **Cepat untuk coding** : Meningkatkan kecepatan pengembangan fitur dari 200% sampai 300%. *
  * **Sedikit bug** : Mengurangi hingga 40% kesalahan dari manusia (pemrogram). *
  * **Intuitif** : Dukungan editor hebat. Penyelesaian di mana pun. Lebih sedikit _debugging_.
  * **Mudah** : Dibuat mudah digunakan dan dipelajari. Sedikit waktu membaca dokumentasi.
  * **Ringkas** : Mengurasi duplikasi kode. Beragam fitur dari setiap deklarasi parameter. Lebih sedikit _bug_.
  * **Handal** : Dapatkan kode siap-digunakan. Dengan dokumentasi otomatis interaktif.
  * **Standar-resmi** : Berdasarkan (kompatibel dengan ) standar umum untuk API: OpenAPI (sebelumnya disebut Swagger) dan JSON Schema.


* estimasi berdasarkan pengujian tim internal pengembangan applikasi siap pakai.
## Sponsor¶
![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png) ![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png) ![](https://fastapi.tiangolo.com/img/sponsors/porter.png) ![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg) ![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg) ![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png) ![](https://fastapi.tiangolo.com/img/sponsors/coherence.png) ![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png) ![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png) ![](https://fastapi.tiangolo.com/img/sponsors/liblab.png) ![](https://fastapi.tiangolo.com/img/sponsors/render.svg) ![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg) ![](https://fastapi.tiangolo.com/img/sponsors/databento.svg) ![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png) ![](https://fastapi.tiangolo.com/img/sponsors/svix.svg) ![](https://fastapi.tiangolo.com/img/sponsors/stainless.png) ![](https://fastapi.tiangolo.com/img/sponsors/permit.png)
Sponsor lainnya
## Opini¶
"_[...] Saya banyak menggunakan**FastAPI** sekarang ini. [...] Saya berencana menggunakannya di semua tim servis ML Microsoft. Beberapa dari mereka sudah mengintegrasikan dengan produk inti _Windows_ * dan sebagian produk **Office**._"
Kabir Khan - **Microsoft** (ref)
"_Kami adopsi library**FastAPI** untuk membuat server **REST** yang melakukan kueri untuk menghasilkan **prediksi**. [untuk Ludwig]_"
Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber** (ref)
"_**Netflix** dengan bangga mengumumkan rilis open-source orkestrasi framework **manajemen krisis** : **Dispatch**! [dibuat dengan **FastAPI**]_"
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** (ref)
"_Saya sangat senang dengan**FastAPI**. Sangat menyenangkan!_"
Brian Okken - **Python Bytes podcast host** (ref)
"_Jujur, apa yang anda buat sangat solid dan berkualitas. Ini adalah yang saya inginkan di**Hug** - sangat menginspirasi melihat seseorang membuat ini._"
Timothy Crosley - **Hug creator** (ref)
"_Jika anda ingin mempelajari**framework moderen** untuk membangun REST API, coba **FastAPI** [...] cepat, mudah digunakan dan dipelajari [...]_"
"_Kami sudah pindah ke**FastAPI** untuk **API** kami [...] Saya pikir kamu juga akan suka [...]_"
Ines Montani - Matthew Honnibal - **Explosion AI founders - spaCy creators** (ref) - (ref)
"_Jika anda ingin membuat API Python siap pakai, saya merekomendasikan**FastAPI**. FastAPI **didesain indah** , **mudah digunakan** dan **sangat scalable** , FastAPI adalah **komponen kunci** di strategi pengembangan API pertama kami dan mengatur banyak otomatisasi dan service seperti TAC Engineer kami._"
Deon Pillsbury - **Cisco** (ref)
## **Typer** , CLI FastAPI¶
![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)
Jika anda mengembangkan app CLI yang digunakan di terminal bukan sebagai API web, kunjungi **Typer**.
**Typer** adalah saudara kecil FastAPI. Dan ditujukan sebagai **CLI FastAPI**. ⌨️ 🚀
## Prayarat¶
FastAPI berdiri di pundak raksasa:
  * Starlette untuk bagian web.
  * Pydantic untuk bagian data.


## Instalasi¶
Buat dan aktifkan virtual environment kemudian _install_ FastAPI:
```

fast →pip install "fastapi[standard]"restart ↻

```

**Catatan** : Pastikan anda menulis `"fastapi[standard]"` dengan tanda petik untuk memastikan bisa digunakan di semua _terminal_.
## Contoh¶
### Buat app¶
  * Buat file `main.py` dengan:


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

Atau gunakan `async def`...
Jika kode anda menggunakan `async` / `await`, gunakan `async def`:
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

**Catatan** :
Jika anda tidak paham, kunjungi _"Panduan cepat"_ bagian `async` dan `await` di dokumentasi.
### Jalankan¶
Jalankan _server_ dengan:
```

fast →fastapi dev main.py ╭────────── FastAPI CLI - Development mode ───────────╮ │                           │ │ Serving at: http://127.0.0.1:8000         │ │                           │ │ API docs: http://127.0.0.1:8000/docs        │ │                           │ │ Running in development mode, for production use:  │ │                           │ │ fastapi run                    │ │                           │ ╰─────────────────────────────────────────────────────╯INFO:   Will watch for changes in these directories: ['/home/user/code/awesomeapp']INFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)INFO:   Started reloader process [2248755] using WatchFilesINFO:   Started server process [2248757]INFO:   Waiting for application startup.INFO:   Application startup complete.restart ↻

```

Mengenai perintah `fastapi dev main.py`...
Perintah `fastapi dev` membaca file `main.py`, memeriksa app **FastAPI** di dalamnya, dan menjalan server dengan Uvicorn.
Secara otomatis, `fastapi dev` akan mengaktifkan _auto-reload_ untuk pengembangan lokal.
Informasi lebih lanjut kunjungi Dokumen FastAPI CLI.
### Periksa¶
Buka _browser_ di http://127.0.0.1:8000/items/5?q=somequery.
Anda akan melihat respon JSON berikut:
```
{"item_id":5,"q":"somequery"}

```

Anda telah membuat API:
  * Menerima permintaan HTTP di _path_ `/` dan `/items/{item_id}`.
  * Kedua _paths_ menerima _operasi_ `GET` (juga disebut _metode_ HTTP).
  * _path_ `/items/{item_id}` memiliki _parameter path_ `item_id` yang harus berjenis `int`.
  * _path_ `/items/{item_id}` memiliki _query parameter_ `q` berjenis `str`.


### Dokumentasi API interaktif¶
Sekarang kunjungi http://127.0.0.1:8000/docs.
Anda akan melihat dokumentasi API interaktif otomatis (dibuat oleh Swagger UI):
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Dokumentasi API alternatif¶
Kemudian kunjungi http://127.0.0.1:8000/redoc.
Anda akan melihat dokumentasi alternatif otomatis (dibuat oleh ReDoc):
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Contoh upgrade¶
Sekarang ubah `main.py` untuk menerima struktur permintaan `PUT`.
Deklarasikan struktur menggunakan tipe standar Python, berkat Pydantic.
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

Server `fastapi dev` akan otomatis memuat kembali.
### Upgrade dokumentasi API interaktif¶
Kunjungi http://127.0.0.1:8000/docs.
  * Dokumentasi API interaktif akan otomatis diperbarui, termasuk kode yang baru:


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * Klik tombol "Try it out", anda dapat mengisi parameter dan langsung berinteraksi dengan API:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Kemudian klik tombol "Execute", tampilan pengguna akan berkomunikasi dengan API, mengirim parameter, mendapatkan dan menampilkan hasil ke layar:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Upgrade dokumentasi API alternatif¶
Kunjungi http://127.0.0.1:8000/redoc.
  * Dokumentasi alternatif akan menampilkan parameter _query_ dan struktur _request_ :


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### Ringkasan¶
Singkatnya, anda mendeklarasikan **sekali** jenis parameter, struktur, dll. sebagai parameter fungsi.
Anda melakukannya dengan tipe standar moderen Python.
Anda tidak perlu belajar sintaksis, metode, _classs_ baru dari _library_ tertentu, dll.
Cukup **Python** standar.
Sebagai contoh untuk `int`:
```
item_id: int

```

atau untuk model lebih rumit `Item`:
```
item: Item

```

...dengan sekali deklarasi anda mendapatkan:
  * Dukungan editor, termasuk:
    * Pelengkapan kode.
    * Pengecekan tipe.
  * Validasi data:
    * Kesalahan otomatis dan jelas ketika data tidak sesuai.
    * Validasi hingga untuk object JSON bercabang mendalam.
  * Konversi input data: berasal dari jaringan ke data dan tipe Python. Membaca dari:
    * JSON.
    * Parameter path.
    * Parameter query.
    * Cookie.
    * Header.
    * Form.
    * File.
  * Konversi output data: konversi data Python ke tipe jaringan data (seperti JSON):
    * Konversi tipe Python (`str`, `int`, `float`, `bool`, `list`, dll).
    * Objek `datetime`.
    * Objek `UUID`.
    * Model database.
    * ...dan banyak lagi.
  * Dokumentasi interaktif otomatis, termasuk 2 alternatif tampilan pengguna:
    * Swagger UI.
    * ReDoc.


Kembali ke kode contoh sebelumnya, **FastAPI** akan:
  * Validasi apakah terdapat `item_id` di _path_ untuk permintaan `GET` dan `PUT` requests.
  * Validasi apakah `item_id` berjenit `int` untuk permintaan `GET` dan `PUT`.
    * Jika tidak, klien akan melihat pesan kesalahan jelas.
  * Periksa jika ada parameter _query_ opsional bernama `q` (seperti `http://127.0.0.1:8000/items/foo?q=somequery`) untuk permintaan `GET`.
    * Karena parameter `q` dideklarasikan dengan `= None`, maka bersifat opsional.
    * Tanpa `None` maka akan menjadi wajib ada (seperti struktur di kondisi dengan `PUT`).
  * Untuk permintaan `PUT` `/items/{item_id}`, membaca struktur sebagai JSON:
    * Memeriksa terdapat atribut wajib `name` harus berjenis `str`.
    * Memeriksa terdapat atribut wajib`price` harus berjenis `float`.
    * Memeriksa atribut opsional `is_offer`, harus berjenis `bool`, jika ada.
    * Semua ini juga sama untuk objek json yang bersarang mendalam.
  * Konversi dari dan ke JSON secara otomatis.
  * Dokumentasi segalanya dengan OpenAPI, dengan menggunakan:
    * Sistem dokumentasi interaktif.
    * Sistem otomatis penghasil kode, untuk banyak bahasa.
  * Menyediakan 2 tampilan dokumentasi web interaktif dengan langsung.


Kita baru menyentuh permukaannya saja, tetapi anda sudah mulai paham gambaran besar cara kerjanya.
Coba ubah baris:
```
  return {"item_name": item.name, "item_id": item_id}

```

...dari:
```
    ... "item_name": item.name ...

```

...menjadi:
```
    ... "item_price": item.price ...

```

...anda akan melihat kode editor secara otomatis melengkapi atributnya dan tahu tipe nya:
![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)
Untuk contoh lengkap termasuk fitur lainnya, kunjungi Tutorial - Panduan Pengguna.
**Peringatan spoiler** : tutorial - panduan pengguna termasuk:
  * Deklarasi **parameter** dari tempat berbeda seperti: **header** , **cookie** , **form field** and **file**.
  * Bagaimana mengatur **batasan validasi** seperti `maximum_length`atau `regex`.
  * Sistem **Dependency Injection** yang hebat dan mudah digunakan.
  * Keamanan dan autentikasi, termasuk dukungan ke **OAuth2** dengan **JWT token** dan autentikasi **HTTP Basic**.
  * Teknik lebih aju (tetapi mudah dipakai untuk deklarasi **model JSON bersarang ke dalam** (berkat Pydantic).
  * Integrasi **GraphQL** dengan Strawberry dan library lainnya.
  * Fitur lainnya (berkat Starlette) seperti:
    * **WebSocket**
    * Test yang sangat mudah berdasarkan HTTPX dan `pytest`
    * **CORS**
    * **Cookie Session**
    * ...dan lainnya.


## Performa¶
Tolok ukur Independent TechEmpower mendapati aplikasi **FastAPI** berjalan menggunakan Uvicorn sebagai salah satu framework Python tercepat yang ada, hanya di bawah Starlette dan Uvicorn itu sendiri (digunakan di internal FastAPI). (*)
Penjelasan lebih lanjut, lihat bagian Tolok ukur.
## Dependensi¶
FastAPI bergantung pada Pydantic dan Starlette.
### Dependensi `standar`¶
Ketika anda meng-_install_ FastAPI dengan `pip install "fastapi[standard]"`, maka FastAPI akan menggunakan sekumpulan dependensi opsional `standar`:
Digunakan oleh Pydantic:
  * `email-validator` - untuk validasi email.


Digunakan oleh Starlette:
  * `httpx` - Dibutuhkan jika anda menggunakan `TestClient`.
  * `jinja2` - Dibutuhkan jika anda menggunakan konfigurasi template bawaan.
  * `python-multipart` - Dibutuhkan jika anda menggunakan form dukungan "parsing", dengan `request.form()`.


Digunakan oleh FastAPI / Starlette:
  * `uvicorn` - untuk server yang memuat dan melayani aplikasi anda. Termasuk `uvicorn[standard]`, yang memasukan sejumlah dependensi (misal `uvloop`) untuk needed melayani dengan performa tinggi.
  * `fastapi-cli` - untuk menyediakan perintah `fastapi`.


### Tanpda dependensi `standard`¶
Jika anda tidak ingin menambahkan dependensi opsional `standard`, anda dapat menggunakan `pip install fastapi` daripada `pip install "fastapi[standard]"`.
### Dependensi Opsional Tambahan¶
Ada beberapa dependensi opsional yang bisa anda install.
Dependensi opsional tambahan Pydantic:
  * `pydantic-settings` - untuk manajemen setting.
  * `pydantic-extra-types` - untuk tipe tambahan yang digunakan dengan Pydantic.


Dependensi tambahan opsional FastAPI:
  * `orjson` - Diperlukan jika anda akan menggunakan`ORJSONResponse`.
  * `ujson` - Diperlukan jika anda akan menggunakan `UJSONResponse`.


## Lisensi¶
Project terlisensi dengan lisensi MIT.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
Kembali ke atas 
  *[Penyelesaian]: juga dikenal otomatis-lengkap, pelengkapan otomatis, kecerdasan
  *[CLI]: Command Line Interface
  *[Konversi]: juga disebut: serialization, parsing, marshalling
  *[Dependency Injection]: also known as components, resources, providers, services, injectables
  *["parsing"]: converting the string that comes from an HTTP request into Python data
