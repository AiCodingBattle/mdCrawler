Django
The web framework for perfectionists with deadlines.
Changer de thème (actuellement : automatique)
Changer de thème (actuellement : clair)
Changer de thème (actuellement : sombre)
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
  * Changer de thème (actuellement : automatique)
Changer de thème (actuellement : clair)
Changer de thème (actuellement : sombre)
Toggle Light / Dark / Auto color theme


# Documentation
Search: Rechercher
  * Getting Help


  * el
  * en
  * es
  * id
  * it
  * ja
  * ko
  * pl
  * pt-br
  * zh-hans
  * Langue : **fr**


  * 1.8
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
  * Version de la documentation : **5.1**


  * 

# Documentation de Django¶
Tout ce que vous devez savoir sur Django.
## Premiers pas¶
Django ou la programmation sont nouveaux pour vous ? C’est le bon endroit pour démarrer !
  * **Pour commencer :** Aperçu | Installation
  * **Tutoriel :** 1ère partie : requêtes et réponses | 2ème partie : les modèles et le site d’administration | 3ème partie : vues et gabarits | 4ème partie : formulaires et vues génériques | 5ème partie : tests | 6ème partie : fichiers statiques | 7ème partie : personnalisation du site d’administration | 8ème partie : ajout de paquets tiers
  * **Tutoriels avancés :** Comment écrire des applications réutilisables | Écriture de votre première contribution à Django


## Obtenir de l’aide¶
Des problèmes ? Nous aimerions vous aider !
  * Essayez la FAQ – elle contient des réponses à de nombreuses questions courantes.
  * En recherche d’informations spécifiques ? Essayez Index, Index du module ou la table des matières détaillée.
  * Rien trouvé ? Lisez FAQ : Obtenir de l’aide pour des informations sur la recherche de soutien et sur la manière de poser des questions à la communauté.
  * Signalez des anomalies de Django dans notre système de tickets (en anglais).


## Organisation de la documentation¶
Django possède une documentation abondante. Un aperçu général de la façon dont elle est structurée peut aider à trouver ce que l’on cherche :
  * Les tutoriels vous conduisent par la main à travers une série d’étapes en vue de la création d’une application Web. Commencez par là si vous débutez avec Django ou avec le développement d’applications Web. Consultez également les « Premiers pas ».
  * Les guides thématiques abordent des thèmes et concepts clés d’un point de vue général et fournissent des informations et explications détaillées sur les éléments fondamentaux.
  * Les guides de référence contiennent des références techniques pour les API et autres aspects de la machinerie Django. Ils présentent son fonctionnement et la manière de l’exploiter en partant du principe que les concepts clés de base sont maîtrisés.
  * Les guides pratiques sont des marches à suivre. Vous êtes guidé pas-à-pas dans la résolution de problèmes et de scénarios classiques. Les connaissances requises sont plus élevées que pour les tutoriels et le fonctionnement de base de Django doit être compris.


## La couche des modèles¶
Django présente une couche d’abstraction (les « modèles ») pour structurer et manipuler les données de votre application Web. Pour en savoir plus, voyez ci-dessous :
  * **Modèles :** Introduction aux modèles | Les types de champs | Index | Les options Meta | La classe Model
  * **QuerySets :** Création de requêtes | Référence des méthodes QuerySet | Expressions de recherche
  * **Instances des modèles :** Méthodes des instances | Accès aux objets liés
  * **Migrations :** Introduction aux migrations | Référence des opérations | Édition de schéma | Écriture de migrations
  * **Avancé :** Managers | SQL brut | Transactions | Aggrégation | Recherche | Champs personnalisés | Base de données multiples | Expressions de recherche personnalisées | Expressions de requêtes | Expressions conditionelles | Fonctions de base de données
  * **Autre :** Bases de données prises en charge | Bases de données existantes | Données initiales | Optimisation des accès aux bases de données | Fonctionnalités spécifiques à PostgreSQL


## La couche des vues¶
Django possède le concept des « vues » qui englobe la logique responsable du traitement des requêtes des utilisateurs et le renvoi des réponses. Trouvez tout ce qu’il faut savoir sur les vues au travers des liens ci-dessous :
  * **Les bases :** URLconfs | Les fonctions Vue | Raccourcis | Décorateurs | Prise en charge du code asynchrone
  * **Référence :** Vues incluses | Les objets requête-réponse | Les objets TemplateResponse
  * **Téléchargement de fichiers :** Aperçu | Les objets fichiers | L’API de stockage | Gestion des fichiers | Stockage personnalisé
  * **Vues fondées sur les classes :** Aperçu | Vues d’affichages incluses | Vues d’édition incluses | Utilisation des mixins | Référence de l’API | Sommaire général
  * **Avancé :** Production de CSV | Production de PDF
  * **Middleware :** Aperçu | Classes middleware incluses


## La couche des gabarits¶
La couche des gabarits fournit une syntaxe adaptée aux concepteurs Web pour le rendu des informations à présenter aux utilisateurs. Pour apprendre comment les concepteurs Web peuvent utiliser cette syntaxe et comment elle peut être étendue par les programmeurs, lisez :
  * **Les bases :** Aperçu
  * **Pour les concepteurs :** Aperçu du langage | Balises et filtres inclus | Humanisation
  * **Pour les programmeurs :** L’API des gabarits | Balises et filtres personnalisés | Moteur de gabarit personnalisé


## Formulaires¶
Django fournit un cadre applicatif riche pour faciliter la création de formulaires et la manipulation des données de formulaires.
  * **Les bases :** Aperçu | L’API des formulaires | Champs inclus | Composants inclus
  * **Avancé:** Formulaires pour modèles | Intégration de médias | Jeux de formulaires | Personnalisation de la validation


## Le processus de développement¶
Apprendre comment différents composants et outils peuvent vous aider à développer et à tester les applications Django :
  * **Paramètres :** Aperçu | Liste complète des paramètres (settings)
  * **Applications :** Aperçu
  * **Exceptions :** Aperçu
  * **django-admin et manage.py:** Aperçu | Ajout de commandes personnalisées
  * **Tests :** Introduction | Écriture et exécution des tests | Outils de recherche inclus | Sujets avancés
  * **Déploiment :** Aperçu | Serveurs WSGI | Serveurs ASGI | Déploiement des fichiers statiques | Suivi des erreurs de code par courriel | Contrôles avant déploiement


## L’administration¶
Trouvez tout ce qu’il faut savoir sur l’interface d’administration automatique, l’une des fonctionnalités les plus populaires de Django :
  * Le site d’administration
  * Les actions d’administration
  * Le générateur de documentation dans l’administration


## Sécurité¶
La sécurité est un sujet d’importance capitale dans le développement d’applications Web et Django offre plusieurs outils et mécanismes de protection :
  * Aperçu de la sécurité
  * Alertes de sécurité publiées pour Django
  * Protection contre le clickjacking
  * Protection contre la falsification de requêtes inter-sites (CSRF)
  * La signature cryptographique
  * Intergiciel de sécurité


## Internationalisation et régionalisation¶
Django contient un cadre applicatif robuste pour gérer l’internationalisation et la régionalisation dans le développement d’applications multilingues et pour différentes régions du monde :
  * Aperçu | Internationalisation | Régionalisation | Régionalisation de la mise en forme d’interfaces Web et de la saisie dans les formulaires
  * Fuseaux horaires


## Performance et optimisations¶
Il existe une variété de techniques et d’outils pour aider à rendre votre code plus performant, plus rapide et moins gourmand en ressources système.
  * Aperçu de la performance et des optimisations


## Cadre applicatif géographique¶
GeoDjango se veut un cadre applicatif Web géographique de classe mondiale. Son but est de faciliter au maximum la création d’application Web GIS et l’exploitation du potentiel de données géolocalisées.
## Outils d’usage courant pour les applications Web¶
Django fournit plusieurs outils fréquemment utilisés dans le développement d’applications Web :
  * **Authentification :** Aperçu | Utilisation du système d’authentification | Gestion des mots de passe | Personnalisation de l’authentification | Référence de l’API
  * Gestion des caches
  * Journalisation
  * Envoi de courriels
  * Flux de syndication (RSS/Atom)
  * Pagination
  * Infrastructure de messages
  * Sérialisation
  * Sessions
  * Sitemaps
  * Gestion de fichiers statiques
  * Validation de données


## Autres fonctionnalités essentielles¶
En savoir plus sur quelques autres fonctionnalités essentielles de l’infrastructure Django :
  * Traitement de contenu conditionnel
  * Types de contenus et relations génériques
  * Pages statiques
  * Redirections
  * Signaux
  * Infrastructure de vérifications systèmes
  * L’infrastructure des sites
  * Unicode et Django


## Le projet libre Django¶
En savoir plus sur le processus de développement du projet Django lui-même et sur la manière d’y contribuer :
  * **Communauté :** Contribuer à Django | Le processus de publication | Structure des équipes | Le dépôt du code source de Django | La politique de sécurité | Les listes de diffusion et le forum
  * **Philosophie conceptuelle :** Aperçu
  * **Documentation:** À propos de cette documentation
  * **Distribution par des tierces-parties :** Aperçu
  * **Évolution de Django:** Stabilité de l’API | Notes de publication et instructions de mises à jour | Processus d’obsolescence


Sommaire de la documentation Django
Premiers pas 
Back to Top
# Informations supplémentaires
## Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * Tim Drijvers donated to the Django Software Foundation to support Django development. Donate today! 


## Parcourir
  * Précédent : Sommaire de la documentation Django
  * Suivant : Premiers pas
  * Table des matières
  * Index général
  * Index des modules Python


## Vous êtes ici :
  * Documentation de Django 5.1
    * Documentation de Django


## Obtenir de l'aide
FAQ
    Essayez la FAQ, vous y trouverez des réponses à de nombreuses questions courantes.
Index, Index des modules, or Sommaire
    Pratique lorsqu'on cherche des informations précises.
Django Discord Server
    Join the Django Discord Community.
Official Django Forum
    Join the community on the Django Forum.
Ticket tracker
    Signalez des bogues de Django ou de sa documentation dans notre système de suivi de tickets.
## Télécharger :
Hors ligne (Django 5.1) : HTML | PDF | ePub Offert par Read the Docs. 
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
