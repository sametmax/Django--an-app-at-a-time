# -*- coding: utf-8 -*-

"""
    "routing" is declaring what url will trigger which vue function to be
    called.
"""

from django.conf.urls import patterns, url, include


urlpatterns = patterns('',

    # If the URL looks like ......./prefix/, then call the prefix() view
    # function

    url(r'prefix/$', 'app3_basic_routing.views.prefix'),

    # It's possible to map an URL to a view from anywhere (such as another app)
    url(r'hello_from_app1/', 'app1_hello.views.hello'),

    # You can also include a whole urls.py from anywhere
    url(r'app2_included/', include('app2_hello_again.urls')),

    # We still have two parts in this URL declaration :
    # - on the left what the URL should look like
    # - on the right the view function that Django will call
    #
    # The left part is now more complicated : it's a full featured
    # regular expression :
    #
    #  - (?P<name>\w+) will match any set of letters and _ then capture it
    #    under the name of "name" to pass it as a parameter to hello()
    #  - (?P<prefix>\w+) will match any additional set of letters and _, after
    #   the first slash, catpure is under the name "prefix" to pass it as
    #   a parameter to hello().
    #
    # This syntax is not specific to Django, it's plain old regular expressions
    # and you need to know regular expressions if you want to make advanced
    # uses of routing in Django.
    #

    url(r'(?P<name>\w+)/(?P<prefix>\w+)/$', 'app3_basic_routing.views.hello'),

    # We can declare several routes going to the SAME view.
    # Here we add one route without the prefix, to make the prefix optional.
    # REMEMBER: in routing, always add the most specific routes first
    # because the URL will be compared from the top patterns to the bottom ones.

    url(r'(?P<name>\w+)/$', 'app3_basic_routing.views.hello'),

    # This index view is the root route, you should always declare it last
    # because it's view will be called if no other URLs match.

    url(r'', 'app3_basic_routing.views.index'),


)
