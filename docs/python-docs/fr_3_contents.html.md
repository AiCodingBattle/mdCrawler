### Navigation
  * index
  * modules |
  * suivant |
  * ![Python logo](https://docs.python.org/fr/3/_static/py.svg)
  * Python »
  * EnglishSpanishFrenchItalianJapaneseKoreanPolishBrazilian PortugueseTurkishSimplified ChineseTraditional Chinese
dev (3.14)3.13.23.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
  * 3.13.2 Documentation » 
  * Contenu de la documentation Python
  * | 
  * Theme  Auto Light Dark |


# Contenu de la documentation Python¶
  * Nouveautés de Python
    * What's New In Python 3.13
      * Summary -- Release Highlights
      * Nouvelles fonctionnalités
        * A better interactive interpreter
        * Improved error messages
        * Free-threaded CPython
        * An experimental just-in-time (JIT) compiler
        * Defined mutation semantics for `locals()`
        * Support for mobile platforms
      * Autres changements au langage
      * Nouveaux modules
      * Modules améliorés
        * argparse
        * _array_
        * _ast_
        * _asyncio_
        * base64
        * _compileall_
        * _concurrent.futures_
        * configparser
        * copy
        * ctypes
        * dbm
        * dis
        * doctest
        * email
        * enum
        * `fractions`
        * glob
        * _importlib_
        * io
        * _ipaddress_
        * itertools
        * marshal
        * _math_
        * mimetypes
        * mmap
        * _multiprocessing_
        * _os_
        * `os.path`
        * _pathlib_
        * _pdb_
        * queue
        * _random_
        * `re`
        * `shutils`
        * `site`
        * `sqlite3`
        * `ssl`
        * `statistics`
        * subprocess
        * _sys_
        * tempfile
        * _time_
        * tkinter
        * traceback
        * `types`
        * _typing_
        * _unicodedata_
        * _venv_
        * warnings
        * _xml_
        * `zipimport`
      * Optimisations
      * Removed Modules And APIs
        * PEP 594: Remove "dead batteries" from the standard library
        * 2to3
        * builtins
        * configparser
        * `importlib.metadata`
        * locale
        * opcode
        * optparse
        * _pathlib_
        * `re`
        * tkinter.tix
        * turtle
        * _typing_
        * unittest
        * urllib
        * webbrowser
      * New Deprecations
        * Pending Removal in Python 3.14
        * Pending Removal in Python 3.15
        * Pending removal in Python 3.16
        * Pending Removal in Future Versions
      * CPython Bytecode Changes
      * Changements à l'API C
        * Nouvelles fonctionnalités
        * Changed C APIs
        * Limited C API Changes
        * Removed C APIs
        * Deprecated C APIs
          * Pending Removal in Python 3.14
          * Pending Removal in Python 3.15
          * Pending Removal in Future Versions
      * Changements à la compilation
      * Porting to Python 3.13
        * Changements dans l'API Python
        * Changements dans l'API C
      * Regression Test Changes
      * Notable changes in 3.13.1
        * _sys_
    * What's New In Python 3.12
      * Résumé – Points marquants de cette version
      * Nouvelles fonctionnalités
        * PEP 695: Type Parameter Syntax
        * PEP 701: Syntactic formalization of f-strings
        * PEP 684: A Per-Interpreter GIL
        * PEP 669: Low impact monitoring for CPython
        * PEP 688: Making the buffer protocol accessible in Python
        * PEP 709: Comprehension inlining
        * Improved Error Messages
      * Nouvelles fonctionnalités reliées aux indications de types
        * PEP 692: Using `TypedDict` for more precise `**kwargs` typing
        * PEP 698: Override Decorator for Static Typing
      * Autres changements au langage
      * Nouveaux modules
      * Modules améliorés
        * _array_
        * _asyncio_
        * calendar
        * csv
        * dis
        * `fractions`
        * importlib.resources
        * _inspect_
        * itertools
        * _math_
        * _os_
        * `os.path`
        * _pathlib_
        * _pdb_
        * _random_
        * `shutils`
        * `sqlite3`
        * `statistics`
        * _sys_
        * tempfile
        * threading
        * tkinter
        * tokenize
        * `types`
        * _typing_
        * _unicodedata_
        * unittest
        * uuid
      * Optimisations
      * Changements au code intermédiaire CPython
      * Demos and Tools
      * Obsolescence
        * Pending Removal in Python 3.13
        * Pending Removal in Python 3.14
        * Pending Removal in Python 3.15
        * Pending removal in Python 3.16
        * Pending Removal in Future Versions
      * Retraits
        * asynchat and asyncore
        * configparser
        * _distutils_
        * ensurepip
        * enum
        * _ftplib_
        * gzip
        * _hashlib_
        * _importlib_
        * imp
        * io
        * locale
        * smtpd
        * `sqlite3`
        * `ssl`
        * unittest
        * webbrowser
        * xml.etree.ElementTree
        * `zipimport`
        * Autres
      * Porting to Python 3.12
        * Changements dans l'API Python
      * Changements à la compilation
      * Changements à l'API C
        * Nouvelles fonctionnalités
        * Porting to Python 3.12
        * Obsolescence
          * Pending Removal in Python 3.14
          * Pending Removal in Python 3.15
          * Pending Removal in Future Versions
        * Retraits
    * Les nouveautés de Python 3.11
      * Résumé – Points forts de la publication
      * Nouvelles fonctionnalités
        * PEP 657 : amélioration de l'emplacement des erreurs dans les traces d'appels
        * PEP 654 : Groupes d'exception et `except*`
        * PEP 678: Exceptions can be enriched with notes
        * Améliorations du lanceur Windows `py.exe`
      * Nouvelles fonctionnalités reliées aux indications de types
        * PEP 646: Variadic generics
        * PEP 655: Marking individual `TypedDict` items as required or not-required
        * PEP 673: `Self` type
        * PEP 675: Arbitrary literal string type
        * PEP 681: Data class transforms
        * PEP 563 may not be the future
      * Autres changements au langage
      * Autres changements à l'implémentation de CPython
      * Nouveaux modules
      * Modules améliorés
        * `asyncio`
        * contextlib
        * `dataclasses`
        * _datetime_
        * enum
        * `fcntl`
        * `fractions`
        * functools
        * gzip
        * _hashlib_
        * `IDLE` et `idlelib`
        * `inspect`
        * locale
        * logging
        * `math`
        * `operator`
        * `os`
        * _pathlib_
        * `re`
        * `shutils`
        * `socket`
        * `sqlite3`
        * _string_
        * `sys`
        * `sysconfig`
        * tempfile
        * `threading`
        * `time`
        * tkinter
        * traceback
        * _typing_
        * `unicodedata`
        * unittest
        * `venv`
        * warnings
        * `zipfile`
      * Optimisations
      * Faster CPython
        * Faster Startup
          * Frozen imports / Static code objects
        * Faster Runtime
          * Cheaper, lazy Python frames
          * Inlined Python function calls
          * PEP 659: Specializing Adaptive Interpreter
        * Misc
        * FAQ
          * How should I write my code to utilize these speedups?
          * Will CPython 3.11 use more memory?
          * I don't see any speedups in my workload. Why?
          * Is there a JIT compiler?
        * À propos
      * Changements au code intermédiaire CPython
        * New opcodes
        * Replaced opcodes
        * Changed/removed opcodes
      * Obsolescence
        * Language/Builtins
        * Modules
        * Bibliothèque Standard
      * Pending Removal in Python 3.12
      * Retraits
      * Portage vers Python 3.11
      * Changements à la compilation
      * Changements à l'API C
        * Nouvelles fonctionnalités
        * Portage vers Python 3.11
        * Obsolescence
        * Pending Removal in Python 3.12
        * Retraits
      * Notable changes in 3.11.4
        * tarfile
      * Notable changes in 3.11.5
        * OpenSSL
    * Les nouveautés de Python 3.10
      * Résumé – Points forts de la publication
      * Nouvelles fonctionnalités
        * Gestionnaires de contextes entre parenthèses
        * Meilleurs messages d'erreurs
          * `SyntaxError`
          * `IndentationError`
          * `AttributeError`
          * `NameError`
        * PEP 626 : numéros de lignes précis pour le débogage et les autres outils
        * PEP 634 : filtrage par motifs structurels
          * Syntaxe et opérations
          * Approche déclarative
          * Filtre simple : apparier à un littéral
            * Comportement sans l'attrape-tout
          * Filtres avec un littéral et une variable
          * Filtres et classes
            * Filtres avec arguments positionnels
          * Filtres imbriqués
          * Filtres complexes et attrape-tout
          * Garde
          * Autres fonctionnalités importantes
        * `EncodingWarning` et option `encoding="locale"` optionnels
      * Nouvelles fonctionnalités reliées aux indications de types
        * PEP 604 : nouvel opérateur d'union de types
        * PEP 612 : variables de spécification de paramètres
        * PEP 613 : `TypeAlias`
        * PEP 647 : gardes de type définies par l'utilisateur
      * Autres changements au langage
      * Nouveaux modules
      * Modules améliorés
        * `asyncio`
        * `argparse`
        * `array`
        * `asynchat`, `asyncore`, `smtpd`
        * `base64`
        * `bdb`
        * `bisect`
        * `codecs`
        * `collections.abc`
        * `contextlib`
        * `curses`
        * `dataclasses`
          * `__slots__`
          * Champs obligatoirement nommés
        * `distutils`
        * `doctest`
        * `encodings`
        * enum
        * `fileinput`
        * `faulthandler`
        * `gc`
        * `glob`
        * `hashlib`
        * `hmac`
        * IDLE et `idlelib`
        * `importlib.metadata`
        * `inspect`
        * itertools
        * `linecache`
        * `os`
        * `os.path`
        * `pathlib`
        * `platform`
        * `pprint`
        * `py_compile`
        * `pyclbr`
        * `shelve`
        * `statistics`
        * `site`
        * `socket`
        * `ssl`
        * `sqlite3`
        * `sys`
        * `_thread`
        * `threading`
        * `traceback`
        * `types`
        * `typing`
        * `unittest`
        * `urllib.parse`
        * `xml`
        * `zipimport`
      * Optimisations
      * Obsolescence
      * Retrait
      * Portage vers Python 3.10
        * Changements à la syntaxe de Python
        * Changements dans l'API Python
        * Changements dans l'API C
      * Changements au code intermédiaire CPython
      * Changements à la compilation
      * Changements à l'API C
        * PEP 652 : maintenance d'une ABI stable
        * Nouvelles fonctionnalités
        * Portage vers Python 3.10
        * Obsolescence
        * Retrait
      * Notable security feature in 3.10.7
      * Notable security feature in 3.10.8
      * Notable changes in 3.10.12
        * tarfile
    * Les nouveautés de Python 3.9
      * Résumé – Points marquants de cette version
      * Vous devez vérifier la présence de `DeprecationWarning` dans votre code
      * Nouvelles fonctionnalités
        * Opérateurs de fusion et de mise à jour de dictionnaires
        * Nouvelles méthodes sur les chaînes pour retirer des préfixes et des suffixes
        * Indication des types paramétrables dans les collections natives
        * Nouvel analyseur syntaxique
      * Autres changements au langage
      * Nouveaux modules
        * _zoneinfo_
        * _graphlib_
      * Modules améliorés
        * _ast_
        * _asyncio_
        * _compileall_
        * _concurrent.futures_
        * _curses_
        * _datetime_
        * _distutils_
        * _fcntl_
        * _ftplib_
        * _gc_
        * _hashlib_
        * _http_
        * _IDLE_ et _idlelib_
        * _imaplib_
        * _importlib_
        * _inspect_
        * _ipaddress_
        * _math_
        * _multiprocessing_
        * _nntplib_
        * _os_
        * _pathlib_
        * _pdb_
        * _poplib_
        * _pprint_
        * _pydoc_
        * _random_
        * _signal_
        * _smtplib_
        * _socket_
        * _time_
        * _sys_
        * _tracemalloc_
        * _typing_
        * _unicodedata_
        * _venv_
        * _xml_
      * Optimisations
      * Obsolescence
      * Retraits
      * Portage vers Python 3.9
        * Changements dans l'API Python
        * Changements dans l'API C
        * Changements au code intermédiaire CPython
      * Changements à la compilation
      * Changements à l'API C
        * Nouvelles fonctionnalités
        * Portage vers Python 3.9
        * Retraits
      * Changements importants dans Python 3.9.1
        * _typing_
        * Prise en charge de _macOS_ 11.0 (Big Sur) et de Mac sur processeur Apple
      * Changements importants dans Python 3.9.2
        * _collections.abc_
        * _urllib.parse_
      * Notable changes in Python 3.9.3
      * Notable changes in Python 3.9.5
        * _urllib.parse_
      * Notable security feature in 3.9.14
      * Notable changes in 3.9.17
        * tarfile
    * Nouveautés de Python 3.8
      * Summary -- Release highlights
      * Nouvelles fonctionnalités
        * Expression d'affectation
        * Positional-only parameters
        * Parallel filesystem cache for compiled bytecode files
        * Debug build uses the same ABI as release build
        * f-strings support `=` for self-documenting expressions and debugging
        * PEP 578: Python Runtime Audit Hooks
        * PEP 587: Python Initialization Configuration
        * PEP 590: Vectorcall: a fast calling protocol for CPython
        * Pickle protocol 5 with out-of-band data buffers
      * Autres changements au langage
      * Nouveaux modules
      * Modules améliorés
        * ast
        * asyncio
        * builtins
        * collections
        * cProfile
        * csv
        * curses
        * ctypes
        * datetime
        * functools
        * _gc_
        * gettext
        * gzip
        * _IDLE_ et _idlelib_
        * _inspect_
        * io
        * itertools
        * json.tool
        * logging
        * _math_
        * mmap
        * multiprocessing
        * _os_
        * `os.path`
        * pathlib
        * pickle
        * plistlib
        * _pprint_
        * `py_compile`
        * shlex
        * `shutils`
        * _socket_
        * `ssl`
        * `statistics`
        * sys
        * tarfile
        * threading
        * tokenize
        * tkinter
        * time
        * _typing_
        * unicodedata
        * unittest
        * venv
        * weakref
        * _xml_
        * xmlrpc
      * Optimizations
      * Build and C API Changes
      * Obsolescence
      * API and Feature Removals
      * Porting to Python 3.8
        * Changes in Python behavior
        * Changements dans l'API Python
        * Changements dans l'API C
        * Changements au code intermédiaire CPython
        * Demos and Tools
      * Notable changes in Python 3.8.1
      * Notable changes in Python 3.8.2
      * Notable changes in Python 3.8.3
      * Notable changes in Python 3.8.8
      * Notable changes in Python 3.8.9
      * Notable changes in Python 3.8.10
        * Prise en charge de _macOS_ 11.0 (Big Sur) et de Mac sur processeur Apple
      * Notable changes in Python 3.8.10
        * _urllib.parse_
      * Notable changes in Python 3.8.12
        * Changements dans l'API Python
      * Notable security feature in 3.8.14
      * Notable changes in 3.8.17
        * tarfile
    * What's New In Python 3.7
      * Summary -- Release Highlights
      * Nouvelles fonctionnalités
        * PEP 563: Postponed Evaluation of Annotations
        * PEP 538: Legacy C Locale Coercion
        * PEP 540: Forced UTF-8 Runtime Mode
        * PEP 553: Built-in `breakpoint()`
        * PEP 539: New C API for Thread-Local Storage
        * PEP 562: Customization of Access to Module Attributes
        * PEP 564: New Time Functions With Nanosecond Resolution
        * PEP 565: Show DeprecationWarning in `__main__`
        * PEP 560: Core Support for `typing` module and Generic Types
        * PEP 552: Hash-based .pyc Files
        * PEP 545: Python Documentation Translations
        * Python Development Mode (-X dev)
      * Autres changements au langage
      * Nouveaux modules
        * contextvars
        * `dataclasses`
        * importlib.resources
      * Modules améliorés
        * argparse
        * asyncio
        * binascii
        * calendar
        * collections
        * compileall
        * concurrent.futures
        * contextlib
        * cProfile
        * crypt
        * datetime
        * dbm
        * decimal
        * dis
        * distutils
        * enum
        * functools
        * _gc_
        * `hmac`
        * http.client
        * http.server
        * idlelib and IDLE
        * importlib
        * io
        * _ipaddress_
        * itertools
        * locale
        * logging
        * _math_
        * mimetypes
        * msilib
        * multiprocessing
        * _os_
        * pathlib
        * _pdb_
        * `py_compile`
        * _pydoc_
        * queue
        * `re`
        * _signal_
        * _socket_
        * socketserver
        * `sqlite3`
        * `ssl`
        * _string_
        * subprocess
        * sys
        * time
        * tkinter
        * tracemalloc
        * `types`
        * unicodedata
        * unittest
        * unittest.mock
        * urllib.parse
        * uu
        * uuid
        * warnings
        * _xml_
        * xml.etree
        * xmlrpc.server
        * zipapp
        * zipfile
      * Changements à l'API C
      * Changements à la compilation
      * Optimizations
      * Autres changements à l'implémentation de CPython
      * Deprecated Python Behavior
      * Deprecated Python modules, functions and methods
        * aifc
        * asyncio
        * collections
        * dbm
        * enum
        * gettext
        * importlib
        * locale
        * macpath
        * threading
        * _socket_
        * `ssl`
        * sunau
        * sys
        * wave
      * Deprecated functions and types of the C API
      * Platform Support Removals
      * API and Feature Removals
      * Module Removals
      * Windows-only Changes
      * Porting to Python 3.7
        * Changes in Python Behavior
        * Changements dans l'API Python
        * Changements dans l'API C
        * Changements au code intermédiaire CPython
        * Windows-only Changes
        * Other CPython implementation changes
      * Notable changes in Python 3.7.1
      * Notable changes in Python 3.7.2
      * Notable changes in Python 3.7.6
      * Notable changes in Python 3.7.10
      * Notable changes in Python 3.7.11
      * Notable security feature in 3.7.14
    * What's New In Python 3.6
      * Résumé – Points forts de la publication
      * Nouvelles fonctionnalités
        * PEP 498: Formatted string literals
        * PEP 526: Syntax for variable annotations
        * PEP 515: Underscores in Numeric Literals
        * PEP 525: Asynchronous Generators
        * PEP 530: Asynchronous Comprehensions
        * PEP 487: Simpler customization of class creation
        * PEP 487: Descriptor Protocol Enhancements
        * PEP 519: Adding a file system path protocol
        * PEP 495: Local Time Disambiguation
        * PEP 529: Change Windows filesystem encoding to UTF-8
        * PEP 528: Change Windows console encoding to UTF-8
        * PEP 520: Preserving Class Attribute Definition Order
        * PEP 468: Preserving Keyword Argument Order
        * New dict implementation
        * PEP 523: Adding a frame evaluation API to CPython
        * PYTHONMALLOC environment variable
        * DTrace and SystemTap probing support
      * Autres changements au langage
      * Nouveaux modules
        * secrets
      * Modules améliorés
        * _array_
        * ast
        * asyncio
        * binascii
        * cmath
        * collections
        * concurrent.futures
        * contextlib
        * datetime
        * decimal
        * distutils
        * email
        * `encodings`
        * enum
        * `faulthandler`
        * `fileinput`
        * _hashlib_
        * http.client
        * idlelib and IDLE
        * importlib
        * _inspect_
        * json
        * logging
        * _math_
        * multiprocessing
        * _os_
        * pathlib
        * _pdb_
        * pickle
        * pickletools
        * _pydoc_
        * _random_
        * `re`
        * readline
        * rlcompleter
        * shlex
        * `site`
        * `sqlite3`
        * _socket_
        * socketserver
        * `ssl`
        * `statistics`
        * struct
        * subprocess
        * sys
        * telnetlib
        * time
        * timeit
        * tkinter
        * traceback
        * tracemalloc
        * _typing_
        * unicodedata
        * unittest.mock
        * urllib.request
        * urllib.robotparser
        * venv
        * warnings
        * winreg
        * winsound
        * xmlrpc.client
        * zipfile
        * zlib
      * Optimizations
      * Build and C API Changes
      * Autres Améliorations
      * Obsolescence
        * Nouveaux mot-clefs
        * Deprecated Python behavior
        * Deprecated Python modules, functions and methods
          * asynchat
          * asyncore
          * dbm
          * distutils
          * grp
          * importlib
          * _os_
          * `re`
          * `ssl`
          * tkinter
          * venv
        * _xml_
        * Deprecated functions and types of the C API
        * Deprecated Build Options
      * Retraits
        * API and Feature Removals
      * Porting to Python 3.6
        * Changes in 'python' Command Behavior
        * Changements dans l'API Python
        * Changements dans l'API C
        * Changements au code intermédiaire CPython
      * Notable changes in Python 3.6.2
        * New `make regen-all` build target
        * Removal of `make touch` build target
      * Notable changes in Python 3.6.4
      * Notable changes in Python 3.6.5
      * Notable changes in Python 3.6.7
      * Notable changes in Python 3.6.10
      * Notable changes in Python 3.6.13
      * Notable changes in Python 3.6.14
    * Nouveautés de Python 3.5
      * Résumé – Points forts de la publication
      * Nouvelles fonctionnalités
        * PEP 492 - Coroutines with async and await syntax
        * PEP 465 - A dedicated infix operator for matrix multiplication
        * PEP 448 - Additional Unpacking Generalizations
        * PEP 461 - percent formatting support for bytes and bytearray
        * PEP 484 - Type Hints
        * PEP 471 - os.scandir() function -- a better and faster directory iterator
        * PEP 475: Retry system calls failing with EINTR
        * PEP 479: Change StopIteration handling inside generators
        * PEP 485: A function for testing approximate equality
        * PEP 486: Make the Python Launcher aware of virtual environments
        * PEP 488 : Élimination des fichiers PYO
        * PEP 489: Multi-phase extension module initialization
      * Autres changements au langage
      * Nouveaux modules
        * _typing_
        * zipapp
      * Modules améliorés
        * argparse
        * asyncio
        * bz2
        * cgi
        * cmath
        * code
        * collections
        * collections.abc
        * compileall
        * concurrent.futures
        * configparser
        * contextlib
        * csv
        * curses
        * dbm
        * difflib
        * distutils
        * doctest
        * email
        * enum
        * `faulthandler`
        * functools
        * glob
        * gzip
        * heapq
        * _http_
        * http.client
        * idlelib and IDLE
        * _imaplib_
        * imghdr
        * importlib
        * _inspect_
        * io
        * _ipaddress_
        * json
        * `linecache`
        * locale
        * logging
        * lzma
        * _math_
        * multiprocessing
        * `operator`
        * _os_
        * pathlib
        * pickle
        * _poplib_
        * `re`
        * readline
        * selectors
        * `shutils`
        * _signal_
        * smtpd
        * _smtplib_
        * sndhdr
        * _socket_
        * `ssl`
          * Memory BIO Support
          * Application-Layer Protocol Negotiation Support
          * Other Changes
        * `sqlite3`
        * subprocess
        * sys
        * `sysconfig`
        * tarfile
        * threading
        * time
        * timeit
        * tkinter
        * traceback
        * `types`
        * unicodedata
        * unittest
        * unittest.mock
        * urllib
        * wsgiref
        * xmlrpc
        * xml.sax
        * zipfile
      * Other module-level changes
      * Optimizations
      * Build and C API Changes
      * Obsolescence
        * Nouveaux mot-clefs
        * Deprecated Python Behavior
        * Unsupported Operating Systems
        * Deprecated Python modules, functions and methods
      * Retraits
        * API and Feature Removals
      * Portage vers Python 3.5
        * Changes in Python behavior
        * Changements dans l'API Python
        * Changements dans l'API C
      * Notable changes in Python 3.5.4
        * New `make regen-all` build target
        * Removal of `make touch` build target
    * Nouveautés de Python 3.4
      * Summary -- Release Highlights
      * Nouvelles fonctionnalités
        * PEP 453: Explicit Bootstrapping of PIP in Python Installations
          * Bootstrapping pip By Default
          * Documentation Changes
        * PEP 446: Newly Created File Descriptors Are Non-Inheritable
        * Improvements to Codec Handling
        * PEP 451: A ModuleSpec Type for the Import System
        * Autres changements au langage
      * Nouveaux modules
        * asyncio
        * ensurepip
        * enum
        * pathlib
        * selectors
        * `statistics`
        * tracemalloc
      * Modules améliorés
        * abc
        * aifc
        * argparse
        * audioop
        * base64
        * collections
        * colorsys
        * contextlib
        * dbm
        * dis
        * doctest
        * email
        * filecmp
        * functools
        * _gc_
        * glob
        * _hashlib_
        * `hmac`
        * html
        * _http_
        * idlelib and IDLE
        * importlib
        * _inspect_
        * _ipaddress_
        * logging
        * marshal
        * mmap
        * multiprocessing
        * `operator`
        * _os_
        * _pdb_
        * pickle
        * plistlib
        * _poplib_
        * _pprint_
        * pty
        * _pydoc_
        * `re`
        * resource
        * select
        * `shelve`
        * `shutils`
        * smtpd
        * _smtplib_
        * _socket_
        * `sqlite3`
        * `ssl`
        * stat
        * struct
        * subprocess
        * sunau
        * sys
        * tarfile
        * textwrap
        * threading
        * traceback
        * `types`
        * urllib
        * unittest
        * venv
        * wave
        * weakref
        * xml.etree
        * zipfile
      * CPython Implementation Changes
        * PEP 445: Customization of CPython Memory Allocators
        * PEP 442: Safe Object Finalization
        * PEP 456: Secure and Interchangeable Hash Algorithm
        * PEP 436: Argument Clinic
        * Other Build and C API Changes
        * Autres Améliorations
        * Significant Optimizations
      * Obsolescence
        * Deprecations in the Python API
        * Fonctionnalités obsolètes
      * Retraits
        * Operating Systems No Longer Supported
        * API and Feature Removals
        * Code Cleanups
      * Portage vers Python 3.4
        * Changes in 'python' Command Behavior
        * Changements dans l'API Python
        * Changements dans l'API C
      * Changed in 3.4.3
        * PEP 476: Enabling certificate verification by default for stdlib http clients
    * Nouveautés de Python 3.3
      * Résumé – Points forts de la publication
      * PEP 405: Virtual Environments
      * PEP 420: Implicit Namespace Packages
      * PEP 3118: New memoryview implementation and buffer protocol documentation
        * Caractéristiques
        * API changes
      * PEP 393: Flexible String Representation
        * Functionality
        * Performance and resource usage
      * PEP 397: Python Launcher for Windows
      * PEP 3151: Reworking the OS and IO exception hierarchy
      * PEP 380: Syntax for Delegating to a Subgenerator
      * PEP 409: Suppressing exception context
      * PEP 414: Explicit Unicode literals
      * PEP 3155: Qualified name for classes and functions
      * PEP 412: Key-Sharing Dictionary
      * PEP 362: Function Signature Object
      * PEP 421: Adding sys.implementation
        * SimpleNamespace
      * Using importlib as the Implementation of Import
        * New APIs
        * Visible Changes
      * Autres changements au langage
      * A Finer-Grained Import Lock
      * Builtin functions and types
      * Nouveaux modules
        * `faulthandler`
        * _ipaddress_
        * lzma
      * Modules améliorés
        * abc
        * _array_
        * base64
        * binascii
        * bz2
        * `codecs`
        * collections
        * contextlib
        * crypt
        * curses
        * datetime
        * decimal
          * Caractéristiques
          * API changes
        * email
          * Policy Framework
          * Provisional Policy with New Header API
          * Other API Changes
        * _ftplib_
        * functools
        * _gc_
        * `hmac`
        * _http_
        * html
        * _imaplib_
        * _inspect_
        * io
        * itertools
        * logging
        * _math_
        * mmap
        * multiprocessing
        * _nntplib_
        * _os_
        * _pdb_
        * pickle
        * _pydoc_
        * `re`
        * sched
        * select
        * shlex
        * `shutils`
        * _signal_
        * smtpd
        * _smtplib_
        * _socket_
        * socketserver
        * `sqlite3`
        * `ssl`
        * stat
        * struct
        * subprocess
        * sys
        * tarfile
        * tempfile
        * textwrap
        * threading
        * time
        * `types`
        * unittest
        * urllib
        * webbrowser
        * xml.etree.ElementTree
        * zlib
      * Optimizations
      * Build and C API Changes
      * Obsolescence
        * Unsupported Operating Systems
        * Deprecated Python modules, functions and methods
        * Deprecated functions and types of the C API
        * Fonctionnalités obsolètes
      * Portage vers Python 3.3
        * Portage de code Python
        * Porting C code
        * Building C extensions
        * Command Line Switch Changes
    * Nouveautés de Python 3.2
      * PEP 384: Defining a Stable ABI
      * PEP 389: Argparse Command Line Parsing Module
      * PEP 391: Dictionary Based Configuration for Logging
      * PEP 3148: The `concurrent.futures` module
      * PEP 3147: PYC Repository Directories
      * PEP 3149: ABI Version Tagged .so Files
      * PEP 3333: Python Web Server Gateway Interface v1.0.1
      * Autres changements au langage
      * New, Improved, and Deprecated Modules
        * email
        * elementtree
        * functools
        * itertools
        * collections
        * threading
        * datetime and time
        * _math_
        * abc
        * io
        * reprlib
        * logging
        * csv
        * contextlib
        * decimal and fractions
        * ftp
        * popen
        * select
        * gzip and zipfile
        * tarfile
        * _hashlib_
        * ast
        * _os_
        * `shutils`
        * `sqlite3`
        * html
        * _socket_
        * `ssl`
        * nntp
        * certificates
        * _imaplib_
        * http.client
        * unittest
        * _random_
        * _poplib_
        * asyncore
        * tempfile
        * _inspect_
        * _pydoc_
        * dis
        * dbm
        * ctypes
        * `site`
        * `sysconfig`
        * _pdb_
        * configparser
        * urllib.parse
        * mailbox
        * turtledemo
      * Fils d'exécution
      * Optimizations
      * Unicode
      * Codecs
      * Documentation
      * IDLE
      * Code Repository
      * Build and C API Changes
      * Portage vers Python 3.2
    * Nouveautés de Python 3.1
      * PEP 372: Ordered Dictionaries
      * PEP 378: Format Specifier for Thousands Separator
      * Autres changements au langage
      * New, Improved, and Deprecated Modules
      * Optimizations
      * IDLE
      * Build and C API Changes
      * Portage vers Python 3.1
    * Nouveautés de Python 3.0
      * Common Stumbling Blocks
        * Print Is A Function
        * Views And Iterators Instead Of Lists
        * Ordering Comparisons
        * Integers
        * Text Vs. Data Instead Of Unicode Vs. 8-bit
      * Overview Of Syntax Changes
        * New Syntax
        * Changed Syntax
        * Removed Syntax
      * Changes Already Present In Python 2.6
      * Library Changes
      * **PEP 3101** : A New Approach To String Formatting
      * Changes To Exceptions
      * Miscellaneous Other Changes
        * Operators And Special Methods
        * Builtins
      * Build and C API Changes
      * Performances
      * Portage vers Python 3.0
    * Nouveautés de Python 2.7
      * The Future for Python 2.x
      * Changes to the Handling of Deprecation Warnings
      * Python 3.1 Features
      * PEP 372: Adding an Ordered Dictionary to collections
      * PEP 378: Format Specifier for Thousands Separator
      * PEP 389: The argparse Module for Parsing Command Lines
      * PEP 391: Dictionary-Based Configuration For Logging
      * PEP 3106: Dictionary Views
      * PEP 3137: The memoryview Object
      * Autres changements au langage
        * Interpreter Changes
        * Optimizations
      * New and Improved Modules
        * New module: importlib
        * New module: sysconfig
        * ttk: Themed Widgets for Tk
        * Updated module: unittest
        * Module mis-à-jour : ElementTree 1.3
      * Build and C API Changes
        * Capsules
        * Port-Specific Changes: Windows
        * Port-Specific Changes: Mac OS X
        * Port-Specific Changes: FreeBSD
      * Autres changements et corrections
      * Portage vers Python 2.7
      * New Features Added to Python 2.7 Maintenance Releases
        * Two new environment variables for debug mode
        * PEP 434: IDLE Enhancement Exception for All Branches
        * PEP 466: Network Security Enhancements for Python 2.7
        * PEP 477: Backport ensurepip (PEP 453) to Python 2.7
          * Bootstrapping pip By Default
          * Documentation Changes
        * PEP 476: Enabling certificate verification by default for stdlib http clients
        * PEP 493: HTTPS verification migration tools for Python 2.7
        * New `make regen-all` build target
        * Removal of `make touch` build target
      * Remerciements
    * Nouveautés de Python 2.6
      * Python 3.0
      * Changes to the Development Process
        * New Issue Tracker: Roundup
        * New Documentation Format: reStructuredText Using Sphinx
      * PEP 343: The 'with' statement
        * Écrire des gestionnaires de contexte
        * Le module _contextlib_
      * PEP 366: Explicit Relative Imports From a Main Module
      * PEP 370: Per-user `site-packages` Directory
      * PEP 371: The `multiprocessing` Package
      * PEP 3101: Advanced String Formatting
      * PEP 3105: `print` As a Function
      * PEP 3110: Exception-Handling Changes
      * PEP 3112: Byte Literals
      * PEP 3116: New I/O Library
      * PEP 3118: Revised Buffer Protocol
      * PEP 3119: Abstract Base Classes
      * PEP 3127: Integer Literal Support and Syntax
      * PEP 3129: Class Decorators
      * PEP 3141: A Type Hierarchy for Numbers
        * The `fractions` Module
      * Autres changements au langage
        * Optimizations
        * Interpreter Changes
      * New and Improved Modules
        * The `ast` module
        * The `future_builtins` module
        * The `json` module: JavaScript Object Notation
        * The `plistlib` module: A Property-List Parser
        * ctypes Enhancements
        * Improved SSL Support
      * Deprecations and Removals
      * Build and C API Changes
        * Port-Specific Changes: Windows
        * Port-Specific Changes: Mac OS X
        * Port-Specific Changes: IRIX
      * Portage vers Python 2.6
      * Remerciements
    * Nouveautés de Python 2.5
      * PEP 308 : Expressions conditionnelles
      * PEP 309 : Application partielle de fonction
      * PEP 314: Metadata for Python Software Packages v1.1
      * PEP 328: Absolute and Relative Imports
      * PEP 338: Executing Modules as Scripts
      * PEP 341: Unified try/except/finally
      * PEP 342: New Generator Features
      * PEP 343: The 'with' statement
        * Écrire des gestionnaires de contexte
        * Le module _contextlib_
      * PEP 352: Exceptions as New-Style Classes
      * PEP 353: Using ssize_t as the index type
      * PEP 357: The '__index__' method
      * Autres changements au langage
        * Changements de l’interpréteur interactif
        * Optimizations
      * Modules ajoutés, modifiés, et supprimés
        * The ctypes package
        * The ElementTree package
        * The hashlib package
        * The sqlite3 package
        * The wsgiref package
      * Build and C API Changes
        * Port-Specific Changes
      * Portage vers Python 2.5
      * Remerciements
    * Nouveautés de Python 2.4
      * PEP 218: Built-In Set Objects
      * PEP 237: Unifying Long Integers and Integers
      * PEP 289: Generator Expressions
      * PEP 292: Simpler String Substitutions
      * PEP 318: Decorators for Functions and Methods
      * PEP 322: Reverse Iteration
      * PEP 324: New subprocess Module
      * PEP 327: Decimal Data Type
        * Why is Decimal needed?
        * The `Decimal` type
        * The `Context` type
      * PEP 328: Multi-line Imports
      * PEP 331: Locale-Independent Float/String Conversions
      * Autres changements au langage
        * Optimizations
      * New, Improved, and Deprecated Modules
        * cookielib
        * doctest
      * Build and C API Changes
        * Port-Specific Changes
      * Portage vers Python 2.4
      * Remerciements
    * Nouveautés de Python 2.3
      * PEP 218: A Standard Set Datatype
      * PEP 255 : Générateurs simples
      * PEP 263: Source Code Encodings
      * PEP 273: Importing Modules from ZIP Archives
      * PEP 277: Unicode file name support for Windows NT
      * PEP 278: Universal Newline Support
      * PEP 279: enumerate()
      * PEP 282: The logging Package
      * PEP 285 : Un type booléen
      * PEP 293: Codec Error Handling Callbacks
      * PEP 301: Package Index and Metadata for Distutils
      * PEP 302: New Import Hooks
      * PEP 305: Comma-separated Files
      * PEP 307: Pickle Enhancements
      * Extended Slices
      * Autres changements au langage
        * String Changes
        * Optimizations
      * New, Improved, and Deprecated Modules
        * Date/Time Type
        * The optparse Module
      * Pymalloc: A Specialized Object Allocator
      * Build and C API Changes
        * Port-Specific Changes
      * Autres changements et corrections
      * Portage vers Python 2.3
      * Remerciements
    * Nouveautés de Python 2.2
      * Introduction
      * PEP 252 et 253 : Changements concernant les types et classes
        * Anciennes et nouvelles classes
        * Descripteurs
        * Héritage multiple : la règle du diamant
        * Attribute Access
        * Related Links
      * PEP 234 : Itérateurs
      * PEP 255 : Générateurs simples
      * PEP 237: Unifying Long Integers and Integers
      * PEP 238: Changing the Division Operator
      * Unicode Changes
      * PEP 227: Nested Scopes
      * New and Improved Modules
      * Interpreter Changes and Fixes
      * Autres changements et corrections
      * Remerciements
    * Nouveautés de Python 2.1
      * Introduction
      * PEP 227: Nested Scopes
      * PEP 236 : Directives `__future__`
      * PEP 207: Rich Comparisons
      * PEP 230: Warning Framework
      * PEP 229: New Build System
      * PEP 205: Weak References
      * PEP 232 : Attributs de fonctions
      * PEP 235: Importing Modules on Case-Insensitive Platforms
      * PEP 217: Interactive Display Hook
      * PEP 208: New Coercion Model
      * PEP 241: Metadata in Python Packages
      * New and Improved Modules
      * Autres changements et corrections
      * Remerciements
    * Nouveautés de Python 2.0
      * Introduction
      * À propos de Python 1.6.
      * Nouveau processus de développement
      * Unicode
      * Compréhensions de listes
      * Opérateurs d’affectation augmentées
      * Méthodes de chaînes de caractères
      * Garbage Collection of Cycles
      * Other Core Changes
        * Changements mineurs du langage
        * Changements concernant les fonctions primitives
      * Porting to 2.0
      * Extending/Embedding Changes
      * Distutils: Making Modules Easy to Install
      * Modules XML
        * Support de SAX2
        * Support du DOM
        * Relationship to PyXML
      * Module changes
      * Nouveaux modules
      * IDLE Improvements
      * Deleted and Deprecated Modules
      * Remerciements
    * Changelog
      * Python next
        * Tools/Demos
        * Library
        * IDLE
        * Core and Builtins
        * C API
        * Build
      * Python 3.13.2 final
        * macOS
        * Windows
        * Tools/Demos
        * Tests
        * Security
        * Library
        * Documentation
        * Core and Builtins
        * C API
        * Build
      * Python 3.13.1 final
        * macOS
        * Windows
        * Tools/Demos
        * Tests
        * Security
        * Library
        * IDLE
        * Documentation
        * Core and Builtins
        * C API
        * Build
      * Python 3.13.0 final
        * Core and Builtins
      * Python 3.13.0 release candidate 3
        * macOS
        * Windows
        * Tests
        * Library
        * IDLE
        * Documentation
        * Core and Builtins
        * C API
        * Build
      * Python 3.13.0 release candidate 2
        * macOS
        * Windows
        * Tools/Demos
        * Tests
        * Security
        * Library
        * IDLE
        * Core and Builtins
        * C API
        * Build
      * Python 3.13.0 release candidate 1
        * Tests
        * Security
        * Library
        * IDLE
        * Core and Builtins
        * C API
        * Build
      * Python 3.13.0 beta 4
        * Tests
        * Library
        * IDLE
        * Documentation
        * Core and Builtins
        * C API
        * Build
      * Python 3.13.0 beta 3
        * Core and Builtins
        * Library
        * Build
        * C API
      * Python 3.13.0 beta 2
        * Security
        * Core and Builtins
        * Library
        * Tests
        * Build
        * Windows
        * C API
      * Python 3.13.0 beta 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Build
        * Windows
        * macOS
        * IDLE
        * C API
      * Python 3.13.0 alpha 6
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * C API
      * Python 3.13.0 alpha 5
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.13.0 alpha 4
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.13.0 alpha 3
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * C API
      * Python 3.13.0 alpha 2
        * Core and Builtins
        * Library
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.13.0 alpha 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.12.0 beta 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.12.0 alpha 7
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * Tools/Demos
        * C API
      * Python 3.12.0 alpha 6
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * C API
      * Python 3.12.0 alpha 5
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
      * Python 3.12.0 alpha 4
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * Tools/Demos
        * C API
      * Python 3.12.0 alpha 3
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * Tools/Demos
        * C API
      * Python 3.12.0 alpha 2
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * C API
      * Python 3.12.0 alpha 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.11.0 beta 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * Tools/Demos
        * C API
      * Python 3.11.0 alpha 7
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * Tools/Demos
        * C API
      * Python 3.11.0 alpha 6
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * IDLE
        * C API
      * Python 3.11.0 alpha 5
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * C API
      * Python 3.11.0 alpha 4
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * C API
      * Python 3.11.0 alpha 3
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * C API
      * Python 3.11.0 alpha 2
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * C API
      * Python 3.11.0 alpha 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.10.0 beta 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * C API
      * Python 3.10.0 alpha 7
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * IDLE
        * C API
      * Python 3.10.0 alpha 6
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * C API
      * Python 3.10.0 alpha 5
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * C API
      * Python 3.10.0 alpha 4
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * macOS
        * Tools/Demos
        * C API
      * Python 3.10.0 alpha 3
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.10.0 alpha 2
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * C API
      * Python 3.10.0 alpha 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * C API
      * Python 3.9.0 beta 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * Tools/Demos
        * C API
      * Python 3.9.0 alpha 6
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.9.0 alpha 5
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.9.0 alpha 4
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * IDLE
        * C API
      * Python 3.9.0 alpha 3
        * Core and Builtins
        * Library
        * Documentation
        * Build
        * IDLE
        * C API
      * Python 3.9.0 alpha 2
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * C API
      * Python 3.9.0 alpha 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.8.0 beta 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.8.0 alpha 4
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.8.0 alpha 3
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.8.0 alpha 2
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Windows
        * IDLE
      * Python 3.8.0 alpha 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.7.0 final
        * Library
        * C API
      * Python 3.7.0 release candidate 1
        * Core and Builtins
        * Library
        * Documentation
        * Build
        * Windows
        * IDLE
      * Python 3.7.0 beta 5
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * macOS
        * IDLE
      * Python 3.7.0 beta 4
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
      * Python 3.7.0 beta 3
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.7.0 beta 2
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
      * Python 3.7.0 beta 1
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * C API
      * Python 3.7.0 alpha 4
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Windows
        * Tools/Demos
        * C API
      * Python 3.7.0 alpha 3
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.7.0 alpha 2
        * Core and Builtins
        * Library
        * Documentation
        * Build
        * IDLE
        * C API
      * Python 3.7.0 alpha 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.6.6 final
      * Python 3.6.6 release candidate 1
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.6.5 final
        * Tests
        * Build
      * Python 3.6.5 release candidate 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.6.4 final
      * Python 3.6.4 release candidate 1
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * macOS
        * IDLE
        * Tools/Demos
        * C API
      * Python 3.6.3 final
        * Library
        * Build
      * Python 3.6.3 release candidate 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * IDLE
        * Tools/Demos
      * Python 3.6.2 final
      * Python 3.6.2 release candidate 2
        * Security
      * Python 3.6.2 release candidate 1
        * Security
        * Core and Builtins
        * Library
        * IDLE
        * C API
        * Build
        * Documentation
        * Tools/Demos
        * Tests
        * Windows
      * Python 3.6.1 final
        * Core and Builtins
        * Build
      * Python 3.6.1 release candidate 1
        * Core and Builtins
        * Library
        * IDLE
        * Windows
        * C API
        * Documentation
        * Tests
        * Build
      * Python 3.6.0 final
      * Python 3.6.0 release candidate 2
        * Core and Builtins
        * Tools/Demos
        * Windows
        * Build
      * Python 3.6.0 release candidate 1
        * Core and Builtins
        * Library
        * C API
        * Documentation
        * Tools/Demos
      * Python 3.6.0 beta 4
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
      * Python 3.6.0 beta 3
        * Core and Builtins
        * Library
        * Windows
        * Build
        * Tests
      * Python 3.6.0 beta 2
        * Core and Builtins
        * Library
        * Windows
        * C API
        * Build
        * Tests
      * Python 3.6.0 beta 1
        * Core and Builtins
        * Library
        * IDLE
        * C API
        * Tests
        * Build
        * Tools/Demos
        * Windows
      * Python 3.6.0 alpha 4
        * Core and Builtins
        * Library
        * IDLE
        * Tests
        * Windows
        * Build
      * Python 3.6.0 alpha 3
        * Security
        * Core and Builtins
        * Library
        * IDLE
        * C API
        * Build
        * Tools/Demos
        * Documentation
        * Tests
      * Python 3.6.0 alpha 2
        * Security
        * Core and Builtins
        * Library
        * IDLE
        * Documentation
        * Tests
        * Windows
        * Build
        * C API
        * Tools/Demos
      * Python 3.6.0 alpha 1
        * Security
        * Core and Builtins
        * Library
        * IDLE
        * Documentation
        * Tests
        * Build
        * Windows
        * Tools/Demos
        * C API
      * Python 3.5.5 final
      * Python 3.5.5 release candidate 1
        * Security
        * Core and Builtins
        * Library
      * Python 3.5.4 final
        * Library
      * Python 3.5.4 release candidate 1
        * Security
        * Core and Builtins
        * Library
        * Documentation
        * Tests
        * Build
        * Windows
        * C API
      * Python 3.5.3 final
      * Python 3.5.3 release candidate 1
        * Security
        * Core and Builtins
        * Library
        * IDLE
        * C API
        * Documentation
        * Tests
        * Tools/Demos
        * Windows
        * Build
      * Python 3.5.2 final
        * Core and Builtins
        * Tests
        * IDLE
      * Python 3.5.2 release candidate 1
        * Security
        * Core and Builtins
        * Library
        * IDLE
        * Documentation
        * Tests
        * Build
        * Windows
        * Tools/Demos
      * Python 3.5.1 final
        * Core and Builtins
        * Windows
      * Python 3.5.1 release candidate 1
        * Core and Builtins
        * Library
        * IDLE
        * Documentation
        * Tests
        * Build
        * Windows
        * Tools/Demos
      * Python 3.5.0 final
        * Build
      * Python 3.5.0 release candidate 4
        * Library
        * Build
      * Python 3.5.0 release candidate 3
        * Core and Builtins
        * Library
      * Python 3.5.0 release candidate 2
        * Core and Builtins
        * Library
      * Python 3.5.0 release candidate 1
        * Core and Builtins
        * Library
        * IDLE
        * Documentation
        * Tests
      * Python 3.5.0 beta 4
        * Core and Builtins
        * Library
        * Build
      * Python 3.5.0 beta 3
        * Core and Builtins
        * Library
        * Tests
        * Documentation
        * Build
      * Python 3.5.0 beta 2
        * Core and Builtins
        * Library
      * Python 3.5.0 beta 1
        * Core and Builtins
        * Library
        * IDLE
        * Tests
        * Documentation
        * Tools/Demos
      * Python 3.5.0 alpha 4
        * Core and Builtins
        * Library
        * Build
        * Tests
        * Tools/Demos
        * C API
      * Python 3.5.0 alpha 3
        * Core and Builtins
        * Library
        * Build
        * Tests
        * Tools/Demos
      * Python 3.5.0 alpha 2
        * Core and Builtins
        * Library
        * Build
        * C API
        * Windows
      * Python 3.5.0 alpha 1
        * Core and Builtins
        * Library
        * IDLE
        * Build
        * C API
        * Documentation
        * Tests
        * Tools/Demos
        * Windows
  * Le tutoriel Python
    * 1. Mise en bouche
    * 2. Mode d'emploi de l'interpréteur Python
      * 2.1. Lancement de l'interpréteur
        * 2.1.1. Passage d'arguments
        * 2.1.2. Mode interactif
      * 2.2. L'interpréteur et son environnement
        * 2.2.1. Encodage du code source
    * 3. Introduction informelle à Python
      * 3.1. Utilisation de Python comme une calculatrice
        * 3.1.1. Les nombres
        * 3.1.2. Text
        * 3.1.3. Listes
      * 3.2. Premiers pas vers la programmation
    * 4. D'autres outils de contrôle de flux
      * 4.1. L'instruction `if`
      * 4.2. L'instruction `for`
      * 4.3. La fonction `range()`
      * 4.4. Les instructions `break` et `continue`
      * 4.5. La clause `else` au sein des boucles
      * 4.6. L'instruction `pass`
      * 4.7. L'instruction `match`
      * 4.8. Définir des fonctions
      * 4.9. Davantage sur la définition des fonctions
        * 4.9.1. Valeur par défaut des arguments
        * 4.9.2. Les arguments nommés
        * 4.9.3. Paramètres spéciaux
          * 4.9.3.1. Les arguments positionnels-ou-nommés
          * 4.9.3.2. Paramètres positionnels uniquement
          * 4.9.3.3. Arguments nommés uniquement
          * 4.9.3.4. Exemples de fonctions
          * 4.9.3.5. Récapitulatif
        * 4.9.4. Listes d'arguments arbitraires
        * 4.9.5. Séparation des listes d'arguments
        * 4.9.6. Fonctions anonymes
        * 4.9.7. Chaînes de documentation
        * 4.9.8. Annotations de fonctions
      * 4.10. Aparté : le style de codage
    * 5. Structures de données
      * 5.1. Compléments sur les listes
        * 5.1.1. Utilisation des listes comme des piles
        * 5.1.2. Utilisation des listes comme des files
        * 5.1.3. Listes en compréhension
        * 5.1.4. Listes en compréhensions imbriquées
      * 5.2. L'instruction `del`
      * 5.3. _n_ -uplets et séquences
      * 5.4. Ensembles
      * 5.5. Dictionnaires
      * 5.6. Techniques de boucles
      * 5.7. Plus d'informations sur les conditions
      * 5.8. Comparer des séquences avec d'autres types
    * 6. Modules
      * 6.1. Les modules en détail
        * 6.1.1. Exécuter des modules comme des scripts
        * 6.1.2. Les dossiers de recherche de modules
        * 6.1.3. Fichiers Python « compilés »
      * 6.2. Modules standards
      * 6.3. La fonction `dir()`
      * 6.4. Les paquets
        * 6.4.1. Importer * depuis un paquet
        * 6.4.2. Références internes dans un paquet
        * 6.4.3. Paquets dans plusieurs dossiers
    * 7. Les entrées/sorties
      * 7.1. Formatage de données
        * 7.1.1. Les chaines de caractères formatées (_f-strings_)
        * 7.1.2. La méthode de chaine de caractères `format()`
        * 7.1.3. Formatage de chaînes à la main
        * 7.1.4. Anciennes méthodes de formatage de chaînes
      * 7.2. Lecture et écriture de fichiers
        * 7.2.1. Méthodes des objets fichiers
        * 7.2.2. Sauvegarde de données structurées avec le module `json`
    * 8. Erreurs et exceptions
      * 8.1. Les erreurs de syntaxe
      * 8.2. Exceptions
      * 8.3. Gestion des exceptions
      * 8.4. Déclencher des exceptions
      * 8.5. Chaînage d'exceptions
      * 8.6. Exceptions définies par l'utilisateur
      * 8.7. Définition d'actions de nettoyage
      * 8.8. Actions de nettoyage prédéfinies
      * 8.9. Levée et gestion de multiples exceptions non corrélées
      * 8.10. Enrichissement des exceptions avec des notes
    * 9. Classes
      * 9.1. Objets et noms : préambule
      * 9.2. Portées et espaces de nommage en Python
        * 9.2.1. Exemple de portées et d'espaces de nommage
      * 9.3. Une première approche des classes
        * 9.3.1. Syntaxe de définition des classes
        * 9.3.2. Objets classes
        * 9.3.3. Objets instances
        * 9.3.4. Objets méthode
        * 9.3.5. Variables de classe et d’instance
      * 9.4. Remarques diverses
      * 9.5. Héritage
        * 9.5.1. Héritage multiple
      * 9.6. Variables privées
      * 9.7. Trucs et astuces
      * 9.8. Itérateurs
      * 9.9. Générateurs
      * 9.10. Expressions et générateurs
    * 10. Survol de la bibliothèque standard
      * 10.1. Interface avec le système d'exploitation
      * 10.2. Jokers sur les noms de fichiers
      * 10.3. Paramètres passés en ligne de commande
      * 10.4. Redirection de la sortie d'erreur et fin d'exécution
      * 10.5. Recherche de motifs dans les chaînes
      * 10.6. Mathématiques
      * 10.7. Accès à internet
      * 10.8. Dates et heures
      * 10.9. Compression de données
      * 10.10. Mesure des performances
      * 10.11. Contrôle qualité
      * 10.12. Piles fournies
    * 11. Survol de la bibliothèque standard -- Deuxième partie
      * 11.1. Formatage de l'affichage
      * 11.2. Gabarits (_templates_ en anglais)
      * 11.3. Traitement des données binaires
      * 11.4. Fils d'exécution
      * 11.5. Journalisation
      * 11.6. Références faibles
      * 11.7. Outils pour les listes
      * 11.8. Decimal Floating-Point Arithmetic
    * 12. Environnements virtuels et paquets
      * 12.1. Introduction
      * 12.2. Création d'environnements virtuels
      * 12.3. Gestion des paquets avec _pip_
    * 13. Pour aller plus loin
    * 14. Édition interactive des entrées et substitution d'historique
      * 14.1. Complétion automatique et édition de l'historique
      * 14.2. Alternatives à l'interpréteur interactif
    * 15. Floating-Point Arithmetic: Issues and Limitations
      * 15.1. Erreurs de représentation
    * 16. Annexe
      * 16.1. Mode interactif
        * 16.1.1. Gestion des erreurs
        * 16.1.2. Scripts Python exécutables
        * 16.1.3. Configuration du mode interactif
        * 16.1.4. Modules de personnalisation
  * Installation et utilisation de Python
    * 1. Ligne de commande et environnement
      * 1.1. Ligne de commande
        * 1.1.1. Options de l'interface
        * 1.1.2. Options génériques
        * 1.1.3. Options diverses
        * 1.1.4. Controlling color
        * 1.1.5. Options à ne pas utiliser
      * 1.2. Variables d'environnement
        * 1.2.1. Variables en mode débogage
    * 2. Utilisation de Python sur les plateformes Unix
      * 2.1. Récupérer et installer la dernière version de Python
        * 2.1.1. Sur Linux
          * 2.1.1.1. Installing IDLE
        * 2.1.2. Sur FreeBSD et OpenBSD
      * 2.2. Compiler Python
      * 2.3. Fichiers et chemins liés à Python
      * 2.4. Divers
      * 2.5. Version personnalisée d'OpenSSL
    * 3. Configurer Python
      * 3.1. Build Requirements
      * 3.2. Generated files
        * 3.2.1. configure script
      * 3.3. Options de configuration
        * 3.3.1. Options générales
        * 3.3.2. C compiler options
        * 3.3.3. Linker options
        * 3.3.4. Options for third-party dependencies
        * 3.3.5. Options de WebAssembly
        * 3.3.6. Options d'installation
        * 3.3.7. Options de performance
        * 3.3.8. Compilation de Python en mode débogage
        * 3.3.9. Debug options
        * 3.3.10. Linker options
        * 3.3.11. Libraries options
        * 3.3.12. Security Options
        * 3.3.13. macOS Options
        * 3.3.14. iOS Options
        * 3.3.15. Cross Compiling Options
      * 3.4. Python Build System
        * 3.4.1. Main files of the build system
        * 3.4.2. Main build steps
        * 3.4.3. Main Makefile targets
          * 3.4.3.1. make
          * 3.4.3.2. make platform
          * 3.4.3.3. make profile-opt
          * 3.4.3.4. make clean
          * 3.4.3.5. make distclean
          * 3.4.3.6. make install
          * 3.4.3.7. make test
          * 3.4.3.8. make buildbottest
          * 3.4.3.9. make regen-all
        * 3.4.4. C extensions
      * 3.5. Compiler and linker flags
        * 3.5.1. Preprocessor flags
        * 3.5.2. Compiler flags
        * 3.5.3. Linker flags
    * 4. Utilisation de Python sur Windows
      * 4.1. L'installateur complet
        * 4.1.1. Étapes d'installation
        * 4.1.2. Suppression de la limitation `MAX_PATH`
        * 4.1.3. Installation sans l'interface utilisateur
        * 4.1.4. Installation sans téléchargement
        * 4.1.5. Modification d'une installation
        * 4.1.6. Installing Free-threaded Binaries
      * 4.2. Le paquet Microsoft Store
        * 4.2.1. Problèmes connus
          * 4.2.1.1. Redirection des données locales, du registre et des chemins temporaires
      * 4.3. Les paquets _nuget.org_
        * 4.3.1. Free-threaded packages
      * 4.4. Le paquet intégrable
        * 4.4.1. Application Python
        * 4.4.2. Embarquer Python
      * 4.5. Paquets alternatifs
      * 4.6. Configurer Python
        * 4.6.1. Digression : définition des variables d'environnement
        * 4.6.2. Trouver l'exécutable Python
      * 4.7. Mode UTF-8
      * 4.8. Lanceur Python pour Windows
        * 4.8.1. Pour commencer
          * 4.8.1.1. Depuis la ligne de commande
          * 4.8.1.2. Environnements virtuels
          * 4.8.1.3. À partir d'un script
          * 4.8.1.4. À partir d'associations de fichiers
        * 4.8.2. Lignes Shebang
        * 4.8.3. Arguments dans les lignes _shebang_
        * 4.8.4. Personnalisation
          * 4.8.4.1. Personnalisation via des fichiers INI
          * 4.8.4.2. Personnalisation des versions Python par défaut
        * 4.8.5. Diagnostics
        * 4.8.6. Exécution à vide
        * 4.8.7. Installation à la demande
        * 4.8.8. Codes de retour
      * 4.9. Recherche de modules
      * 4.10. Modules supplémentaires
        * 4.10.1. PyWin32
        * 4.10.2. cx_Freeze
      * 4.11. Compiler Python sous Windows
      * 4.12. Autres plateformes
    * 5. Using Python on macOS
      * 5.1. Using Python for macOS from `python.org`
        * 5.1.1. Étapes d'installation
        * 5.1.2. Comment exécuter un script Python
      * 5.2. Alternative Distributions
      * 5.3. Installation de paquets Python additionnels
      * 5.4. GUI Programming
      * 5.5. Sujets avancés
        * 5.5.1. Installing Free-threaded Binaries
        * 5.5.2. Installing using the command line
        * 5.5.3. Distributing Python Applications
        * 5.5.4. App Store Compliance
      * 5.6. Autres ressources
    * 6. Using Python on Android
      * 6.1. Adding Python to an Android app
    * 7. Using Python on iOS
      * 7.1. Python at runtime on iOS
        * 7.1.1. iOS version compatibility
        * 7.1.2. Platform identification
        * 7.1.3. Standard library availability
        * 7.1.4. Binary extension modules
        * 7.1.5. Compiler stub binaries
      * 7.2. Installing Python on iOS
        * 7.2.1. Tools for building iOS apps
        * 7.2.2. Adding Python to an iOS project
        * 7.2.3. Testing a Python package
      * 7.3. App Store Compliance
    * 8. Éditeurs et IDEs
      * 8.1. IDLE --- Python editor and shell
      * 8.2. Other Editors and IDEs
  * La référence du langage Python
    * 1. Introduction
      * 1.1. Autres implémentations
      * 1.2. Notations
    * 2. Analyse lexicale
      * 2.1. Structure des lignes
        * 2.1.1. Lignes logiques
        * 2.1.2. Lignes physiques
        * 2.1.3. Commentaires
        * 2.1.4. Déclaration d'encodage
        * 2.1.5. Continuation de ligne explicite
        * 2.1.6. Continuation de ligne implicite
        * 2.1.7. Lignes vierges
        * 2.1.8. Indentation
        * 2.1.9. Espaces entre lexèmes
      * 2.2. Autres lexèmes
      * 2.3. Identifiants et mots-clés
        * 2.3.1. Mots-clés
        * 2.3.2. Mots-clés ad hoc
        * 2.3.3. Classes réservées pour les identifiants
      * 2.4. Littéraux
        * 2.4.1. Littéraux de chaînes de caractères et de suites d'octets
          * 2.4.1.1. Escape sequences
        * 2.4.2. Concaténation de chaînes de caractères
        * 2.4.3. f-strings
        * 2.4.4. Littéraux numériques
        * 2.4.5. Entiers littéraux
        * 2.4.6. Floating-point literals
        * 2.4.7. Imaginaires littéraux
      * 2.5. Opérateurs
      * 2.6. Délimiteurs
    * 3. Modèle de données
      * 3.1. Objets, valeurs et types
      * 3.2. Hiérarchie des types standards
        * 3.2.1. `None`
        * 3.2.2. NotImplemented
        * 3.2.3. Ellipse
        * 3.2.4. `numbers.Number`
          * 3.2.4.1. `numbers.Integral`
          * 3.2.4.2. `numbers.Real` (`float`)
          * 3.2.4.3. `numbers.Complex` (`complex`)
        * 3.2.5. Séquences
          * 3.2.5.1. Séquences immuables
          * 3.2.5.2. Séquences mutables
        * 3.2.6. Ensembles
        * 3.2.7. Tableaux de correspondances
          * 3.2.7.1. Dictionnaires
        * 3.2.8. Types appelables
          * 3.2.8.1. Fonctions définies par l'utilisateur
            * 3.2.8.1.1. Special read-only attributes
            * 3.2.8.1.2. Special writable attributes
          * 3.2.8.2. Méthodes d'instances
          * 3.2.8.3. Fonctions génératrices (ou générateurs)
          * 3.2.8.4. Fonctions coroutines
          * 3.2.8.5. Fonctions génératrices (ou générateurs) asynchrones
          * 3.2.8.6. Fonctions natives
          * 3.2.8.7. Méthodes natives
          * 3.2.8.8. Classes
          * 3.2.8.9. Instances de classe
        * 3.2.9. Modules
          * 3.2.9.1. Import-related attributes on module objects
          * 3.2.9.2. Other writable attributes on module objects
          * 3.2.9.3. Module dictionaries
        * 3.2.10. Classes déclarées par le développeur
          * 3.2.10.1. Special attributes
          * 3.2.10.2. Special methods
        * 3.2.11. Instances de classe
          * 3.2.11.1. Special attributes
        * 3.2.12. Objets entrées-sorties (ou objets fichiers)
        * 3.2.13. Types internes
          * 3.2.13.1. Objets Code
            * 3.2.13.1.1. Special read-only attributes
            * 3.2.13.1.2. Methods on code objects
          * 3.2.13.2. Objets cadres
            * 3.2.13.2.1. Special read-only attributes
            * 3.2.13.2.2. Special writable attributes
            * 3.2.13.2.3. Frame object methods
          * 3.2.13.3. Objets traces d'appels
          * 3.2.13.4. Objets tranches
          * 3.2.13.5. Objets méthodes statiques
          * 3.2.13.6. Objets méthodes de classes
      * 3.3. Méthodes spéciales
        * 3.3.1. Personnalisation de base
        * 3.3.2. Personnalisation de l'accès aux attributs
          * 3.3.2.1. Personnalisation de l'accès aux attributs d'un module
          * 3.3.2.2. Implémentation de descripteurs
          * 3.3.2.3. Invocation des descripteurs
          * 3.3.2.4. créneaux prédéfinis (`__slots__`)
        * 3.3.3. Personnalisation de la création de classes
          * 3.3.3.1. Métaclasses
          * 3.3.3.2. Résolution des entrées MRO
          * 3.3.3.3. Détermination de la métaclasse appropriée
          * 3.3.3.4. Préparation de l'espace de nommage de la classe
          * 3.3.3.5. Exécution du corps de la classe
          * 3.3.3.6. Création de l'objet classe
          * 3.3.3.7. Cas d'utilisations des métaclasses
        * 3.3.4. Personnalisation des instances et vérification des sous-classes
        * 3.3.5. Émulation de types génériques
          * 3.3.5.1. Intention de ___class_getitem___
          * 3.3.5.2. ___class_getitem___ contre ___getitem___
        * 3.3.6. Émulation d'objets appelables
        * 3.3.7. Émulation de types conteneurs
        * 3.3.8. Émulation de types numériques
        * 3.3.9. Gestionnaire de contexte With
        * 3.3.10. Arguments positionnels dans le filtrage par motif sur les classes
        * 3.3.11. Emulating buffer types
        * 3.3.12. Recherche des méthodes spéciales
      * 3.4. Coroutines
        * 3.4.1. Objets _attendables_ (_awaitable_)
        * 3.4.2. Objets coroutines
        * 3.4.3. Itérateurs asynchrones
        * 3.4.4. Gestionnaires de contexte asynchrones
    * 4. Modèle d'exécution
      * 4.1. Structure d'un programme
      * 4.2. Noms et liaisons
        * 4.2.1. Liaisons des noms
        * 4.2.2. Résolution des noms
        * 4.2.3. Annotation scopes
        * 4.2.4. Lazy evaluation
        * 4.2.5. Noms natifs et restrictions d'exécution
        * 4.2.6. Interaction avec les fonctionnalités dynamiques
      * 4.3. Exceptions
    * 5. Le système d'importation
      * 5.1. `importlib`
      * 5.2. Les paquets
        * 5.2.1. Paquets classiques
        * 5.2.2. Paquets espaces de nommage
      * 5.3. Recherche
        * 5.3.1. Cache des modules
        * 5.3.2. Chercheurs et chargeurs
        * 5.3.3. Points d'entrées automatiques pour l'importation
        * 5.3.4. Méta-chemins
      * 5.4. Chargement
        * 5.4.1. Chargeurs
        * 5.4.2. Sous-modules
        * 5.4.3. Spécificateurs de modules
        * 5.4.4. l'attribut `__path__` des modules
        * 5.4.5. Représentation textuelle d'un module
        * 5.4.6. Invalidation de _bytecode_ mis en cache
      * 5.5. Le chercheur dans _path_
        * 5.5.1. Chercheurs d'entrée dans _path_
        * 5.5.2. Protocole des chercheurs d'entrée dans _path_
      * 5.6. Remplacement du système d'importation standard
      * 5.7. Importations relatives au paquet
      * 5.8. Cas particulier de `__main__`
        * 5.8.1. `__main__.__spec__`
      * 5.9. Références
    * 6. Expressions
      * 6.1. Conversions arithmétiques
      * 6.2. Atomes
        * 6.2.1. Identifiants (noms)
          * 6.2.1.1. Private name mangling
        * 6.2.2. Littéraux
        * 6.2.3. Formes parenthésées
        * 6.2.4. Agencements des listes, ensembles et dictionnaires
        * 6.2.5. Agencements de listes
        * 6.2.6. Agencements d'ensembles
        * 6.2.7. Agencements de dictionnaires
        * 6.2.8. Expressions génératrices
        * 6.2.9. Expressions `yield`
          * 6.2.9.1. Méthodes des générateurs-itérateurs
          * 6.2.9.2. Exemples
          * 6.2.9.3. Fonctions génératrices asynchrones
          * 6.2.9.4. Méthodes des générateurs-itérateurs asynchrones
      * 6.3. Primaires
        * 6.3.1. Références à des attributs
        * 6.3.2. sélection (ou indiçage)
        * 6.3.3. Tranches
        * 6.3.4. Appels
      * 6.4. Expression `await`
      * 6.5. L'opérateur puissance
      * 6.6. Arithmétique unaire et opérations sur les bits
      * 6.7. Opérations arithmétiques binaires
      * 6.8. Opérations de décalage
      * 6.9. Opérations binaires bit à bit
      * 6.10. Comparaisons
        * 6.10.1. Comparaisons de valeurs
        * 6.10.2. Opérations de tests d’appartenance à un ensemble
        * 6.10.3. Comparaisons d'identifiants
      * 6.11. Opérations booléennes
      * 6.12. Expressions d'affectation
      * 6.13. Expressions conditionnelles
      * 6.14. Expressions lambda
      * 6.15. Listes d'expressions
      * 6.16. Ordre d'évaluation
      * 6.17. Priorités des opérateurs
    * 7. Les instructions simples
      * 7.1. Les expressions
      * 7.2. Les assignations
        * 7.2.1. Les assignations augmentées
        * 7.2.2. Les assignations annotées
      * 7.3. L'instruction `assert`
      * 7.4. L'instruction `pass`
      * 7.5. L'instruction `del`
      * 7.6. L'instruction `return`
      * 7.7. L'instruction `yield`
      * 7.8. L'instruction `raise`
      * 7.9. L'instruction `break`
      * 7.10. L'instruction `continue`
      * 7.11. L'instruction `import`
        * 7.11.1. L'instruction future
      * 7.12. L'instruction `global`
      * 7.13. L'instruction `nonlocal`
      * 7.14. The `type` statement
    * 8. Instructions composées
      * 8.1. L'instruction `if`
      * 8.2. L'instruction `while`
      * 8.3. L'instruction `for`
      * 8.4. L'instruction `try`
        * 8.4.1. clause `except`
        * 8.4.2. clause `except*`
        * 8.4.3. clause `else`
        * 8.4.4. clause `finally`
      * 8.5. L'instruction `with`
      * 8.6. L'instruction `match`
        * 8.6.1. Aperçu
        * 8.6.2. Gardes
        * 8.6.3. Bloc `case` attrape-tout
        * 8.6.4. Filtres
          * 8.6.4.1. Filtres OU
          * 8.6.4.2. Filtres AS
          * 8.6.4.3. Filtres littéraux
          * 8.6.4.4. Filtres de capture
          * 8.6.4.5. Filtres attrape-tout
          * 8.6.4.6. Filtres par valeurs
          * 8.6.4.7. Filtres de groupes
          * 8.6.4.8. Filtres de séquences
          * 8.6.4.9. Filtres associatifs
          * 8.6.4.10. Filtres de classes
      * 8.7. Définition de fonctions
      * 8.8. Définition de classes
      * 8.9. Coroutines
        * 8.9.1. Définition de fonctions coroutines
        * 8.9.2. L'instruction `async for`
        * 8.9.3. L'instruction `async with`
      * 8.10. Type parameter lists
        * 8.10.1. Generic functions
        * 8.10.2. Generic classes
        * 8.10.3. Generic type aliases
    * 9. Composants de plus haut niveau
      * 9.1. Programmes Python complets
      * 9.2. Fichier d'entrée
      * 9.3. Entrée interactive
      * 9.4. Entrée d'expression
    * 10. Spécification complète de la grammaire
  * La bibliothèque standard
    * Introduction
      * Notes sur la disponibilité
        * Plateformes WebAssembly
        * Mobile platforms
    * Fonctions natives
    * Constantes natives
      * Constantes ajoutées par le module `site`
    * Types natifs
      * Valeurs booléennes
      * Opérations booléennes — `and`, `or`, `not`
      * Comparaisons
      * Types numériques — `int`, `float`, `complex`
        * Opérations sur les bits des nombres entiers
        * Méthodes supplémentaires sur les entiers
        * Méthodes supplémentaires sur les nombres à virgule flottante
        * Hachage des types numériques
      * Boolean Type - `bool`
      * Les types itérateurs
        * Types générateurs
      * Types séquentiels — `list`, `tuple`, `range`
        * Opérations communes sur les séquences
        * Types de séquences immuables
        * Types de séquences mutables
        * Listes
        * _N_ -uplets
        * _Ranges_
      * Type Séquence de Texte — `str`
        * Méthodes de chaînes de caractères
        * Formatage de chaines à la `printf`
      * Séquences Binaires — `bytes`, `bytearray`, `vue mémoire`
        * Objets _bytes_
        * Objets _bytearray_
        * Opérations sur les _bytes_ et _bytearray_
        * Formatage de _bytes_ a la `printf`
        * Vues mémoire
      * Types d'ensembles — `set`, `frozenset`
      * Les types de correspondances — `dict`
        * Les vues de dictionnaires
      * Le type gestionnaire de contexte
      * Types d'annotation de type — Alias générique, Union
        * Type Alias générique
          * Classes génériques standards
          * Attributs spéciaux des alias génériques
        * Type Union
      * Autres types natifs
        * Modules
        * Les classes et instances de classes
        * Fonctions
        * Méthodes
        * Objets code
        * Objets type
        * L'objet Null
        * L'objet points de suspension (ou ellipse)
        * L'objet _NotImplemented_
        * Objets internes
      * Attributs spéciaux
      * Limitation de longueur de conversion de chaîne vers un entier
        * API concernées
        * Configuration de la limite
        * Configuration recommandée
    * Exceptions natives
      * Contexte des exceptions
      * Hériter des exceptions natives
      * Classes mères
      * Exceptions concrètes
        * Exceptions système
      * Avertissements
      * Exception groups
      * Hiérarchie des exceptions
    * Services de Manipulation de Texte
      * `string` --- Common string operations
        * Chaînes constantes
        * Formatage personnalisé de chaîne
        * Syntaxe de formatage de chaîne
          * Mini-langage de spécification de format
          * Exemples de formats
        * Chaînes modèles
        * Fonctions d'assistance
      * `re` --- Regular expression operations
        * Syntaxe des expressions rationnelles
        * Contenu du module
          * Flags
          * Fonctions
          * Exceptions
        * Objets d'expressions rationnelles
        * Objets de correspondance
        * Exemples d'expressions rationnelles
          * Rechercher une paire
          * Simuler _scanf()_
          * Comparaison de _search()_ et _match()_
          * Construire un répertoire téléphonique
          * Mélanger les lettres des mots
          * Trouver tous les adverbes
          * Trouver tous les adverbes et leurs positions
          * Notation brute de chaînes
          * Écrire un analyseur lexical
      * `difflib` --- Helpers for computing deltas
        * SequenceMatcher Objects
        * SequenceMatcher Examples
        * Differ Objects
        * Differ Example
        * A command-line interface to difflib
        * ndiff example
      * `textwrap` --- Text wrapping and filling
      * `unicodedata` --- Unicode Database
      * `stringprep` --- Internet String Preparation
      * `readline` --- GNU readline interface
        * Fichier d'initialisation
        * Tampon de ligne
        * Fichier d'historique
        * Liste d'historique
        * Fonctions de rappel au démarrage
        * Complétion
        * Exemple
      * `rlcompleter` --- Completion function for GNU readline
    * Services autour des Données Binaires
      * `struct` --- Interpret bytes as packed binary data
        * Fonctions et exceptions
        * Chaînes de spécification du format
          * Boutisme, taille et alignement
          * Caractères de format
          * Exemples
        * Applications
          * Native Formats
          * Standard Formats
        * Classes
      * `codecs` --- Codec registry and base classes
        * Classes de base de codecs
          * Gestionnaires d'erreurs
          * Stateless Encoding and Decoding
          * Incremental Encoding and Decoding
            * IncrementalEncoder Objects
            * IncrementalDecoder Objects
          * Stream Encoding and Decoding
            * StreamWriter Objects
            * StreamReader Objects
            * StreamReaderWriter Objects
            * StreamRecoder Objects
        * Encodings and Unicode
        * Standard Encodings
        * Python Specific Encodings
          * Text Encodings
          * Binary Transforms
          * Text Transforms
        * `encodings.idna` --- Internationalized Domain Names in Applications
        * `encodings.mbcs` --- Windows ANSI codepage
        * `encodings.utf_8_sig` --- UTF-8 codec with BOM signature
    * Types de données
      * `datetime` — Types de base pour la date et l'heure
        * Objets avisés et naïfs
        * Constantes
        * Types disponibles
          * Propriétés communes
          * Catégorisation d'un objet en « avisé » ou « naïf »
        * Objets `timedelta`
          * Exemples d'utilisation de la classe `timedelta` :
        * Objets `date`
          * Exemple d'utilisation de la classe `date` :
        * Objets `datetime`
          * Exemple d'utilisation de la classe `datetime` :
        * Objets `time`
          * Exemples d'utilisation de `time`
        * Objets `tzinfo`
        * Objets `timezone`
        * `strftime()` and `strptime()` Behavior
          * `strftime()` and `strptime()` Format Codes
          * Détail technique
      * `zoneinfo` --- IANA time zone support
        * Utilisation de `ZoneInfo`
        * Sources de données
          * Configurer les sources de données
            * Configuration à la compilation
            * Configuration par l'environnement
            * Configuration à l'exécution
        * La classe `ZoneInfo`
          * Représentation sous forme de chaîne de caractères
          * Sérialisation Pickle
        * Fonctions
        * Variables globales
        * Exceptions et avertissements
      * `calendar` --- General calendar-related functions
        * Utilisation en ligne de commande.
      * `collections` --- Container datatypes
        * Objets `ChainMap`
          * Exemples et cas pratiques utilisant `ChainMap`
        * Objets `Counter`
        * Objets `deque`
          * Cas pratiques utilisant `deque`
        * Objets `defaultdict`
          * Exemples utilisant `defaultdict`
        * `namedtuple()` : fonction de construction pour _n_ -uplets avec des champs nommés
        * Objets `OrderedDict`
          * Exemples et cas pratiques utilisant `OrderDict`
        * Objets `UserDict`
        * Objets `UserList`
        * Objets `UserString`
      * `collections.abc` --- Abstract Base Classes for Containers
        * Classes de base abstraites de collections
        * Collections Abstract Base Classes -- Detailed Descriptions
        * Exemples et recettes
      * `heapq` --- Heap queue algorithm
        * Exemples simples
        * Notes d'implémentation de la file de priorité
        * Théorie
      * `bisect` --- Array bisection algorithm
        * Notes sur la performance
        * Chercher dans des listes triées
        * Exemples
      * `array` --- Efficient arrays of numeric values
      * `weakref` --- Weak references
        * Objets à références faibles
        * Exemple
        * Finalizer Objects
        * Comparing finalizers with `__del__()` methods
      * `types` --- Dynamic type creation and names for built-in types
        * Dynamic Type Creation
        * Standard Interpreter Types
        * Additional Utility Classes and Functions
        * Coroutine Utility Functions
      * `copy` --- Shallow and deep copy operations
      * `pprint` — L’affichage élégant de données
        * Fonctions
        * Les Objets PrettyPrinter
        * Exemple
      * `reprlib` --- Alternate `repr()` implementation
        * Repr Objects
        * Subclassing Repr Objects
      * `enum` --- Support for enumerations
        * Contenu du module
        * Types de données
          * Noms de la forme `__dunder__` disponibles
          * Noms de la forme `_sunder_` disponibles
        * Utilitaires et décorateurs
        * Notes
      * `graphlib` --- Functionality to operate with graph-like structures
        * Exceptions
    * Modules numériques et mathématiques
      * `numbers` --- Numeric abstract base classes
        * La tour numérique
        * Notes for type implementers
          * Ajouter plus d'ABC numériques
          * Implémentation des opérations arithmétiques
      * `math` --- Mathematical functions
        * Number-theoretic functions
        * Floating point arithmetic
        * Floating point manipulation functions
        * Power, exponential and logarithmic functions
        * Summation and product functions
        * Conversion angulaire
        * Fonctions trigonométriques
        * Fonctions hyperboliques
        * Fonctions spéciales
        * Constantes
      * `cmath` --- Mathematical functions for complex numbers
        * Conversion vers et à partir de coordonnées polaires
        * Fonctions logarithme et exponentielle
        * Fonctions trigonométriques
        * Fonctions hyperboliques
        * Fonctions de classifications
        * Constantes
      * `decimal` --- Decimal fixed-point and floating-point arithmetic
        * Introduction pratique
        * Les objets _Decimal_
          * Opérandes logiques
        * Objets de contexte
        * Constantes
        * Modes d'arrondi
        * Signaux
        * Floating-Point Notes
          * Mitigating round-off error with increased precision
          * Special values
        * Working with threads
        * Cas pratiques
        * FAQ _decimal_
      * `fractions` --- Rational numbers
      * `random` --- Generate pseudo-random numbers
        * Fonctions de gestion d'état
        * Fonctions pour les octets
        * Fonctions pour les entiers
        * Fonctions pour les séquences
        * Discrete distributions
        * Distributions pour les nombres réels
        * Générateur alternatif
        * Remarques sur la reproductibilité
        * Exemples
        * Cas pratiques
        * Command-line usage
        * Command-line example
      * `statistics` --- Mathematical statistics functions
        * Moyennes et mesures de la tendance centrale
        * Mesures de la dispersion
        * Statistics for relations between two inputs
        * Détails des fonctions
        * Exceptions
        * Objets `NormalDist`
        * Examples and Recipes
          * Classic probability problems
          * Monte Carlo inputs for simulations
          * Approximating binomial distributions
          * Naive bayesian classifier
    * Modules de programmation fonctionnelle
      * `itertools` --- Functions creating iterators for efficient looping
        * Itertool Functions
        * Recettes _itertools_
      * `functools` --- Higher-order functions and operations on callable objects
        * Objets `partial`
      * `operator` — Opérateurs standards en tant que fonctions
        * Correspondances entre opérateurs et fonctions
        * Opérateurs en-place
    * Accès aux Fichiers et aux Dossiers
      * `pathlib` — Chemins de système de fichiers orientés objet
        * Utilisation basique
        * Exceptions
        * Chemins purs
          * Propriétés générales
          * Opérateurs
          * Accéder aux parties individuelles
          * Méthodes et propriétés
        * Chemins concrets
          * Analyse et génération des URI
          * Expansion et résolution de chemins
          * Requête sur type et statut du fichier
          * Lecture et écriture de fichiers
          * Lecture des dossiers
          * Création de fichiers et de dossiers
          * Renommage et suppression
          * Permissions et propriété
        * Pattern language
        * Comparaison avec les outils du module `glob`
        * Comparaison aux modules `os` et `os.path`
          * Outils correspondants
      * `os.path` --- Common pathname manipulations
      * `stat` --- Interpreting `stat()` results
      * `filecmp` --- File and Directory Comparisons
        * La classe `dircmp`
      * `tempfile` --- Generate temporary files and directories
        * Exemples
        * Fonctions et variables obsolètes
      * `glob` --- Unix style pathname pattern expansion
        * Exemples
      * `fnmatch` --- Unix filename pattern matching
      * `linecache` --- Random access to text lines
      * `shutil` --- High-level file operations
        * Opérations sur les répertoires et les fichiers
          * Platform-dependent efficient copy operations
          * copytree example
          * rmtree example
        * Archiving operations
          * Archiving example
          * Archiving example with _base_dir_
        * Querying the size of the output terminal
    * Persistance des données
      * `pickle` --- Python object serialization
        * Relations aux autres modules Python
          * Comparaison avec `marshal`
          * Comparaison avec `json`
        * Format du flux de données
        * Interface du module
        * Quels objets sont sérialisables ?
        * Sérialisation des instances d'une classe
          * Persistance d'objets externes
          * Tables de distribution
          * Traitement des objets à état
        * Réduction personnalisée pour les types, fonctions et autres objets
        * Tampons hors-bande
          * API des producteurs
          * API des consommateurs
          * Exemple
        * Restriction des noms dans l'espace de nommage global
        * Performances
        * Exemples
      * `copyreg` --- Register `pickle` support functions
        * Exemple
      * `shelve` --- Python object persistence
        * Limites
        * Exemple
      * `marshal` --- Internal Python object serialization
      * `dbm` --- Interfaces to Unix "databases"
        * `dbm.sqlite3` --- SQLite backend for dbm
        * `dbm.gnu` --- GNU database manager
        * `dbm.ndbm` --- New Database Manager
        * `dbm.dumb` --- Portable DBM implementation
      * `sqlite3` --- DB-API 2.0 interface for SQLite databases
        * Tutoriel
        * Références
          * Fonctions du module
          * Fonctions et constantes du module
          * Connection objects
          * Cursor objects
          * Row objects
          * Blob objects
          * PrepareProtocol objects
          * Exceptions
          * SQLite and Python types
          * Default adapters and converters (deprecated)
          * Command-line interface
        * How-to guides
          * How to use placeholders to bind values in SQL queries
          * How to adapt custom Python types to SQLite values
            * How to write adaptable objects
            * How to register adapter callables
          * How to convert SQLite values to custom Python types
          * Adapter and converter recipes
          * How to use connection shortcut methods
          * How to use the connection context manager
          * How to work with SQLite URIs
          * How to create and use row factories
          * How to handle non-UTF-8 text encodings
        * Explanation
          * Transaction control
            * Transaction control via the `autocommit` attribute
            * Transaction control via the `isolation_level` attribute
    * Compression de donnée et archivage
      * `zlib` --- Compression compatible with **gzip**
      * `gzip` --- Support for **gzip** files
        * Exemples d'utilisation
        * Interface en ligne de commande
          * Options de la ligne de commande
      * `bz2` --- Support for **bzip2** compression
        * (Dé)compression de fichiers
        * (Dé)compression incrémentielle
        * (Dé)compression en une fois
        * Exemples d'utilisation
      * `lzma` --- Compression using the LZMA algorithm
        * Lire et écrire des fichiers compressés
        * Compresser et décompresser une donnée en mémoire
        * Divers
        * Préciser des chaînes de filtre personnalisées
        * Exemples
      * `zipfile` --- Work with ZIP archives
        * Objets ZipFile
        * Objets _Path_
        * Objets _PyZipFile_
        * Objets _ZipInfo_
        * Interface en ligne de commande
          * Options de la ligne de commande
        * Problèmes de décompression
          * À cause du fichier lui-même
          * Limitations du système de fichiers
          * Ressources limitées
          * Interruption
          * Comportements par défaut de l'extraction
      * `tarfile` --- Read and write tar archive files
        * Les objets _TarFile_
        * Les objets _TarInfo_
        * Extraction filters
          * Default named filters
          * Filter errors
          * Hints for further verification
          * Supporting older Python versions
          * Stateful extraction filter example
        * Interface en ligne de commande
          * Options de la ligne de commande
        * Exemples
        * Formats _tar_ pris en charge
        * Problèmes _unicode_
    * Formats de fichiers
      * `csv` --- CSV File Reading and Writing
        * Contenu du module
        * Dialectes et paramètres de formatage
        * Objets lecteurs
        * Objets transcripteurs
        * Exemples
      * `configparser` --- Configuration file parser
        * Premiers pas
        * Types de données prises en charge
        * Valeurs de substitution
        * Structure des fichiers _INI_ prise en change
        * Unnamed Sections
        * Interpolation des valeurs
        * Protocole d'accès associatif
        * Personnalisation du comportement de l'analyseur
        * Legacy API Examples
        * ConfigParser Objects
        * RawConfigParser Objects
        * Exceptions
      * `tomllib` --- Parse TOML files
        * Exemples
        * Conversion Table
      * `netrc` --- netrc file processing
        * Objets _netrc_
      * `plistlib` --- Generate and parse Apple `.plist` files
        * Exemples
    * Service de cryptographie
      * `hashlib` --- Algorithmes de hachage sécurisés et synthèse de messages
        * Algorithmes de hachage
        * Utilisation
        * Constructeurs
        * Attributes
        * Objets de calcul d'empreinte
        * Empreintes de messages de taille variable SHAKE
        * Calcul d'empreinte (ou hachage) de fichiers
        * Dérivation de clé
        * BLAKE2
          * Création d'objets de calcul d'empreinte
          * Constantes
          * Exemples
            * Hachage simple
            * Production de tailles d'empreintes différentes
            * Hachage avec clé – Code d'authentification de message
            * Hachage randomisé
            * Personnalisation
            * Mode Arbre
          * Crédits
      * `hmac` --- Keyed-Hashing for Message Authentication
      * `secrets` --- Generate secure random numbers for managing secrets
        * Nombres aléatoires
        * Génération de jetons
          * Combien d'octets mon jeton doit-il comporter ?
        * Autres fonctions
        * Recettes et bonnes pratiques
    * Services génériques du système d'exploitation
      * `os` --- Miscellaneous operating system interfaces
        * Noms de fichiers, arguments en ligne de commande, et variables d'environnement
        * Le mode UTF-8 de Python
        * Paramètres de processus
        * Création de fichiers objets
        * Opérations sur les descripteurs de fichiers
          * Demander la taille d'un terminal
          * Héritage de descripteurs de fichiers
        * Fichiers et répertoires
          * Timer File Descriptors
          * Attributs étendus pour Linux
        * Gestion des processus
        * Interface pour l'ordonnanceur
        * Diverses informations sur le système
        * Nombres aléatoires
      * `io` --- Core tools for working with streams
        * Aperçu
          * Entrée/sortie de texte
          * Binary I/O
          * Raw I/O
        * Encodage de texte
          * Opt-in EncodingWarning
        * Interface de haut niveau du module
        * Class hierarchy
          * I/O Base Classes
          * Raw File I/O
          * Buffered Streams
          * Entrée/sortie de texte
        * Performances
          * Binary I/O
          * Entrée/sortie de texte
          * Fils d'exécution
          * Réentrance
      * `time` --- Time access and conversions
        * Fonctions
        * Constantes d’identification d’horloge
        * Constantes de fuseau horaire
      * `logging` --- Logging facility for Python
        * Enregistreurs
        * Niveaux de journalisation
        * Gestionnaires
        * Formateurs
        * Filtres
        * Objets LogRecord
        * LogRecord attributes
        * LoggerAdapter Objects
        * Thread Safety
        * Fonctions de niveau module
        * Module-Level Attributes
        * Integration with the warnings module
      * `logging.config` --- Logging configuration
        * Configuration functions
        * Security considerations
        * Configuration dictionary schema
          * Dictionary Schema Details
          * Incremental Configuration
          * Object connections
          * User-defined objects
          * Handler configuration order
          * Access to external objects
          * Access to internal objects
          * Import resolution and custom importers
          * Configuring QueueHandler and QueueListener
        * Configuration file format
      * `logging.handlers` --- Logging handlers
        * Gestionnaire à flux — _StreamHandler_
        * Gestionnaire à fichier — _FileHandler_
        * Gestionnaire à puits sans fond — _NullHandler_
        * Gestionnaire à fichier avec surveillance — _WatchedFileHandler_
        * Base des gestionnaires à roulement —  _BaseRotatingHandler_
        * Gestionnaire à roulement de fichiers — _RotatingFileHandler_
        * Gestionnaire à roulement de fichiers périodique — _TimedRotatingFileHandler_
        * Gestionnaire à connecteur —  _SocketHandler_
        * DatagramHandler
        * SysLogHandler
        * NTEventLogHandler
        * SMTPHandler
        * MemoryHandler
        * HTTPHandler
        * QueueHandler
        * QueueListener
      * `platform` --- Access to underlying platform's identifying data
        * Multiplateformes
        * Plateforme Java
        * Plateforme Windows
        * macOS Platform
        * iOS Platform
        * Plateformes Unix
        * Linux Platforms
        * Android Platform
      * `errno` --- Standard errno system symbols
      * `ctypes` --- A foreign function library for Python
        * Didacticiel de _ctypes_
          * Chargement des DLL
          * Accès aux fonctions des DLL chargées
          * Appel de fonctions
          * Types de données de base
          * Appel de fonctions, suite
          * Calling variadic functions
          * Appel de fonctions avec des types de données personnalisés
          * Définition du type des arguments nécessaires (prototypes de fonction)
          * Types de sortie
          * Passage de pointeurs (passage de paramètres par référence)
          * Structures et unions
          * Alignement et boutisme des structures et des unions
          * Champs de bits dans les structures et les unions
          * Tableaux
          * Pointeurs
          * Conversions de type
          * Types incomplets
          * Fonctions de rappel
          * Accès aux variables exportées depuis une DLL
          * Pièges
          * Types de données à taille flottante
        * Référence du module
          * Recherche de bibliothèques partagées
          * Chargement des bibliothèques partagées
          * Fonctions externes
          * Prototypes de fonction
          * Fonctions utilitaires
          * Types de données
          * Types de données de base
          * Types de données dérivés de Structure
          * Tableaux et pointeurs
    * Command Line Interface Libraries
      * `argparse` --- Parser for command-line options, arguments and subcommands
        * Objets `ArgumentParser`
          * Le paramètre _prog_
          * Le paramètre _usage_
          * Le paramètre _description_
          * Le paramètre _epilog_
          * Le paramètre _parents_
          * Le paramètre _formatter_class_
          * Le paramètre _prefix_chars_
          * Le paramètre _fromfile_prefix_chars_
          * Le paramètre _argument_default_
          * Le paramètre _allow_abbrev_
          * Le paramètre _conflict_handler_
          * Le paramètre _add_help_
          * Le paramètre _exit_on_error_
        * La méthode _add_argument()_
          * Le paramètre _name_or_flags_
          * Le paramètre _action_
          * Le paramètre _nargs_
          * Le paramètre _const_
          * Le paramètre _default_
          * Le paramètre _type_
          * Le paramètre _choices_
          * Le paramètre _required_
          * Le paramètre _help_
          * Le paramètre _metavar_
          * Le paramètre _dest_
          * deprecated
          * Classes Action
        * La méthode _parse_args()_
          * Syntaxe de la valeur des options
          * Arguments invalides
          * Arguments contenant `-`
          * Arguments abrégés (par comparaison de leurs préfixes)
          * Au-delà de `sys.argv`
          * L'objet `Namespace`
        * Autres outils
          * Sous commandes
          * Objets `FileType`
          * Groupes d'arguments
          * Exclusion mutuelle
          * Valeurs par défaut de l'analyseur
          * Afficher l'aide
          * Analyse partielle
          * Personnaliser le _parsing_ de fichiers
          * Méthodes d'interruptions
          * Analyse entremêlée
          * Registering custom types or actions
        * Exceptions
          * Tutoriel _argparse_
            * Concepts
            * Les bases
            * Introduction aux arguments positionnels
            * Introduction aux arguments optionnels
              * Les paramètres raccourcis
            * Combinaison d'arguments positionnels et optionnels
            * Aller un peu plus loin
              * Specifying ambiguous arguments
              * Paramètres en conflit
            * How to translate the argparse output
            * Custom type converters
            * Conclusion
          * Migrating `optparse` code to `argparse`
      * `optparse` --- Parser for command line options
        * Choosing an argument parsing library
        * Introduction
        * Background
          * Terminology
          * What are options for?
          * What are positional arguments for?
        * Tutoriel
          * Understanding option actions
          * The store action
          * Handling boolean (flag) options
          * Other actions
          * Valeurs par défaut
          * Generating help
            * Grouping Options
          * Printing a version string
          * How `optparse` handles errors
          * Putting it all together
        * Reference Guide
          * Creating the parser
          * Populating the parser
          * Defining options
          * Option attributes
          * Standard option actions
          * Standard option types
          * Analyse des arguments
          * Querying and manipulating your option parser
          * Conflicts between options
          * Nettoyage
          * Other methods
        * Option Callbacks
          * Defining a callback option
          * How callbacks are called
          * Raising errors in a callback
          * Callback example 1: trivial callback
          * Callback example 2: check option order
          * Callback example 3: check option order (generalized)
          * Callback example 4: check arbitrary condition
          * Callback example 5: fixed arguments
          * Callback example 6: variable arguments
        * Extending `optparse`
          * Adding new types
          * Adding new actions
        * Exceptions
      * `getpass` --- Portable password input
      * `fileinput` --- Iterate over lines from multiple input streams
      * `curses` --- Terminal handling for character-cell displays
        * Fonctions
        * Window Objects
        * Constantes
      * `curses.textpad` --- Text input widget for curses programs
        * Textbox objects
      * `curses.ascii` --- Utilities for ASCII characters
      * `curses.panel` --- A panel stack extension for curses
        * Fonctions
        * Panel Objects
    * Exécution concourante
      * `threading` --- Thread-based parallelism
        * Données locales au fil d'exécution
        * Objets _Threads_
        * Verrous
        * RLock Objects
        * Condition Objects
        * Semaphore Objects
          * `Semaphore` Example
        * Event Objects
        * Timer Objects
        * Barrier Objects
        * Using locks, conditions, and semaphores in the `with` statement
      * `multiprocessing` --- Process-based parallelism
        * Introduction
          * La classe `Process`
          * Contextes et méthodes de démarrage
          * Échange d'objets entre les processus
          * Synchronisation entre processus
          * Partager un état entre les processus
          * Utiliser un pool de _workers_
        * Référence
          * `Process` et exceptions
          * Tubes (_pipes_) et files (_queues_)
          * Divers
          * Objets de connexions
          * Primitives de synchronisation
          * Objets `ctypes` partagés
            * Le module `multiprocessing.sharedctypes`
          * Gestionnaires
            * Gestionnaires personnalisés
            * Utiliser un gestionnaire distant
          * Objets mandataires
            * Nettoyage
          * Pools de processus
          * Auditeurs et Clients
            * Formats d'adresses
          * Clés d'authentification
          * Journalisation
          * Le module `multiprocessing.dummy`
        * Lignes directrices de programmation
          * Toutes les méthodes de démarrage
          * Les méthodes de démarrage _spawn_ et _forkserver_
        * Exemples
      * `multiprocessing.shared_memory` --- Shared memory for direct access across processes
      * The `concurrent` package
      * `concurrent.futures` --- Launching parallel tasks
        * Executor Objects
        * ThreadPoolExecutor
          * ThreadPoolExecutor Example
        * ProcessPoolExecutor
          * ProcessPoolExecutor Example
        * Future Objects
        * Module Functions
        * Exception classes
      * `subprocess` --- Subprocess management
        * Utiliser le module `subprocess`
          * Arguments fréquemment utilisés
          * Constructeur de _Popen_
          * Exceptions
        * Considérations de sécurité
        * Objets _Popen_
        * Utilitaires _Popen_ pour Windows
          * Constantes Windows
        * Ancienne interface (_API_) haut-niveau
        * Remplacer les fonctions plus anciennes par le module `subprocess`
          * Remplacement de la substitution de commandes de terminal **/bin/sh**
          * Remplacer les _pipes_ du _shell_
          * Remplacer `os.system()`
          * Remplacer les fonctions de la famille `os.spawn`
          * Remplacer `os.popen()`, `os.popen2()`, `os.popen3()`
          * Replacing functions from the `popen2` module
        * Remplacement des fonctions originales d'invocation du _shell_
        * Notes
          * Convertir une séquence d'arguments vers une chaîne de caractères sous Windows
          * Disabling use of `vfork()` or `posix_spawn()`
      * `sched` --- Event scheduler
        * Scheduler Objects
      * `queue` --- A synchronized queue class
        * Objets `Queue`
          * Terminating queues
        * Objets `SimpleQueue`
      * `contextvars` --- Context Variables
        * Variables de contexte
        * Gestion de contexte manuelle
        * Gestion avec _asyncio_
      * `_thread` --- Low-level threading API
    * Réseau et communication entre processus
      * `asyncio` --- Asynchronous I/O
        * Exécuteurs (_runners_)
          * Exécution d'un programme asynchrone
          * Gestionnaire de contexte de l'exécuteur
          * Gestion de l'interruption par le clavier
        * Coroutines et tâches
          * Coroutines
          * _Attendables_
          * Création de tâches
          * Annulation de tâche
          * Groupes de tâches
            * Terminating a Task Group
          * Attente
          * Exécution de tâches de manière concurrente
          * Eager Task Factory
          * Protection contre l'annulation
          * Délais d'attente
          * Primitives d'attente
          * Exécution dans des fils d'exécution (_threads_)
          * Planification depuis d'autres fils d'exécution
          * Introspection
          * Objets _Task_
        * Flux (_streams_)
          * Flux lecteurs (_StreamReader_)
          * Flux écrivains (_StreamWriter_)
          * Exemples
            * Client d'écho TCP utilisant des flux
            * Serveur d'écho TCP utilisant des flux
            * Récupération des en-têtes HTTP
            * Ouverture d'un connecteur pour attendre les données à l'aide de flux
        * Primitives de synchronisation
          * Verrou (_lock_)
          * Événement (_Event_)
          * Condition
          * Sémaphore
          * Sémaphore capé (_BoundedSemaphore_)
          * Barrière (_Barrier_)
        * Sous-processus
          * Créer des sous-processus
          * Constantes
          * Interagir avec les sous-processus
            * Sous-processus et fils d'exécution
            * Exemples
        * Files d'attente (_queues_)
          * File d'attente (_queue_)
          * File avec priorité
          * Pile (LIFO)
          * Exceptions
          * Exemples
        * Exceptions
        * Boucle d'évènements
          * Méthodes de la boucle d'évènements
            * Démarrer et arrêter une boucle d'évènements
            * Planification des fonctions de rappel
            * Planification des rappels différés
            * Création de _Futures_ et des tâches
            * Création de connexions
            * Création de serveurs
            * Transfert de fichiers
            * Passage du flux en TLS
            * Surveillance de descripteur de fichier
            * Travail direct avec des objets _socket_
            * DNS
            * Travail avec des tubes (_pipes_)
            * Signaux Unix
            * Exécution de code dans des pools de threads ou de processus
            * API de gestion d'erreur
            * Activation du mode débogage
            * Exécution de sous-processus
          * Fonctions de rappel sur des descripteurs
          * Objets Serveur
          * Implémentations de boucle d'évènements
          * Exemples
            * "Hello World" avec `call_soon()`
            * Affichage de la date actuelle avec `call_later()`
            * Surveillance des événements de lecture pour un descripteur de fichier
            * Gestion des signaux _SIGINT_ et _SIGTERM_
        * Futures
          * Fonctions pour _Future_
          * Objet _Future_
        * Transports et Protocoles
          * Transports
            * Hiérarchie des transports
            * Classe de base des Transports
            * Transports en lecture seule
            * Transports en lecture-écriture
            * Transports par datagrammes
            * Transports entre sous-processus
          * Protocoles
            * Protocoles de base
            * Protocoles de base
            * Protocoles connectés
            * Protocoles connectés avec tampon
            * Protocoles par datagrammes (non connectés)
            * Protocoles liés aux sous-processus
          * Exemples
            * Serveur _écho_ en TCP
            * Client _écho_ en TCP
            * Serveur _écho_ en UDP
            * Client _écho_ en UDP
            * Connexion de connecteurs existants
            * _loop.subprocess_exec()_ et _SubprocessProtocol_
        * Politiques
          * Obtenir et définir la politique
          * Objets politiques
          * Observateurs de processus
          * Politiques personnalisées
        * Prise en charge de la plate-forme
          * Toutes plateformes
          * Windows
            * Prise en charge des sous-processus sous Windows
          * macOS
        * Extension
          * Écriture d'une boucle d'événements personnalisée
          * Constructeurs privés _Future_ et _Task_
          * Prise en charge de la durée de vie des tâches
        * Index de l'API de haut niveau
          * Tâches
          * Files d'attente
          * Sous-processus
          * Flux (_streams_)
          * Synchronisation
          * Exceptions
        * Index de l'API de bas niveau
          * Obtenir une boucle d'évènements
          * Méthodes de la boucle d'évènements
          * Transports
          * Protocoles
          * Politiques de boucle d'événements
        * Programmer avec _asyncio_
          * Mode débogage
          * Programmation concurrente et multi-fils
          * Exécution de code bloquant
          * Journalisation
          * Détection des coroutines jamais attendues
          * Détection des exceptions jamais récupérées
      * `socket` --- Low-level networking interface
        * Socket families
        * Module contents
          * Exceptions
          * Constantes
          * Fonctions
            * Creating sockets
            * Autres fonctions
        * Socket Objects
        * Notes on socket timeouts
          * Timeouts and the `connect` method
          * Timeouts and the `accept` method
        * Exemple
      * `ssl` --- TLS/SSL wrapper for socket objects
        * Fonctions, constantes et exceptions
          * Création de connecteurs
          * Création de contexte
          * Exceptions
          * Random generation
          * Certificate handling
          * Constantes
        * SSL Sockets
        * SSL Contexts
        * Certificates
          * Certificate chains
          * CA certificates
          * Combined key and certificate
          * Self-signed certificates
        * Exemples
          * Testing for SSL support
          * Client-side operation
          * Server-side operation
        * Notes on non-blocking sockets
        * Memory BIO Support
        * SSL session
        * Security considerations
          * Best defaults
          * Manual settings
            * Verifying certificates
            * Protocol versions
            * Cipher selection
          * Multi-processing
        * TLS 1.3
      * `select` --- Waiting for I/O completion
        * `/dev/poll` Polling Objects
        * Edge and Level Trigger Polling (epoll) Objects
        * Polling Objects
        * Kqueue Objects
        * Kevent Objects
      * `selectors` --- High-level I/O multiplexing
        * Introduction
        * Classes
        * Exemples
      * `signal` --- Set handlers for asynchronous events
        * General rules
          * Execution of Python signal handlers
          * Signals and threads
        * Module contents
        * Examples
        * Note on SIGPIPE
        * Note on Signal Handlers and Exceptions
      * `mmap` --- Memory-mapped file support
        * MADV_* Constants
        * MAP_* Constants
    * Traitement des données provenant d'Internet
      * `email` --- An email and MIME handling package
        * `email.message`: Representing an email message
        * `email.parser`: Parsing email messages
          * API _FeedParser_
          * API de _Parser_
          * Notes complémentaires
        * `email.generator`: Generating MIME documents
        * `email.policy`: Policy Objects
        * `email.errors`: Exception and Defect classes
        * `email.headerregistry`: Custom Header Objects
        * `email.contentmanager`: Managing MIME Content
          * Instances de gestionnaires de contenus
        * `email`: Exemples
        * `email.message.Message` : représentation d'un message électronique à l'aide de l'API `compat32`
        * `email.mime`: Creating email and MIME objects from scratch
        * `email.header`: Internationalized headers
        * `email.charset`: Representing character sets
        * `email.encoders`: Encoders
        * `email.utils`: Miscellaneous utilities
        * `email.iterators`: Iterators
      * `json` --- JSON encoder and decoder
        * Utilisation de base
        * Encodeurs et décodeurs
        * Exceptions
        * Conformité au standard et Interopérabilité
          * Encodage des caractères
          * Valeurs numériques infinies et NaN
          * Noms répétés au sein d'un objet
          * Valeurs de plus haut niveau (hors objets ou tableaux)
          * Limitations de l'implémentation
        * Interface en ligne de commande
          * Options de la ligne de commande
      * `mailbox` --- Manipulate mailboxes in various formats
        * `Mailbox` objects
          * `Maildir` objects
          * `mbox` objects
          * `MH` objects
          * `Babyl` objects
          * `MMDF` objects
        * `Message` objects
          * `MaildirMessage` objects
          * `mboxMessage` objects
          * `MHMessage` objects
          * `BabylMessage` objects
          * `MMDFMessage` objects
        * Exceptions
        * Exemples
      * `mimetypes` --- Map filenames to MIME types
        * MimeTypes Objects
      * `base64` --- Base16, Base32, Base64, Base85 Data Encodings
        * Considérations de sécurité
      * `binascii` --- Convert between binary and ASCII
      * `quopri` --- Encode and decode MIME quoted-printable data
    * Outils de traitement de balises structurées
      * `html` --- HyperText Markup Language support
      * `html.parser` --- Simple HTML and XHTML parser
        * Exemple d'application de l'analyseur HTML
        * Méthodes de la classe `HTMLParser`
        * Exemples
      * `html.entities` --- Definitions of HTML general entities
      * Modules de traitement XML
        * Vulnérabilités XML
        * The `defusedxml` Package
      * `xml.etree.ElementTree` --- The ElementTree XML API
        * Tutoriel
          * Arborescence et éléments XML
          * Analyse XML
          * API à flux tiré
          * Atteinte d'éléments d'intérêt
          * Modification d'un fichier XML
          * Création de documents XML
          * Analyse d'un XML avec des espaces de noms
        * Prise en charge de _XPath_
          * Exemple
          * Prise en charge de la syntaxe _XPath_
        * Référence
          * Fonctions
        * Prise en charge de _XInclude_
          * Exemple
        * Référence
          * Fonctions
          * Objets _Element_
          * Objets _ElementTree_
          * Objets _QName_
          * Objets _TreeBuilder_
          * Objets _XMLParser_
          * Objets _XMLPullParser_
          * Exceptions
      * `xml.dom` --- The Document Object Model API
        * Contenu du module
        * Objets dans le DOM
          * Objets DOMImplementation
          * Objets nœuds
          * Objet NodeList
          * Objets DocumnentType
          * Objets Document
          * Objets Elements
          * Objets Attr
          * Objets NameNodeMap
          * Objets Comment
          * Objets Text et CDATASection
          * Objets ProcessingInstruction
          * Exceptions
        * Conformité
          * Correspondance des types
          * Méthodes d'accès
      * `xml.dom.minidom` --- Minimal DOM implementation
        * Objets DOM
        * Exemple DOM
        * _minidom_ et le standard DOM
      * `xml.dom.pulldom` --- Support for building partial DOM trees
        * Objets _DOMEventStream_
      * `xml.sax` --- Support for SAX2 parsers
        * Les objets _SAXException_
      * `xml.sax.handler` --- Base classes for SAX handlers
        * Objets _ContentHandler_
        * Objets _DTDHandler_
        * Objets _EntityResolver_
        * Objets _ErrorHandler_
        * Objets _LexicalHandler_
      * `xml.sax.saxutils` --- SAX Utilities
      * `xml.sax.xmlreader` --- Interface for XML parsers
        * XMLReader Objects
        * IncrementalParser Objects
        * Locator Objects
        * InputSource Objects
        * The `Attributes` Interface
        * The `AttributesNS` Interface
      * `xml.parsers.expat` --- Fast XML parsing using Expat
        * Objets _XMLParser_
        * ExpatError Exceptions
        * Exemple
        * Content Model Descriptions
        * Expat error constants
    * Gestion des protocoles internet
      * `webbrowser` --- Convenient web-browser controller
        * Browser Controller Objects
      * `wsgiref` --- WSGI Utilities and Reference Implementation
        * `wsgiref.util` — outils pour les environnements WSGI
        * `wsgiref.headers` -- WSGI response header tools
        * `wsgiref.simple_server` -- a simple WSGI HTTP server
        * `wsgiref.validate` --- WSGI conformance checker
        * `wsgiref.handlers` -- server/gateway base classes
        * `wsgiref.types` -- WSGI types for static type checking
        * Exemples
      * `urllib` --- URL handling modules
      * `urllib.request` --- Extensible library for opening URLs
        * Request Objects
        * OpenerDirector Objects
        * BaseHandler Objects
        * HTTPRedirectHandler Objects
        * HTTPCookieProcessor Objects
        * ProxyHandler Objects
        * HTTPPasswordMgr Objects
        * HTTPPasswordMgrWithPriorAuth Objects
        * AbstractBasicAuthHandler Objects
        * HTTPBasicAuthHandler Objects
        * ProxyBasicAuthHandler Objects
        * AbstractDigestAuthHandler Objects
        * HTTPDigestAuthHandler Objects
        * ProxyDigestAuthHandler Objects
        * HTTPHandler Objects
        * HTTPSHandler Objects
        * FileHandler Objects
        * DataHandler Objects
        * FTPHandler Objects
        * CacheFTPHandler Objects
        * UnknownHandler Objects
        * HTTPErrorProcessor Objects
        * Exemples
        * Legacy interface
        * `urllib.request` Restrictions
      * `urllib.response` --- Response classes used by urllib
      * `urllib.parse` --- Parse URLs into components
        * URL Parsing
        * URL parsing security
        * Parsing ASCII Encoded Bytes
        * Structured Parse Results
        * URL Quoting
      * `urllib.error` --- Exception classes raised by urllib.request
      * `urllib.robotparser` --- Parser for robots.txt
      * `http` --- HTTP modules
        * Codes d'état HTTP
        * HTTP status category
        * HTTP methods
      * `http.client` --- HTTP protocol client
        * Les objets HTTPConnection
        * Les objets HTTPResponse
        * Exemples
        * Les objets HTTPMessage
      * `ftplib` --- FTP protocol client
        * Référence
          * FTP objects
          * FTP_TLS objects
          * Module variables
      * `poplib` --- POP3 protocol client
        * POP3 Objects
        * POP3 Example
      * `imaplib` --- IMAP4 protocol client
        * IMAP4 Objects
        * IMAP4 Example
      * `smtplib` --- SMTP protocol client
        * SMTP Objects
        * SMTP Example
      * `uuid` --- UUID objects according to **RFC 4122**
        * Utilisation en ligne de commande.
        * Exemple
        * Command-Line Example
      * `socketserver` --- A framework for network servers
        * Notes sur la création de serveurs
        * Objets serveur
        * Objets gestionnaire de requêtes
        * Exemples
          * Exemple pour `socketserver.TCPServer`
          * Exemple pour `socketserver.UDPServer`
          * Classes de mélange asynchrone
      * `http.server` --- HTTP servers
        * Considérations de sécurité
      * `http.cookies` --- HTTP state management
        * Objets _Cookie_
        * Objets _Morsel_
        * Exemple
      * `http.cookiejar` --- Cookie handling for HTTP clients
        * CookieJar and FileCookieJar Objects
        * FileCookieJar subclasses and co-operation with web browsers
        * CookiePolicy Objects
        * DefaultCookiePolicy Objects
        * Objets _Cookie_
        * Exemples
      * `xmlrpc` --- XMLRPC server and client modules
      * `xmlrpc.client` --- XML-RPC client access
        * ServerProxy Objects
        * Objets DateTime
        * Binary Objects
        * Fault Objects
        * ProtocolError Objects
        * MultiCall Objects
        * Convenience Functions
        * Example of Client Usage
        * Example of Client and Server Usage
      * `xmlrpc.server` --- Basic XML-RPC servers
        * SimpleXMLRPCServer Objects
          * SimpleXMLRPCServer Example
        * CGIXMLRPCRequestHandler
        * Documenting XMLRPC server
        * DocXMLRPCServer Objects
        * DocCGIXMLRPCRequestHandler
      * `ipaddress` --- IPv4/IPv6 manipulation library
        * Fonctions fabriques pratiques
        * Adresses IP
          * Objets adresse
          * Conversion vers les chaînes et les entiers
          * Opérateurs
            * Opérateurs de comparaison
            * Opérateurs arithmétiques
        * Définitions de réseaux IP
          * Préfixe, masque réseau et masque de l'hôte
          * Objets réseau
          * Opérateurs
            * Opérateurs logiques
            * Itération
            * Réseaux en tant que conteneurs d'adresses
        * Objets interface
          * Opérateurs
            * Opérateurs logiques
        * Autres fonctions au niveau de module
        * Exceptions personnalisées
    * Services multimédia
      * `wave` --- Read and write WAV files
        * Objets Wave_read
        * Objets Wave_write
      * `colorsys` --- Conversions between color systems
    * Internationalisation
      * `gettext` --- Multilingual internationalization services
        * API GNU **gettext**
        * API basée sur les classes
          * La classe `NullTranslations`
          * La classe `GNUTranslations`
          * Support du catalogue de message de Solaris
          * Le constructeur _Catalog_
        * Internationaliser vos programmes et modules
          * Localiser votre module
          * Localiser votre application
          * Changer de langue à la volée
          * Traductions différées
        * Remerciements
      * `locale` --- Internationalization services
        * Contexte, détails, conseils, astuces et mises en garde
        * Pour les auteurs d'extensions et les programmes qui intègrent Python
        * Accéder aux catalogues de messages
    * Cadriciels d'applications
      * `turtle` — Tortue graphique
        * Introduction
        * Get started
        * Tutoriel
          * Starting a turtle environment
          * Basic drawing
            * Réglage des stylos
            * The turtle's position
          * Making algorithmic patterns
        * How to...
          * Get started as quickly as possible
          * Use the `turtle` module namespace
          * Use turtle graphics in a script
          * Use object-oriented turtle graphics
        * Turtle graphics reference
          * Les méthodes du module _Turtle_
          * Méthodes de _TurtleScreen_ /_Screen_
        * Méthodes de _RawTurtle_ /_Turtle_ et leurs fonctions correspondantes
          * Les mouvements dans le module _Turtle_
          * Connaître l'état de la tortue
          * Paramètres de mesure
          * Réglage des stylos
            * État des stylos
            * Réglage des couleurs
            * Remplissage
            * Plus des réglages pour le dessin
          * État de la tortue
            * Visibilité
            * Apparence
          * Utilisation des événements
          * Méthodes spéciales de la tortue
          * Formes composées
        * Méthodes de TurtleScreen/Screen et leurs fonctions correspondantes
          * Réglage de la fenêtre
          * Réglage de l'animation
          * Utilisation des événements concernant l'écran
          * Méthodes de saisie
          * Paramétrages et méthodes spéciales
          * Méthodes spécifiques à Screen, non héritées de TurtleScreen
        * Classes publiques
        * Explication
        * Aide et configuration
          * Utilisation de l'aide
          * Traduction de chaînes de documents en différentes langues
          * Comment configurer _Screen_ et _Turtle_
        * `turtledemo` — Scripts de démonstration
        * Modifications depuis Python 2.6
        * Modifications depuis Python 3.0
      * `cmd` --- Support for line-oriented command interpreters
        * Objets Cmd
        * Exemple
      * `shlex` --- Simple lexical analysis
        * shlex Objects
        * Parsing Rules
        * Improved Compatibility with Shells
    * Interfaces Utilisateur Graphiques avec Tk
      * `tkinter` --- Python interface to Tcl/Tk
        * Architecture
        * Modules _Tkinter_
        * Guide de survie _Tkinter_
          * Un simple programme _Hello World_
          * Concepts importants de _Tk_
          * Comprendre comment _Tkinter_ enveloppe _Tcl/Tk_
          * Comment puis-je… ? Quelle option… ?
          * Navigation dans le manuel de référence _Tcl/Tk_
        * Fils d'exécution multiples
        * Guide pratique
          * Définition des options
          * L'empaqueteur
          * Options de l'empaqueteur
          * Association des variables de l'objet graphique
          * Le gestionnaire de fenêtres
          * Types de données des options _Tk_
          * Liaisons et événements
          * Le paramètre index
          * Images
        * Gestionnaires de fichiers
      * `tkinter.colorchooser` --- Color choosing dialog
      * `tkinter.font` --- Tkinter font wrapper
      * Boîtes de dialogue _Tkinter_
        * `tkinter.simpledialog` – Boîtes de dialogue de saisie standard de _Tkinter_
        * `tkinter.filedialog` – Boîtes de dialogue de sélection de fichiers
          * Boîtes de dialogue de chargement et sauvegarde natives
        * `tkinter.commondialog` – Modèles de fenêtre de dialogue
      * `tkinter.messagebox` --- Tkinter message prompts
      * `tkinter.scrolledtext` --- Scrolled Text Widget
      * `tkinter.dnd` --- Drag and drop support
      * `tkinter.ttk` --- Tk themed widgets
        * Utilisation de _Ttk_
        * Widgets _Ttk_
        * Widget
          * Options standards
          * Options de widget avec barre de défilement
          * Options d'étiquette (_label_)
          * Options de compatibilité
          * États des widgets
          * ttk.Widget
        * Combobox
          * Options
          * Événements virtuels
          * ttk.Combobox
        * Spinbox
          * Options
          * Événements virtuels
          * ttk.Spinbox
        * Carnet de notes (_notebook_)
          * Options
          * Options d'onglet
          * Identifiants d'onglet
          * Événements virtuels
          * ttk.Notebook
        * Barre de progression
          * Options
          * ttk.Progressbar
        * Séparateur
          * Options
        * Poignée de redimensionnement
          * Notes spécifiques à une plateforme
          * Bogues
        * Arborescence
          * Options
          * Options d'éléments
          * Options de balise
          * Identifiants de colonnes
          * Événements virtuels
          * ttk.Treeview
        * Style Ttk
          * Dispositions de mise en page
      * IDLE --- Python editor and shell
        * Menus
          * Menu _File_ (Console et Éditeur)
          * Menu _Edit_ (console et éditeur)
          * Menu _Format_ (fenêtre d'édition uniquement)
          * Menu _Run_ (fenêtre d'édition uniquement)
          * Menu Shell (fenêtre de console uniquement)
          * Menu _Debug_ (fenêtre de console uniquement)
          * Menu _Options_ (console et éditeur)
          * Menu _Windows_ (console et éditeur)
          * Menu _Help_ (console et éditeur)
          * Context menus
        * Editing and Navigation
          * Fenêtre d'édition
          * Raccourcis clavier
          * Indentation automatique
          * Recherche et substitution
          * Complétions
          * Info-bulles
          * Contexte du code
          * Shell window
          * Coloration du texte
        * Startup and Code Execution
          * Utilisation de la ligne de commande
          * Échec au démarrage
          * Exécuter le code de l'utilisateur
          * Sortie de l'utilisateur sur la console
          * Développer des applications _tkinter_
          * Exécution sans sous-processus
        * Help and Preferences
          * Sources d'aide
          * Modifier les préférences
          * _IDLE_ sous _macOS_
          * Extensions
        * idlelib --- implementation of IDLE application
    * Outils de développement
      * `typing` — Prise en charge des annotations de type
        * Specification for the Python Type System
        * Alias de type
        * _NewType_
        * Annotating callable objects
        * Génériques
        * Annotating tuples
        * The type of class objects
        * Annotating generators and coroutines
        * Types génériques définis par l'utilisateur
        * Le type `Any`
        * Sous-typage nominal et sous-typage structurel
        * Classe de données
          * Special typing primitives
            * Special types
            * Special forms
            * Building generic types and type aliases
            * Other special directives
          * Protocoles
          * ABCs for working with IO
          * Functions and decorators
          * Utilitaires d'introspection
          * Constante
          * Deprecated aliases
            * Aliases to built-in types
            * Aliases to types in `collections`
            * Aliases to other concrete types
            * Aliases to container ABCs in `collections.abc`
            * Aliases to asynchronous ABCs in `collections.abc`
            * Aliases to other ABCs in `collections.abc`
            * Aliases to `contextlib` ABCs
        * Étapes d'Obsolescence des Fonctionnalités Majeures
      * `pydoc` --- Documentation generator and online help system
      * Python Development Mode
        * Effects of the Python Development Mode
        * ResourceWarning Example
        * Bad file descriptor error example
      * `doctest` — Exemples de tests interactifs en Python
        * Utilisation simple : vérifier des exemples dans des _docstrings_
        * Utilisation simple : vérifier des exemples dans un fichier texte
        * Comment ça marche
          * Quelles _docstrings_ sont considérées ?
          * Comment les exemples _docstring_ sont-ils identifiés ?
          * Quel est le contexte d'exécution ?
          * Qu'en est-il des exceptions ?
          * Options de ligne de commande
          * Instructions
          * Avertissements
        * API de base
        * API de tests unitaires
        * API avancé
          * Objets _doctest_
          * Exemples d'objets
          * Objets _DocTestFinder_
          * Objets _DocTestParser_
          * Objets _TestResults_
          * Objets _DocTestRunner_
          * Objets _OutputChecker_
        * Débogage
        * Éditorial
      * `unittest` --- Unit testing framework
        * Exemple basique
        * Interface en ligne de commande
          * Options de la ligne de commande
        * Découverte des tests
        * Organiser le code de test
        * Réutilisation d'ancien code de test
        * Ignorer des tests et des erreurs prévisibles
        * Distinguer les itérations de test à l'aide de sous-tests
        * Classes et fonctions
          * Scénarios de tests
          * Regroupement des tests
          * Chargement et exécution des tests
            * Protocole de chargement des tests (_load_tests Protocol_)
        * Classes et modules d'aménagements des tests
          * Classes de mise en place (_setUpClass_) et de démantèlement des tests (_tearDownClass_)
          * Module de mise en place (_setUpModule_) et de démantèlement des tests (_tearDownModule_)
        * Traitement des signaux
      * `unittest.mock` --- mock object library
        * Guide rapide
        * La classe _Mock_
          * Calling
          * Deleting Attributes
          * Mock names and the name attribute
          * Attaching Mocks as Attributes
        * The patchers
          * patch
          * patch.object
          * patch.dict
          * patch.multiple
          * patch methods: start and stop
          * patch builtins
          * TEST_PREFIX
          * Nesting Patch Decorators
          * Where to patch
          * Patching Descriptors and Proxy Objects
        * MagicMock and magic method support
          * Mocking Magic Methods
          * Magic Mock
        * Helpers
          * sentinel
          * DEFAULT
          * appel
          * create_autospec
          * ANY
          * FILTER_DIR
          * mock_open
          * Autospeccing
          * Sealing mocks
        * Order of precedence of `side_effect`, `return_value` and _wraps_
      * `unittest.mock` --- getting started
        * Utilisation de Mock ou l'art de singer
          * Simulation des méthodes
          * S'assurer de la bonne utilisation d'un objet
          * Simulation des classes
          * Naming your mocks
          * Tracking all Calls
          * Setting Return Values and Attributes
          * Raising exceptions with mocks
          * Side effect functions and iterables
          * Mocking asynchronous iterators
          * Mocking asynchronous context manager
          * Creating a Mock from an Existing Object
          * Using side_effect to return per file content
        * Patch Decorators
        * Further Examples
          * Mocking chained calls
          * Partial mocking
          * Mocking a Generator Method
          * Applying the same patch to every test method
          * Mocking Unbound Methods
          * Checking multiple calls with mock
          * Coping with mutable arguments
          * Nesting Patches
          * Mocking a dictionary with MagicMock
          * Mock subclasses and their attributes
          * Mocking imports with patch.dict
          * Tracking order of calls and less verbose call assertions
          * More complex argument matching
      * `test` --- Regression tests package for Python
        * Writing Unit Tests for the `test` package
        * Running tests using the command-line interface
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
        * Dumping the traceback
        * Fault handler state
        * Dumping the tracebacks after a timeout
        * Dumping the traceback on a user signal
        * Issue with file descriptors
        * Exemple
      * `pdb` — Le débogueur Python
        * Commande du débogueur
      * The Python Profilers
        * Introduction to the profilers
        * Instant User's Manual
        * `profile` and `cProfile` Module Reference
        * The `Stats` Class
        * What Is Deterministic Profiling?
        * Limitations
        * Calibration
        * Using a custom timer
      * `timeit` --- Measure execution time of small code snippets
        * Exemples simples
        * Interface Python
        * Interface en ligne de commande
        * Exemples
      * `trace` --- Trace or track Python statement execution
        * Utilisation en ligne de commande.
          * Main options
          * Modifiers
          * Filters
        * Programmatic Interface
      * `tracemalloc` --- Trace memory allocations
        * Exemples
          * Display the top 10
          * Compute differences
          * Get the traceback of a memory block
          * Pretty top
            * Record the current and peak size of all traced memory blocks
        * API
          * Fonctions
          * DomainFilter
          * Filter
          * Frame
          * Snapshot
          * Statistic
          * StatisticDiff
          * Trace
          * Traceback
    * Paquets et distribution de paquets logiciels
      * `ensurepip` --- Bootstrapping the `pip` installer
        * Interface en ligne de commande
        * API du module
      * `venv` --- Creation of virtual environments
        * Création d'environnements virtuels
        * How venvs work
        * API
        * Un exemple d'extension de `EnvBuilder`
      * `zipapp` --- Manage executable Python zip archives
        * Exemple de base
        * Interface en ligne de commande
        * API Python
        * Exemples
        * Spécification de l'interprète
        * Création d'applications autonomes avec _zipapp_
          * Mises en garde
        * Le format d'archive d'application Zip Python
    * Environnement d'exécution Python
      * `sys` --- System-specific parameters and functions
      * `sys.monitoring` --- Execution event monitoring
        * Tool identifiers
          * Registering and using tools
        * Events
          * Local events
          * Ancillary events
          * Other events
          * The STOP_ITERATION event
        * Turning events on and off
          * Setting events globally
          * Per code object events
          * Disabling events
        * Registering callback functions
          * Callback function arguments
      * `sysconfig` --- Provide access to Python's configuration information
        * Configuration variables
        * Installation paths
        * User scheme
          * `posix_user`
          * `nt_user`
          * `osx_framework_user`
        * Home scheme
          * `posix_home`
        * Prefix scheme
          * `posix_prefix`
          * `nt`
        * Installation path functions
        * Autres fonctions
        * Using `sysconfig` as a script
      * `builtins` --- Built-in objects
      * `__main__` --- Top-level code environment
        * `__name__ == '__main__'`
          * Qu'est-ce que l'« environnement d'exécution principal » ?
          * Utilisation idiomatique
          * Considérations liées à l'empaquetage
        * Le fichier `__main__.py` dans les paquets Python
          * Utilisation idiomatique
        * `import __main__`
      * `warnings` --- Warning control
        * Catégories d'avertissement
        * Le filtre des avertissements
          * Repeated Warning Suppression Criteria
          * Rédaction de filtres d'avertissement
          * Filtre d'avertissement par défaut
          * Outrepasser le filtre par défaut
        * Suppression temporaire des avertissements
        * Tester les avertissements
        * Mise à jour du code pour les nouvelles versions des dépendances
        * Fonctions disponibles
        * Gestionnaires de contexte disponibles
      * `dataclasses` --- Data Classes
        * Classe de données
        * Post-initialisation
        * Variables de classe
        * Variables d'initialisation
        * Instances figées
        * Héritage
        * Re-ordering of keyword-only parameters in `__init__()`
        * Fabriques de valeurs par défaut
        * Valeurs par défaut mutables
        * Descriptor-typed fields
      * `contextlib` — Utilitaires pour les contextes s'appuyant sur l'instruction `with`
        * Utilitaires
        * Exemples et Recettes
          * Gérer un nombre variable de gestionnaires de contexte
          * Attraper des exceptions depuis les méthodes `__enter__`
          * Nettoyer dans une méthode `__enter__`
          * Remplacer un `try-finally` avec une option variable
          * Utiliser un gestionnaire de contexte en tant que décorateur de fonction
        * Gestionnaires de contexte à usage unique, réutilisables et réentrants
          * Gestionnaires de contexte réentrants
          * Gestionnaires de contexte réutilisables
      * `abc` --- Abstract Base Classes
      * `atexit` --- Exit handlers
        * Exemple avec `atexit`
      * `traceback` --- Print or retrieve a stack traceback
        * Fonctions de niveau module
        * `TracebackException` Objects
        * `StackSummary` Objects
        * `FrameSummary` Objects
        * Examples of Using the Module-Level Functions
        * Examples of Using `TracebackException`
      * `__future__` --- Future statement definitions
        * Contenu du module
      * `gc` --- Garbage Collector interface
      * `inspect` --- Inspect live objects
        * Types et membres
        * Récupération du code source
        * Introspection des appelables avec l'objet Signature
        * Classes et fonctions
        * La pile d'interpréteur
        * Recherche dynamique d'attributs
        * Current State of Generators, Coroutines, and Asynchronous Generators
        * Bit d'option des objets code
        * Buffer flags
        * Interface en ligne de commande
      * `site` --- Site-specific configuration hook
        * `sitecustomize`
        * `usercustomize`
        * Readline configuration
        * Module contents
        * Interface en ligne de commande
    * Interpréteurs Python personnalisés
      * `code` --- Interpreter base classes
        * Interactive Interpreter Objects
        * Interactive Console Objects
      * `codeop` --- Compile Python code
    * Importer des modules
      * `zipimport` --- Import modules from Zip archives
        * Objets _zimporter_
        * Exemples
      * `pkgutil` --- Package extension utility
      * `modulefinder` --- Find modules used by a script
        * Exemples d'utilisation de la classe `ModuleFinder`
      * `runpy` --- Locating and executing Python modules
      * `importlib` --- The implementation of `import`
        * Introduction
        * Fonctions
        * `importlib.abc` -- Abstract base classes related to import
        * `importlib.machinery` -- Importers and path hooks
        * `importlib.util` -- Utility code for importers
        * Exemples
          * Importing programmatically
          * Checking if a module can be imported
          * Importing a source file directly
          * Implementing lazy imports
          * Setting up an importer
          * Approximating `importlib.import_module()`
      * `importlib.resources` -- Package resource reading, opening and access
        * API par fonction
      * `importlib.resources.abc` -- Abstract base classes for resources
      * `importlib.metadata` -- Accessing package metadata
        * Aperçu
        * API par fonction
          * Entry points
          * Distribution metadata
          * Distribution versions
          * Distribution files
          * Distribution requirements
          * Mapping import to distribution packages
        * Distributions
        * Distribution Discovery
        * Extending the search algorithm
          * Exemple
      * The initialization of the `sys.path` module search path
        * Environnements virtuels
        * _pth files
        * Embedded Python
    * Services du Langage Python
      * `ast` --- Abstract Syntax Trees
        * Grammaire abstraite
        * Classes de nœuds
          * Root nodes
          * Littéraux
          * Variables
          * Expressions
            * Indiçage
            * Compréhensions
          * Instructions
            * Importations
          * Contrôle de l'exécution
          * Pattern matching
          * Type parameters
          * Définition de fonctions et de classes
          * `async` et `await`
        * Outils du module `ast`
        * Options du compilateur
        * Utilisation en ligne de commande
      * `symtable` --- Access to the compiler's symbol tables
        * Generating Symbol Tables
        * Examining Symbol Tables
        * Utilisation en ligne de commande.
      * `token` --- Constants used with Python parse trees
      * `keyword` --- Testing for Python keywords
      * `tokenize` --- Tokenizer for Python source
        * Analyse Lexicale
        * Utilisation en ligne de commande.
        * Exemples
      * `tabnanny` --- Detection of ambiguous indentation
      * `pyclbr` --- Python module browser support
        * Objets fonctions
        * Objets classes
      * `py_compile` --- Compile Python source files
        * Interface en ligne de commande
      * `compileall` --- Byte-compile Python libraries
        * Utilisation en ligne de commande
        * Fonctions publiques
      * `dis` --- Disassembler for Python bytecode
        * Command-line interface
        * Analyse du code intermédiaire
        * Analyse de fonctions
        * Les instructions du code intermédiaire en Python
        * Opcode collections
      * `pickletools` --- Tools for pickle developers
        * Utilisation de la ligne de commande
          * Options de la ligne de commande
        * Programmatic Interface
    * Services spécifiques à MS Windows
      * `msvcrt` --- Useful routines from the MS VC++ runtime
        * Opérations sur les fichiers
        * Entrées-sorties sur un terminal
        * Autres fonctions
      * `winreg` --- Windows registry access
        * Fonctions
        * Constantes
          * HKEY_* Constants
          * Access Rights
            * 64-bit Specific
          * Value Types
        * Registry Handle Objects
      * `winsound` --- Sound-playing interface for Windows
    * Services spécifiques à Unix
      * `posix` --- The most common POSIX system calls
        * Prise en charge de gros fichiers
        * Contenu du Module
      * `pwd` --- The password database
      * `grp` --- The group database
      * `termios` --- POSIX style tty control
        * Exemple
      * `tty` --- Terminal control functions
      * `pty` --- Pseudo-terminal utilities
        * Exemple
      * `fcntl` --- The `fcntl` and `ioctl` system calls
      * `resource` --- Resource usage information
        * Resource Limits
        * Resource Usage
      * `syslog` --- Unix syslog library routines
        * Exemples
          * Exemple simple
    * Modules command-line interface (CLI)
    * Modules remplacés
      * `getopt` --- C-style parser for command line options
    * Removed Modules
    * Considérations de sécurité
  * Extension et intégration de l'interpréteur Python
    * Les outils tiers recommandés
    * Création d'extensions sans outils tiers
      * 1. Étendre Python en C ou C++
        * 1.1. Un exemple simple
        * 1.2. Intermezzo : les erreurs et les exceptions
        * 1.3. Retour vers l'exemple
        * 1.4. La fonction d'initialisation et le tableau des méthodes du module
        * 1.5. Compilation et liaison
        * 1.6. Appeler des fonctions Python en C
        * 1.7. Extraire des paramètres dans des fonctions d'extension
        * 1.8. Paramètres nommés pour des fonctions d'extension
        * 1.9. Créer des valeurs arbitraires
        * 1.10. Compteurs de références
          * 1.10.1. Comptage de références en Python
          * 1.10.2. Règles concernant la possession de références
          * 1.10.3. Terrain dangereux
          * 1.10.4. Pointeurs `NULL`
        * 1.11. Écrire des extensions en C++
        * 1.12. Fournir une API en langage C pour un module d'extension
      * 2. Tutoriel : définir des types dans des extensions
        * 2.1. Les bases
        * 2.2. ajout de données et de méthodes à l'exemple basique
        * 2.3. Contrôle précis sur les attributs de données
        * 2.4. Prise en charge du ramasse-miettes cyclique
        * 2.5. Sous-classement d'autres types
      * 3. Définir les types d'extension : divers sujets
        * 3.1. Finalisation et libération de mémoire
        * 3.2. Présentation de l'objet
        * 3.3. Gestion des attributs
          * 3.3.1. Gestion des attributs génériques
          * 3.3.2. Gestion des attributs de type spécifiques
        * 3.4. Comparaison des objets
        * 3.5. Gestion de protocoles abstraits
        * 3.6. Prise en charge de la référence faible
        * 3.7. Plus de suggestions
      * 4. Construire des extensions C et C++
        * 4.1. Building C and C++ Extensions with setuptools
      * 5. Construire des extensions C et C++ sur Windows
        * 5.1. Une approche "recette de cuisine"
        * 5.2. Différences entre Unix et Windows
        * 5.3. Utiliser les DLL en pratique
    * Intégrer l'interpréteur CPython dans une plus grande application
      * 1. Intégrer Python dans une autre application
        * 1.1. Intégration de très haut niveau
        * 1.2. Au-delà de l'intégration de haut niveau : survol
        * 1.3. Intégration pure
        * 1.4. Étendre un Python intégré
        * 1.5. Intégrer Python dans du C++
        * 1.6. Compiler et Lier en environnement Unix ou similaire
  * Manuel de référence de l'API Python/C
    * Introduction
      * Coding standards
      * Include Files
      * Useful macros
      * Objects, Types and Reference Counts
        * Compteurs de références
          * Reference Count Details
        * Types
      * Exceptions
      * Embarquer Python
      * Debugging Builds
    * Stabilité de l’API C
      * Unstable C API
      * ABI stable
        * Limited C API
        * Stable ABI
        * Porté de l’API restreinte et performance
        * Inconvénients de l’API restreinte
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
        * Analyse des arguments
          * Chaînes et tampons
          * Les nombres
          * Autres objets
          * Fonction de l'API
        * Construction des valeurs
      * Conversion et formatage de chaînes
      * PyHash API
      * Réflexion
      * Codec registry and support functions
        * Codec lookup API
        * Registry API for Unicode encoding error handlers
      * PyTime C API
        * Types
        * Clock Functions
        * Raw Clock Functions
        * Conversion functions
      * Support for Perf Maps
    * Couche d'abstraction des objets
      * Protocole Objet
      * Call Protocol
        * The _tp_call_ Protocol
        * The Vectorcall Protocol
          * Contrôle de la récursion
          * Vectorcall Support API
        * Object Calling API
        * Call Support API
      * Number Protocol
      * Sequence Protocol
      * Protocole de correspondance
      * Protocole d'itération
      * Protocole tampon
        * La structure _buffer_
        * Buffer request types
          * request-independent fields
          * readonly, format
          * shape, strides, suboffsets
          * contiguity requests
          * compound requests
        * Complex arrays
          * NumPy-style: shape and strides
          * PIL-style: shape, strides and suboffsets
        * Fonctions relatives aux tampons
    * Couche des objets concrets
      * Objets fondamentaux
        * Objets type
          * Creating Heap-Allocated Types
        * L'objet `None`
      * Objets numériques
        * Objets _Integer_
        * Les objets booléens
        * Floating-Point Objects
          * Pack and Unpack functions
            * Pack functions
            * Unpack functions
        * Objets représentant des nombres complexes
          * Nombres complexes en tant que structures C
          * Nombres complexes en tant qu'objets Python
      * Objets séquences
        * Objets _bytes_
        * Objets tableau d'octets
          * Macros de vérification de type
          * Fonctions directes sur l'API
          * Macros
        * Objets Unicode et Codecs
          * Objets Unicode
            * Type Unicode
            * Unicode Character Properties
            * Creating and accessing Unicode strings
            * Locale Encoding
            * File System Encoding
            * wchar_t Support
          * Built-in Codecs
            * Generic Codecs
            * UTF-8 Codecs
            * UTF-32 Codecs
            * UTF-16 Codecs
            * UTF-7 Codecs
            * Unicode-Escape Codecs
            * Raw-Unicode-Escape Codecs
            * Latin-1 Codecs
            * ASCII Codecs
            * Character Map Codecs
            * MBCS codecs for Windows
            * Methods & Slots
          * Methods and Slot Functions
        * Tuple Objects
        * Struct Sequence Objects
        * List Objects
      * Objets conteneurs
        * Objets dictionnaires
        * Set Objects
      * Objets fonctions
        * Objets fonction
        * Instance Method Objects
        * Objets méthode
        * Objets Cellules
        * Objets code
        * Extra information
      * Autres objets
        * Objets fichiers
        * Module Objects
          * Initializing C modules
            * Single-phase initialization
            * Multi-phase initialization
            * Low-level module creation functions
            * Support functions
          * Module lookup
        * Itérateurs
        * Les descripteurs
        * Slice Objects
          * Ellipsis Object
        * Objets de type MemoryView
        * Objets à références faibles
        * Capsules
        * Objets décrivant les _frames_
          * Frame Locals Proxies
          * Internal Frames
        * Objets générateur
        * Objets coroutines
        * Context Variables Objects
        * Objets DateTime
        * Objects for Type Hinting
    * Initialization, Finalization, and Threads
      * Before Python Initialization
      * Global configuration variables
      * Initializing and finalizing the interpreter
      * Process-wide parameters
      * Thread State and the Global Interpreter Lock
        * Releasing the GIL from extension code
        * Non-Python created threads
        * Cautions about fork()
        * High-level API
        * Low-level API
      * Sub-interpreter support
        * A Per-Interpreter GIL
        * Bugs and caveats
      * Asynchronous Notifications
      * Profiling and Tracing
      * Reference tracing
      * Support avancé du débogueur
      * Thread Local Storage Support
        * Thread Specific Storage (TSS) API
          * Dynamic Allocation
          * Méthodes
        * Thread Local Storage (TLS) API
      * Primitives de synchronisation
        * Python Critical Section API
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
        * Customize pymalloc Arena Allocator
      * The mimalloc allocator
      * tracemalloc C API
      * Exemples
    * Implémentation d'objets
      * Allouer des objets dans le tas
      * Common Object Structures
        * Base object types and macros
        * Implementing functions and methods
        * Accessing attributes of extension types
          * Member flags
          * Member types
          * Defining Getters and Setters
      * Objets type
        * Quick Reference
          * "tp slots"
          * sub-slots
          * slot typedefs
        * PyTypeObject Definition
        * PyObject Slots
        * PyVarObject Slots
        * PyTypeObject Slots
        * Static Types
        * Heap Types
        * Number Object Structures
        * Mapping Object Structures
        * Sequence Object Structures
        * Buffer Object Structures
        * Async Object Structures
        * Slot Type typedefs
        * Exemples
      * Supporting Cyclic Garbage Collection
        * Controlling the Garbage Collector State
        * Querying Garbage Collector State
    * Version des API et ABI
    * Monitoring C API
    * Generating Execution Events
      * Managing the Monitoring State
  * Installation de modules Python
    * Vocabulaire
    * Utilisation de base
    * Comment puis-je … ?
      * ... Installer `pip` avec une version de Python antérieures à la 3.4 ?
      * ... Installer des paquets juste pour l'utilisateur actuel ?
      * ... Installer des paquets Python scientifiques ?
      * ... Travailler avec plusieurs versions de Python installés en parallèle ?
    * Les problèmes d'installation typiques
      * Installer dans le Python du système sur Linux
      * `Pip` n'est pas installé
      * Installation d'extensions binaires
  * Les HOWTOs de Python
  * Questions fréquemment posées sur Python
    * FAQ générale sur Python
      * Informations générales
      * Python c'est le monde réel
    * FAQ de programmation
      * Questions générales
      * Fondamentaux
      * Nombres et chaînes de caractères
      * Performances
      * Séquences (_n_ -uplets / listes)
      * Objets
      * Modules
    * FAQ sur l'histoire et la conception
      * Pourquoi Python utilise-t-il l'indentation pour grouper les instructions ?
      * Pourquoi ai-je d'étranges résultats suite à de simples opérations arithmétiques ?
      * Pourquoi les calculs à virgules flottantes sont si imprécis ?
      * Pourquoi les chaînes de caractères Python sont-elles immuables ?
      * Pourquoi _self_ doit-il être explicitement utilisé dans les définitions et les appels de méthodes ?
      * Pourquoi ne puis-je pas utiliser d'assignation dans une expression ?
      * Pourquoi Python utilise des méthodes pour certaines fonctionnalités (ex : `list.index()`) mais des fonctions pour d'autres (ex : `len(list)`) ?
      * Pourquoi `join()` est une méthode de chaîne plutôt qu'une méthode de liste ou de _n_ -uplet ?
      * À quel point les exceptions sont-elles rapides ?
      * Pourquoi n'y a-t-il pas une instruction _switch_ ou une structure similaire à _switch / case_ en Python ?
      * Est-il possible d'émuler des fils d'exécution dans l'interpréteur plutôt que se baser sur les implémentations spécifiques aux systèmes d'exploitation ?
      * Pourquoi les expressions lambda ne peuvent pas contenir d'instructions ?
      * Python peut-il être compilé en code machine, en C ou dans un autre langage ?
      * Comment Python gère la mémoire ?
      * Pourquoi CPython n'utilise-t-il pas un modèle de ramasse-miettes plus traditionnel ?
      * Pourquoi toute la mémoire n'est pas libérée lorsque _CPython_ s'arrête ?
      * Pourquoi les _n_ -uplets et les _list_ sont deux types de données séparés ?
      * Comment les listes sont-elles implémentées dans CPython ?
      * Comment les dictionnaires sont-ils implémentés dans CPython ?
      * Pourquoi les clés du dictionnaire sont immuables ?
      * Pourquoi `list.sort()` ne renvoie pas la liste triée ?
      * Comment spécifier une interface et appliquer une spécification d’interface en Python ?
      * Pourquoi n'y a-t-il pas de `goto` en Python ?
      * Pourquoi les chaînes de caractères brutes (r-strings) ne peuvent-elles pas se terminer par un _backslash_ ?
      * Pourquoi la déclaration `with` pour les assignations d'attributs n'existe pas en Python ?
      * Pourquoi l'instruction `with` ne prend-elle pas en charge les générateurs ?
      * Pourquoi les deux-points sont-ils nécessaires pour les déclarations `if/while/def/class` ?
      * Pourquoi Python permet-il les virgules à la fin des listes et des _n_ -uplets ?
    * FAQ sur la bibliothèque et les extensions
      * Questions générales sur la bibliothèque
      * Tâches fréquentes
      * Fils d'exécution
      * Les entrées/sorties
      * Programmation réseau et Internet
      * Bases de données
      * Mathématiques et calcul numérique
    * FAQ extension/intégration
      * Puis-je créer mes propres fonctions en C ?
      * Puis-je créer mes propres fonctions en C++ ?
      * Écrire directement en C est difficile ; existe-t-il des alternatives ?
      * Comment puis-je exécuter des instructions quelconques Python à partir de C ?
      * Comment puis-je évaluer une expression quelconque de Python à partir de C ?
      * Comment puis-je extraire des donnés en C d'un objet Python ?
      * Comment utiliser Py_BuildValue() pour créer un _n_ -uplet de longueur définie ?
      * Comment puis-je appeler la méthode d'un objet à partir de C ?
      * Comment puis-je récupérer la sortie de `PyErr_Print()` (ou tout ce qui s'affiche sur _stdout_ /_stderr_) ?
      * Comment accéder à un module écrit en Python à partir de C ?
      * Comment s'interfacer avec les objets C++ depuis Python ?
      * J'ai ajouté un module en utilisant le fichier _Setup_ et la compilation échoue ; pourquoi ?
      * Comment déboguer une extension ?
      * Je veux compiler un module Python sur mon système Linux, mais il manque certains fichiers. Pourquoi ?
      * Comment distinguer une « entrée incomplète » (_incomplete input_) d'une « entrée invalide » (_invalid input_) ?
      * Comment puis-je trouver les symboles g++ indéfinis `__builtin_new` ou `__pure_virtual` ?
      * Puis-je créer une classe d'objets avec certaines méthodes implémentées en C et d'autres en Python (p. ex. en utilisant l'héritage) ?
    * FAQ : Python et Windows
      * Comment exécuter un programme Python sous Windows ?
      * Comment rendre des scripts Python exécutables ?
      * Pourquoi Python met-il du temps à démarrer ?
      * Comment construire un exécutable depuis un script Python ?
      * Est-ce qu'un fichier `*.pyd` est la même chose qu'une DLL ?
      * Comment puis-je intégrer Python dans une application Windows ?
      * Comment empêcher mon éditeur d'utiliser des tabulations dans mes fichiers Python ?
      * Comment puis-je vérifier de manière non bloquante qu'une touche a été pressée ?
      * Comment résoudre l'erreur « `api-ms-win-crt-runtime-l1-1-0.dll` manquante » ?
    * FAQ interface graphique
      * Questions générales sur l'interface graphique
      * Quelles boîtes à outils IUG existent pour Python ?
      * Questions à propos de _Tkinter_
    * FAQ "Pourquoi Python est installé sur mon ordinateur ?"
      * Qu'est-ce que Python ?
      * Pourquoi Python est installé sur ma machine ?
      * Puis-je supprimer Python ?
  * Deprecations
    * Pending Removal in Python 3.14
    * Pending Removal in Python 3.15
    * Pending removal in Python 3.16
    * Pending Removal in Future Versions
    * C API Deprecations
      * Pending Removal in Python 3.14
      * Pending Removal in Python 3.15
      * Pending Removal in Future Versions
  * Glossaire
  * About this documentation
    * Contributors to the Python documentation
  * S'attaquer aux bogues
    * Bogues de documentation
    * Utilisation du gestionnaire de tickets Python
    * Commencer à contribuer à Python vous-même
  * Copyright
  * Histoire et licence
    * Histoire du logiciel
    * Conditions générales pour accéder à, ou utiliser, Python
      * PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
      * LICENCE D'UTILISATION BEOPEN.COM POUR PYTHON 2.0
      * LICENCE D'UTILISATION CNRI POUR PYTHON 1.6.1
      * LICENCE D'UTILISATION CWI POUR PYTHON 0.9.0 à 1.2
      * ZERO-CLAUSE BSD LICENSE FOR CODE IN THE PYTHON DOCUMENTATION
    * Licences et remerciements pour les logiciels tiers
      * Mersenne twister
      * Interfaces de connexion (_sockets_)
      * Interfaces de connexion asynchrones
      * Gestion de témoin (_cookie_)
      * Traçage d'exécution
      * Les fonctions UUencode et UUdecode
      * Appel de procédures distantes en XML (_RPC_ , pour _Remote Procedure Call_)
      * test_epoll
      * Select kqueue
      * SipHash24
      * _strtod_ et _dtoa_
      * OpenSSL
      * expat
      * libffi
      * zlib
      * cfuhash
      * libmpdec
      * Ensemble de tests C14N du W3C
      * mimalloc
      * _asyncio_
      * Global Unbounded Sequences (GUS)


#### Sujet suivant
Nouveautés de Python
### Cette page
  * Signalement de bogue
  * Voir la source 


«
### Navigation
  * index
  * modules |
  * suivant |
  * ![Python logo](https://docs.python.org/fr/3/_static/py.svg)
  * Python »
  * EnglishSpanishFrenchItalianJapaneseKoreanPolishBrazilian PortugueseTurkishSimplified ChineseTraditional Chinese
dev (3.14)3.13.23.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
  * 3.13.2 Documentation » 
  * Contenu de la documentation Python
  * | 
  * Theme  Auto Light Dark |


©  Copyright  2001-2025, Python Software Foundation. This page is licensed under the Python Software Foundation License Version 2. Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License. See History and License for more information. The Python Software Foundation is a non-profit corporation. Please donate. Mis à jour le févr. 17, 2025 (05:58 UTC). Found a bug? Créé en utilisant Sphinx 8.1.3. 
