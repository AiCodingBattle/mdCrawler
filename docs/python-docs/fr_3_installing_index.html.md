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
  * Installation de modules Python
  * | 
  * Theme  Auto Light Dark |


# Installation de modules Python¶
Email:
    
distutils-sig@python.org
En tant que logiciel libre populaire, Python bénéficie d'une communauté active de contributeurs et d'utilisateurs qui rendent à leur tour leurs logiciels disponibles, sous licence libre, pour les autres développeurs Python.
Cela permet aux utilisateurs de Python de partager et de collaborer efficacement, bénéficiant des solutions que les autres ont déjà crées pour résoudre les problèmes communs (ou même, parfois, rares !), aussi que de partager leurs propres solutions à tous.
This guide covers the installation part of the process. For a guide to creating and sharing your own Python projects, refer to the Python packaging user guide.
Note
Pour les entreprises et autres institutions, gardez en tête que certaines organisations ont leurs propres règles sur l'utilisation et la contribution au logiciel libre. Prenez ces règles en compte lorsque vous utilisez les outils de distribution et d'installation fournis par Python.
## Vocabulaire¶
  * `pip` est l'outil d'installation de prédilection. À partir de Python 3.4, il est inclus par défaut avec l'installateur de Python.
  * Un _environnement virtuel_ est un environnement Python semi-isolé qui autorise les paquets à être installés pour une application particulière, plutôt que d'être installés au niveau du système.
  * `venv` est l'outil standard pour créer des environnements virtuels, et est intégré à Python depuis la version 3.3. Depuis Python 3.4, il installe aussi `pip` dans tous les environnements virtuels créés.
  * `virtualenv` est une alternative tierce à `venv` (et son prédécesseur). Elle permet la création d'environnements virtuels pour les versions de Python antérieures à 3.4, qui ne fournissent pas de `venv`, ou ne sont pas capables d'installer automatiquement `pip` dans les environnements créés.
  * L'Index des Paquets Python est un dépôt public des paquets sous licence ouverte disponibles pour tous les utilisateurs Python.
  * the Python Packaging Authority is the group of developers and documentation authors responsible for the maintenance and evolution of the standard packaging tools and the associated metadata and file format standards. They maintain a variety of tools, documentation, and issue trackers on GitHub.
  * `distutils` est le premier système de construction et de distribution ajouté à la bibliothèque standard en 1998. Bien que l'utilisation directe de `distutils` soit progressivement supprimée, elle reste le fondement de l'infrastructure actuelle de construction de paquet et de distribution. Au-delà de rester dans la bibliothèque standard, son nom vit aussi sous d'autres formes, tel que la liste de diffusion utilisée pour coordonner le développement et les standards de la création de paquet.


Modifié dans la version 3.5: L'utilisation de `venv` est maintenant recommandée pour créer vos environnements virtuels.
Voir aussi
Guide Utilisateur de l'Empaquetage Python : Créer et utiliser des environnements virtuels
## Utilisation de base¶
Les outils standards de création de paquets sont tous conçus pour être utilisés à partir de la ligne de commande.
La commande suivante va installer la dernière version d'un module et ses dépendances depuis le _Python Package Index_ :
```
python -m pip install SomePackage

```

Note
Pour les utilisateurs POSIX (y compris Mac OS X et Linux), les exemples de ce guide supposent l'utilisation d'un environnement virtuel.
Pour les utilisateurs de Windows, les exemples de ce guide supposent que l'option proposant de modifier la variable d'environnement PATH à été cochée lors de l'installation de Python.
Il est aussi possible de préciser une version minimum exacte directement depuis la ligne de commande. Utiliser des caractères de comparaison tel que `>`, `<` ou d'autres caractères spéciaux qui sont interprétés par le _shell_ , le nom du paquet et la version doivent être mis entre guillemets :
```
python -m pip install SomePackage==1.0.4  # specific version
python -m pip install "SomePackage>=1.0.4" # minimum version

```

Normalement, si un module approprié est déjà installé, l'installer à nouveau n'aura aucun effet. La mise à jour de modules existants doit être demandée explicitement :
```
python -m pip install --upgrade SomePackage

```

Plus d'informations et de ressources concernant `pip` et ses capacités peuvent être trouvées dans le Python Packaging User Guide.
La création d'environnements virtuels est réalisée grâce au module `venv`. Installer des paquets au sein de l'environnement virtuel courant utilise les commandes montrées précédemment.
Voir aussi
Guide Utilisateur de l'Empaquetage Python : Installer les paquets de la distribution Python
## Comment puis-je … ?¶
Ce sont des réponses rapides ou des liens pour certaines tâches courantes.
### ... Installer `pip` avec une version de Python antérieures à la 3.4 ?¶
Python n'a commencé à fournir `pip` depuis Python 3.4. Pour les versions précédentes, `pip` a besoin d'être "amorcé" tel que décrit dans le _Python Packaging User Guide_.
Voir aussi
Guide Utilisateur de l'Empaquetage Python : Pré-requis pour installer des paquets
### ... Installer des paquets juste pour l'utilisateur actuel ?¶
Donner l'option `--user` à `python -m pip install` lui fera installer un paquet juste pour l'utilisateur en cours, plutôt que pour tous les utilisateurs du système.
### ... Installer des paquets Python scientifiques ?¶
Un certain nombre de paquets scientifiques Python ont des dépendances binaires complexes, et ne sont pas actuellement faciles à installer directement avec `pip`. Pour le moment, il est souvent plus simple pour les utilisateurs d'installer ces paquets par d'autres moyens plutôt que d'essayer de les installer avec `pip`.
Voir aussi
Guide Utilisateur de l'Empaquetage Python : Installer des paquets scientifiques
### ... Travailler avec plusieurs versions de Python installés en parallèle ?¶
Sous Linux, Max OS X et autres systèmes POSIX, utiliser les commandes Python de la version souhaitée en combinaison avec l'option `-m` permet de lancer la version appropriée de `pip` :
```
python2  -m pip install SomePackage # default Python 2
python2.7 -m pip install SomePackage # specifically Python 2.7
python3  -m pip install SomePackage # default Python 3
python3.4 -m pip install SomePackage # specifically Python 3.4

```

Les versions appropriées des commandes `pip` peuvent aussi être disponibles.
Sous Windows, utilisez le lanceur Python `py` en combinaison avec l'option `-m` :
```
py -2  -m pip install SomePackage # default Python 2
py -2.7 -m pip install SomePackage # specifically Python 2.7
py -3  -m pip install SomePackage # default Python 3
py -3.4 -m pip install SomePackage # specifically Python 3.4

```

## Les problèmes d'installation typiques¶
### Installer dans le Python du système sur Linux¶
Sur les systèmes Linux, une installation de Python sera généralement incluse dans le cadre de la distribution. Installer dans cette installation de Python nécessite un accès _root_ sur le système, et peut interférer avec le fonctionnement du gestionnaire de paquets du système et d'autres composants du système si un composant est mis à jour de façon inattendue en utilisant `pip`.
Sur de tels systèmes, il est souvent préférable d'utiliser un environnement virtuel ou une installation par l'utilisateur lors de l'installation des paquets avec `pip`.
### `Pip` n'est pas installé¶
Il est possible que `pip` ne soit pas installé par défaut. Une solution est :
```
python -m ensurepip --default-pip

```

Il existe également des ressources supplémentaires pour installer pip.
### Installation d'extensions binaires¶
Python a généralement beaucoup misé sur une distribution basée sur les sources, avec laquelle les utilisateurs finaux devaient compiler, lors de l'installation, les modules d'extension à partir des sources.
Avec l'introduction du format binaire `wheel`, et la possibilité de publier des _wheels_ , pour, au moins Windows et Mac OS X, via le _Python Package Index_ , ce problème devrait diminuer au fil du temps, car les utilisateurs sont plus régulièrement en mesure d'installer des extensions pré-compilées plutôt que de devoir les compiler eux-mêmes.
Certaines solutions pour installer des paquets scientifiques qui ne sont pas encore disponibles comme `wheel` pré-construites peuvent aussi aider à obtenir d'autres extensions binaires sans devoir les construire localement.
Voir aussi
Guide Utilisateur de l'Empaquetage Python : Extensions binaires
### Table des matières
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


#### Sujet précédent
Monitoring C API
#### Sujet suivant
Les HOWTOs de Python
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
  * Installation de modules Python
  * | 
  * Theme  Auto Light Dark |


©  Copyright  2001-2025, Python Software Foundation. This page is licensed under the Python Software Foundation License Version 2. Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License. See History and License for more information. The Python Software Foundation is a non-profit corporation. Please donate. Mis à jour le févr. 17, 2025 (05:58 UTC). Found a bug? Créé en utilisant Sphinx 8.1.3. 
