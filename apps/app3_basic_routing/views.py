# -*- coding: utf-8 -*-

"""
     Nous avons 3 vues cette fois :

     - une principale à la racine de notre motif d'URLs
     - une statique avec une URL préfixée
     - une dynamique avec des paramètres dans l'URL
"""



from django.shortcuts import render


def index(request):
    """
        Cette vue sert uniquement à servir le template
    """
    return render(request, 'app3_index.html')


def prefix(request):
    """
        Cette vue sert uniquement à servir le template
    """
    return render(request, 'prefix.html')


def hello(request, name, prefix="hello"):
    """
        La vue "hello", avec des arguments. La premier est obligatoire, le
        second est optionnel et a une valeur par défaut.

        Ces valeurs seront extraites de l'URL et passées automatiquement à la
        vue.

        Regardez urls.py pour voir comment nous demandons à Django de le faire.
    """

    # Le context contient maintenant deux variables. Si vous êtes paresseux,
    # vous pouvez utiliser "context = locals()" pour récupérer un dictionnaire
    # de toutes les variables et éviter de remplir le contexte manuellement.
    context = {
        'name': name,
        'prefix': prefix
    }

    return render(request, 'hello3.html', context)

