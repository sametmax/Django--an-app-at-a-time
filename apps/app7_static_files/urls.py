# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [

    # On met les fichiers de template dans un dossier nommé selon l'application.
    # Ainsi nous créons un "namespace", et les autres application peuvent
    # appeler leurs templates de la même manière. Cela permet aussi à tout
    # autre application d'écraser spécifiquement ces templates si elles le
    # souhaitent.
    url(r'basics/',
        TemplateView.as_view(template_name="app7_static_files/basics.html"),
        name="static_files_basics"),

    url(r'flexible/',
        TemplateView.as_view(template_name="app7_static_files/flexible_layout.html"),
        name="flexible_layout"),

    url(r'production/', 'app7_static_files.views.production',
        name="prod_static_files"),

    url(r'',
        TemplateView.as_view(template_name="app7_static_files/index.html")),
]
