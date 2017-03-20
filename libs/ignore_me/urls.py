# -*- coding: utf-8 -*-
#
from django.conf.urls import url

import ignore_me.views

urlpatterns = [
    url(r'', ignore_me.views.index),
]
