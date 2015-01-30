from django.test import TestCase

from .models import Page


class SearchTest(TestCase):

    def test_search(self):
        Page.objects.create(name='Home', description='Home page')
        Page.objects.create(name='About', description='About the site')
        print(Page.objects.search("home"))
        # >> [<Page: Page object>]
        print(Page.objects.search(query="page | site", raw=True))
        # >> [<Page: Page object>, <Page: Page object>]
