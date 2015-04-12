# -*- coding: utf-8 -*-

"""
    We will use most views from the previous app.
"""


from django.shortcuts import render
from django.core.urlresolvers import reverse


def index(request):
    # reverse() can take a route name (and optionally, url parameters),
    # and return the proper URL based on all urls.py. Here we get
    # "/app4/prefix/"
    first_link = reverse('prefix')
    return render(request, 'app4_index.html', {'first_link': first_link})
