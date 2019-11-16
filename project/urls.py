
from django.urls import include, path
from django.contrib import admin

urlpatterns = [

    # this displays the admin on the url /admin/
    path('admin/', admin.site.urls),

    # include all our apps, one by one

    # this say that any url starting with 'app1' should be directed to the
    # first app
    path('app1/', include('app1_hello.urls')),

    path('app2/', include('app2_hello_again.urls')),
    path('app3/', include('app3_basic_routing.urls')),
    path('app4/', include('app4_links.urls')),
    path('app5/', include('app5_get_post_and_cookies.urls')),
    path('app6/', include('app6_template_tools.urls')),
    path('app7/', include('app7_static_files.urls')),
    path('app8/', include('app8_base.urls')),

    # ignore this, it's the page of the project listing all the apps
    path('', include('ignore_me.urls')),
]
