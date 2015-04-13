# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [

    url(r'filters/', 'app6_template_tools.views.filters',
        name="template_filters"),
    url(r'tags/', 'app6_template_tools.views.tags',
        name="template_tags"),
    url(r'inheritance/', 'app6_template_tools.views.inheritance',
        name="template_inheritance"),
    url(r'includes/', 'app6_template_tools.views.includes',
        name="template_includes"),

    # TemplateView is a generic view, meaning a view that is already coded
    # and provided by Django. There are a lot of them to do various tasks,
    # usually for stuff you do very often.
    # TemplateView is also a class based view, while you have been using
    # only functions to create views until now.
    # Don't worry about it.
    # You just need to know that TemplateView allow you to render a template
    # directly with this syntax, without the need to code a empty view
    # yourself.
    url(r'direct-to-template/',
        TemplateView.as_view(template_name='app6_direct.html'),
        name="direct_to_template"),

    url(r'', 'app6_template_tools.views.index'),

]
