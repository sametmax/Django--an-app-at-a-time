# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin


# Obligatoire pour que l'admin fonctionne
admin.autodiscover()


urlpatterns = patterns('',

    # affiche l'admin à l'URL /admin/
    url(r'^admin/', include(admin.site.urls)),

    # inclut nos apps, une par une

    # Ceci dit que tout URL commençant par 'app1' doir être dirigée sur notre
    # première app
    url(r'^app1/', include('app1_hello.urls')),

    url(r'^app2/', include('app2_hello_again.urls')),


    # Ignorez cela, c'est la page listant toutes les autres apps
    url(r'^$', include('ignore_me.urls')),
)
