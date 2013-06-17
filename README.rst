*******************************
Django, une app à la fois
*******************************


Comment l'utiliser ?
======================

Téléchargez et décompressez le projet, puis lancez `python ./manage.py`.

Vous n'avez pas besoin d'installer quoi que ce soit.

Allez à l'URL http://127.0.0.1:8000 et jouez avec les apps.

Lorsque vous souhaitez voir comme ça marche, allez dans le dossier "apps" et lisez le code source commenté.

Chaque app par du principe que vous comprenez les précédentes, et contient un README pour vous guider.

Liens de téléchargement :

  - `English version <https://github.com/sametmax/Django--an-app-at-a-time/archive/master.zip>`_
  - `Version française <https://github.com/sametmax/Django--an-app-at-a-time/archive/fran%C3%A7ais.zip>`_


Contenu
=================

- "apps" : contient toutes les applications, ordonnées par complexité et dépendances. C'est ce que vous voulez lire.
- "porject" : le project Django lui-même, contenant les paramètres et la définition principale des URL. Vous devriez y ketter un oeil de temps à autres pour remettre les applications dans leur context, et également apprendre quelques astuces.
- "libs" : les dépendances telles que Django qu'il faudrait normalement installer. Inutile de regarder là dedans, mais vous pouvez si vous commencer à vous sentir à l'aise avec Django.
- "libs/ignore_me" : l'app qui liste toutes les apps, et la page principale du projet. Vous pouvez l'ignorer, ce n'est pas très intéressant.
- "manage.py" : la commande qui permet d'interragir avec le projet Django. Celle-ci a été quelque peu modifiée, donc ne la remplacez pas.
- ".gitignore" : un fichier de configuration pour Git. Vous n'avez pas besoin de cela pour Django. Il est ici pour m'aider.


Notes
==========

Dans un vrai projet, vous DEVREZ installer quelque chose. Les dependances sont ici fournies directement dans le projet pour des raisons pratiques, mais vous utiliseriez normalement pip et virtual env dans un projet réel.

Par ailleurs, ceci n'est PAS un tutorual. Le but n'est pas de remplacer un cours complet pour apprendre comment Django fonctionner, mais plutôt de donner un exemple complet de commet faire chaque tache dans le cadre de Django.

Les traductions et corrections orthographiques sont les bienvenues.

