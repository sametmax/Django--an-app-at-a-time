# coding: utf-8

from django.conf.urls import url


# import the 'hello' function from the module 'views' of the app 'app1_hello'"
from app1_hello.views import hello


urlpatterns = [

    # This tells Django to call the function hello for any URL
    url(r'', hello),

]


# This URL pattern is included in project/urls.py, this is why it works.
# You will want to read this file to understand URL routing better.
