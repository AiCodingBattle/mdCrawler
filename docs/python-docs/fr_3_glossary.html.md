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
  * Glossaire
  * | 
  * Theme  Auto Light Dark |


# Glossaire¶
`>>>`¶
    
The default Python prompt of the interactive shell. Often seen for code examples which can be executed interactively in the interpreter.
`...`¶
    
Peut faire référence à :
  * The default Python prompt of the interactive shell when entering the code for an indented code block, when within a pair of matching left and right delimiters (parentheses, square brackets, curly braces or triple quotes), or after specifying a decorator.
  * La constante `Ellipsis`.


classe mère abstraite¶
    
Les classes mères abstraites (ABC, suivant l'abréviation anglaise _Abstract Base Class_) complètent le duck-typing en fournissant un moyen de définir des interfaces pour les cas où d'autres techniques comme `hasattr()` seraient inélégantes ou subtilement fausses (par exemple avec les méthodes magiques). Les ABC introduisent des sous-classes virtuelles qui n'héritent pas d'une classe mais qui sont quand même reconnues par `isinstance()` ou `issubclass()` (voir la documentation du module `abc`). Python contient de nombreuses ABC pour les structures de données (dans le module `collections.abc`), les nombres (dans le module `numbers`), les flux (dans le module `io`) et les chercheurs-chargeurs du système d'importation (dans le module `importlib.abc`). Vous pouvez créer vos propres ABC avec le module `abc`.
annotation¶
    
Étiquette associée à une variable, un attribut de classe, un paramètre de fonction ou une valeur de retour. Elle est utilisée par convention comme type hint.
Les annotations de variables locales ne sont pas accessibles au moment de l'exécution, mais les annotations de variables globales, d'attributs de classe et de fonctions sont stockées dans l'attribut spécial `__annotations__` des modules, classes et fonctions, respectivement.
Voir annotation de variable, annotation de fonction, les **PEP 484** et **PEP 526**, qui décrivent cette fonctionnalité. Voir aussi Bonnes pratiques concernant les annotations sur les bonnes pratiques concernant les annotations.
argument¶
    
Valeur, donnée à une fonction ou à une méthode lors de son appel. Il existe deux types d'arguments :
  * _argument nommé_ : un argument précédé d'un identifiant (comme `name=`) ou un dictionnaire précédé de `**`, lors d'un appel de fonction. Par exemple, `3` et `5` sont tous les deux des arguments nommés dans l'appel à `complex()` ici :
```
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})

```

  * _argument positionnel_ : un argument qui n'est pas nommé. Les arguments positionnels apparaissent au début de la liste des arguments, ou donnés sous forme d'un itérable précédé par `*`. Par exemple, `3` et `5` sont tous les deux des arguments positionnels dans les appels suivants :
```
complex(3, 5)
complex(*(3, 5))

```



Les arguments se retrouvent dans le corps de la fonction appelée parmi les variables locales. Voir la section Appels à propos des règles dictant cette affectation. Syntaxiquement, toute expression est acceptée comme argument, et c'est la valeur résultante de l'expression qui sera affectée à la variable locale.
Voir aussi paramètre dans le glossaire, la question Différence entre argument et paramètre de la FAQ et la **PEP 362**.
gestionnaire de contexte asynchrone¶
    
(_asynchronous context manager_ en anglais) Objet contrôlant l'environnement à l'intérieur d'une instruction `async with` en définissant les méthodes `__aenter__()` et `__aexit__()`. A été Introduit par la **PEP 492**.
générateur asynchrone¶
    
Fonction qui renvoie un itérateur de générateur asynchrone. Cela ressemble à une coroutine définie par `async def`, sauf qu'elle contient une ou des expressions `yield` produisant ainsi uns série de valeurs utilisables dans une boucle `async for`.
Générateur asynchrone fait généralement référence à une fonction, mais peut faire référence à un _itérateur de générateur asynchrone_ dans certains contextes. Dans les cas où le sens voulu n'est pas clair, utiliser l'ensemble des termes lève l’ambiguïté.
Un générateur asynchrone peut contenir des expressions `await` ainsi que des instructions `async for`, et `async with`.
itérateur de générateur asynchrone¶
    
Objet créé par un générateur asynchrone.
C'est un asynchronous iterator qui, lorsqu'il est appelé via la méthode `__anext__()` renvoie un objet _awaitable_ qui exécute le corps de la fonction du générateur asynchrone jusqu'au prochain `yield`.
Each `yield` temporarily suspends processing, remembering the execution state (including local variables and pending try-statements). When the _asynchronous generator iterator_ effectively resumes with another awaitable returned by `__anext__()`, it picks up where it left off. See **PEP 492** and **PEP 525**.
itérable asynchrone¶
    
Objet qui peut être utilisé dans une instruction `async for`. Sa méthode `__aiter__()` doit renvoyer un asynchronous iterator. A été introduit par la **PEP 492**.
itérateur asynchrone¶
    
Objet qui implémente les méthodes `__aiter__()` et `__anext__()`. `__anext__()` doit renvoyer un objet awaitable. Tant que la méthode `__anext__()` produit des objets _awaitable_ , le `async for` appelant les consomme. L'itérateur asynchrone lève une exception `StopAsyncIteration` pour signifier la fin de l'itération. A été introduit par la **PEP 492**.
attribut¶
    
Valeur associée à un objet et habituellement désignée par son nom _via_ une notation utilisant des points. Par exemple, si un objet _o_ possède un attribut _a_ , cet attribut est référencé par _o.a_.
Il est possible de donner à un objet un attribut dont le nom n'est pas un identifiant tel que défini pour les Identifiants et mots-clés, par exemple en utilisant `setattr()`, si l'objet le permet. Un tel attribut ne sera pas accessible à l'aide d'une expression pointée et on devra y accéder avec `getattr()`.
attendable (_awaitable_)¶
    
Objet pouvant être utilisé dans une expression `await`. Ce peut être une coroutine ou un objet avec une méthode `__await__()`. Voir aussi la **PEP 492**.
BDFL¶
    
Dictateur bienveillant à vie (_Benevolent Dictator For Life_ en anglais). Pseudonyme de Guido van Rossum, le créateur de Python.
fichier binaire¶
    
A file object able to read and write bytes-like objects. Examples of binary files are files opened in binary mode (`'rb'`, `'wb'` or `'rb+'`), `sys.stdin.buffer`, `sys.stdout.buffer`, and instances of `io.BytesIO` and `gzip.GzipFile`.
Consultez fichier texte, un objet fichier capable de lire et d'écrire des objets `str`.
référence empruntée¶
    
In Python's C API, a borrowed reference is a reference to an object, where the code using the object does not own the reference. It becomes a dangling pointer if the object is destroyed. For example, a garbage collection can remove the last strong reference to the object and so destroy it.
Il est recommandé d'appeler `Py_INCREF()` sur la référence empruntée, ce qui la transforme _in situ_ en une référence forte. Vous pouvez faire une exception si vous êtes certain que l'objet ne peut pas être supprimé avant la dernière utilisation de la référence empruntée. Voir aussi la fonction `Py_NewRef()`, qui crée une nouvelle référence forte.
objet octet-compatible¶
    
Un objet gérant le protocole tampon et pouvant exporter un tampon (_buffer_ en anglais) C-contigu. Cela inclut les objets `bytes`, `bytearray` et `array.array`, ainsi que beaucoup d'objets `memoryview`. Les objets octets-compatibles peuvent être utilisés pour diverses opérations sur des données binaires, comme la compression, la sauvegarde dans un fichier binaire ou l'envoi sur le réseau.
Certaines opérations nécessitent de travailler sur des données binaires variables. La documentation parle de ceux-ci comme des _read-write bytes-like objects_. Par exemple, `bytearray` ou une `memoryview` d'un `bytearray` en font partie. D'autres opérations nécessitent de travailler sur des données binaires stockées dans des objets immuables («  _objets octets-compatibles en lecture seule_ »), par exemple des `bytes` ou des `memoryview` d'un objet `bytes`.
code intermédiaire (_bytecode_)¶
    
Le code source, en Python, est compilé en un code intermédiaire (_bytecode_ en anglais), la représentation interne à CPython d'un programme Python. Le code intermédiaire est mis en cache dans un fichier `.pyc` de manière à ce qu'une seconde exécution soit plus rapide (la compilation en code intermédiaire a déjà été faite). On dit que ce _langage intermédiaire_ est exécuté sur une virtual machine qui exécute des instructions machine pour chaque instruction du code intermédiaire. Notez que le code intermédiaire n'a pas vocation à fonctionner sur différentes machines virtuelles Python ou à être stable entre différentes versions de Python.
La documentation du module dis fournit une liste des instructions du code intermédiaire.
appelable (_callable_)¶
    
Un appelable est un objet qui peut être appelé, éventuellement avec un ensemble d'arguments (voir argument), avec la syntaxe suivante :
```
callable(argument1, argument2, argumentN)

```

Une fonction, et par extension une méthode, est un appelable. Une instance d'une classe qui implémente la méthode `__call__()` est également un appelable.
fonction de rappel (_callback_)¶
    
Une fonction (classique, par opposition à une coroutine) passée en argument pour être exécutée plus tard.
classe¶
    
Modèle pour créer des objets définis par l'utilisateur. Une définition de classe (_class_) contient normalement des définitions de méthodes qui agissent sur les instances de la classe.
variable de classe¶
    
Une variable définie dans une classe et destinée à être modifiée uniquement au niveau de la classe (c'est-à-dire, pas dans une instance de la classe).
closure variable¶
    
A free variable referenced from a nested scope that is defined in an outer scope rather than being resolved at runtime from the globals or builtin namespaces. May be explicitly defined with the `nonlocal` keyword to allow write access, or implicitly defined if the variable is only being read.
For example, in the `inner` function in the following code, both `x` and `print` are free variables, but only `x` is a _closure variable_ :
```
defouter():
  x = 0
  definner():
    nonlocal x
    x += 1
    print(x)
  return inner

```

Due to the `codeobject.co_freevars` attribute (which, despite its name, only includes the names of closure variables rather than listing all referenced free variables), the more general free variable term is sometimes used even when the intended meaning is to refer specifically to closure variables.
nombre complexe¶
    
Extension des nombres réels familiers, dans laquelle tous les nombres sont exprimés sous la forme d'une somme d'une partie réelle et d'une partie imaginaire. Les nombres imaginaires sont les nombres réels multipliés par l'unité imaginaire (la racine carrée de `-1`, souvent écrite `i` en mathématiques ou `j` par les ingénieurs). Python comprend nativement les nombres complexes, écrits avec cette dernière notation : la partie imaginaire est écrite avec un suffixe `j`, exemple, `3+1j`. Pour utiliser les équivalents complexes de `math`, utilisez `cmath`. Les nombres complexes sont un concept assez avancé en mathématiques. Si vous ne connaissez pas ce concept, vous pouvez tranquillement les ignorer.
context¶
    
This term has different meanings depending on where and how it is used. Some common meanings:
  * The temporary state or environment established by a context manager via a `with` statement.
  * The collection of key­value bindings associated with a particular `contextvars.Context` object and accessed via `ContextVar` objects. Also see context variable.
  * A `contextvars.Context` object. Also see current context.


context management protocol¶
    
The `__enter__()` and `__exit__()` methods called by the `with` statement. See **PEP 343**.
gestionnaire de contexte¶
    
An object which implements the context management protocol and controls the environment seen in a `with` statement. See **PEP 343**.
variable de contexte¶
    
A variable whose value depends on which context is the current context. Values are accessed via `contextvars.ContextVar` objects. Context variables are primarily used to isolate state between concurrent asynchronous tasks.
contigu¶
    
Un tampon (_buffer_ en anglais) est considéré comme contigu s’il est soit _C-contigu_ soit _Fortran-contigu_. Les tampons de dimension zéro sont C-contigus et Fortran-contigus. Pour un tableau à une dimension, ses éléments doivent être placés en mémoire l’un à côté de l’autre, dans l’ordre croissant de leur indice, en commençant à zéro. Pour qu’un tableau multidimensionnel soit C-contigu, le dernier indice doit être celui qui varie le plus rapidement lors du parcours de ses éléments dans l’ordre de leur adresse mémoire. À l'inverse, dans les tableaux Fortran-contigu, c’est le premier indice qui doit varier le plus rapidement.
coroutine¶
    
Les coroutines sont une forme généralisée des fonctions. On entre dans une fonction en un point et on en sort en un autre point. On peut entrer, sortir et reprendre l'exécution d'une coroutine en plusieurs points. Elles peuvent être implémentées en utilisant l'instruction `async def`. Voir aussi la **PEP 492**.
fonction coroutine¶
    
Fonction qui renvoie un objet coroutine. Une fonction coroutine peut être définie par l'instruction `async def` et peut contenir les mots clés `await`, `async for` ainsi que `async with`. A été introduit par la **PEP 492**.
CPython¶
    
L'implémentation canonique du langage de programmation Python, tel que distribué sur python.org. Le terme "CPython" est utilisé dans certains contextes lorsqu'il est nécessaire de distinguer cette implémentation des autres comme _Jython_ ou _IronPython_.
current context¶
    
The context (`contextvars.Context` object) that is currently used by `ContextVar` objects to access (get or set) the values of context variables. Each thread has its own current context. Frameworks for executing asynchronous tasks (see `asyncio`) associate each task with a context which becomes the current context whenever the task starts or resumes execution.
décorateur¶
    
Fonction dont la valeur de retour est une autre fonction. Un décorateur est habituellement utilisé pour transformer une fonction via la syntaxe `@wrapper`, dont les exemples typiques sont : `classmethod()` et `staticmethod()`.
La syntaxe des décorateurs est simplement du sucre syntaxique, les définitions des deux fonctions suivantes sont sémantiquement équivalentes :
```
deff(arg):
  ...
f = staticmethod(f)
@staticmethod
deff(arg):
  ...

```

Quoique moins fréquemment utilisé, le même concept existe pour les classes. Consultez la documentation définitions de fonctions et définitions de classes pour en savoir plus sur les décorateurs.
descripteur¶
    
Any object which defines the methods `__get__()`, `__set__()`, or `__delete__()`. When a class attribute is a descriptor, its special binding behavior is triggered upon attribute lookup. Normally, using _a.b_ to get, set or delete an attribute looks up the object named _b_ in the class dictionary for _a_ , but if _b_ is a descriptor, the respective descriptor method gets called. Understanding descriptors is a key to a deep understanding of Python because they are the basis for many features including functions, methods, properties, class methods, static methods, and reference to super classes.
Pour plus d'informations sur les méthodes des descripteurs, consultez Implémentation de descripteurs ou le guide pour l'utilisation des descripteurs.
dictionnaire¶
    
An associative array, where arbitrary keys are mapped to values. The keys can be any object with `__hash__()` and `__eq__()` methods. Called a hash in Perl.
dictionnaire en compréhension (ou dictionnaire en intension)¶
    
Écriture concise pour traiter tout ou partie des éléments d'un itérable et renvoyer un dictionnaire contenant les résultats. `results = {n: n ** 2 for n in range(10)}` génère un dictionnaire contenant des clés `n` liées à leurs valeurs `n ** 2`. Voir compréhensions.
vue de dictionnaire¶
    
Objets retournés par les méthodes `dict.keys()`, `dict.values()` et `dict.items()`. Ils fournissent des vues dynamiques des entrées du dictionnaire, ce qui signifie que lorsque le dictionnaire change, la vue change. Pour transformer une vue en vraie liste, utilisez `list(dictview)`. Voir Les vues de dictionnaires.
chaîne de documentation (_docstring_)¶
    
A string literal which appears as the first expression in a class, function or module. While ignored when the suite is executed, it is recognized by the compiler and put into the `__doc__` attribute of the enclosing class, function or module. Since it is available via introspection, it is the canonical place for documentation of the object.
typage canard (_duck-typing_)¶
    
Style de programmation qui ne prend pas en compte le type d'un objet pour déterminer s'il respecte une interface, mais qui appelle simplement la méthode ou l'attribut (_Si ça a un bec et que ça cancane, ça doit être un canard_ , _duck_ signifie canard en anglais). En se concentrant sur les interfaces plutôt que les types, du code bien construit améliore sa flexibilité en autorisant des substitutions polymorphiques. Le _duck-typing_ évite de vérifier les types via `type()` ou `isinstance()`, Notez cependant que le _duck-typing_ peut travailler de pair avec les classes mère abstraites. À la place, le _duck-typing_ utilise plutôt `hasattr()` ou la programmation EAFP.
EAFP¶
    
Il est plus simple de demander pardon que demander la permission (_Easier to Ask for Forgiveness than Permission_ en anglais). Ce style de développement Python fait l'hypothèse que le code est valide et traite les exceptions si cette hypothèse s'avère fausse. Ce style, propre et efficace, est caractérisé par la présence de beaucoup de mots clés `try` et `except`. Cette technique de programmation contraste avec le style LBYL utilisé couramment dans les langages tels que C.
expression¶
    
Suite logique de termes et chiffres conformes à la syntaxe Python dont l'évaluation fournit une valeur. En d'autres termes, une expression est une suite d'éléments tels que des noms, opérateurs, littéraux, accès d'attributs, méthodes ou fonctions qui aboutissent à une valeur. Contrairement à beaucoup d'autres langages, les différentes constructions du langage ne sont pas toutes des expressions. On trouve également des instructions qui ne peuvent pas être utilisées comme expressions, tel que `while`. Les affectations sont également des instructions et non des expressions.
module d'extension¶
    
Module écrit en C ou C++, utilisant l'API C de Python pour interagir avec Python et le code de l'utilisateur.
f-string¶
    
Chaîne littérale préfixée de `'f'` ou `'F'`. Les "f-strings" sont un raccourci pour formatted string literals. Voir la **PEP 498**.
objet fichier¶
    
An object exposing a file-oriented API (with methods such as `read()` or `write()`) to an underlying resource. Depending on the way it was created, a file object can mediate access to a real on-disk file or to another type of storage or communication device (for example standard input/output, in-memory buffers, sockets, pipes, etc.). File objects are also called _file-like objects_ or _streams_.
Il existe en réalité trois catégories de fichiers objets : les fichiers binaires bruts, les fichiers binaires avec tampon (_buffer_) et les fichiers textes. Leurs interfaces sont définies dans le module `io`. Le moyen le plus simple et direct de créer un objet fichier est d'utiliser la fonction `open()`.
objet fichier-compatible¶
    
Synonyme de objet fichier.
encodage du système de fichiers et gestionnaire d'erreurs associé¶
    
Encodage et gestionnaire d'erreurs utilisés par Python pour décoder les octets fournis par le système d'exploitation et encoder les chaînes de caractères Unicode afin de les passer au système.
L'encodage du système de fichiers doit impérativement pouvoir décoder tous les octets jusqu'à 128. Si ce n'est pas le cas, certaines fonctions de l'API lèvent `UnicodeError`.
Cet encodage et son gestionnaire d'erreur peuvent être obtenus à l'aide des fonctions `sys.getfilesystemencoding()` et `sys.getfilesystemencodeerrors()`.
L'encodage du système de fichiers et gestionnaire d'erreurs associé sont configurés au démarrage de Python par la fonction `PyConfig_Read()` : regardez `filesystem_encoding` et `filesystem_errors` dans les membres de `PyConfig`.
Voir aussi encodage régional.
chercheur¶
    
Objet qui essaie de trouver un chargeur pour le module en cours d'importation.
There are two types of finder: meta path finders for use with `sys.meta_path`, and path entry finders for use with `sys.path_hooks`.
See Chercheurs et chargeurs and `importlib` for much more detail.
division entière¶
    
Division mathématique arrondissant à l'entier inférieur. L'opérateur de la division entière est `//`. Par exemple l'expression `11 // 4` vaut `2`, contrairement à `11 / 4` qui vaut `2.75`. Notez que `(-11) // 4` vaut `-3` car l'arrondi se fait à l'entier inférieur. Voir la **PEP 328**.
free threading¶
    
A threading model where multiple threads can run Python bytecode simultaneously within the same interpreter. This is in contrast to the global interpreter lock which allows only one thread to execute Python bytecode at a time. See **PEP 703**.
free variable¶
    
Formally, as defined in the language execution model, a free variable is any variable used in a namespace which is not a local variable in that namespace. See closure variable for an example. Pragmatically, due to the name of the `codeobject.co_freevars` attribute, the term is also sometimes used as a synonym for closure variable.
fonction¶
    
Suite d'instructions qui renvoie une valeur à son appelant. On peut lui passer des arguments qui pourront être utilisés dans le corps de la fonction. Voir aussi paramètre, méthode et Définition de fonctions.
annotation de fonction¶
    
annotation d'un paramètre de fonction ou valeur de retour.
Les annotations de fonctions sont généralement utilisées pour des indications de types : par exemple, cette fonction devrait prendre deux arguments `int` et devrait également avoir une valeur de retour de type `int` :
```
defsum_two_numbers(a: int, b: int) -> int:
  return a + b

```

L'annotation syntaxique de la fonction est expliquée dans la section Définition de fonctions.
Voir annotation de variable et la **PEP 484**, qui décrivent cette fonctionnalité. Voir aussi Bonnes pratiques concernant les annotations sur les bonnes pratiques concernant les annotations.
__future__¶
    
Une importation depuis le futur s'écrit `from __future__ import <fonctionnalité>`. Lorsqu'une importation du futur est active dans un module, Python compile ce module avec une certaine modification de la syntaxe ou du comportement qui est vouée à devenir standard dans une version ultérieure. Le module `__future__` documente les possibilités pour _fonctionnalité_. L'importation a aussi l'effet normal d'importer une variable du module. Cette variable contient des informations utiles sur la fonctionnalité en question, notamment la version de Python dans laquelle elle a été ajoutée, et celle dans laquelle elle deviendra standard :
>>>```
>>> import__future__
>>> __future__.division
_Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)

```

ramasse-miettes¶
    
(_garbage collection_ en anglais) Mécanisme permettant de libérer de la mémoire lorsqu'elle n'est plus utilisée. Python utilise un ramasse-miettes par comptage de référence et un ramasse-miettes cyclique capable de détecter et casser les références circulaires. Le ramasse-miettes peut être contrôlé en utilisant le module `gc`.
générateur¶
    
Fonction qui renvoie un itérateur de générateur. Cela ressemble à une fonction normale, en dehors du fait qu'elle contient une ou des expressions `yield` produisant une série de valeurs utilisable dans une boucle _for_ ou récupérées une à une via la fonction `next()`.
Fait généralement référence à une fonction génératrice mais peut faire référence à un _itérateur de générateur_ dans certains contextes. Dans les cas où le sens voulu n'est pas clair, utiliser les termes complets lève l’ambiguïté.
itérateur de générateur¶
    
Objet créé par une fonction générateur.
Each `yield` temporarily suspends processing, remembering the execution state (including local variables and pending try-statements). When the _generator iterator_ resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).
expression génératrice¶
    
An expression that returns an iterator. It looks like a normal expression followed by a `for` clause defining a loop variable, range, and an optional `if` clause. The combined expression generates values for an enclosing function:
>>>```
>>> sum(i*i for i in range(10))     # sum of squares 0, 1, 4, ... 81
285

```

fonction générique¶
    
Fonction composée de plusieurs fonctions implémentant les mêmes opérations pour différents types. L'implémentation à utiliser est déterminée lors de l'appel par l'algorithme de répartition.
Voir aussi single dispatch, le décorateur `functools.singledispatch()` et la **PEP 443**.
type générique¶
    
Un type qui peut être paramétré ; généralement un conteneur comme `list` ou `dict`. Utilisé pour les indications de type et les annotations.
Pour plus de détails, voir types alias génériques et le module `typing`. On trouvera l'historique de cette fonctionnalité dans les **PEP 483**, **PEP 484** et **PEP 585**.
GIL¶
    
Voir global interpreter lock.
verrou global de l'interpréteur¶
    
(_global interpreter lock_ en anglais) Mécanisme utilisé par l'interpréteur CPython pour s'assurer qu'un seul fil d'exécution (_thread_ en anglais) n'exécute le bytecode à la fois. Cela simplifie l'implémentation de CPython en rendant le modèle objet (incluant des parties critiques comme la classe native `dict`) implicitement protégé contre les accès concourants. Verrouiller l'interpréteur entier rend plus facile l'implémentation de multiples fils d'exécution (_multi-thread_ en anglais), au détriment malheureusement de beaucoup du parallélisme possible sur les machines ayant plusieurs processeurs.
Cependant, certains modules d'extension, standards ou non, sont conçus de manière à libérer le GIL lorsqu'ils effectuent des tâches lourdes tel que la compression ou le hachage. De la même manière, le GIL est toujours libéré lors des entrées-sorties.
As of Python 3.13, the GIL can be disabled using the `--disable-gil` build configuration. After building Python with this option, code must be run with `-X gil=0` or after setting the `PYTHON_GIL=0` environment variable. This feature enables improved performance for multi-threaded applications and makes it easier to use multi-core CPUs efficiently. For more details, see **PEP 703**.
_pyc_ utilisant le hachage¶
    
Un fichier de cache de code intermédiaire (_bytecode_ en anglais) qui utilise le hachage plutôt que l'heure de dernière modification du fichier source correspondant pour déterminer sa validité. Voir Invalidation de bytecode mis en cache.
hachable¶
    
An object is _hashable_ if it has a hash value which never changes during its lifetime (it needs a `__hash__()` method), and can be compared to other objects (it needs an `__eq__()` method). Hashable objects which compare equal must have the same hash value.
La hachabilité permet à un objet d'être utilisé comme clé de dictionnaire ou en tant que membre d'un ensemble (type _set_), car ces structures de données utilisent ce _hash_.
La plupart des types immuables natifs de Python sont hachables, mais les conteneurs mutables (comme les listes ou les dictionnaires) ne le sont pas ; les conteneurs immuables (comme les n-uplets ou les ensembles figés) ne sont hachables que si leurs éléments sont hachables. Les instances de classes définies par les utilisateurs sont hachables par défaut. Elles sont toutes considérées différentes (sauf avec elles-mêmes) et leur valeur de hachage est calculée à partir de leur `id()`.
IDLE¶
    
Environnement d'apprentissage et de développement intégré pour Python. IDLE est un éditeur basique et un interpréteur livré avec la distribution standard de Python.
immortal¶
    
 _Immortal objects_ are a CPython implementation detail introduced in **PEP 683**.
If an object is immortal, its reference count is never modified, and therefore it is never deallocated while the interpreter is running. For example, `True` and `None` are immortal in CPython.
immuable¶
    
Objet dont la valeur ne change pas. Les nombres, les chaînes et les _n_ -uplets sont immuables. Ils ne peuvent être modifiés. Un nouvel objet doit être créé si une valeur différente doit être stockée. Ils jouent un rôle important quand une valeur de _hash_ constante est requise, typiquement en clé de dictionnaire.
chemin des importations¶
    
Liste de entrées dans lesquelles le chercheur basé sur les chemins cherche les modules à importer. Typiquement, lors d'une importation, cette liste vient de `sys.path` ; pour les sous-paquets, elle peut aussi venir de l'attribut `__path__` du paquet parent.
importation¶
    
Processus rendant le code Python d'un module disponible dans un autre.
importateur¶
    
Objet qui trouve et charge un module, en même temps un chercheur et un chargeur.
interactif¶
    
Python has an interactive interpreter which means you can enter statements and expressions at the interpreter prompt, immediately execute them and see their results. Just launch `python` with no arguments (possibly by selecting it from your computer's main menu). It is a very powerful way to test out new ideas or inspect modules and packages (remember `help(x)`). For more on interactive mode, see Mode interactif.
interprété¶
    
Python est un langage interprété, en opposition aux langages compilés, bien que la frontière soit floue en raison de la présence d'un compilateur en code intermédiaire. Cela signifie que les fichiers sources peuvent être exécutés directement, sans avoir à compiler un fichier exécutable intermédiaire. Les langages interprétés ont généralement un cycle de développement / débogage plus court que les langages compilés. Cependant, ils s'exécutent généralement plus lentement. Voir aussi interactif.
arrêt de l'interpréteur¶
    
Lorsqu'on lui demande de s'arrêter, l'interpréteur Python entre dans une phase spéciale où il libère graduellement les ressources allouées, comme les modules ou quelques structures de données internes. Il fait aussi quelques appels au ramasse-miettes. Cela peut déclencher l'exécution de code dans des destructeurs ou des fonctions de rappels de _weakrefs_. Le code exécuté lors de l'arrêt peut rencontrer des exceptions puisque les ressources auxquelles il fait appel sont susceptibles de ne plus fonctionner, (typiquement les modules des bibliothèques ou le mécanisme de _warning_).
La principale raison d'arrêt de l'interpréteur est que le module `__main__` ou le script en cours d'exécution a terminé de s'exécuter.
itérable¶
    
An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as `list`, `str`, and `tuple`) and some non-sequence types like `dict`, file objects, and objects of any classes you define with an `__iter__()` method or with a `__getitem__()` method that implements sequence semantics.
Iterables can be used in a `for` loop and in many other places where a sequence is needed (`zip()`, `map()`, ...). When an iterable object is passed as an argument to the built-in function `iter()`, it returns an iterator for the object. This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call `iter()` or deal with iterator objects yourself. The `for` statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. See also iterator, sequence, and generator.
itérateur¶
    
An object representing a stream of data. Repeated calls to the iterator's `__next__()` method (or passing it to the built-in function `next()`) return successive items in the stream. When no more data are available a `StopIteration` exception is raised instead. At this point, the iterator object is exhausted and any further calls to its `__next__()` method just raise `StopIteration` again. Iterators are required to have an `__iter__()` method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a `list`) produces a fresh new iterator each time you pass it to the `iter()` function or use it in a `for` loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.
Vous trouverez davantage d'informations dans Les types itérateurs.
**Particularité de l'implémentation CPython :** CPython does not consistently apply the requirement that an iterator define `__iter__()`. And also please note that the free-threading CPython does not guarantee the thread-safety of iterator operations.
fonction clé¶
    
Une fonction clé est un objet appelable qui renvoie une valeur à fins de tri ou de classement. Par exemple, la fonction `locale.strxfrm()` est utilisée pour générer une clé de classement prenant en compte les conventions de classement spécifiques aux paramètres régionaux courants.
Plusieurs outils dans Python acceptent des fonctions clés pour déterminer comment les éléments sont classés ou groupés. On peut citer les fonctions `min()`, `max()`, `sorted()`, `list.sort()`, `heapq.merge()`, `heapq.nsmallest()`, `heapq.nlargest()` et `itertools.groupby()`.
Il existe plusieurs moyens de créer une fonction clé. Par exemple, la méthode `str.lower()` peut servir de fonction clé pour effectuer des recherches insensibles à la casse. Aussi, il est possible de créer des fonctions clés avec des expressions `lambda`, comme `lambda r: (r[0], r[2])`. Par ailleurs `attrgetter()`, `itemgetter()` et `methodcaller()` permettent de créer des fonctions clés. Voir le guide pour le tri pour des exemples de création et d'utilisation de fonctions clefs.
argument nommé¶
    
Voir argument.
lambda¶
    
Fonction anonyme sous la forme d'une expression et ne contenant qu'une seule expression, exécutée lorsque la fonction est appelée. La syntaxe pour créer des fonctions lambda est : `lambda [parameters]: expression`
LBYL¶
    
Regarde avant de sauter, (_Look before you leap_ en anglais). Ce style de programmation consiste à vérifier des conditions avant d'effectuer des appels ou des accès. Ce style contraste avec le style EAFP et se caractérise par la présence de beaucoup d'instructions `if`.
Dans un environnement avec plusieurs fils d'exécution (_multi-threaded_ en anglais), le style _LBYL_ peut engendrer un séquencement critique (_race condition_ en anglais) entre le "regarde" et le "sauter". Par exemple, le code `if key in mapping: return mapping[key]` peut échouer si un autre fil d'exécution supprime la clé _key_ du _mapping_ après le test mais avant l'accès. Ce problème peut être résolu avec des verrous (_locks_) ou avec l'approche EAFP.
liste¶
    
A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list since access to elements is _O_(1).
liste en compréhension (ou liste en intension)¶
    
Écriture concise pour manipuler tout ou partie des éléments d'une séquence et renvoyer une liste contenant les résultats. `result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0]` génère la liste composée des nombres pairs de 0 à 255 écrits sous formes de chaînes de caractères et en hexadécimal (`0x…`). La clause `if` est optionnelle. Si elle est omise, tous les éléments du `range(256)` seront utilisés.
chargeur¶
    
An object that loads a module. It must define the `exec_module()` and `create_module()` methods to implement the `Loader` interface. A loader is typically returned by a finder. See also:
  * Chercheurs et chargeurs
  * `importlib.abc.Loader`
  * **PEP 302**


encodage régional¶
    
Sous Unix, il est défini par la variable régionale LC_CTYPE. Il peut être modifié par `locale.setlocale(locale.LC_CTYPE, new_locale)`.
Sous Windows, c'est un encodage ANSI (par ex. : `"cp1252"`).
Sous Android et VxWorks, Python utilise `"utf-8"` comme encodage régional.
`locale.getencoding()` can be used to get the locale encoding.
Voir aussi l'encodage du systèmes de fichiers et gestionnaire d'erreurs associé.
méthode magique¶
    
Un synonyme informel de special method.
tableau de correspondances (_mapping_ en anglais)¶
    
Conteneur permettant de rechercher des éléments à partir de clés et implémentant les méthodes spécifiées dans les classes mères abstraites des `tableaux de correspondances` (immuables) ou `tableaux de correspondances mutables` (voir les classes mères abstraites). Les classes suivantes sont des exemples de tableaux de correspondances : `dict`, `collections.defaultdict`, `collections.OrderedDict` et `collections.Counter`.
chercheur dans les méta-chemins¶
    
Un chercheur renvoyé par une recherche dans `sys.meta_path`. Les chercheurs dans les méta-chemins ressemblent, mais sont différents des chercheurs d'entrée dans path.
Voir `importlib.abc.MetaPathFinder` pour les méthodes que les chercheurs dans les méta-chemins doivent implémenter.
métaclasse¶
    
Classe d'une classe. Les définitions de classe créent un nom pour la classe, un dictionnaire de classe et une liste de classes parentes. La métaclasse a pour rôle de réunir ces trois paramètres pour construire la classe. La plupart des langages orientés objet fournissent une implémentation par défaut. La particularité de Python est la possibilité de créer des métaclasses personnalisées. La plupart des utilisateurs n'auront jamais besoin de cet outil, mais lorsque le besoin survient, les métaclasses offrent des solutions élégantes et puissantes. Elles sont utilisées pour journaliser les accès à des propriétés, rendre sûrs les environnements _multi-threads_ , suivre la création d'objets, implémenter des singletons et bien d'autres tâches.
Plus d'informations sont disponibles dans : Métaclasses.
méthode¶
    
Fonction définie à l'intérieur d'une classe. Lorsqu'elle est appelée comme un attribut d'une instance de cette classe, la méthode reçoit l'instance en premier argument (qui, par convention, est habituellement nommé `self`). Voir function et nested scope.
ordre de résolution des méthodes¶
    
Method Resolution Order is the order in which base classes are searched for a member during lookup. See The Python 2.3 Method Resolution Order for details of the algorithm used by the Python interpreter since the 2.3 release.
module¶
    
Objet utilisé pour organiser une portion unitaire de code en Python. Les modules ont un espace de nommage et peuvent contenir n'importe quels objets Python. Charger des modules est appelé importer.
Voir aussi paquet.
spécificateur de module¶
    
Espace de nommage contenant les informations, relatives à l'importation, utilisées pour charger un module. C'est une instance de la classe `importlib.machinery.ModuleSpec`.
See also Spécificateurs de modules.
MRO¶
    
Voir ordre de résolution des méthodes.
mutable¶
    
Un objet mutable peut changer de valeur tout en gardant le même `id()`. Voir aussi immuable.
_n_ -uplet nommé¶
    
Le terme "n-uplet nommé" s'applique à tous les types ou classes qui héritent de la classe `tuple` et dont les éléments indexables sont aussi accessibles en utilisant des attributs nommés. Les types et classes peuvent avoir aussi d'autres caractéristiques.
Plusieurs types natifs sont appelés n-uplets, y compris les valeurs retournées par `time.localtime()` et `os.stat()`. Un autre exemple est `sys.float_info` :
>>>```
>>> sys.float_info[1]          # indexed access
1024
>>> sys.float_info.max_exp       # named field access
1024
>>> isinstance(sys.float_info, tuple)  # kind of tuple
True

```

Some named tuples are built-in types (such as the above examples). Alternatively, a named tuple can be created from a regular class definition that inherits from `tuple` and that defines named fields. Such a class can be written by hand, or it can be created by inheriting `typing.NamedTuple`, or with the factory function `collections.namedtuple()`. The latter techniques also add some extra methods that may not be found in hand-written or built-in named tuples.
espace de nommage¶
    
L'endroit où une variable est stockée. Les espaces de nommage sont implémentés avec des dictionnaires. Il existe des espaces de nommage globaux, natifs ou imbriqués dans les objets (dans les méthodes). Les espaces de nommage favorisent la modularité car ils permettent d'éviter les conflits de noms. Par exemple, les fonctions `builtins.open` et `os.open()` sont différenciées par leurs espaces de nom. Les espaces de nommage aident aussi à la lisibilité et la maintenabilité en rendant clair quel module implémente une fonction. Par exemple, écrire `random.seed()` ou `itertools.islice()` affiche clairement que ces fonctions sont implémentées respectivement dans les modules `random` et `itertools`.
paquet-espace de nommage¶
    
A package which serves only as a container for subpackages. Namespace packages may have no physical representation, and specifically are not like a regular package because they have no `__init__.py` file.
Namespace packages allow several individually installable packages to have a common parent package. Otherwise, it is recommended to use a regular package.
For more information, see **PEP 420** and Paquets espaces de nommage.
Voir aussi module.
portée imbriquée¶
    
Possibilité de faire référence à une variable déclarée dans une définition englobante. Typiquement, une fonction définie à l'intérieur d'une autre fonction a accès aux variables de cette dernière. Souvenez-vous cependant que cela ne fonctionne que pour accéder à des variables, pas pour les assigner. Les variables locales sont lues et assignées dans l'espace de nommage le plus proche. Tout comme les variables globales qui sont stockés dans l'espace de nommage global, le mot clef `nonlocal` permet d'écrire dans l'espace de nommage dans lequel est déclarée la variable.
nouvelle classe¶
    
Old name for the flavor of classes now used for all class objects. In earlier Python versions, only new-style classes could use Python's newer, versatile features like `__slots__`, descriptors, properties, `__getattribute__()`, class methods, and static methods.
objet¶
    
N'importe quelle donnée comportant des états (sous forme d'attributs ou d'une valeur) et un comportement (des méthodes). C'est aussi (`object`) l'ancêtre commun à absolument toutes les nouvelles classes.
optimized scope¶
    
A scope where target local variable names are reliably known to the compiler when the code is compiled, allowing optimization of read and write access to these names. The local namespaces for functions, generators, coroutines, comprehensions, and generator expressions are optimized in this fashion. Note: most interpreter optimizations are applied to all scopes, only those relying on a known set of local and nonlocal variable names are restricted to optimized scopes.
paquet¶
    
module Python qui peut contenir des sous-modules ou des sous-paquets. Techniquement, un paquet est un module qui possède un attribut `__path__`.
Voir aussi paquet classique et namespace package.
paramètre¶
    
Entité nommée dans la définition d'une fonction (ou méthode), décrivant un argument (ou dans certains cas des arguments) que la fonction accepte. Il existe cinq sortes de paramètres :
  * _positional-or-keyword_ : l'argument peut être passé soit par sa position, soit en tant que argument nommé. C'est le type de paramètre par défaut. Par exemple, _foo_ et _bar_ dans l'exemple suivant :
```
deffunc(foo, bar=None): ...

```



  * _positional-only_ : définit un argument qui ne peut être fourni que par position. Les paramètres _positional-only_ peuvent être définis en insérant un caractère "/" dans la liste de paramètres de la définition de fonction après eux. Par exemple : _posonly1_ et _posonly2_ dans le code suivant :
```
deffunc(posonly1, posonly2, /, positional_or_keyword): ...

```



  * _keyword-only_ : l'argument ne peut être fourni que nommé. Les paramètres _keyword-only_ peuvent être définis en utilisant un seul paramètre _var-positional_ , ou en ajoutant une étoile (`*`) seule dans la liste des paramètres avant eux. Par exemple, _kw_only1_ et _kw_only2_ dans le code suivant :
```
deffunc(arg, *, kw_only1, kw_only2): ...

```

  * _var-positional_ : une séquence d'arguments positionnels peut être fournie (en plus de tous les arguments positionnels déjà acceptés par d'autres paramètres). Un tel paramètre peut être défini en préfixant son nom par une `*`. Par exemple _args_ ci-après :
```
deffunc(*args, **kwargs): ...

```

  * _var-keyword_ : une quantité arbitraire d'arguments peut être passée, chacun étant nommé (en plus de tous les arguments nommés déjà acceptés par d'autres paramètres). Un tel paramètre est défini en préfixant le nom du paramètre par `**`. Par exemple, _kwargs_ ci-dessus.


Les paramètres peuvent spécifier des arguments obligatoires ou optionnels, ainsi que des valeurs par défaut pour les arguments optionnels.
Voir aussi argument dans le glossaire, la question sur la différence entre les arguments et les paramètres dans la FAQ, la classe `inspect.Parameter`, la section Définition de fonctions et la **PEP 362**.
entrée de chemin¶
    
Emplacement dans le chemin des importations (_import path_ en anglais, d'où le _path_) que le chercheur basé sur les chemins consulte pour trouver des modules à importer.
chercheur de chemins¶
    
chercheur renvoyé par un appelable sur un `sys.path_hooks` (c'est-à-dire un point d'entrée pour la recherche dans path) qui sait où trouver des modules lorsqu'on lui donne une entrée de path.
Voir `importlib.abc.PathEntryFinder` pour les méthodes qu'un chercheur d'entrée dans _path_ doit implémenter.
point d'entrée pour la recherche dans _path_¶
    
A callable on the `sys.path_hooks` list which returns a path entry finder if it knows how to find modules on a specific path entry.
chercheur basé sur les chemins¶
    
L'un des chercheurs dans les méta-chemins par défaut qui cherche des modules dans un chemin des importations.
objet simili-chemin¶
    
Objet représentant un chemin du système de fichiers. Un objet simili-chemin est un objet `str` ou un objet `bytes` représentant un chemin ou un objet implémentant le protocole `os.PathLike`. Un objet qui accepte le protocole `os.PathLike` peut être converti en un chemin `str` ou `bytes` du système de fichiers en appelant la fonction `os.fspath()`. `os.fsdecode()` et `os.fsencode()` peuvent être utilisées, respectivement, pour garantir un résultat de type `str` ou `bytes` à la place. A été Introduit par la **PEP 519**.
PEP¶
    
 _Python Enhancement Proposal_ (Proposition d'amélioration de Python). Une PEP est un document de conception fournissant des informations à la communauté Python ou décrivant une nouvelle fonctionnalité pour Python, ses processus ou son environnement. Les PEP doivent fournir une spécification technique concise et une justification des fonctionnalités proposées.
Les PEP sont censées être les principaux mécanismes pour proposer de nouvelles fonctionnalités majeures, pour recueillir les commentaires de la communauté sur une question et pour documenter les décisions de conception qui sont intégrées en Python. L’auteur du PEP est responsable de l’établissement d’un consensus au sein de la communauté et de documenter les opinions contradictoires.
Voir la **PEP 1**.
portion¶
    
Jeu de fichiers dans un seul dossier (pouvant être stocké sous forme de fichier zip) qui contribue à l'espace de nommage d'un paquet, tel que défini dans la **PEP 420**.
argument positionnel¶
    
Voir argument.
API provisoire¶
    
Une API provisoire est une API qui n'offre aucune garantie de rétrocompatibilité (la bibliothèque standard exige la rétrocompatibilité). Bien que des changements majeurs d'une telle interface ne soient pas attendus, tant qu'elle est étiquetée provisoire, des changements cassant la rétrocompatibilité (y compris sa suppression complète) peuvent survenir si les développeurs principaux le jugent nécessaire. Ces modifications ne surviendront que si de sérieux problèmes sont découverts et qu'ils n'avaient pas été identifiés avant l'ajout de l'API.
Même pour les API provisoires, les changements cassant la rétrocompatibilité sont considérés comme des "solutions de dernier recours". Tout ce qui est possible sera fait pour tenter de résoudre les problèmes en conservant la rétrocompatibilité.
Ce processus permet à la bibliothèque standard de continuer à évoluer avec le temps, sans se bloquer longtemps sur des erreurs d'architecture. Voir la **PEP 411** pour plus de détails.
paquet provisoire¶
    
Voir provisional API.
Python 3000¶
    
Surnom donné à la série des Python 3.x (très vieux surnom donné à l'époque où Python 3 représentait un futur lointain). Aussi abrégé _Py3k_.
_Pythonique_¶
    
Idée, ou bout de code, qui colle aux idiomes de Python plutôt qu'aux concepts communs rencontrés dans d'autres langages. Par exemple, il est idiomatique en Python de parcourir les éléments d'un itérable en utilisant `for`. Beaucoup d'autres langages n'ont pas cette possibilité, donc les gens qui ne sont pas habitués à Python utilisent parfois un compteur numérique à la place :
```
for i in range(len(food)):
  print(food[i])

```

Plutôt qu'utiliser la méthode, plus propre et élégante, donc _Pythonique_ :
```
for piece in food:
  print(piece)

```

nom qualifié¶
    
Nom, comprenant des points, montrant le "chemin" de l'espace de nommage global d'un module vers une classe, fonction ou méthode définie dans ce module, tel que défini dans la **PEP 3155**. Pour les fonctions et classes de premier niveau, le nom qualifié est le même que le nom de l'objet :
>>>```
>>> classC:
...   classD:
...     defmeth(self):
...       pass
...
>>> C.__qualname__
'C'
>>> C.D.__qualname__
'C.D'
>>> C.D.meth.__qualname__
'C.D.meth'

```

Lorsqu'il est utilisé pour nommer des modules, le _nom qualifié complet_ (_fully qualified name - FQN_ en anglais) signifie le chemin complet (séparé par des points) vers le module, incluant tous les paquets parents. Par exemple : `email.mime.text` :
>>>```
>>> importemail.mime.text
>>> email.mime.text.__name__
'email.mime.text'

```

nombre de références¶
    
The number of references to an object. When the reference count of an object drops to zero, it is deallocated. Some objects are immortal and have reference counts that are never modified, and therefore the objects are never deallocated. Reference counting is generally not visible to Python code, but it is a key element of the CPython implementation. Programmers can call the `sys.getrefcount()` function to return the reference count for a particular object.
paquet classique¶
    
paquet traditionnel, tel qu'un dossier contenant un fichier `__init__.py`.
Voir aussi paquet-espace de nommage.
REPL¶
    
An acronym for the "read–eval–print loop", another name for the interactive interpreter shell.
__slots__¶
    
Déclaration dans une classe qui économise de la mémoire en pré-allouant de l'espace pour les attributs des instances et qui élimine le dictionnaire (des attributs) des instances. Bien que populaire, cette technique est difficile à maîtriser et devrait être réservée à de rares cas où un grand nombre d'instances dans une application devient un sujet critique pour la mémoire.
séquence¶
    
An iterable which supports efficient element access using integer indices via the `__getitem__()` special method and defines a `__len__()` method that returns the length of the sequence. Some built-in sequence types are `list`, `str`, `tuple`, and `bytes`. Note that `dict` also supports `__getitem__()` and `__len__()`, but is considered a mapping rather than a sequence because the lookups use arbitrary hashable keys rather than integers.
The `collections.abc.Sequence` abstract base class defines a much richer interface that goes beyond just `__getitem__()` and `__len__()`, adding `count()`, `index()`, `__contains__()`, and `__reversed__()`. Types that implement this expanded interface can be registered explicitly using `register()`. For more documentation on sequence methods generally, see Common Sequence Operations.
ensemble en compréhension (ou ensemble en intension)¶
    
Une façon compacte de traiter tout ou partie des éléments d'un itérable et de renvoyer un _set_ avec les résultats. `results = {c for c in 'abracadabra' if c not in 'abc'}` génère l'ensemble contenant les lettres « r » et « d » `{'r', 'd'}`. Voir Agencements des listes, ensembles et dictionnaires.
distribution simple¶
    
Forme de distribution, comme les fonction génériques, où l'implémentation est choisie en fonction du type d'un seul argument.
tranche¶
    
(_slice_ en anglais), un objet contenant habituellement une portion de séquence. Une tranche est créée en utilisant la notation `[]` avec des `:` entre les nombres lorsque plusieurs sont fournis, comme dans `variable_name[1:3:5]`. Cette notation utilise des objets `slice` en interne.
soft deprecated¶
    
A soft deprecated API should not be used in new code, but it is safe for already existing code to use it. The API remains documented and tested, but will not be enhanced further.
Soft deprecation, unlike normal deprecation, does not plan on removing the API and will not emit warnings.
See PEP 387: Soft Deprecation.
méthode spéciale¶
    
(_special method_ en anglais) Méthode appelée implicitement par Python pour exécuter une opération sur un type, comme une addition. De telles méthodes ont des noms commençant et terminant par des doubles tirets bas. Les méthodes spéciales sont documentées dans Méthodes spéciales.
instruction¶
    
Une instruction (_statement_ en anglais) est un composant d'un "bloc" de code. Une instruction est soit une expression, soit une ou plusieurs constructions basées sur un mot-clé, comme `if`, `while` ou `for`.
static type checker¶
    
An external tool that reads Python code and analyzes it, looking for issues such as incorrect types. See also type hints and the `typing` module.
référence forte¶
    
In Python's C API, a strong reference is a reference to an object which is owned by the code holding the reference. The strong reference is taken by calling `Py_INCREF()` when the reference is created and released with `Py_DECREF()` when the reference is deleted.
Une référence forte est créée à l'aide de la fonction `Py_NewRef()`. Il faut normalement appeler `Py_DECREF()` dessus avant de sortir de sa portée lexicale, sans quoi il y a une fuite de référence.
Voir aussi référence empruntée.
encodages de texte¶
    
Une chaîne de caractères en Python est une suite de points de code Unicode (dans l'intervalle `U+0000`--`U+10FFFF`). Pour stocker ou transmettre une chaîne, il est nécessaire de la sérialiser en suite d'octets.
Sérialiser une chaîne de caractères en une suite d'octets s'appelle « encoder » et recréer la chaîne à partir de la suite d'octets s'appelle « décoder ».
Il existe de multiples codecs pour la sérialisation de texte, que l'on regroupe sous l'expression « encodages de texte ».
fichier texte¶
    
Objet fichier capable de lire et d'écrire des objets `str`. Souvent, un fichier texte (_text file_ en anglais) accède en fait à un flux de donnée en octets et gère l'encodage de texte automatiquement. Des exemples de fichiers textes sont les fichiers ouverts en mode texte (`'r'` ou `'w'`), `sys.stdin`, `sys.stdout` et les instances de `io.StringIO`.
Voir aussi fichier binaire pour un objet fichier capable de lire et d'écrire des objets octets-compatibles.
chaîne entre triple guillemets¶
    
Chaîne qui est délimitée par trois guillemets simples (`'`) ou trois guillemets doubles (`"`). Bien qu'elle ne fournisse aucune fonctionnalité qui ne soit pas disponible avec une chaîne entre guillemets, elle est utile pour de nombreuses raisons. Elle vous autorise à insérer des guillemets simples et doubles dans une chaîne sans avoir à les protéger et elle peut s'étendre sur plusieurs lignes sans avoir à terminer chaque ligne par un `\`. Elle est ainsi particulièrement utile pour les chaînes de documentation (_docstrings_).
type¶
    
The type of a Python object determines what kind of object it is; every object has a type. An object's type is accessible as its `__class__` attribute or can be retrieved with `type(obj)`.
alias de type¶
    
Synonyme d'un type, créé en affectant le type à un identifiant.
Les alias de types sont utiles pour simplifier les indications de types. Par exemple :
```
defremove_gray_shades(
    colors: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
  pass

```

pourrait être rendu plus lisible comme ceci :
```
Color = tuple[int, int, int]
defremove_gray_shades(colors: list[Color]) -> list[Color]:
  pass

```

Voir `typing` et la **PEP 484**, qui décrivent cette fonctionnalité.
indication de type¶
    
L'annotation qui spécifie le type attendu pour une variable, un attribut de classe, un paramètre de fonction ou une valeur de retour.
Type hints are optional and are not enforced by Python but they are useful to static type checkers. They can also aid IDEs with code completion and refactoring.
Les indications de type de variables globales, d'attributs de classe et de fonctions, mais pas de variables locales, peuvent être consultées en utilisant `typing.get_type_hints()`.
Voir `typing` et la **PEP 484**, qui décrivent cette fonctionnalité.
retours à la ligne universels¶
    
Une manière d'interpréter des flux de texte dans lesquels sont reconnues toutes les fins de ligne suivantes : la convention Unix `'\n'`, la convention Windows `'\r\n'` et l'ancienne convention Macintosh `'\r'`. Voir la **PEP 278** et la **PEP 3116**, ainsi que la fonction `bytes.splitlines()` pour d'autres usages.
annotation de variable¶
    
annotation d'une variable ou d'un attribut de classe.
Lorsque vous annotez une variable ou un attribut de classe, l'affectation est facultative :
```
classC:
  field: 'annotation'

```

Les annotations de variables sont généralement utilisées pour des indications de types : par exemple, cette variable devrait prendre des valeurs de type `int` :
```
count: int = 0

```

La syntaxe d'annotation de variable est expliquée dans la section Les assignations annotées.
Reportez-vous à annotation de fonction, à la **PEP 484** et à la **PEP 526** qui décrivent cette fonctionnalité. Voir aussi Bonnes pratiques concernant les annotations sur les bonnes pratiques concernant les annotations.
environnement virtuel¶
    
Environnement d'exécution isolé (en mode coopératif) qui permet aux utilisateurs de Python et aux applications d'installer et de mettre à jour des paquets sans interférer avec d'autres applications Python fonctionnant sur le même système.
Voir aussi `venv`.
machine virtuelle¶
    
Ordinateur défini entièrement par du logiciel. La machine virtuelle (_virtual machine_) de Python exécute le code intermédiaire produit par le compilateur de _bytecode_.
Le zen de Python¶
    
Liste de principes et de préceptes utiles pour comprendre et utiliser le langage. Cette liste peut être obtenue en tapant "`import this`" dans une invite Python interactive.
#### Sujet précédent
Deprecations
#### Sujet suivant
About this documentation
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
  * Glossaire
  * | 
  * Theme  Auto Light Dark |


©  Copyright  2001-2025, Python Software Foundation. This page is licensed under the Python Software Foundation License Version 2. Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License. See History and License for more information. The Python Software Foundation is a non-profit corporation. Please donate. Mis à jour le févr. 17, 2025 (05:58 UTC). Found a bug? Créé en utilisant Sphinx 8.1.3. 
