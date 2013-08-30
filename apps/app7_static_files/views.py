# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.conf import settings


def production(request):

    # You can pass anything in the templates, including the whole settings
    # object which contains everything that is inside the settings.py file.
    context = {
        'settings': settings,
        # used for Apache conf
        'STRIPPED_STATIC_URL': settings.STATIC_URL.rstrip('/')
    }
    return render(request, 'app7_static_files/prod_static_files.html', context)