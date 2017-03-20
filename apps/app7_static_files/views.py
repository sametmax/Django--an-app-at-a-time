# coding: utf-8


from django.shortcuts import render
from django.conf import settings


def production(request):

    # On peut passer ce que l'on veut vers les templates, y compris l'objet
    # settings au complet qui contient tout ce qu'il y a dans le fichier
    # settings.py.
    context = {
        'settings': settings,
        # Utilisé pour la configuration Apache
        'STRIPPED_STATIC_URL': settings.STATIC_URL.rstrip('/')
    }
    return render(request, 'app7_static_files/prod_static_files.html', context)
