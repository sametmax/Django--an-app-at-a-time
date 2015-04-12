# -*- coding: utf-8 -*-

from django.conf.urls import url


urlpatterns = [

    # This says to django to call the function
    # 'home' in the module 'views' of the app 'app1_hello'" for any URL
    url(r'', 'app1_hello.views.hello'),

]


# This url pattern is included in project/urls.py, this is why it works.
# You will want to read this file to understand url routing better.
