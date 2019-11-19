"settings.py" contient les paramètres de votre projet Django. C'est un module python ordinaire, que vous pouvez importer et utiliser comme n'importe quel autre module.

"urls.py" contient le code qui associe des urls avec des apps. Grâce à ce fichier, quand quelqu'un va sur votre site sur une certaine url, c'est le code de la bonne app qui s'exécute.

"wsgi.py" est seulement utilisé en production, vous pouvez l'ignorer. Cependant, vous ne pouvez pas le supprimer, car il est devenu obligatoire dans la dernière version de Django.
