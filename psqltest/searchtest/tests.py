# -*- coding: utf-8 -*-
from django.test import TestCase

from .models import Page


class SearchTest(TestCase):

    def test_search(self):
        Page.objects.create(name='Главная', description='главная')
        Page.objects.create(name='неглавная', description='неглавная')
        pages = Page.objects.search("главная")
        print(pages)
        assert len(pages) == 1
        pages = Page.objects.search(query="главное | неглавное", raw=True)
        print(pages)
        assert len(pages) == 2
