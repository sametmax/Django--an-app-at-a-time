# -*- coding: utf-8 -*-

"""
    We have 3 views this time :

    - one main view at the root of the app URL pattern
    - one static view with a prefix
    - one dynamic view with url parameter
"""



from django.shortcuts import render


def index(request):
    """
        This view's only purpose is to serve the template.
    """
    return render(request, 'app3_index.html')


def prefix(request):
    """
        This view's only purpose is to serve the template.
    """
    return render(request, 'prefix.html')


def hello(request, name, prefix="hello"):
    """
        Hello view with arguments. The first argument is mandatory,
        the second one is optional and has a default value.

        These values will be extracted from the URL and passed automatically
        to this view.

        Have a look at urls.py to see how we ask for it.
    """

    # The context now contains two variable. If you are lazy, you can
    # use context = locals() to create a dictionary of all local variables
    # and avoid populting the context manually
    context = {
        'name': name,
        'prefix': prefix
    }

    return render(request, 'hello3.html', context)

