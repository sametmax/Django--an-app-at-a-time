
"""
    On appelle "routing" la correspondance entre les URLS et les fonctions
    vues.
"""

from django.urls import path, include

# on peut importer plusieurs vues sur la même ligne
from app3_basic_routing.views import hello, index, prefix

# on peut créer des alias pour éviter des conflits de nom
from app1_hello.views import hello as hello1

urlpatterns = [

    # Si l'URL ressemble à ...../prefix/, alors appeler la fonction vue
    # prefix()

    path('prefix/', prefix),

    # On peut lier une URL a une vue de n'importe où (comme depuis une autre app)
    path('hello_from_app1/', hello1),

    # On peut aussi inclure un urls.py depuis n'importe où
    path('app2_included/', include('app2_hello_again.urls')),


    # Ici nous définissons une URL avec des composants variables. Ex:
    #
    #  <str:name> va chercher tout caractère  autre  "/" et les capturer
    #  dans la variable "name" afin de la passer en paramètre à hello()

    path('<str:prefix>/<str:name>/', hello),

    # On peut déclarer plusieurs route pour la même vue.
    # Ici nous ajoutons une route sans le préfixe, afin de rendre celui-ci
    # optionnel.
    # RAPPELEZ-VOUS : dans le routing, il faut toujours ajouter les routes
    # les plus spécifiques en premières car les URLs seront comparées depuis
    # les motifs du vers ceux du bas.

    path('<str:name>/', hello),


    # Cette route est la route racine de l'application, vous devez toujours
    # la déclarer en dernier car elle va récupérer toutes les URLS qui ne
    # correspondent pas au reste et donc c'est la vue appelée par défaut.

    path('', index),


]
