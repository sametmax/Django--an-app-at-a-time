#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

from __future__ import unicode_literals, absolute_import

import re

from django.test import TestCase
from django.conf import settings


class SimpleAppsTest(TestCase):

    def assertInResponse(self, text, response, flags=re.U|re.I):
        return self.assertTrue(re.search(text,
                               response.content.decode('utf8'),
                               flags=flags))


    def assertGetReturns(self, url, text):
        return self.assertInResponse(text, self.client.get(url))


    def test_home(self):

        response = self.client.get("/")

        for app in settings.INSTALLED_APPS:
            if app.startswith('app'):
                self.assertInResponse(app.split('_')[0].title(), response)


    def test_app1(self):
        self.assertGetReturns('/app1/', "Hello world")


    def test_app2(self):
        self.assertGetReturns('/app2/', "Hello world")


    def test_app3(self):

        response = self.client.get("/app3/")

        links = (
            'prefix/',
            'world/',
            'You/',
            'You/Hey/'
        )

        self.assertTrue(self.client.get('/app3/' + links[0]).status_code == 200)

        for link in links[1:]:
            self.assertInResponse(link, response)
            link_response = self.client.get('/app3/' + link)
            for world in link.split('/'):
                self.assertInResponse(world, link_response)
