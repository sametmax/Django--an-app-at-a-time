# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [

    # this displays the admin on the url /admin/
    url(r'^admin/', include(admin.site.urls)),

    # include all our apps, one by one

    # this say that any url starting with 'app1' should be directed to the
    # first app
    url(r'^app1/', include('app1_hello.urls')),

    url(r'^app2/', include('app2_hello_again.urls')),
    url(r'^app3/', include('app3_basic_routing.urls')),
    url(r'^app4/', include('app4_links.urls')),
    url(r'^app5/', include('app5_get_post_and_cookies.urls')),
    url(r'^app6/', include('app6_template_tools.urls')),
    url(r'^app7/', include('app7_static_files.urls')),
    url(r'^app8/', include('app8_base.urls')),

    # ignore this, it's the page of the project listing all the apps
    url(r'^$', include('ignore_me.urls')),
]
