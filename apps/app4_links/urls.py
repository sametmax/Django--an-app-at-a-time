

"""
    À partir du moment où on commence à avoir beaucoup de route, on peut leur
    donner des noms et s'y référer plus tard, quand on a besoin d'un lien
    pour l'une d'entre elles.

    Ici on va utiliser les MÊME urls et vues que dans l'app précédente, mais
    en leur donnant des noms.
"""

from django.urls import path, include

# Il est possible d'utiliser un préfix complet pour éviter les conflits de nom
# Le choix vous appartient, il n'y a pas de meilleure solution.
import app1_hello.views
import app3_basic_routing.views
import app4_links.views

urlpatterns = [

    # Donner un nom est aussi simple que passer un paramètre "name".
    # Nous allons utiliser ce nom dans views.py, donc aller dans ce fichier
    # pour voir ce qu'on en fait.
    path("prefix/", app3_basic_routing.views.prefix, name="prefix"),

    # À partir de là, on va utiliser les noms dans le template, donc
    # regardez dans templates/app4_index.html pour voir comment
    # on utilise ces noms.
    path("hello_from_app1/", app1_hello.views.hello, name="hello"),

    # Utiliser un nom pour un include ne marchera pas et ne produira pas
    # ce que vous voulez. Si vous voulez bénéficier des noms de route dans
    # ce cas, nommés les routes contenues dans le fichier urls.py inclu.
    path("app2_included/", include("app2_hello_again.urls"), name="include"),

    path(
        "<str:name>/<str:prefix>/", app3_basic_routing.views.hello, name="hello_prefix"
    ),
    path("<str:name>/", app3_basic_routing.views.hello, name="hello_name"),
    path("", app4_links.views.index),
]
