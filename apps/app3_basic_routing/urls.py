
"""
    "routing" is declaring what URL will trigger which vue function to be
    called.
"""

from django.urls import path, include

# you can import several views on the same line
from app3_basic_routing.views import hello, index, prefix

# you can alias imports if you want to avoid name conflicts
from app1_hello.views import hello as hello1


urlpatterns = [

    # If the URL looks like ......./prefix/, then call the prefix() view
    # function

    path('prefix/', prefix),

    # It's possible to map an URL to a view from anywhere (such as another app)
    path('hello_from_app1/', hello1),

    # You can also include a whole urls.py from anywhere
    path('app2_included/', include('app2_hello_again.urls')),

    # Here we define URL with variable parts. E.G:
    #
    #  <str:name> will match any charater other then "/" then capture it
    #  under the variable "name" to pass it as a parameter to hello()

    path('<str:prefix>/<str:name>/', hello),

    # We can declare several routes going to the SAME view.
    # Here we add one route without the prefix, to make the prefix optional.
    # REMEMBER: in routing, always add the most specific routes first
    # because the URL will be compared from the top patterns to the bottom ones.

    path('<str:name>/', hello),

    # This index view is the root route, you should always declare it last
    # because it's view will be called if no other URLs match.

    path('', index),


]
