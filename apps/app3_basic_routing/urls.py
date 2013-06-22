# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include


"""
    On appelle "routing" la correspondance entre les URLS et les fonctions
    vues.
"""


urlpatterns = patterns('',

    # Si l'URL ressemble à ...../prefix/, alors appeler la fonction vue
    # prefix()

    url(r'prefix/$', 'app3_basic_routing.views.prefix'),

    # On peut lier une URL a une vue de n'importe où (comme depuis une autre app)
    url(r'hello_from_app1/', 'app1_hello.views.hello'),

    # On peut aussi inclure un urls.py depuis n'importe où
    url(r'app2_included/', include('app2_hello_again.urls')),


    # Nous avons toujours deux parties dans cette déclaration de route :
    # - à gauche ce à quoi l'URL doit ressembler
    # - à droite la fonction que Django appellera
    #
    # La partie de gauche est maintenant plus compliquée : c'est une
    # expression rationnelle complète.
    #
    # - (?P<name>\w+) correspond à n'importe quel jeu de lettres et _, puis
    #   le capture sous le nom "name" et pour le passer en paramètre à hello()
    # - (?P<prefix>\w+) correspond à n'importe quel jeu de lettres et _
    #   après un slash, puis le capture sous le nom "prefix" pour le passer
    #   en paramètres à hello()
    #
    # Cette syntaxe n'est pas spécifique à Django, c'est celle des expressions
    # rationnelles ordinaires, et il vous faut la connaitre si vous voulez
    # utiliser le routing de Django de manière avancée

    url(r'(?P<name>\w+)/(?P<prefix>\w+)/$', 'app3_basic_routing.views.hello'),

    # On peut déclarer plusieurs route pour la même vue.
    # Ici nous ajoutons une route sans le préfixe, afin de rendre celui-ci
    # optionnel.
    # RAPPELEZ-VOUS : dans le routing, il faut toujours ajouter les routes
    # les plus spécifiques en premières car les URLs seront comparées depuis
    # les motifs du vers ceux du bas.

    url(r'(?P<name>\w+)/$', 'app3_basic_routing.views.hello'),


    # Cette route est la route racine de l'application, vous devez toujours
    # la déclarer en dernier car elle va récupérer toutes les URLS qui ne
    # correspondent pas au reste et donc c'est la vue appelée par défaut.

    url(r'', 'app3_basic_routing.views.index'),


)
