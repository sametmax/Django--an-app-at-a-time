# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('',

    # This says to Django to call the function
    # 'home' in the module 'views' of the app 'app1_hello'" for any URL
    url(r'', 'app1_hello.views.hello'),

)


# This URL pattern is included in project/urls.py, this is why it works.
# You will want to read this file to understand URL routing better.
