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
  * Le tutoriel Python
  * | 
  * Theme  Auto Light Dark |


# Le tutoriel Python¶
Python est un langage de programmation puissant et facile à apprendre. Il dispose de structures de données de haut niveau et permet une approche simple mais efficace de la programmation orientée objet. Parce que sa syntaxe est élégante, que son typage est dynamique et qu'il est interprété, Python est un langage idéal pour l'écriture de scripts et le développement rapide d'applications dans de nombreux domaines et sur la plupart des plateformes.
L'interpréteur Python et sa vaste bibliothèque standard sont disponibles librement, sous forme de sources ou de binaires, pour toutes les plateformes majeures depuis le site Internet https://www.python.org/ et peuvent être librement redistribués. Ce même site distribue et pointe vers des modules, des programmes et des outils tiers. Enfin, il constitue une source de documentation.
L'interpréteur Python peut être facilement étendu par de nouvelles fonctions et types de données implémentés en C ou C++ (ou tout autre langage appelable depuis le C). Python est également adapté comme langage d'extension pour personnaliser des applications.
Dans ce tutoriel, nous introduisons, de façon informelle, les concepts de base ainsi que les fonctionnalités du langage Python et de son écosystème. Il est utile de disposer d'un interpréteur Python à portée de main pour mettre en pratique les notions abordées. Si ce n'est pas possible, pas de souci, les exemples sont inclus et le tutoriel est adapté à une lecture "hors ligne".
Pour une description des objets et modules de la bibliothèque standard, reportez-vous à La bibliothèque standard. La référence du langage Python présente le langage de manière plus formelle. Pour écrire des extensions en C ou en C++, lisez Extension et intégration de l'interpréteur Python et Manuel de référence de l'API Python/C. Des livres sont également disponibles qui couvrent Python dans le détail.
L'ambition de ce tutoriel n'est pas d'être exhaustif et de couvrir chaque fonctionnalité, ni même toutes les fonctionnalités les plus utilisées. Il vise, en revanche, à introduire les fonctionnalités les plus notables et à vous donner une bonne idée de la saveur et du style du langage. Après l'avoir lu, vous serez capable de lire et d'écrire des modules et des programmes Python et vous serez prêt à en apprendre davantage sur les modules de la bibliothèque Python décrits dans La bibliothèque standard.
Pensez aussi à consulter le Glossaire.
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


#### Sujet précédent
Changelog
#### Sujet suivant
1. Mise en bouche
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
  * Le tutoriel Python
  * | 
  * Theme  Auto Light Dark |


©  Copyright  2001-2025, Python Software Foundation. This page is licensed under the Python Software Foundation License Version 2. Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License. See History and License for more information. The Python Software Foundation is a non-profit corporation. Please donate. Mis à jour le févr. 17, 2025 (05:58 UTC). Found a bug? Créé en utilisant Sphinx 8.1.3. 
