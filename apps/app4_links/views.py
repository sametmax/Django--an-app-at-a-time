# coding: utf-8

"""
    La plupart des vues utilisées viennent de la précédente app.
"""


from django.shortcuts import render
from django.core.urlresolvers import reverse


def index(request):
    # reverse() peut prendre le nom d'une route (et optionnellement des paramètres)
    # et retourne l'URL correspondante en se bansant sur les urls.py. Ici
    # on va avoir "app3/prefix/"
    first_link = reverse('prefix')
    return render(request, 'app4_index.html', {'first_link': first_link})
