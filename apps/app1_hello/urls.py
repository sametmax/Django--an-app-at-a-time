# coding: utf-8

from django.conf.urls import url

# import la fonction 'hello' du module 'views' de l'app 'app1_hello'"
from app1_hello.views import hello


urlpatterns = [

    # Cela dit à Django d'appeler la fonction 'hello' pour tout url
    url(r'', hello),

]

# Cette configuration d'URL est incluse depuis "project/urls.py", ce qui
# explique pourquoi cela fonctionne. Vous devriez lire ce fichier pour
# mieux comprendre le routing URL.

