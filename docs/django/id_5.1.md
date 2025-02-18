Django
The web framework for perfectionists with deadlines.
Ganti tema (tema saat ini: otomatis)
Ganti tema (tema saat ini: terang)
Ganti tema (tema saat ini: gelap)
Toggle Light / Dark / Auto color theme
Menu
  * Overview
  * Download
  * Documentation
  * News
  * Community
  * Code
  * Issues
  * About
  * ♥ Donate
  * Ganti tema (tema saat ini: otomatis)
Ganti tema (tema saat ini: terang)
Ganti tema (tema saat ini: gelap)
Toggle Light / Dark / Auto color theme


# Dokumentasi
Search: Cari
  * Getting Help


  * el
  * en
  * es
  * fr
  * it
  * ja
  * ko
  * pl
  * pt-br
  * zh-hans
  * Language: **id**


  * 1.10
  * 1.11
  * 2.0
  * 2.1
  * 2.2
  * 3.0
  * 3.1
  * 3.2
  * 4.0
  * 4.1
  * 4.2
  * 5.0
  * dev
  * Documentation version: **5.1**


  * 

# Dokumentasi Django¶
Apapun yang perlu anda ketahui mengenai Django.
## Langkah awal¶
Apakah anda baru di Django atau di pemrograman? Ini adalah tempat untuk memulai!
  * **Untuk Permulaan:** gambaran singkat | pemasangan
  * **Tutorial:** Part 1: Requests and responses | Part 2: Models and the admin site | Part 3: Views and templates | Part 4: Forms and generic views | Part 5: Testing | Part 6: Static files | Part 7: Customizing the admin site | Part 8: Adding third-party packages
  * **Tutorial Lanjutan:** How to write reusable apps | Writing your first contribution to Django


## Mendapatkan bantuan¶
Mengalami masalah? Kami senang membantu!
  * Kunjungi halaman FAQ -- Untuk mendapatkan jawaban dari beberapa pertanyaan umum.
  * Mencari informasi spesifik? Coba:ref:genindex, Indeks Modul atau the detailed table of contents.
  * Tidak menemukan apapun? Lihat FAQ: Mendapatkan Bantuan untuk informasi terkait dukungan dan mengajukan pertanyaan ke komunitas.
  * Laporkan bug yang terdapat pada Django di ticket tracker kami.


## Bagaimana dokumentasi diatur¶
Django mempunyai banyak dokumentasi. Ikhstisar tingkat-tinggi dari bagaimana dia disusun akan membantu anda mengetahui dimana mencari untuk hal-hal tertentu:
  * Tutorials membawamu dengan tangan melalui rangkaian dari langkah untuk membuat aplikasi jaringan. Dimulai disini jika anda baru terhadap Django atau pengembangan aplikasi. Juga lihat "Langkah awal".
  * Topic guides mengobrolkan kunci topik dan konsep pada tingkat tinggi dan menyediakan informasi latar belakang berguna dan penjelasan.
  * Reference guides mengandung acuan teknis untuk API dan aspek lain dari perlengkapan Django. Mereka menggambarkan bagaimana itu bekerja dan bagaimana menggunakannya bahwa anda mempunyai pemahaman dasar dari kunci konsep.
  * How-to guides adalah resep-resep. Mereka memandu anda melalui langkah-langkah dalam mengalamatkan kunci masalah dan kasus-penggunaan. Mereka lebih ahli dari pada tutorial dan menganggap beberapa pengetahuan dari bagaimana Django bekerja.


## Lapisan model¶
Django menyediakan lapisan abstrak ("models") untuk membentuk dan merubah data dari aplikasi jaringan anda. Pelajari lebih tentang itu dibawah ini:
  * **Models:** Introduction to models | Field types | Indexes | Meta options | Model class
  * **QuerySets:** Making queries | QuerySet method reference | Lookup expressions
  * **Contoh Model:** Instance methods | Accessing related objects
  * **Perpindahan:** Introduction to Migrations | Operations reference | SchemaEditor | Writing migrations
  * **Lanjutan:** Managers | Raw SQL | Transactions | Aggregation | Search | Custom fields | Multiple databases | Custom lookups | Query Expressions | Conditional Expressions | Database Functions
  * **Lainnya:** Supported databases | Legacy databases | Providing initial data | Optimize database access | PostgreSQL specific features


## Lapisan tampilan¶
Django mempunyai konsep "tampilan" untuk merangkum tanggung jawab logis untuk mengolah permintaan pengguna dan mengembalikan tanggapan. Temukan semua anda butuhkan untuk mengetahui tentang tampilan melalui tautan dibawah ini:
  * **Dasar-dasar:** URLconfs | View functions | Shortcuts | Decorators | Asynchronous Support
  * **Acuan:** Built-in Views | Request/response objects | TemplateResponse objects
  * **Unggah berkas:** Overview | File objects | Storage API | Managing files | Custom storage
  * **Tampilan berbasis-kelas:** Overview | Built-in display views | Built-in editing views | Using mixins | API reference | Flattened index
  * **Lanjutan:** Generating CSV | Generating PDF
  * **Middleware:** Overview | Built-in middleware classes


## Lapisan cetakan¶
Lapisan cetakan menyediakan sintaksis ramah-perancang untuk membangun informasi untuk dibawakan ke pengguna. Pelajari bagaimana sinktaksis ini dapat digunakan oleh perancang dan bagaimana dia dapat diperluas oleh pemrogram.
  * **Dasar:** Overview
  * **Untuk perancang:** Language overview | Built-in tags and filters | Humanization
  * **Untuk pemrogram:** Template API | Custom tags and filters | Custom template backend


## Formulir¶
Django menyediakan kerangka kaya untuk memfasilitasi pembuatan formulir dan manipulasi data.
  * **Dasar** Overview | Form API | Built-in fields | Built-in widgets
  * **Lanjutan:** Forms for models | Integrating media | Formsets | Customizing validation


## Pengolahan pengembangan¶
Pelajari tentang beragam komponen dan alat untuk membantu anda dalam mengembangkan dan mencoba aplikasi Django:
  * **Pengaturan:** Overview | Full list of settings
  * **Aplikasi:** Overview
  * **Pengecualian:** Overview
  * **django-admin dan manage.py:** Overview | Adding custom commands
  * **Percobaan:** Introduction | Writing and running tests | Included testing tools | Advanced topics
  * **Deployment:** Overview | WSGI servers | ASGI servers | Deploying static files | Tracking code errors by email | Deployment checklist


## Admin¶
Temukan semua anda butuhkan untuk mengetahui tentang otomatisasi antarmuka admin, satu dari fitur paling terkenal Django:
  * Admin site
  * Admin actions
  * Admin documentation generator


## Keamanan¶
Keamanan adalah topik sangat penting dari aplikasi jaringan dandDjango menyediakan banyak peralatan perlindungan dan mekanisme:
  * Security overview
  * Disclosed security issues in Django
  * Clickjacking protection
  * Cross Site Request Forgery protection
  * Cryptographic signing
  * Security Middleware


## Internasionalisasi dan lokalisasi¶
Django menawarkan kerangka internasionalisasi dan lokalisasi yang kuat untuk memandu anda dalam mengembangkan aplikasi untuk banyak bahasa dan wilayah dunia:
  * Overview | Internationalization | Localization | Localized web UI formatting and form input
  * Time zones


## Penampilan dan optimalisasi¶
Terdapat beragam teknik dan alat yang dapat membantu mendapatkan kode anda berjalan efesien - cepat, dan menggunakan sedikit sumberdaya sistem.
  * Performance and optimization overview


## Kerangka geografis¶
GeoDjango berniat menjadi kerangka kerja geografis kelas dunia. Tujuannya adalah membuatnya semudah mungkin membangun aplikasi jaringan GIS dan memanfaatkan kekuatan data yang diaktifkan secara spasial.
## Peralatan aplikasi jaringan umum¶
Django menawarkan banyak peralatan yang umum dibutuhkan dalam pengembangan aplikasi jaringan:
  * **Pembuktian keaslian:** Overview | Using the authentication system | Password management | Customizing authentication | API Reference
  * Caching
  * Logging
  * Sending emails
  * Syndication feeds (RSS/Atom)
  * Pagination
  * Messages framework
  * Serialization
  * Sessions
  * Sitemaps
  * Static files management
  * Data validation


## Fungsionalitas inti lain¶
Pelajari tentang beberapa fungsi inti lainnya dari kerangka Django:
  * Conditional content processing
  * Content types and generic relations
  * Flatpages
  * Redirects
  * Signals
  * System check framework
  * The sites framework
  * Unicode in Django


## Proyek sumber-terbuka Django¶
Mempelajari bagaimana pengolahan pengembangan untuk proyek Django itu sendiri dan tentang bagaimana anda dapat membantu:
  * **Komunitas:** Contributing to Django | The release process | Team organization | The Django source code repository | Security policies | Mailing lists and Forum
  * **Filosofi rancangan:** Overview
  * **Dokumentasi:** Tentang dokumentasi ini
  * **Sebaran pihak-ketiga:** Overview
  * **Django berkali-kali:** API stability | Release notes and upgrading instructions | Deprecation Timeline


Konten Dokumentasi Django
Mulai 
Back to Top
# Additional Information
## Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * Benjamin Wohlwend donated to the Django Software Foundation to support Django development. Donate today! 


## Browse
  * Prev: Konten Dokumentasi Django
  * Next: Mulai
  * Table of contents
  * Indeks Umum
  * Indeks Modul Python


## You are here:
  * Django 5.1 documentation
    * Dokumentasi Django


## Getting help
FAQ
    Try the FAQ — it's got answers to many common questions.
Index, Module Index, or Table of Contents
    Handy when looking for specific information.
Django Discord Server
    Join the Django Discord Community.
Official Django Forum
    Join the community on the Django Forum.
Ticket tracker
    Report bugs with Django or Django documentation in our ticket tracker.
## Download:
Offline (Django 5.1): HTML | PDF | ePub Provided by Read the Docs. 
# Django Links
## Learn More
  * About Django
  * Getting Started with Django
  * Team Organization
  * Django Software Foundation
  * Code of Conduct
  * Diversity Statement


## Get Involved
  * Join a Group
  * Contribute to Django
  * Submit a Bug
  * Report a Security Issue
  * Individual membership


## Get Help
  * Getting Help FAQ
  * Django Discord
  * Official Django Forum


## Follow Us
  * GitHub
  * Twitter
  * Fediverse (Mastodon)
  * News RSS


## Support Us
  * Sponsor Django
  * Corporate membership
  * Official merchandise store
  * Benevity Workplace Giving Program


Django
  * Hosting by In-kind donors
  * Design by Threespot & andrevv


© 2005-2025  Django Software Foundation and individual contributors. Django is a registered trademark of the Django Software Foundation. 
