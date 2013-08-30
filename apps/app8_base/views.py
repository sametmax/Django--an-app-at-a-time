# -*- coding: utf-8 -*-


from django.shortcuts import render

# When you create a reusable view, make sure to document it properly
def index(request, title, examples, header=None, footer=None, extra_context={},
          template_name='app8_base/index.html'):
    """
        Views displaying a listing of example for a given app.

        `request` is passed automatically, but you MUST pass at least
        `examples` via `kwargs` in urls.py.

        `examples` should be a list of tuples (view name, title) that will
        be used to generate the list of links to the app's examples.

        `title` should be a string to be used as the page title.

        `header` is an optional text to display before the examples.

        `footer` is an optional text to display after the examples.

        You can add an arbitrary value in the context by passing `extra_context`,
        which will be then available in the template.

        Default template is app8_base/base.html, but you may change it
        by passing `app8_base/index.html`.

        :exemple:

            url(r'', 'app8_base.views.index', kwargs={
                'examples':[
                    ('view1_name', 'The title for this link'),
                    ('view2_name', 'The title for this other link'),
                ],
                'header': 'Some text to display before',
                extra_context: {'settings': settings}
            }),

    """

    # The work of the views is really only to stuff everything in the context
    # and render the right remplate.
    context = {}
    context['title'] = title
    context['examples'] = examples
    context['header'] = header
    context['footer'] = footer
    context.update(extra_context)

    return render(request, template_name, context)