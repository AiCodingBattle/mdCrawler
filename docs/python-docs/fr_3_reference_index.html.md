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
  * La référence du langage Python
  * | 
  * Theme  Auto Light Dark |


# La référence du langage Python¶
Cette documentation décrit la syntaxe et la « sémantique interne » du langage. Elle peut être laconique, mais essaye d'être exhaustive et exacte. La sémantique des objets natifs secondaires, des fonctions, et des modules est documentée dans La bibliothèque standard. Pour une présentation informelle du langage, voyez plutôt Le tutoriel Python. Pour les développeurs C ou C++, deux manuels supplémentaires existent : Extension et intégration de l'interpréteur Python survole l'écriture d'extensions, et Manuel de référence de l'API Python/C décrit l'interface C/C++ en détail.
  * 1. Introduction
    * 1.1. Autres implémentations
    * 1.2. Notations
  * 2. Analyse lexicale
    * 2.1. Structure des lignes
    * 2.2. Autres lexèmes
    * 2.3. Identifiants et mots-clés
    * 2.4. Littéraux
    * 2.5. Opérateurs
    * 2.6. Délimiteurs
  * 3. Modèle de données
    * 3.1. Objets, valeurs et types
    * 3.2. Hiérarchie des types standards
    * 3.3. Méthodes spéciales
    * 3.4. Coroutines
  * 4. Modèle d'exécution
    * 4.1. Structure d'un programme
    * 4.2. Noms et liaisons
    * 4.3. Exceptions
  * 5. Le système d'importation
    * 5.1. `importlib`
    * 5.2. Les paquets
    * 5.3. Recherche
    * 5.4. Chargement
    * 5.5. Le chercheur dans _path_
    * 5.6. Remplacement du système d'importation standard
    * 5.7. Importations relatives au paquet
    * 5.8. Cas particulier de `__main__`
    * 5.9. Références
  * 6. Expressions
    * 6.1. Conversions arithmétiques
    * 6.2. Atomes
    * 6.3. Primaires
    * 6.4. Expression `await`
    * 6.5. L'opérateur puissance
    * 6.6. Arithmétique unaire et opérations sur les bits
    * 6.7. Opérations arithmétiques binaires
    * 6.8. Opérations de décalage
    * 6.9. Opérations binaires bit à bit
    * 6.10. Comparaisons
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
    * 7.3. L'instruction `assert`
    * 7.4. L'instruction `pass`
    * 7.5. L'instruction `del`
    * 7.6. L'instruction `return`
    * 7.7. L'instruction `yield`
    * 7.8. L'instruction `raise`
    * 7.9. L'instruction `break`
    * 7.10. L'instruction `continue`
    * 7.11. L'instruction `import`
    * 7.12. L'instruction `global`
    * 7.13. L'instruction `nonlocal`
    * 7.14. The `type` statement
  * 8. Instructions composées
    * 8.1. L'instruction `if`
    * 8.2. L'instruction `while`
    * 8.3. L'instruction `for`
    * 8.4. L'instruction `try`
    * 8.5. L'instruction `with`
    * 8.6. L'instruction `match`
    * 8.7. Définition de fonctions
    * 8.8. Définition de classes
    * 8.9. Coroutines
    * 8.10. Type parameter lists
  * 9. Composants de plus haut niveau
    * 9.1. Programmes Python complets
    * 9.2. Fichier d'entrée
    * 9.3. Entrée interactive
    * 9.4. Entrée d'expression
  * 10. Spécification complète de la grammaire


#### Sujet précédent
8. Éditeurs et IDEs
#### Sujet suivant
1. Introduction
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
  * La référence du langage Python
  * | 
  * Theme  Auto Light Dark |


©  Copyright  2001-2025, Python Software Foundation. This page is licensed under the Python Software Foundation License Version 2. Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License. See History and License for more information. The Python Software Foundation is a non-profit corporation. Please donate. Mis à jour le févr. 17, 2025 (05:58 UTC). Found a bug? Créé en utilisant Sphinx 8.1.3. 
