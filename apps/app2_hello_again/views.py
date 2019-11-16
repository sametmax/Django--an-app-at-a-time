# coding: utf-8

"""
    Since everything in Django is just Python, you can add docstring to
    every module, class and function. And you should.

    This module does the EXACT same thing as app1, but show you the step
    by step process so you can see what's happening.

    You don't need to do this in your site, it's just here so you can
    see the how it works.
"""


from django.template import loader
from django.http import HttpResponse


def hello(request):
    """
       Display an HTML page with "Hello world" as a main title
    """

    # creates the template context from a dictionary, so that in the template
    # you can use the value "world" via the "name" variable
    template = loader.get_template('hello2.html')
    html = template.render({"name": "world"})

    return HttpResponse(html)
