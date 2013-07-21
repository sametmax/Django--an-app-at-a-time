# -*- coding: utf-8 -*-

"""
    À partir du moment où on commence à avoir beaucoup de route, on peut leur
    donner des noms et s'y référer plus tard, quand on a besoin d'un lien
    pour l'une d'entre elles.

    Ici on va utiliser les MÊME urls et vues que dans l'app précédente, mais
    en leur donnant des noms.
"""

from django.conf.urls import patterns, url, include


urlpatterns = patterns('',

    # Donner un nom est aussi simple que passer un paramètre "nom".
    # Nous allons utiliser ce nom dans views.py, donc aller dans ce fichier
    # pour voir ce qu'on en fait.
    url(r'prefix/$', 'app3_basic_routing.views.prefix', name="prefix"),

    # À partir de là, on va utiliser les noms dans le template, donc
    # regardez dans templates/app4_index.html pour voir comment
    # on utilise ces noms.
    url(r'hello_from_app1/', 'app1_hello.views.hello', name="hello"),

    # Utiliser un nom pour un include ne marchera pas et ne produira pas
    # ce que vous voulez. Si vous voulez bénéficier des noms de route dans
    # ce cas, nommés les routes contenues dans le fichier urls.py inclu.
    url(r'app2_included/', include('app2_hello_again.urls'), name="include"),

    # En Python, il est utilisé de bouger les paramètres sur un autre ligne,
    # donc on utilise cela pour les empiler afin de ne pas faire une
    # loooooooooooooong ligne.
    url(r'(?P<name>\w+)/(?P<prefix>\w+)/$',
        'app3_basic_routing.views.hello',
        name='hello_prefix'),

    url(r'(?P<name>\w+)/$', 'app3_basic_routing.views.hello', name='hello_name'),

    url(r'', 'app4_links.views.index'),

)
