# -*- coding: utf-8 -*-

from django.conf.urls import url


# On peut également mapper une URL à une vue en passant directement la vue
# importée (et nom une chaîne, comme dans app1)
from app2_hello_again.views import hello


urlpatterns = [
    url(r'', hello),
]
