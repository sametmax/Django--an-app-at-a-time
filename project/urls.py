
from django.urls import include, path
from django.contrib import admin



urlpatterns = [

    # Affiche l'admin à l'URL /admin/
    path('admin/', admin.site.urls),

    # Inclut nos apps, une par une.

    # Ceci dit que tout URL commençant par 'app1' doit être dirigée sur notre
    # première app.
    path('app1/', include('app1_hello.urls')),

    path('app2/', include('app2_hello_again.urls')),
    path('app3/', include('app3_basic_routing.urls')),
    path('app4/', include('app4_links.urls')),
    path('app5/', include('app5_get_post_and_cookies.urls')),
    path('app6/', include('app6_template_tools.urls')),
    path('app7/', include('app7_static_files.urls')),
    path('app8/', include('app8_base.urls')),

    # Ignorez cela, c'est la page listant toutes les autres apps.
    path('', include('ignore_me.urls')),
]
