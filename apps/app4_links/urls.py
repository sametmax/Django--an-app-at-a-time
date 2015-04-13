# -*- coding: utf-8 -*-

"""
    When you start having a lot of routes, you can give them names, and
    refer to this name later, when you want a link for them.

    Here we will use the SAME URLs and views as in the previous app,
    but we will give them names.
"""

from django.conf.urls import url, include


urlpatterns = [

    # Giving a name is as simple as passing a "name" parameter.
    # We will use this name in views.py, so go to this file to see what
    # we do with it.
    url(r'prefix/$', 'app3_basic_routing.views.prefix', name="prefix"),

    # Starting from here, we will use names in the template,
    # so look at templates/app4_index.html to see how we use this name.
    url(r'hello_from_app1/', 'app1_hello.views.hello', name="hello"),

    # Naming routes doesn't work with include. This will not do what you
    # expect. To benefit from name, you should name routes from
    # the included urls.py.
    url(r'app2_included/', include('app2_hello_again.urls'), name="include"),

    # In Python it's allowed to move parameters on another line, so we use
    # this to stack them so it doesn't make a loooooooooooong line.
    url(r'(?P<name>\w+)/(?P<prefix>\w+)/$',
        'app3_basic_routing.views.hello',
        name='hello_prefix'),

    url(r'(?P<name>\w+)/$', 'app3_basic_routing.views.hello', name='hello_name'),

    url(r'', 'app4_links.views.index'),

]
