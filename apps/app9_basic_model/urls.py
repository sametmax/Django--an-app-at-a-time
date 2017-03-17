# -*- coding: utf-8 -*-


from django.conf.urls import url


urlpatterns = [

    url(r'person/add/', 'app9_basic_model.views.add_person', name="add_person"),
    url(r'persons/', 'app9_basic_model.views.person_list', name="person_list"),

    # on generic view from app8 comes in handy
    url(r'', 'app8_base.views.index', kwargs={
        'title': 'Creating a very simple model',
        'examples': [
            ('add_person', 'Add a new person'),
            ('person_list', 'List all the persons')
        ],
        'header': 'You MUST run <code>./manage.py syncdb</code> before clicking.'
    }),

]
