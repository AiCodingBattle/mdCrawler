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
  * Deprecations
  * | 
  * Theme  Auto Light Dark |


# Deprecations¶
## Pending Removal in Python 3.14¶
  * `argparse`: The _type_ , _choices_ , and _metavar_ parameters of `argparse.BooleanOptionalAction` are deprecated and will be removed in 3.14. (Contributed by Nikita Sobolev in gh-92248.)
  * `ast`: The following features have been deprecated in documentation since Python 3.8, now cause a `DeprecationWarning` to be emitted at runtime when they are accessed or used, and will be removed in Python 3.14:
    * `ast.Num`
    * `ast.Str`
    * `ast.Bytes`
    * `ast.NameConstant`
    * `ast.Ellipsis`
Use `ast.Constant` instead. (Contributed by Serhiy Storchaka in gh-90953.)
  * `asyncio`:
    * The child watcher classes `MultiLoopChildWatcher`, `FastChildWatcher`, `AbstractChildWatcher` and `SafeChildWatcher` are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in gh-94597.)
    * `asyncio.set_child_watcher()`, `asyncio.get_child_watcher()`, `asyncio.AbstractEventLoopPolicy.set_child_watcher()` and `asyncio.AbstractEventLoopPolicy.get_child_watcher()` are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in gh-94597.)
    * The `get_event_loop()` method of the default event loop policy now emits a `DeprecationWarning` if there is no current event loop set and it decides to create one. (Contributed by Serhiy Storchaka and Guido van Rossum in gh-100160.)
  * `collections.abc`: Deprecated `ByteString`. Prefer `Sequence` or `Buffer`. For use in typing, prefer a union, like `bytes | bytearray`, or `collections.abc.Buffer`. (Contributed by Shantanu Jain in gh-91896.)
  * `email`: Deprecated the _isdst_ parameter in `email.utils.localtime()`. (Contributed by Alan Williams in gh-72346.)
  * `importlib.abc` deprecated classes:
    * `importlib.abc.ResourceReader`
    * `importlib.abc.Traversable`
    * `importlib.abc.TraversableResources`
Use `importlib.resources.abc` classes instead:
    * `importlib.resources.abc.Traversable`
    * `importlib.resources.abc.TraversableResources`
(Contributed by Jason R. Coombs and Hugo van Kemenade in gh-93963.)
  * `itertools` had undocumented, inefficient, historically buggy, and inconsistent support for copy, deepcopy, and pickle operations. This will be removed in 3.14 for a significant reduction in code volume and maintenance burden. (Contributed by Raymond Hettinger in gh-101588.)
  * `multiprocessing`: The default start method will change to a safer one on Linux, BSDs, and other non-macOS POSIX platforms where `'fork'` is currently the default (gh-84559). Adding a runtime warning about this was deemed too disruptive as the majority of code is not expected to care. Use the `get_context()` or `set_start_method()` APIs to explicitly specify when your code _requires_ `'fork'`. See Contextes et méthodes de démarrage.
  * `pathlib`: `is_relative_to()` and `relative_to()`: passing additional arguments is deprecated.
  * `pkgutil`: `find_loader()` and `get_loader()` now raise `DeprecationWarning`; use `importlib.util.find_spec()` instead. (Contributed by Nikita Sobolev in gh-97850.)
  * `pty`:
    * `master_open()`: use `pty.openpty()`.
    * `slave_open()`: use `pty.openpty()`.
  * `sqlite3`:
    * `version` and `version_info`.
    * `execute()` and `executemany()` if named placeholders are used and _parameters_ is a sequence instead of a `dict`.
  * `typing`: `ByteString`, deprecated since Python 3.9, now causes a `DeprecationWarning` to be emitted when it is used.
  * `urllib`: `urllib.parse.Quoter` is deprecated: it was not intended to be a public API. (Contributed by Gregory P. Smith in gh-88168.)


## Pending Removal in Python 3.15¶
  * The import system:
    * Setting `__cached__` on a module while failing to set `__spec__.cached` is deprecated. In Python 3.15, `__cached__` will cease to be set or take into consideration by the import system or standard library. (gh-97879)
    * Setting `__package__` on a module while failing to set `__spec__.parent` is deprecated. In Python 3.15, `__package__` will cease to be set or take into consideration by the import system or standard library. (gh-97879)
  * `ctypes`:
    * The undocumented `ctypes.SetPointerType()` function has been deprecated since Python 3.13.
  * `http.server`:
    * The obsolete and rarely used `CGIHTTPRequestHandler` has been deprecated since Python 3.13. No direct replacement exists. _Anything_ is better than CGI to interface a web server with a request handler.
    * The `--cgi` flag to the **python -m http.server** command-line interface has been deprecated since Python 3.13.
  * `importlib`:
    * `load_module()` method: use `exec_module()` instead.
  * `locale`:
    * The `getdefaultlocale()` function has been deprecated since Python 3.11. Its removal was originally planned for Python 3.13 (gh-90817), but has been postponed to Python 3.15. Use `getlocale()`, `setlocale()`, and `getencoding()` instead. (Contributed by Hugo van Kemenade in gh-111187.)
  * `pathlib`:
    * `PurePath.is_reserved()` has been deprecated since Python 3.13. Use `os.path.isreserved()` to detect reserved paths on Windows.
  * `platform`:
    * `java_ver()` has been deprecated since Python 3.13. This function is only useful for Jython support, has a confusing API, and is largely untested.
  * `threading`:
    * `RLock()` will take no arguments in Python 3.15. Passing any arguments has been deprecated since Python 3.14, as the Python version does not permit any arguments, but the C version allows any number of positional or keyword arguments, ignoring every argument.
  * `types`:
    * `types.CodeType`: Accessing `co_lnotab` was deprecated in **PEP 626** since 3.10 and was planned to be removed in 3.12, but it only got a proper `DeprecationWarning` in 3.12. May be removed in 3.15. (Contributed by Nikita Sobolev in gh-101866.)
  * `typing`:
    * The undocumented keyword argument syntax for creating `NamedTuple` classes (e.g. `Point = NamedTuple("Point", x=int, y=int)`) has been deprecated since Python 3.13. Use the class-based syntax or the functional syntax instead.
    * The `typing.no_type_check_decorator()` decorator function has been deprecated since Python 3.13. After eight years in the `typing` module, it has yet to be supported by any major type checker.
  * `wave`:
    * The `getmark()`, `setmark()`, and `getmarkers()` methods of the `Wave_read` and `Wave_write` classes have been deprecated since Python 3.13.


## Pending removal in Python 3.16¶
  * The import system:
    * Setting `__loader__` on a module while failing to set `__spec__.loader` is deprecated. In Python 3.16, `__loader__` will cease to be set or taken into consideration by the import system or the standard library.
  * `array`:
    * The `'u'` format code (`wchar_t`) has been deprecated in documentation since Python 3.3 and at runtime since Python 3.13. Use the `'w'` format code (`Py_UCS4`) for Unicode characters instead.
  * `asyncio`:
    * `asyncio.iscoroutinefunction()` is deprecated and will be removed in Python 3.16, use `inspect.iscoroutinefunction()` instead. (Contributed by Jiahao Li and Kumar Aditya in gh-122875.)
  * `builtins`:
    * Bitwise inversion on boolean types, `~True` or `~False` has been deprecated since Python 3.12, as it produces surprising and unintuitive results (`-2` and `-1`). Use `not x` instead for the logical negation of a Boolean. In the rare case that you need the bitwise inversion of the underlying integer, convert to `int` explicitly (`~int(x)`).
  * `shutil`:
    * The `ExecError` exception has been deprecated since Python 3.14. It has not been used by any function in `shutil` since Python 3.4, and is now an alias of `RuntimeError`.
  * `symtable`:
    * The `Class.get_methods` method has been deprecated since Python 3.14.
  * `sys`:
    * The `_enablelegacywindowsfsencoding()` function has been deprecated since Python 3.13. Use the `PYTHONLEGACYWINDOWSFSENCODING` environment variable instead.
  * `tarfile`:
    * The undocumented and unused `TarFile.tarfile` attribute has been deprecated since Python 3.13.


## Pending Removal in Future Versions¶
The following APIs will be removed in the future, although there is currently no date scheduled for their removal.
  * `argparse`: Nesting argument groups and nesting mutually exclusive groups are deprecated.
  * `array`'s `'u'` format code (gh-57281)
  * `builtins`:
    * `bool(NotImplemented)`.
    * Generators: `throw(type, exc, tb)` and `athrow(type, exc, tb)` signature is deprecated: use `throw(exc)` and `athrow(exc)` instead, the single argument signature.
    * Currently Python accepts numeric literals immediately followed by keywords, for example `0in x`, `1or x`, `0if 1else 2`. It allows confusing and ambiguous expressions like `[0x1for x in y]` (which can be interpreted as `[0x1 for x in y]` or `[0x1f or x in y]`). A syntax warning is raised if the numeric literal is immediately followed by one of keywords `and`, `else`, `for`, `if`, `in`, `is` and `or`. In a future release it will be changed to a syntax error. (gh-87999)
    * Support for `__index__()` and `__int__()` method returning non-int type: these methods will be required to return an instance of a strict subclass of `int`.
    * Support for `__float__()` method returning a strict subclass of `float`: these methods will be required to return an instance of `float`.
    * Support for `__complex__()` method returning a strict subclass of `complex`: these methods will be required to return an instance of `complex`.
    * Delegation of `int()` to `__trunc__()` method.
    * Passing a complex number as the _real_ or _imag_ argument in the `complex()` constructor is now deprecated; it should only be passed as a single positional argument. (Contributed by Serhiy Storchaka in gh-109218.)
  * `calendar`: `calendar.January` and `calendar.February` constants are deprecated and replaced by `calendar.JANUARY` and `calendar.FEBRUARY`. (Contributed by Prince Roshan in gh-103636.)
  * `codeobject.co_lnotab`: use the `codeobject.co_lines()` method instead.
  * `datetime`:
    * `utcnow()`: use `datetime.datetime.now(tz=datetime.UTC)`.
    * `utcfromtimestamp()`: use `datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)`.
  * `gettext`: Plural value must be an integer.
  * `importlib`:
    * `cache_from_source()` _debug_override_ parameter is deprecated: use the _optimization_ parameter instead.
  * `importlib.metadata`:
    * `EntryPoints` tuple interface.
    * Implicit `None` on return values.
  * `logging`: the `warn()` method has been deprecated since Python 3.3, use `warning()` instead.
  * `mailbox`: Use of StringIO input and text mode is deprecated, use BytesIO and binary mode instead.
  * `os`: Calling `os.register_at_fork()` in multi-threaded process.
  * `pydoc.ErrorDuringImport`: A tuple value for _exc_info_ parameter is deprecated, use an exception instance.
  * `re`: More strict rules are now applied for numerical group references and group names in regular expressions. Only sequence of ASCII digits is now accepted as a numerical reference. The group name in bytes patterns and replacement strings can now only contain ASCII letters and digits and underscore. (Contributed by Serhiy Storchaka in gh-91760.)
  * `sre_compile`, `sre_constants` and `sre_parse` modules.
  * `shutil`: `rmtree()`'s _onerror_ parameter is deprecated in Python 3.12; use the _onexc_ parameter instead.
  * `ssl` options and protocols:
    * `ssl.SSLContext` without protocol argument is deprecated.
    * `ssl.SSLContext`: `set_npn_protocols()` and `selected_npn_protocol()` are deprecated: use ALPN instead.
    * `ssl.OP_NO_SSL*` options
    * `ssl.OP_NO_TLS*` options
    * `ssl.PROTOCOL_SSLv3`
    * `ssl.PROTOCOL_TLS`
    * `ssl.PROTOCOL_TLSv1`
    * `ssl.PROTOCOL_TLSv1_1`
    * `ssl.PROTOCOL_TLSv1_2`
    * `ssl.TLSVersion.SSLv3`
    * `ssl.TLSVersion.TLSv1`
    * `ssl.TLSVersion.TLSv1_1`
  * `sysconfig.is_python_build()` _check_home_ parameter is deprecated and ignored.
  * `threading` methods:
    * `threading.Condition.notifyAll()`: use `notify_all()`.
    * `threading.Event.isSet()`: use `is_set()`.
    * `threading.Thread.isDaemon()`, `threading.Thread.setDaemon()`: use `threading.Thread.daemon` attribute.
    * `threading.Thread.getName()`, `threading.Thread.setName()`: use `threading.Thread.name` attribute.
    * `threading.currentThread()`: use `threading.current_thread()`.
    * `threading.activeCount()`: use `threading.active_count()`.
  * `typing.Text` (gh-92332).
  * `unittest.IsolatedAsyncioTestCase`: it is deprecated to return a value that is not `None` from a test case.
  * `urllib.parse` deprecated functions: `urlparse()` instead
    * `splitattr()`
    * `splithost()`
    * `splitnport()`
    * `splitpasswd()`
    * `splitport()`
    * `splitquery()`
    * `splittag()`
    * `splittype()`
    * `splituser()`
    * `splitvalue()`
    * `to_bytes()`
  * `urllib.request`: `URLopener` and `FancyURLopener` style of invoking requests is deprecated. Use newer `urlopen()` functions and methods.
  * `wsgiref`: `SimpleHandler.stdout.write()` should not do partial writes.
  * `xml.etree.ElementTree`: Testing the truth value of an `Element` is deprecated. In a future release it will always return `True`. Prefer explicit `len(elem)` or `elem is not None` tests instead.
  * `zipimport.zipimporter.load_module()` is deprecated: use `exec_module()` instead.


## C API Deprecations¶
### Pending Removal in Python 3.14¶
  * The `ma_version_tag` field in `PyDictObject` for extension modules (**PEP 699**; gh-101193).
  * Creating `immutable types` with mutable bases (gh-95388).
  * Functions to configure Python's initialization, deprecated in Python 3.11:
    * `PySys_SetArgvEx()`: Set `PyConfig.argv` instead.
    * `PySys_SetArgv()`: Set `PyConfig.argv` instead.
    * `Py_SetProgramName()`: Set `PyConfig.program_name` instead.
    * `Py_SetPythonHome()`: Set `PyConfig.home` instead.
The `Py_InitializeFromConfig()` API should be used with `PyConfig` instead.
  * Global configuration variables:
    * `Py_DebugFlag`: Use `PyConfig.parser_debug` instead.
    * `Py_VerboseFlag`: Use `PyConfig.verbose` instead.
    * `Py_QuietFlag`: Use `PyConfig.quiet` instead.
    * `Py_InteractiveFlag`: Use `PyConfig.interactive` instead.
    * `Py_InspectFlag`: Use `PyConfig.inspect` instead.
    * `Py_OptimizeFlag`: Use `PyConfig.optimization_level` instead.
    * `Py_NoSiteFlag`: Use `PyConfig.site_import` instead.
    * `Py_BytesWarningFlag`: Use `PyConfig.bytes_warning` instead.
    * `Py_FrozenFlag`: Use `PyConfig.pathconfig_warnings` instead.
    * `Py_IgnoreEnvironmentFlag`: Use `PyConfig.use_environment` instead.
    * `Py_DontWriteBytecodeFlag`: Use `PyConfig.write_bytecode` instead.
    * `Py_NoUserSiteDirectory`: Use `PyConfig.user_site_directory` instead.
    * `Py_UnbufferedStdioFlag`: Use `PyConfig.buffered_stdio` instead.
    * `Py_HashRandomizationFlag`: Use `PyConfig.use_hash_seed` and `PyConfig.hash_seed` instead.
    * `Py_IsolatedFlag`: Use `PyConfig.isolated` instead.
    * `Py_LegacyWindowsFSEncodingFlag`: Use `PyPreConfig.legacy_windows_fs_encoding` instead.
    * `Py_LegacyWindowsStdioFlag`: Use `PyConfig.legacy_windows_stdio` instead.
    * `Py_FileSystemDefaultEncoding`: Use `PyConfig.filesystem_encoding` instead.
    * `Py_HasFileSystemDefaultEncoding`: Use `PyConfig.filesystem_encoding` instead.
    * `Py_FileSystemDefaultEncodeErrors`: Use `PyConfig.filesystem_errors` instead.
    * `Py_UTF8Mode`: Use `PyPreConfig.utf8_mode` instead. (see `Py_PreInitialize()`)
The `Py_InitializeFromConfig()` API should be used with `PyConfig` instead.


### Pending Removal in Python 3.15¶
  * The bundled copy of `libmpdecimal`.
  * The `PyImport_ImportModuleNoBlock()`: Use `PyImport_ImportModule()` instead.
  * `PyWeakref_GetObject()` and `PyWeakref_GET_OBJECT()`: Use `PyWeakref_GetRef()` instead.
  * `Py_UNICODE` type and the `Py_UNICODE_WIDE` macro: Use `wchar_t` instead.
  * Python initialization functions:
    * `PySys_ResetWarnOptions()`: Clear `sys.warnoptions` and `warnings.filters` instead.
    * `Py_GetExecPrefix()`: Get `sys.base_exec_prefix` and `sys.exec_prefix` instead.
    * `Py_GetPath()`: Get `sys.path` instead.
    * `Py_GetPrefix()`: Get `sys.base_prefix` and `sys.prefix` instead.
    * `Py_GetProgramFullPath()`: Get `sys.executable` instead.
    * `Py_GetProgramName()`: Get `sys.executable` instead.
    * `Py_GetPythonHome()`: Get `PyConfig.home` or the `PYTHONHOME` environment variable instead.


### Pending Removal in Future Versions¶
The following APIs are deprecated and will be removed, although there is currently no date scheduled for their removal.
  * `Py_TPFLAGS_HAVE_FINALIZE`: Unneeded since Python 3.8.
  * `PyErr_Fetch()`: Use `PyErr_GetRaisedException()` instead.
  * `PyErr_NormalizeException()`: Use `PyErr_GetRaisedException()` instead.
  * `PyErr_Restore()`: Use `PyErr_SetRaisedException()` instead.
  * `PyModule_GetFilename()`: Use `PyModule_GetFilenameObject()` instead.
  * `PyOS_AfterFork()`: Use `PyOS_AfterFork_Child()` instead.
  * `PySlice_GetIndicesEx()`: Use `PySlice_Unpack()` and `PySlice_AdjustIndices()` instead.
  * `PyUnicode_AsDecodedObject()`: Use `PyCodec_Decode()` instead.
  * `PyUnicode_AsDecodedUnicode()`: Use `PyCodec_Decode()` instead.
  * `PyUnicode_AsEncodedObject()`: Use `PyCodec_Encode()` instead.
  * `PyUnicode_AsEncodedUnicode()`: Use `PyCodec_Encode()` instead.
  * `PyUnicode_READY()`: Unneeded since Python 3.12
  * `PyErr_Display()`: Use `PyErr_DisplayException()` instead.
  * `_PyErr_ChainExceptions()`: Use `_PyErr_ChainExceptions1()` instead.
  * `PyBytesObject.ob_shash` member: call `PyObject_Hash()` instead.
  * `PyDictObject.ma_version_tag` member.
  * Thread Local Storage (TLS) API:
    * `PyThread_create_key()`: Use `PyThread_tss_alloc()` instead.
    * `PyThread_delete_key()`: Use `PyThread_tss_free()` instead.
    * `PyThread_set_key_value()`: Use `PyThread_tss_set()` instead.
    * `PyThread_get_key_value()`: Use `PyThread_tss_get()` instead.
    * `PyThread_delete_key_value()`: Use `PyThread_tss_delete()` instead.
    * `PyThread_ReInitTLS()`: Unneeded since Python 3.7.


### Table des matières
  * Deprecations
    * Pending Removal in Python 3.14
    * Pending Removal in Python 3.15
    * Pending removal in Python 3.16
    * Pending Removal in Future Versions
    * C API Deprecations
      * Pending Removal in Python 3.14
      * Pending Removal in Python 3.15
      * Pending Removal in Future Versions


#### Sujet précédent
FAQ "Pourquoi Python est installé sur mon ordinateur ?"
#### Sujet suivant
Glossaire
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
  * Deprecations
  * | 
  * Theme  Auto Light Dark |


©  Copyright  2001-2025, Python Software Foundation. This page is licensed under the Python Software Foundation License Version 2. Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License. See History and License for more information. The Python Software Foundation is a non-profit corporation. Please donate. Mis à jour le févr. 17, 2025 (05:58 UTC). Found a bug? Créé en utilisant Sphinx 8.1.3. 
