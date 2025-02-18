### Navigation
  * index
  * modules |
  * suivant |
  * précédent |
  * ![Python logo](https://docs.python.org/fr/3/_static/py.svg)
  * Python »
  * EnglishSpanishFrenchItalianJapaneseKoreanPolishBrazilian PortugueseTurkishSimplified ChineseTraditional Chinese
dev (3.14)3.13.23.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
  * 3.13.2 Documentation » 
  * Manuel de référence de l'API Python/C
  * | 
  * Theme  Auto Light Dark |


# Manuel de référence de l'API Python/C¶
C'est la documentation de l'API utilisée par les développeurs C et C++ écrivant des modules d'extension ou intégrant Python. Elle va de pair avec Extension et intégration de l'interpréteur Python, qui décrit les principes généraux de l'écriture d'extensions, mais ne rentre pas dans les détails de chaque fonction de l'API.
  * Introduction
    * Coding standards
    * Include Files
    * Useful macros
    * Objects, Types and Reference Counts
    * Exceptions
    * Embarquer Python
    * Debugging Builds
  * Stabilité de l’API C
    * Unstable C API
    * ABI stable
    * Considérations relatives aux plateformes
    * Contenu de l’API restreinte
  * The Very High Level Layer
  * Reference Counting
  * Gestion des exceptions
    * Printing and clearing
    * Lever des exceptions
    * Issuing warnings
    * Querying the error indicator
    * Traitement des signaux
    * Exception Classes
    * Objets exception
    * Objets exception Unicode
    * Contrôle de la récursion
    * Exceptions standards
    * Standard Warning Categories
  * Utilitaires
    * Operating System Utilities
    * System Functions
    * Process Control
    * Importer des modules
    * Data marshalling support
    * Analyse des arguments et construction des valeurs
    * Conversion et formatage de chaînes
    * PyHash API
    * Réflexion
    * Codec registry and support functions
    * PyTime C API
    * Support for Perf Maps
  * Couche d'abstraction des objets
    * Protocole Objet
    * Call Protocol
    * Number Protocol
    * Sequence Protocol
    * Protocole de correspondance
    * Protocole d'itération
    * Protocole tampon
  * Couche des objets concrets
    * Objets fondamentaux
    * Objets numériques
    * Objets séquences
    * Objets conteneurs
    * Objets fonctions
    * Autres objets
  * Initialization, Finalization, and Threads
    * Before Python Initialization
    * Global configuration variables
    * Initializing and finalizing the interpreter
    * Process-wide parameters
    * Thread State and the Global Interpreter Lock
    * Sub-interpreter support
    * Asynchronous Notifications
    * Profiling and Tracing
    * Reference tracing
    * Support avancé du débogueur
    * Thread Local Storage Support
    * Primitives de synchronisation
  * Python Initialization Configuration
    * Example
    * PyWideStringList
    * PyStatus
    * PyPreConfig
    * Preinitialize Python with PyPreConfig
    * PyConfig
    * Initialization with PyConfig
    * Isolated Configuration
    * Python Configuration
    * Python Path Configuration
    * Py_GetArgcArgv()
    * Multi-Phase Initialization Private Provisional API
  * Memory Management
    * Aperçu
    * Allocator Domains
    * Raw Memory Interface
    * Memory Interface
    * Object allocators
    * Default Memory Allocators
    * Customize Memory Allocators
    * Debug hooks on the Python memory allocators
    * The pymalloc allocator
    * The mimalloc allocator
    * tracemalloc C API
    * Exemples
  * Implémentation d'objets
    * Allouer des objets dans le tas
    * Common Object Structures
    * Objets type
    * Supporting Cyclic Garbage Collection
  * Version des API et ABI
  * Monitoring C API
  * Generating Execution Events
    * Managing the Monitoring State


#### Sujet précédent
1. Intégrer Python dans une autre application
#### Sujet suivant
Introduction
### Cette page
  * Signalement de bogue
  * Voir la source 


«
### Navigation
  * index
  * modules |
  * suivant |
  * précédent |
  * ![Python logo](https://docs.python.org/fr/3/_static/py.svg)
  * Python »
  * EnglishSpanishFrenchItalianJapaneseKoreanPolishBrazilian PortugueseTurkishSimplified ChineseTraditional Chinese
dev (3.14)3.13.23.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
  * 3.13.2 Documentation » 
  * Manuel de référence de l'API Python/C
  * | 
  * Theme  Auto Light Dark |


©  Copyright  2001-2025, Python Software Foundation. This page is licensed under the Python Software Foundation License Version 2. Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License. See History and License for more information. The Python Software Foundation is a non-profit corporation. Please donate. Mis à jour le févr. 17, 2025 (05:58 UTC). Found a bug? Créé en utilisant Sphinx 8.1.3. 
