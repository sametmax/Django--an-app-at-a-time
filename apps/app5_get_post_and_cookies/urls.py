# coding: utf-8

from django.conf.urls import url

import app5_get_post_and_cookies.views

urlpatterns = [

    url(r'', app5_get_post_and_cookies.views.hello),

]
