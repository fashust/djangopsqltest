from django.contrib.postgres import fields
from django.db import models


class Hotel(models.Model):
    title = models.CharField(max_length=200)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel)
    title = models.CharField(max_length=200)


class Booking(models.Model):
    room = models.ForeignKey(Room)
    dates = fields.ranges.DateRangeField()
