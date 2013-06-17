# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


# an alternative way of mapping a url to a view is to pass directly the
# imported view (and not a string, like in app1)
from app1_hello.views import hello


urlpatterns = patterns('',
    url(r'', hello),
)
