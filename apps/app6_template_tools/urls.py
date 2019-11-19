from django.urls import path
from django.views.generic import TemplateView

import app6_template_tools.views

urlpatterns = [
    path("filters/", app6_template_tools.views.filters, name="template_filters"),
    path("tags/", app6_template_tools.views.tags, name="template_tags"),
    path(
        "inheritance/",
        app6_template_tools.views.inheritance,
        name="template_inheritance",
    ),
    path("includes/", app6_template_tools.views.includes, name="template_includes"),
    # TemplateView est une vue générique, c'est à dire une vue déjà codée et
    # fournie par Django. Il y en a beaucoup d'autres qui font des tâches variées,
    # généralement pour des choses que l'on fait souvent.
    # TemplateView est aussi une vue sous forme de classe, alors que vous aviez
    # jusqu'ici utilisé uniquement des fonctions pour cela.
    # Ne vous en souciez pas.
    # Vous avez seulement besoin de savoir que TemplateView vous permet
    # de faire le rendu d'un template directement en utilisant cette
    # syntaxe sans avoir besoin de coder la vue directement.
    path(
        "direct-to-template/",
        TemplateView.as_view(template_name="app6_direct.html"),
        name="direct_to_template",
    ),
    path("", app6_template_tools.views.index),

]
