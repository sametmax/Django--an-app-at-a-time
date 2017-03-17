# coding: utf-8

from django.conf.urls import url


# An alternative way is to use relative imports
from .views import hello


urlpatterns = [
    url(r'', hello),
]
