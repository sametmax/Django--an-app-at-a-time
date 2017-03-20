# coding: utf-8

from django.conf.urls import url


# Une alternative est d'utiliser un import relatif
from app2_hello_again.views import hello


urlpatterns = [
    url(r'', hello),
]
