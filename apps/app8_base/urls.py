# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [

    url(r'example1/',
        TemplateView.as_view(template_name="app8_base/example_child.html"),
        name="useless_view1"),

    url(r'example2/',
        TemplateView.as_view(template_name="app8_base/example_child.html"),
        name="useless_view2"),

    # Ici nous utilisons notre vue "index". C'est une vue réutilisable dans
    # le sens qu'elle est très configurable via ses paramètres.
    # Toutes les valeurs dans "kwargs" seront passées en tant que paramètres
    # à "index()". Chaque appel à "index" ressemblera à ceci :
    # index(request, **kwargs).
    # Nous utilisons cela pour passer un header, un footer et les exemples
    # à lister dans notre index. En changeant juste ces valeurs dans la prochaine
    # app, nous pourrons réutiliser le code Python et le template.
    url(r'', 'app8_base.views.index', kwargs={
        'title': 'Créer une application de base',
        'examples': [
            ('useless_view1', 'Cette vue ne fait pas grand chose.'),
            ('useless_view2', 'Celle-là non plus.')
        ],
        'header': 'Cette vue index est codée pour être générique et réutilisable.',
        'footer': 'Ici nous pouvons optionnellement écrire un footer',
    }),

    # Ne soyez pas effrayés par l'illusion de complexité ici.
    # Il s'agit juste de l'habituel url(pattern, view, parametres).
    # Les paramètres sont représentés par "kwargs" et sa valeur. Sa valeur est un dico.
    # Le dico a 4 clés : title, examples, header et footer.
    # La clé "examples" a une liste de tuples pour valeur, tandis que "title",
    # "header" et "footer" ont une string pour valeur.
    # Tout cela est imbriqué, c'est pour cela que cela à l'air compliqué, mais
    # ce sont juste des objets Python ordinaires mélangés ensembles dans un
    # appel de fonction.

]
