# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin


# Obligatoire pour que l'admin fonctionne.
admin.autodiscover()


urlpatterns = patterns('',

    # Affiche l'admin à l'URL /admin/
    url(r'^admin/', include(admin.site.urls)),

    # Inclut nos apps, une par une.

    # Ceci dit que tout URL commençant par 'app1' doit être dirigée sur notre
    # première app.
    url(r'^app1/', include('app1_hello.urls')),

    url(r'^app2/', include('app2_hello_again.urls')),
    url(r'^app3/', include('app3_basic_routing.urls')),
    url(r'^app4/', include('app4_links.urls')),
    url(r'^app5/', include('app5_get_post_and_cookies.urls')),
    url(r'^app6/', include('app6_template_tools.urls')),
    url(r'^app7/', include('app7_static_files.urls')),
    url(r'^app8/', include('app8_base.urls')),

    # Ignorez cela, c'est la page listant toutes les autres apps.
    url(r'^$', include('ignore_me.urls')),
)
