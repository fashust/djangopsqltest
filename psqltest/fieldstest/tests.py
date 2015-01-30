from django.test import TestCase
from psycopg2.extras import NumericRange

from .models import Event, Post, Location, MyJson


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


class HstoreTest(TestCase):

    def test_hstore(self):
        # create
        Location.objects.create(
            name='Minsk', location={'lat': '53.900000000000000000',
                                    'long': '27.566666700000040000'})
        Location.objects.create(
            name='Kyiv', location={'lat': '50.450100000000000000',
                                   'long': '30.523400000000038000'})

        print([l.name for l in Location.objects.filter(
            location__lat__contains='50')])
        # >> [u'Kyiv']

        print([l.name for l in Location.objects.filter(
            location__contained_by={
                'lat': '53.900000000000000000',
                'long': '27.566666700000040000',
                'timezone': 'any'
            })])
        # >> [u'Minsk']


class JsonbTest(TestCase):

    def test_jsonfield(self):
        MyJson.objects.create(json={'a': 1, 'b': {'c': 2, 'd': 3}})
        MyJson.objects.create(json={'d': 3, 'b': {'c': 4, 'f': 5}})

        print([m.json for m in
               MyJson.objects.filter(json__has_all=['a', 'b'])])
        # >> [{u'a': 1, u'b': {u'c': 2, u'd': 3}}]

        print([m.json for m in
               MyJson.objects.filter(json__path_b_c__gt=2)])
        # >> [{u'b': {u'c': 4, u'f': 5}, u'd': 3}]
