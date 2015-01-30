from django.test import TestCase
from psycopg2.extras import NumericRange

from .models import Event, Post


class EventTest(TestCase):

    def test_create_query(self):
        # create
        Event.objects.create(name='Meetup', ages=(18, 70))
        Event.objects.create(name='Meetup 2', ages=(10, 30))
        # query
        events = Event.objects.filter(ages__contains=NumericRange(20, 35))
        print([e.name for e in events])
        # [u'Meetup']

        events = Event.objects.filter(ages__contained_by=NumericRange(0, 55))
        print([e.name for e in events])
        # [u'Meetup 2']

        events = Event.objects.filter(ages__overlap=NumericRange(18, 22))
        print([e.name for e in events])
        # [u'Meetup', u'Meetup 2']

    def test_compare(self):
        # create
        Event.objects.create(name='Meetup', ages=(18, 70))
        Event.objects.create(name='Meetup 2', ages=(10, 30))

        events = Event.objects.filter(ages__fully_lt=NumericRange(31, 35))
        print([e.name for e in events])
        # >> [u'Meetup 2']

        events = Event.objects.filter(ages__adjacent_to=NumericRange(70, 80))
        print([e.name for e in events])
        # >> [u'Meetup']
        print("--------------")


class ArrayTest(TestCase):

    def test_array(self):
        # create
        Post.objects.create(name='First post', tags=['thoughts', 'django'])
        Post.objects.create(name='Second post', tags=['thoughts'])
        Post.objects.create(name='Third post', tags=['tutorial', 'django'])

        print([p.name for p in Post.objects.filter(tags__contains=['django'])])
        # >> [u'First post', u'Third post']
        print([p.name for p in Post.objects.filter(
            tags__contains=['django', 'thoughts'])])
        # >> [u'First post']