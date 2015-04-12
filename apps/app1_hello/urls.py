# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('',

    # This tells django to call the function
    # 'hello' in the module 'views' of the app 'app1_hello'" for any URL
    url(r'', 'app1_hello.views.hello'),

)


# This url pattern is included in project/urls.py, this is why it works.
# You will want to read this file to understand url routing better.
