#!/usr/bin/env python
# coding: utf-8
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
            ('prefix/', 'pr\w?fix'),
            ('world/', 'world'),
            ('You/', 'you'),
            ('You/Hey/', 'hey'),
            ('hello_from_app1/', 'hello'),
            ('app2_included/', 'hello')
        )

        for link, world in links:
            self.assertInResponse(link, response)
            link_response = self.client.get('/app3/' + link)
            self.assertInResponse(world, link_response)
