# -*- coding: utf-8 -*-


from django.shortcuts import render

# Quand on créer une une vue réutilisable, il faut la documentation correctement.
def index(request, title, examples, header=None, footer=None, extra_context={},
          template_name='app8_base/index.html'):
    """
        Vue affichant un listing d'exemples pour une app donnée.

        `request est passé automatiquement en paramètre, mais vous DEVEZ
        passer au moins `examples` via `kwargs` dans urls.py.

        `examples` doit être une liste de tuples (nom de vue, titre) qui sera
        utilisé pour générer la liste des liens vers les exemples de l'app.

        `title` doit être une string qui sera utilisé comme titre de la page.

        `header` est un texte optionnel à afficher avant les exemples.

        `footer` est un texte optionnel à afficher après les exemples.

        Vous pouvez ajouter une valeur abitraire au contexte en passant
        `extra_context` qui sera ensuite disponible dans le template.

        Le template par défaut est app8_base/base.html mais vous pouvez le
        changer en passant `template_name`

        :example:

            url(r'', 'app8_base.views.index', kwargs={
                'examples':[
                    ('nom_de_la_vue', 'Le titre pour ce lien'),
                    ('nom_de_la_vue_2', 'Le titre pour cet autre lien'),
                ],
                'header': Un texte à afficher avant',
                extra_context: {'settings': settings}
            }),

    """

    # Le travail de cette vue est uniquement de mettre toutes les valeurs
    # dans le contexte et de faire un rendu du bon template.
    context = {}
    context['title'] = title
    context['examples'] = examples
    context['header'] = header
    context['footer'] = footer
    context.update(extra_context)

    return render(request, template_name, context)
