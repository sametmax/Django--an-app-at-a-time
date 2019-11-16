# coding: utf-8
#
from django.conf.urls import url

from ignore_me.views import index


urlpatterns = [
    url(r'', index),
]
