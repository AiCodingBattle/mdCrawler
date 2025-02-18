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
  * Extension et intégration de l'interpréteur Python
  * | 
  * Theme  Auto Light Dark |


# Extension et intégration de l'interpréteur Python¶
Ce document décrit comment écrire des modules en C ou C++ pour étendre l'interpréteur Python à de nouveaux modules. En plus de définir de nouvelles fonctions, ces modules peuvent définir de nouveaux types d'objets ainsi que leur méthodes. Ce document explique aussi comment intégrer l'interpréteur Python dans une autre application, pour être utilisé comme langage d'extension. Enfin, ce document montre comment compiler et lier les modules d'extension pour qu'ils puissent être chargés dynamiquement (à l'exécution) dans l'interpréteur, si le système d'exploitation sous-jacent supporte cette fonctionnalité.
Ce document présuppose que vous avez des connaissances de base sur Python. Pour une introduction informelle du langage, voyez Le tutoriel Python. La référence du langage Python donne une définition plus formelle du langage. La bibliothèque standard documente les objets types, fonctions et modules existants (tous intégrés et écrits en Python) qui donnent au langage sa large gamme d'applications.
Pour une description dans sa totalité de l'API Python/C, voir Manuel de référence de l'API Python/C.
## Les outils tiers recommandés¶
This guide only covers the basic tools for creating extensions provided as part of this version of CPython. Third party tools like Cython, cffi, SWIG and Numba offer both simpler and more sophisticated approaches to creating C and C++ extensions for Python.
Voir aussi
Guide d'utilisation de l'empaquetage Python : Extensions binaires
    
Le guide d'utilisation de l'empaquetage Python ne couvre pas uniquement quelques outils disponibles qui simplifient la création d'extensions binaires, mais aborde aussi les différentes raisons pour lesquelles créer un module d'extension peut être souhaitable d'entrée.
## Création d'extensions sans outils tiers¶
Cette section du guide couvre la création d'extensions C et C++ sans l'utilisation d'outils tiers. Cette section est destinée aux créateurs de ces outils, plus que d'être une méthode recommandée pour créer votre propre extension C.
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


## Intégrer l'interpréteur CPython dans une plus grande application¶
Parfois, plutôt que de créer une extension qui s'exécute dans l'interpréteur Python comme application principale, il est préférable d'intégrer l'interpréteur Python dans une application plus large. Cette section donne quelques informations nécessaires au succès de cette opération.
  * 1. Intégrer Python dans une autre application
    * 1.1. Intégration de très haut niveau
    * 1.2. Au-delà de l'intégration de haut niveau : survol
    * 1.3. Intégration pure
    * 1.4. Étendre un Python intégré
    * 1.5. Intégrer Python dans du C++
    * 1.6. Compiler et Lier en environnement Unix ou similaire


### Table des matières
  * Extension et intégration de l'interpréteur Python
    * Les outils tiers recommandés
    * Création d'extensions sans outils tiers
    * Intégrer l'interpréteur CPython dans une plus grande application


#### Sujet précédent
Considérations de sécurité
#### Sujet suivant
1. Étendre Python en C ou C++
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
  * Extension et intégration de l'interpréteur Python
  * | 
  * Theme  Auto Light Dark |


©  Copyright  2001-2025, Python Software Foundation. This page is licensed under the Python Software Foundation License Version 2. Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License. See History and License for more information. The Python Software Foundation is a non-profit corporation. Please donate. Mis à jour le févr. 17, 2025 (05:58 UTC). Found a bug? Créé en utilisant Sphinx 8.1.3. 
