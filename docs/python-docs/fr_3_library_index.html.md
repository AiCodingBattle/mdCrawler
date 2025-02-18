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
  * La bibliothèque standard
  * | 
  * Theme  Auto Light Dark |


# La bibliothèque standard¶
Alors que La référence du langage Python décrit exactement la syntaxe et la sémantique du langage Python, ce manuel de référence de la Bibliothèque décrit la bibliothèque standard distribuée avec Python. Il décrit aussi certains composants optionnels typiquement inclus dans les distributions de Python.
La bibliothèque standard de Python est très grande, elle offre un large éventail d'outils comme le montre la longueur de la table des matières ci-dessous. La bibliothèque contient des modules natifs (écrits en C) exposant les fonctionnalités du système telles que les interactions avec les fichiers qui autrement ne seraient pas accessibles aux développeurs Python, ainsi que des modules écrits en Python exposant des solutions standardisées à de nombreux problèmes du quotidien du développeur. Certains de ces modules sont définis explicitement pour encourager et améliorer la portabilité des programmes Python en abstrayant des spécificités sous-jacentes en API neutres.
Les installateurs de Python pour Windows incluent généralement la bibliothèque standard en entier, et y ajoutent souvent d'autres composants. Pour les systèmes d'exploitation Unix, Python est typiquement fourni sous forme d'une collection de paquets, il peut donc être nécessaire d'utiliser le gestionnaire de paquets fourni par le système d'exploitation pour obtenir certains composants optionnels.
Au delà de la bibliothèque standard, il existe une collection grandissante de plusieurs centaine de milliers de composants (des programmes, des modules, ou des _frameworks_), disponibles dans le Python Package Index.
  * Introduction
    * Notes sur la disponibilité
  * Fonctions natives
  * Constantes natives
    * Constantes ajoutées par le module `site`
  * Types natifs
    * Valeurs booléennes
    * Opérations booléennes — `and`, `or`, `not`
    * Comparaisons
    * Types numériques — `int`, `float`, `complex`
    * Boolean Type - `bool`
    * Les types itérateurs
    * Types séquentiels — `list`, `tuple`, `range`
    * Type Séquence de Texte — `str`
    * Séquences Binaires — `bytes`, `bytearray`, `vue mémoire`
    * Types d'ensembles — `set`, `frozenset`
    * Les types de correspondances — `dict`
    * Le type gestionnaire de contexte
    * Types d'annotation de type — Alias générique, Union
    * Autres types natifs
    * Attributs spéciaux
    * Limitation de longueur de conversion de chaîne vers un entier
  * Exceptions natives
    * Contexte des exceptions
    * Hériter des exceptions natives
    * Classes mères
    * Exceptions concrètes
    * Avertissements
    * Exception groups
    * Hiérarchie des exceptions
  * Services de Manipulation de Texte
    * `string` --- Common string operations
    * `re` --- Regular expression operations
    * `difflib` --- Helpers for computing deltas
    * `textwrap` --- Text wrapping and filling
    * `unicodedata` --- Unicode Database
    * `stringprep` --- Internet String Preparation
    * `readline` --- GNU readline interface
    * `rlcompleter` --- Completion function for GNU readline
  * Services autour des Données Binaires
    * `struct` --- Interpret bytes as packed binary data
    * `codecs` --- Codec registry and base classes
  * Types de données
    * `datetime` — Types de base pour la date et l'heure
    * `zoneinfo` --- IANA time zone support
    * `calendar` --- General calendar-related functions
    * `collections` --- Container datatypes
    * `collections.abc` --- Abstract Base Classes for Containers
    * `heapq` --- Heap queue algorithm
    * `bisect` --- Array bisection algorithm
    * `array` --- Efficient arrays of numeric values
    * `weakref` --- Weak references
    * `types` --- Dynamic type creation and names for built-in types
    * `copy` --- Shallow and deep copy operations
    * `pprint` — L’affichage élégant de données
    * `reprlib` --- Alternate `repr()` implementation
    * `enum` --- Support for enumerations
    * `graphlib` --- Functionality to operate with graph-like structures
  * Modules numériques et mathématiques
    * `numbers` --- Numeric abstract base classes
    * `math` --- Mathematical functions
    * `cmath` --- Mathematical functions for complex numbers
    * `decimal` --- Decimal fixed-point and floating-point arithmetic
    * `fractions` --- Rational numbers
    * `random` --- Generate pseudo-random numbers
    * `statistics` --- Mathematical statistics functions
  * Modules de programmation fonctionnelle
    * `itertools` --- Functions creating iterators for efficient looping
    * `functools` --- Higher-order functions and operations on callable objects
    * `operator` — Opérateurs standards en tant que fonctions
  * Accès aux Fichiers et aux Dossiers
    * `pathlib` — Chemins de système de fichiers orientés objet
    * `os.path` --- Common pathname manipulations
    * `stat` --- Interpreting `stat()` results
    * `filecmp` --- File and Directory Comparisons
    * `tempfile` --- Generate temporary files and directories
    * `glob` --- Unix style pathname pattern expansion
    * `fnmatch` --- Unix filename pattern matching
    * `linecache` --- Random access to text lines
    * `shutil` --- High-level file operations
  * Persistance des données
    * `pickle` --- Python object serialization
    * `copyreg` --- Register `pickle` support functions
    * `shelve` --- Python object persistence
    * `marshal` --- Internal Python object serialization
    * `dbm` --- Interfaces to Unix "databases"
    * `sqlite3` --- DB-API 2.0 interface for SQLite databases
  * Compression de donnée et archivage
    * `zlib` --- Compression compatible with **gzip**
    * `gzip` --- Support for **gzip** files
    * `bz2` --- Support for **bzip2** compression
    * `lzma` --- Compression using the LZMA algorithm
    * `zipfile` --- Work with ZIP archives
    * `tarfile` --- Read and write tar archive files
  * Formats de fichiers
    * `csv` --- CSV File Reading and Writing
    * `configparser` --- Configuration file parser
    * `tomllib` --- Parse TOML files
    * `netrc` --- netrc file processing
    * `plistlib` --- Generate and parse Apple `.plist` files
  * Service de cryptographie
    * `hashlib` --- Algorithmes de hachage sécurisés et synthèse de messages
    * `hmac` --- Keyed-Hashing for Message Authentication
    * `secrets` --- Generate secure random numbers for managing secrets
  * Services génériques du système d'exploitation
    * `os` --- Miscellaneous operating system interfaces
    * `io` --- Core tools for working with streams
    * `time` --- Time access and conversions
    * `logging` --- Logging facility for Python
    * `logging.config` --- Logging configuration
    * `logging.handlers` --- Logging handlers
    * `platform` --- Access to underlying platform's identifying data
    * `errno` --- Standard errno system symbols
    * `ctypes` --- A foreign function library for Python
  * Command Line Interface Libraries
    * `argparse` --- Parser for command-line options, arguments and subcommands
    * `optparse` --- Parser for command line options
    * `getpass` --- Portable password input
    * `fileinput` --- Iterate over lines from multiple input streams
    * `curses` --- Terminal handling for character-cell displays
    * `curses.textpad` --- Text input widget for curses programs
    * `curses.ascii` --- Utilities for ASCII characters
    * `curses.panel` --- A panel stack extension for curses
  * Exécution concourante
    * `threading` --- Thread-based parallelism
    * `multiprocessing` --- Process-based parallelism
    * `multiprocessing.shared_memory` --- Shared memory for direct access across processes
    * The `concurrent` package
    * `concurrent.futures` --- Launching parallel tasks
    * `subprocess` --- Subprocess management
    * `sched` --- Event scheduler
    * `queue` --- A synchronized queue class
    * `contextvars` --- Context Variables
    * `_thread` --- Low-level threading API
  * Réseau et communication entre processus
    * `asyncio` --- Asynchronous I/O
    * `socket` --- Low-level networking interface
    * `ssl` --- TLS/SSL wrapper for socket objects
    * `select` --- Waiting for I/O completion
    * `selectors` --- High-level I/O multiplexing
    * `signal` --- Set handlers for asynchronous events
    * `mmap` --- Memory-mapped file support
  * Traitement des données provenant d'Internet
    * `email` --- An email and MIME handling package
    * `json` --- JSON encoder and decoder
    * `mailbox` --- Manipulate mailboxes in various formats
    * `mimetypes` --- Map filenames to MIME types
    * `base64` --- Base16, Base32, Base64, Base85 Data Encodings
    * `binascii` --- Convert between binary and ASCII
    * `quopri` --- Encode and decode MIME quoted-printable data
  * Outils de traitement de balises structurées
    * `html` --- HyperText Markup Language support
    * `html.parser` --- Simple HTML and XHTML parser
    * `html.entities` --- Definitions of HTML general entities
    * Modules de traitement XML
    * `xml.etree.ElementTree` --- The ElementTree XML API
    * `xml.dom` --- The Document Object Model API
    * `xml.dom.minidom` --- Minimal DOM implementation
    * `xml.dom.pulldom` --- Support for building partial DOM trees
    * `xml.sax` --- Support for SAX2 parsers
    * `xml.sax.handler` --- Base classes for SAX handlers
    * `xml.sax.saxutils` --- SAX Utilities
    * `xml.sax.xmlreader` --- Interface for XML parsers
    * `xml.parsers.expat` --- Fast XML parsing using Expat
  * Gestion des protocoles internet
    * `webbrowser` --- Convenient web-browser controller
    * `wsgiref` --- WSGI Utilities and Reference Implementation
    * `urllib` --- URL handling modules
    * `urllib.request` --- Extensible library for opening URLs
    * `urllib.response` --- Response classes used by urllib
    * `urllib.parse` --- Parse URLs into components
    * `urllib.error` --- Exception classes raised by urllib.request
    * `urllib.robotparser` --- Parser for robots.txt
    * `http` --- HTTP modules
    * `http.client` --- HTTP protocol client
    * `ftplib` --- FTP protocol client
    * `poplib` --- POP3 protocol client
    * `imaplib` --- IMAP4 protocol client
    * `smtplib` --- SMTP protocol client
    * `uuid` --- UUID objects according to **RFC 4122**
    * `socketserver` --- A framework for network servers
    * `http.server` --- HTTP servers
    * `http.cookies` --- HTTP state management
    * `http.cookiejar` --- Cookie handling for HTTP clients
    * `xmlrpc` --- XMLRPC server and client modules
    * `xmlrpc.client` --- XML-RPC client access
    * `xmlrpc.server` --- Basic XML-RPC servers
    * `ipaddress` --- IPv4/IPv6 manipulation library
  * Services multimédia
    * `wave` --- Read and write WAV files
    * `colorsys` --- Conversions between color systems
  * Internationalisation
    * `gettext` --- Multilingual internationalization services
    * `locale` --- Internationalization services
  * Cadriciels d'applications
    * `turtle` — Tortue graphique
    * `cmd` --- Support for line-oriented command interpreters
    * `shlex` --- Simple lexical analysis
  * Interfaces Utilisateur Graphiques avec Tk
    * `tkinter` --- Python interface to Tcl/Tk
    * `tkinter.colorchooser` --- Color choosing dialog
    * `tkinter.font` --- Tkinter font wrapper
    * Boîtes de dialogue _Tkinter_
    * `tkinter.messagebox` --- Tkinter message prompts
    * `tkinter.scrolledtext` --- Scrolled Text Widget
    * `tkinter.dnd` --- Drag and drop support
    * `tkinter.ttk` --- Tk themed widgets
    * IDLE --- Python editor and shell
  * Outils de développement
    * `typing` — Prise en charge des annotations de type
    * `pydoc` --- Documentation generator and online help system
    * Python Development Mode
    * `doctest` — Exemples de tests interactifs en Python
    * `unittest` --- Unit testing framework
    * `unittest.mock` --- mock object library
    * `unittest.mock` --- getting started
    * `test` --- Regression tests package for Python
    * `test.support` --- Utilities for the Python test suite
    * `test.support.socket_helper` --- Utilities for socket tests
    * `test.support.script_helper` --- Utilities for the Python execution tests
    * `test.support.bytecode_helper` --- Support tools for testing correct bytecode generation
    * `test.support.threading_helper` --- Utilities for threading tests
    * `test.support.os_helper` --- Utilities for os tests
    * `test.support.import_helper` --- Utilities for import tests
    * `test.support.warnings_helper` --- Utilities for warnings tests
  * Débogueur et instrumentation
    * Table des évènements d'audit
    * `bdb` --- Debugger framework
    * `faulthandler` --- Dump the Python traceback
    * `pdb` — Le débogueur Python
    * The Python Profilers
    * `timeit` --- Measure execution time of small code snippets
    * `trace` --- Trace or track Python statement execution
    * `tracemalloc` --- Trace memory allocations
  * Paquets et distribution de paquets logiciels
    * `ensurepip` --- Bootstrapping the `pip` installer
    * `venv` --- Creation of virtual environments
    * `zipapp` --- Manage executable Python zip archives
  * Environnement d'exécution Python
    * `sys` --- System-specific parameters and functions
    * `sys.monitoring` --- Execution event monitoring
    * `sysconfig` --- Provide access to Python's configuration information
    * `builtins` --- Built-in objects
    * `__main__` --- Top-level code environment
    * `warnings` --- Warning control
    * `dataclasses` --- Data Classes
    * `contextlib` — Utilitaires pour les contextes s'appuyant sur l'instruction `with`
    * `abc` --- Abstract Base Classes
    * `atexit` --- Exit handlers
    * `traceback` --- Print or retrieve a stack traceback
    * `__future__` --- Future statement definitions
    * `gc` --- Garbage Collector interface
    * `inspect` --- Inspect live objects
    * `site` --- Site-specific configuration hook
  * Interpréteurs Python personnalisés
    * `code` --- Interpreter base classes
    * `codeop` --- Compile Python code
  * Importer des modules
    * `zipimport` --- Import modules from Zip archives
    * `pkgutil` --- Package extension utility
    * `modulefinder` --- Find modules used by a script
    * `runpy` --- Locating and executing Python modules
    * `importlib` --- The implementation of `import`
    * `importlib.resources` -- Package resource reading, opening and access
    * `importlib.resources.abc` -- Abstract base classes for resources
    * `importlib.metadata` -- Accessing package metadata
    * The initialization of the `sys.path` module search path
  * Services du Langage Python
    * `ast` --- Abstract Syntax Trees
    * `symtable` --- Access to the compiler's symbol tables
    * `token` --- Constants used with Python parse trees
    * `keyword` --- Testing for Python keywords
    * `tokenize` --- Tokenizer for Python source
    * `tabnanny` --- Detection of ambiguous indentation
    * `pyclbr` --- Python module browser support
    * `py_compile` --- Compile Python source files
    * `compileall` --- Byte-compile Python libraries
    * `dis` --- Disassembler for Python bytecode
    * `pickletools` --- Tools for pickle developers
  * Services spécifiques à MS Windows
    * `msvcrt` --- Useful routines from the MS VC++ runtime
    * `winreg` --- Windows registry access
    * `winsound` --- Sound-playing interface for Windows
  * Services spécifiques à Unix
    * `posix` --- The most common POSIX system calls
    * `pwd` --- The password database
    * `grp` --- The group database
    * `termios` --- POSIX style tty control
    * `tty` --- Terminal control functions
    * `pty` --- Pseudo-terminal utilities
    * `fcntl` --- The `fcntl` and `ioctl` system calls
    * `resource` --- Resource usage information
    * `syslog` --- Unix syslog library routines
  * Modules command-line interface (CLI)
  * Modules remplacés
    * `getopt` --- C-style parser for command line options
  * Removed Modules
  * Considérations de sécurité


#### Sujet précédent
10. Spécification complète de la grammaire
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
  * La bibliothèque standard
  * | 
  * Theme  Auto Light Dark |


©  Copyright  2001-2025, Python Software Foundation. This page is licensed under the Python Software Foundation License Version 2. Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License. See History and License for more information. The Python Software Foundation is a non-profit corporation. Please donate. Mis à jour le févr. 17, 2025 (05:58 UTC). Found a bug? Créé en utilisant Sphinx 8.1.3. 
