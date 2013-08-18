# -*- coding: utf-8 -*-

import datetime
import random

from django.shortcuts import render


def index(request):
    return render(request, 'app6_index.html')


def filters(request):

    context = {}

    # filter: random, pluralize, length_is, join
    context['people'] = (
        'Mr Black',
        'Mr Pink',
        'Mr White',
        'Mr Pinkman',
        'Yellow Bioman'
    )

    # filter: add
    context['number'] = random.randint(1, 2)

    # filter: intcomma
    context['money'] = 1000000000

    # filter: pluralize
    context['random_people'] = context['people'][0:context['number']]

    # filter: date
    context['today'] = datetime.datetime.now()

    # filter: title
    context['quote'] = "all your bases are belong to us"

    # filter: striptags, safe
    context['html'] = '<a id="me" href="#me">Look at <strong>me !</strong></a>'

    # filter: yesno
    context['answer'] = random.choice((True, False, None))

    # filter: urlizetrunc
    context['url'] = 'http://averylongurltodisplayastruncated.com/index?foo=bar'

    # filter: truncatewords
    context['phrase'] = '''
    A very very very long phrase that we shall truncate so it doesn't get
    to long to read or mess up the layout of our beloved and wonderlful
    website. Did I mentioned I love platipus ?
    '''

    return render(request, 'app6_filters.html', context)


def tags(request):

    context = {}

    # tag: if
    context['answer'] = random.choice((True, False, None))

    # tag: if
    context['number'] = random.randint(1, 2)

    # filter: for
    context['people'] = (
        'Mr Black',
        'Mr Pink',
        'Mr White',
        'Mr Pinkman',
        'Yellow Bioman'
    )

    # filter: for
    context['teams'] = {
        "A": context['people'][:3],
        "B": context['people'][3:],
    }

    return render(request, 'app6_tags.html', context)


def inheritance(request):
    return render(request, 'app6_inheritance.html')


def includes(request):
    return render(request, 'app6_includes.html')