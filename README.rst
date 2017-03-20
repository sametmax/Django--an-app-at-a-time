*******************************
Django, une app à la fois
*******************************

Un projet Django lourdement commenté dédié à l'enseignement du framework ou à rafraichir la mémoire. Chaque app fait la démonstration de quelques fonctionalités essentielles de Django de telle sorte qu'on puisse voir comme elles intéragissent ensemble, simplement en regardant le résultat dans son navigateur. Il n'y a rien à faire à part exécuter et lire.

Pour le moment:

- Project : voir comment settings et urls.py fonctionne
- App 1: hello world
- App 2: encore hello
- App 3: routing de base
- App 4: création de liens
- App 5: GET, POST et cookies
- App 6: templates, tags et filters
- App 7: fichiers statiques
- App 8: app réutilisable

A venir:

- ORM
- Formulaires
- Authentification
- Admin
- Commandes
- Traductions


Comment l’utiliser ?
======================

Téléchargez et décompressez le projet, puis lancez :

    python ./manage.py runservers

Vous pouvez ignorer le warning sur les migrations.

Vous n’avez pas besoin d’installer quoi que ce soit.

Allez à l’URL http://127.0.0.1:8000 et jouez avec les apps.

Lorsque vous souhaitez voir comme ça marche, allez dans le dossier "apps" et lisez le code source commenté.

Chaque app part du principe que vous comprenez les précédentes, et contient un README pour vous guider.

Liens de téléchargement :

  - `English version <https://github.com/sametmax/Django--an-app-at-a-time/archive/master.zip>`_
  - `Version française <https://github.com/sametmax/Django--an-app-at-a-time/archive/fran%C3%A7ais.zip>`_


Contenu
=================

- "apps" : contient toutes les applications, ordonnées par complexité et dépendances. C’est ce que vous voulez lire.
- "project" : le projet Django lui-même, contenant les paramètres et la définition principale des URL. Vous devriez y jeter un œil de temps à autre pour remettre les applications dans leur contexte, et également apprendre quelques astuces.
- "libs" : les dépendances telles que Django qu’il faudrait normalement installer. Inutile de regarder là-dedans, mais vous pouvez si vous commencez à vous sentir à l’aise avec Django.
- "libs/ignore_me" : l’app qui liste toutes les apps, et la page principale du projet. Vous pouvez l’ignorer, ce n’est pas très intéressant.
- "manage.py" : la commande qui permet d’interagir avec le projet Django. Celle-ci a été quelque peu modifiée, donc ne la remplacez pas.
- ".gitignore" : un fichier de configuration pour Git. Vous n’avez pas besoin de cela pour Django. Il est ici pour m’aider.


Notes
==========

Dans un vrai projet, vous DEVREZ installer quelque chose. Les dépendances sont ici fournies directement dans le projet pour des raisons pratiques, mais vous utiliseriez normalement pip et virtual env dans un projet réel.

Par ailleurs, ceci n’est PAS un tutorial. Le but n’est pas de remplacer un cours complet pour apprendre comment Django fonctionne, mais plutôt de donner un exemple complet de comment faire chaque tâche dans le cadre de Django.

Les traductions et corrections orthographiques sont les bienvenues.
