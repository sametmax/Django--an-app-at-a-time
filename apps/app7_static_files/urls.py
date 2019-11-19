
from django.urls import path
from django.views.generic import TemplateView

import app7_static_files.views

# On peut créer les vues à l'avance pour séparer la gestion des vues et le
# routing
basics = TemplateView.as_view(template_name="app7_static_files/basics.html")

urlpatterns = [

    # On met les fichiers de template dans un dossier nommé selon l'application.
    # Ainsi nous créons un "namespace", et les autres application peuvent
    # appeler leurs templates de la même manière. Cela permet aussi à tout
    # autre application d'écraser spécifiquement ces templates si elles le
    # souhaitent.
    path('basics/', basics, name="static_files_basics"),

    # Si vous ne créez pas les vues à l'avance, un peu d'indentation fera
    # tenir le tout proprement
    path(
        'flexible/',
        TemplateView.as_view(
            template_name="app7_static_files/flexible_layout.html"
        ),
        name="flexible_layout"
    ),

    path(
        'production/',
        app7_static_files.views.production,
        name="prod_static_files"
    ),

    path(
        '',
        TemplateView.as_view(template_name="app7_static_files/index.html")
    ),
]
