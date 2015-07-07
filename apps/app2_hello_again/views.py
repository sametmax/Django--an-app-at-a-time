# -*- coding: utf-8 -*-

"""
    Puisque tout dans Django est simplement du Python, vous pouvez utiliser
    des docstrings dans chaque module, classe et fonction. C'est recommandé.

    Ce module fait EXACTEMENT la même chose que app1, mais il vous montre
    le procédé pas à pas afin que vous voyiez ce qui se passe.

    Vous n'avez pas besoin de faire cela dans votre site, c'est juste là pour
    que vous voyiez comment ça marche.

"""


from django.template import Context, loader
from django.http import HttpResponse


def hello(request):
    """
       Affiche une page HTML avec "Hello world" comme titre principal
    """

    # crée un contexte de template depuis un dictionnaire, de telle sorte
    # que notre template puisse utiliser le mot "world" à travers la variable
    # "name"
    d = {"name": "world"}
    template_context = Context(d)
    template = loader.get_template('hello.html')
    html = template.render(template_context)

    return HttpResponse(html)
