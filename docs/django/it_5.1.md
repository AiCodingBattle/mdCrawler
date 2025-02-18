Django
The web framework for perfectionists with deadlines.
Cambia tema (tema corrente: auto)
Cambia tema (tema corrente: chiaro)
Cambia tema (tema corrente: scuro)
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
  * Cambia tema (tema corrente: auto)
Cambia tema (tema corrente: chiaro)
Cambia tema (tema corrente: scuro)
Toggle Light / Dark / Auto color theme


# Documentazione
Search: Cerca
  * Getting Help


  * el
  * en
  * es
  * fr
  * id
  * ja
  * ko
  * pl
  * pt-br
  * zh-hans
  * Language: **it**


  * 3.2
  * 4.0
  * 4.1
  * 4.2
  * 5.0
  * dev
  * Documentation version: **5.1**


  * 

# Documentazione di Django¶
Tutto ciò che devi sapere su Django.
## Primi passi¶
Non conosci ancora Django o non hai mai programmato? Questo è il posto giusto da dove cominciare!
  * **Partendo da zero:** Panoramica | Installazione
  * **Tutorial:** Part 1: Requests and responses | Part 2: Models and the admin site | Part 3: Views and templates | Part 4: Forms and generic views | Part 5: Testing | Part 6: Static files | Part 7: Customizing the admin site | Part 8: Adding third-party packages
  * **Advanced Tutorials:** How to write reusable apps | Writing your first contribution to Django


## Ottieni aiuto¶
Hai problemi? Saremo felici di aiutarti!
  * Prova il FAQ – troverai le risposte alle domande più frequenti.
  * Stai cercando informazioni specifiche? Prova il Indice, Indice dei moduli o il :doc: tavola dettagliata dei contenuti <contents>`.
  * trovato nulla ? guarda faq per informazioni su come ricevere supporto e fare domsnde alla community
  * Segnala le anomalie di Django avvalendoti del nostro sistema di ticketing.


## Com’è organizzata la documentazione¶
Django ha una documentazione molto ampia. Una visione d’insieme di com’è strutturata ti aiuterà a capire dove cercare determinate cose:
  * Tutorials ti porta per mano attraverso una serie di step con il fine di creare una applicazione web. Comincia da qui se sei nuovo di Django o dello sviluppo di applicazioni web. Guarda anche «Primi passi».
  * Guide agli argomenti discutono gli argomenti chiave e i concetti ad un livello abbastanza elevato, e forniscono utili infomazioni e spiegazioni di base.
  * Guide di riferimento contengono riferimenti tecnici per le API e per altri aspetti del complesso di Django. Descrivono come funzione e come utilizzarlo, ma presumono la conoscenza dei concetti fondamentali.
  * Guide How-to sono procedure. Ti guidano attraverso i passi necessari alla soluzioni di problemi fondamentali e di casi d’uso. Sono più avanzati dei tutorial e pressuppongono una certa conoscenza del funzionamento di Django.


## Il livello del modello¶
Django fornisce un layer di astrazione (i «models») per strutturare e manipolare i dati della tua applicazione web. Ottieni maggiori informazioni qui sotto:
  * **Modelli:** Introduzione ai modelli | Tipi di campi | Indici | Meta opzioni | Classe modello
  * **QuerySets:** Eseguire le interrogazioni | Il metodo QuerySet | Le espressioni Lookup
  * **Istanze di Model:** Metodi delle istanze | Accesso ai relativi oggetti
  * **Migrazioni:** Introduzione alle migrazioni | riferimento alle operazioni | Editor dello schema | Scrivere migrazioni
  * **Avanzate:** Managers | SQL diretto | Transazioni | Aggregazioni | Ricerca | Campi personalizzati | Database multipli | Consultazioni personalizzate | Espressioni di interrogazioni | Espressioni condizionali | Funzioni del database
  * **Altro:** Database Supportati | Database Legacy | Fornire i dati iniziali | Ottimizzare l’accesso al database | Caratteristiche specifiche di PostgreSQL


## Il livello vista¶
Django possiede il concetto delle «viste» per incapsulare la logica che gestisce una richiesta dell’utente e la fornitura di una risposta. Tutte le informazioni per comprendere le viste sono consultabili ai seguenti link:
  * **Fondamenti:** URLconfs | Funzioni di View | Scorciatoie | I Decoratori
  * **Riferimento:** Viste Predefinite | Oggetti Request/Reponse | Oggetti TemplateResponse
  * **Upload di file:** Panoramica | Oggetti file | API per storage | Gestire i file | Storage personalizzato
  * **Viste basate su classi:** Panoramica | Viste predefinite per la visualizzazzione | Viste predefinite per modifiche | Usare i mixins | Riferimento all’API | Indice
  * **Avanzato:** Generare CSV | Generare PDF
  * **Middleware:** Panoramica | Classi predefinite per il middleware


## Il livello template¶
Il livello template fornisce una sintassi facile da usare per il designer, permettendo di generare le informazioni da presentare all’utente. Impara l’uso della sintassi come designer e il modo in cui può essere estesa dagli sviluppatori:
  * **Fondamenti:** Panoramica
  * **Per i designer:** Panoramica del linguaggio | Tags e filtri integrati | Umanizzazione
  * **Per gli sviluppatori** Template API | Custom tag and filtri | Custom template backend


## I Form¶
Django fornisce una ricco framework per facilitare la creazione dei Form e la manipolazione dei suoi dati.
  * **Fondamenti:** Panoramica | API del Form | Campi predefiniti | Widget predefiniti
  * **Avanzato:** Form per i modelli | Integrare i media | Formsets | Personalizzare la validazione


## Il processo di sviluppo¶
Imparate a usare i vari strumenti e componenti per aiutarvi a sviluppare e testare le applicazioni in Django:
  * **Impostazioni:** Panoramica | Lista completa delle impostazioni
  * **Applicazioni:** Panoramica
  * **Eccezioni:** Panoramica
  * **django-admin.py e manage.py:** Panoramica | Aggiungere comandi personalizzati
  * **Test:** Introduzione | Scrivere ed eseguire i test | Strumenti di test inclusi | Argomenti avanzati
  * **Rilascio:** Panoramica | WSGI servers | ASGI servers | Rilasciare file statici | Tracciare codici di errore via email | Cose da fare per il rilascio


## L’admin¶
Trova tutto ciò che occorre sull’interfaccia di gestione automatizzata, una delle funzionalità di Django più popolari:
  * Gestisci il sito
  * Azioni di gestione
  * Gestisci il generatore della documentazione


## Sicurezza¶
La sicurezza è un tema di importanza fondamentale nello sviluppo delle applicazioni web e Django fornisce molteplici strumenti e meccanismi di protezione:
  * Panoramica sulla sicurezza
  * Problemi di sicurezza noti in Django
  * Protezione per clickjacking
  * protezione Cross Site Request Forgery
  * Firma per la crittografia
  * Middleware di sicurezza


## Internazionalizzazione e localizzazione¶
Django offre un robusto framework di internazionalizzazione e localizzazione per assisterti nello sviluppo di applicazioni che richiedono diverse lingue e nazionalità:
  * Sommario | Internazionalizzazione | Localizzazione | Formattazione della UI Web localizzata e degli input dei form
  * Fusi orari


## Prestazioni e ottimizzazione¶
Ci sono diverse tecniche e strumenti che possono aiutarti a rendere il codice più efficiente nell’esecuzione - più veloce, usando meno risorse di sistema.
  * Panoramica sulle prestazioni e ottimizzazione


## Framework geografico¶
GeoDjango vuole essere un framework web geografico a livello mondiale. Il suo obiettivo è quello di rendere il più semplice possibile costruire applicazioni web GIS ed imbrigliare il potere dei dati spaziali.
## Strumenti comuni per le applicazioni web¶
Django offre molteplici strumenti dei quali si sente comunemente il bisogno durante lo sviluppo di applicazioni web:
  * **Autenticazione:** Panoramica | Usare il sistema di autenticazione | Gestione della Password | Personalizzare l’autenticazione | Le API
  * Caching
  * Registrare log
  * Inviare email
  * Distribuzione feed (RSS/Atom)
  * Paginazione
  * Framework dei messaggi
  * Serializzazione
  * Sessioni
  * Mappe di sito
  * Gestione statica dei file
  * Validazione dei dati


## Altre funzionalità di base¶
Imparate a usare alcune altre funzionalità fondamentali del framework di Django:
  * Elaborazione condizionale dei contenuti
  * Tipi di contenuto e relazioni generiche
  * Le Flatpage
  * Reindirizzamenti
  * Segnali
  * Framework dei controlli di sistema
  * Framework dei siti
  * Unicode in Django


## Il progetto open-source Django¶
Imparate a usare il processo di sviluppo per il progetto Django stesso e su come si può contribuire:
  * **Community:** Contributing to Django | The release process | Team organization | The Django source code repository | Security policies | Mailing lists and Forum
  * **Filosofia di design:** Panoramica
  * **Documentazione:** Informazioni su questa documentazione
  * **Distribuzioni di terze parti:** Panoramica
  * **Django nel tempo:** Stabilità delle API | Note di rilascio e istruzioni per l’aggiornamento | Cronologia delle deprecazioni


Sommario della documentazione di Django
Come iniziare 
Back to Top
# Additional Information
## Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * Healthchecks donated to the Django Software Foundation to support Django development. Donate today! 


## Browse
  * Prev: Sommario della documentazione di Django
  * Next: Come iniziare
  * Table of contents
  * Indice generale
  * Indice del modulo Python


## You are here:
  * Django 5.1 documentation
    * Documentazione di Django


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
