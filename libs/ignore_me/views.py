# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import os

from django.shortcuts import render
from django.conf import settings


def index(request):
    p = re.compile(r'^app\d+_')
    apps = (a.split('_') for a in settings.INSTALLED_APPS if p.match(a))

    return render(request, 'ignore_me/index.html',
                  {"apps": sorted(apps), "settings": settings})
