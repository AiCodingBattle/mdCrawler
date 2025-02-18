Django
The web framework for perfectionists with deadlines.
Toggle theme (current theme: auto)
Toggle theme (current theme: light)
Toggle theme (current theme: dark)
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
  * Toggle theme (current theme: auto)
Toggle theme (current theme: light)
Toggle theme (current theme: dark)
Toggle Light / Dark / Auto color theme


# Τεκμηρίωση
Search: Αναζήτηση
  * Getting Help


  * en
  * es
  * fr
  * id
  * it
  * ja
  * ko
  * pl
  * pt-br
  * zh-hans
  * Language: **el**


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

# Εγχειρίδιο Django¶
Όλα όσα χρειάζεται να ξέρετε για το Django.
## Πρώτα βήματα¶
Είστε καινούργιος στο Django ή στον προγραμματισμό; Αυτό είναι το κατάλληλο μέρος για να αρχίσετε!
  * **Από την αρχή:** Επισκόπηση | Εγκατάσταση
  * **Tutorial:** Part 1: Requests and responses | Part 2: Models and the admin site | Part 3: Views and templates | Part 4: Forms and generic views | Part 5: Testing | Part 6: Static files | Part 7: Customizing the admin site | Part 8: Adding third-party packages
  * **Advanced Tutorials:** How to write reusable apps | Writing your first contribution to Django


## Μέρη για βοήθεια¶
Έχετε κάποιο πρόβλημα; Θα χαρούμε να σας βοηθήσουμε!
  * Δοκιμάστε το άρθρο Συχνές ερωτήσεις (FAQ) – έχει τις απαντήσεις στις πιο συνηθισμένες ερωτήσεις.
  * Μήπως ψάχνετε κάτι συγκεκριμένο; Δείτε στα Περιεχόμενα, στο Ευρετήριο μονάδων ή στον αναλυτικό πίνακα περιεχομένων.
  * Not found anything? See Συχνές Ερωτήσεις: Λαμβάνοντας βοήθεια for information on getting support and asking questions to the community.
  * Αναφέρετε τυχόν bugs του Django στον ticket tracker.


## Πως είναι δομημένο το documentation¶
Το Django έχει πολύ documentation. Μια επισκόπηση της οργάνωσης του θα σας βοηθήσει να γνωρίζετε πού να ψάξετε για κάτι συγκεκριμένο:
  * Tutorials take you by the hand through a series of steps to create a web application. Start here if you’re new to Django or web application development. Also look at the «Πρώτα βήματα».
  * Το άρθρο χρησιμοποιώντας το Django συζητά επιγραμματικά για βασικά θέματα και έννοιες και παρέχει χρήσιμες πληροφορίες και τεκμηριώσεις.
  * Οι οδηγοί αναφορών περιέχουν τεχνικές αναφορές για τα API και άλλες πτυχές του μηχανισμού του Django. Περιγράφουν πώς λειτουργεί και πώς να το χρησιμοποιήσετε αλλά προϋποθέτει ότι έχετε γνώση βασικών θεμάτων σχετικά με το Django.
  * Οι οδηγοί how-to είναι συνταγές. Σας καθοδηγούν μέσα από βήματα για την επίλυση κοινών προβλημάτων. Είναι πιο προχωρημένα από τα tutorials και προϋποθέτουν ότι έχετε γνώση του τρόπου λειτουργίας του Django.


## Το επίπεδο του μοντέλου (model layer)¶
Django provides an abstraction layer (the «models») for structuring and manipulating the data of your web application. Learn more about it below:
  * **Μοντέλα:** Εισαγωγή στα μοντέλα | Τύποι πεδίων | Ευρετήρια (indexes) | Επιλογές Meta | Η κλάση Model
  * **QuerySets:** Πραγματοποιώντας queries | QuerySet method reference | Lookup expressions
  * **Model instances:** Μέθοδοι του instance | Τρόποι πρόσβασης σε συσχετισμένα objects
  * **Migrations:** Εισαγωγή στα migrations | Λειτουργίες των migrations | SchemaEditor | Γράφοντας migrations
  * **Για προχωρημένους:** Managers | Raw SQL | Transactions | Aggregation | Εύρεση | Προσαρμοσμένα πεδία (fields) μοντέλων | Πολλαπλές βάσεις δεδομένων | Προσαρμοσμένα lookups | Query Expressions | Conditional Expressions | Συναρτήσεις βάσης δεδομένων
  * **Διάφορα:** Υποστηριζόμενες βάσεις δεδομένων | Απαρχαιωμένες βάσεις δεδομένων | Παρέχοντας αρχικές τιμές στα μοντέλα σας | Βελτιστοποίηση πρόσβασης στη βάση δεδομένων | Συγκεκριμένα features για την PostgreSQL


## Το επίπεδο του view¶
Το Django έχει την έννοια των «views» για να αναπαραστήσει τη λογική η οποία είναι υπεύθυνη για την επεξεργασία του request του χρήστη και της επιστροφής ενός response. Βρείτε όλα όσα θα θέλατε να μάθετε για τα views παρακάτω:
  * **The basics:** URLconfs | View functions | Shortcuts | Decorators | Asynchronous Support
  * **Αναφορά:** Built-in Views | Request/response objects | TemplateResponse objects
  * **Ανέβασμα αρχείων:** Επισκόπηση | File objects | Storage API | Διαχειρίζοντας τα αρχεία | Προσαρμοσμένο storage
  * **Class-based views:** Επισκόπηση | Built-in views για εμφάνιση | Built-in views για επεξεργασία | Χρησιμοποιώντας mixins | Αναφορά του API | Flattened index
  * **Για προχωρημένους:** Δημιουργώντας CSV | Δημιουργώντας PDF
  * **Middleware:** Επισκόπηση | Built-in middleware classes


## Το επίπεδο template¶
Το επίπεδο template παρέχει ένα φιλικό προς τον designer συντακτικό για να γίνει render η πληροφορία που παρουσιάζεται στον χρήστη. Μάθετε πως αυτό το συντακτικό μπορεί να χρησιμοποιηθεί από τους designers και πως μπορεί να επεκταθεί από τους προγραμματιστές:
  * **Τα βασικά:** Επισκόπηση
  * **Για τους designers:** Επισκόπηση της γλώσσας | Built-in tags και φίλτρα (filters) | Humanization
  * **For programmers:** Template API | Custom tags and filters | Custom template backend


## Φόρμες¶
Το Django παρέχει ένα πλούσιο framework για να σας διευκολύνει με την δημιουργία των φορμών και τον χειρισμό των δεδομένων των φορμών (form data).
  * **Τα βασικά:** Επισκόπηση | Form API | Built-in πεδία (fields) | Built-in widgets
  * **Για προχωρημένους:** Φόρμες για μοντέλα | Ενσωματώνοντας αρχεία πολυμέσων | Formsets | Προσαρμοσμένo validation


## Η διαδικασία της ανάπτυξης (development proccess)¶
Μάθετε για τα διάφορα components και εργαλεία του Django προκειμένου να σας βοηθήσουν στην ανάπτυξη και στο testing της εφαρμογής σας:
  * **Ρυθμίσεις:** Επισκόπηση | Πλήρης λίστα με τις ρυθμίσεις
  * **Εφαρμογές:** Επισκόπηση
  * **Exceptions:** Επισκόπηση
  * **django-admin και manage.py:** Επισκόπηση | Προσθέτοντας δικές σας διαχειριστικές εντολές
  * **Τεστ:** Εισαγωγή | Γράφοντας και τρέχοντας τα τεστ | Συμπεριλαμβανόμενα εργαλεία για τεστ | Θέματα για προχωρημένους
  * **Deployment:** Overview | WSGI servers | ASGI servers | Deploying static files | Tracking code errors by email | Deployment checklist


## Το site διαχείρισης¶
Βρείτε όλα όσα θα θέλατε να μάθετε σχετικά με το αυτοματοποιημένο διαχειριστικό site του Django, ένα από τα πιο δημοφιλή features του Django:
  * Το site διαχείρισης
  * Ενέργειες (actions) admin
  * Γεννήτρια documentation του admin


## Ασφάλεια¶
Security is a topic of paramount importance in the development of web applications and Django provides multiple protection tools and mechanisms:
  * Επισκόπηση ασφάλειας
  * Αποκαλυφθέντα θέματα ασφαλείας στο Django
  * Προστασία από clickjacking
  * Προστασία από Cross Site Request Forgery
  * Cryptographic signing
  * Security Middleware


## Internationalization και localization¶
Το Django προσφέρει ένα ισχυρό και σταθερό framework όσον αφορά το internationalization και το localization προκειμένου να σας βοηθήσει στην ανάπτυξη εφαρμογών σε πολλές γλώσσες και περιοχές ανά τον κόσμο:
  * Overview | Internationalization | Localization | Localized web UI formatting and form input
  * Ζώνες ώρας (time zones)


## Απόδοση και βελτιστοποίηση¶
Υπάρχουν πολλές τεχνικές και εργαλεία που μπορούν να σας βοηθήσουν στο να κάνετε τον κώδικα σας πιο αποτελεσματικό και γρήγορο, χρησιμοποιώντας λιγότερους πόρους από το σύστημα σας.
  * Επισκόπηση απόδοσης και βελτιστοποίησης


## Γεωγραφικό framework¶
GeoDjango intends to be a world-class geographic web framework. Its goal is to make it as easy as possible to build GIS web applications and harness the power of spatially enabled data.
## Common web application tools¶
Django offers multiple tools commonly needed in the development of web applications:
  * **Authentication:** Επισκόπηση | Χρησιμοποιώντας το σύστημα authentication | Διαχείριση password | Παραμετροποιώντας το authentication | API Reference
  * Caching
  * Logging
  * Αποστολή emails
  * Syndication feeds (RSS/Atom)
  * Σελιδοποίηση (pagination)
  * Messages framework
  * Serialization
  * Sessions
  * Sitemaps
  * Διαχείριση των στατικών αρχείων
  * Data validation


## Άλλες κύριες λειτουργίες¶
Μάθετε για άλλες κύριες λειτουργίες του Django framework:
  * Conditional content processing
  * Content types και generic relations
  * Flatpages
  * Ανακατευθύνσεις (redirects)
  * Signals
  * System check framework
  * Το framework sites
  * Το unicode στο Django


## Το ανοιχτού κώδικα project Django¶
Μάθετε για τη διαδικασία ανάπτυξης του Django project και το πώς μπορείτε να συνεισφέρετε:
  * **Community:** Contributing to Django | The release process | Team organization | The Django source code repository | Security policies | Mailing lists and Forum
  * **Φιλοσοφίες σχεδιασμού κώδικα:** Επισκόπηση
  * **Documentation:** Σχετικά με αυτό το εγχειρίδιο
  * **Διανομές του Django από τρίτους:** Επισκόπηση
  * **Το Django μέσα στο πέρασμα του χρόνου:** Σταθερότητα του API | Release notes και συμβουλές αναβάθμισης | Χρονοδιάγραμμα των deprecations


Περιεχόμενα του εγχειριδίου του Django
Ξεκινώντας 
Back to Top
# Additional Information
## Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * Latham & Martin donated to the Django Software Foundation to support Django development. Donate today! 


## Browse
  * Prev: Περιεχόμενα του εγχειριδίου του Django
  * Next: Ξεκινώντας
  * Table of contents
  * Κεντρικό Ευρετήριοο
  * Ευρετήριο Μονάδων της Python


## You are here:
  * Django 5.1 documentation
    * Εγχειρίδιο Django


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
