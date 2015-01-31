import datetime

from django.test import TestCase
from psycopg2.extras import DateRange

from .models import Hotel, Room, Booking


class BookingTest(TestCase):

    def test_find_overlap(self):
        # create
        hotel = Hotel.objects.create(title='hotel')
        room = Room.objects.create(hotel=hotel, title='room')

        day = datetime.timedelta(days=1)
        date1 = (datetime.datetime.now() + datetime.timedelta(days=7)).date()
        date2 = date1 + day

        Booking.objects.create(room=room, dates=(date1, date2))
        Booking.objects.create(room=room, dates=(date1, date2 + day))
        # find overlapping bookings
        print([b for b in Booking.objects.filter(
            dates__overlap=DateRange(date2, date2 + day, bounds='[)'))])
        # >> [<Booking: Booking object>]
        assert len(Booking.objects.filter(
            dates__overlap=DateRange(date2, date2 + day, bounds='[)'))) == 1
