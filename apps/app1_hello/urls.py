# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('',

    # Cela dit à Django d'appeler la fonction 'hello' du module 'views' de
    # l'app 'app1_hello' pour toute URL.
    url(r'', 'app1_hello.views.hello'),

)

# Cette configuration d'URL est incluse depuis "project/urls.py", ce qui
# explique pourquoi cela fonctionne. Vous devriez lire ce fichier pour
# mieux comprendre le routing URL.

