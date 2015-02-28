import uuid
from django.contrib.postgres import fields
from django.db import models

from postgres.fields import json_field


class Event(models.Model):
    name = models.CharField(max_length=50)
    ages = fields.ranges.IntegerRangeField()


class Post(models.Model):
    name = models.CharField(max_length=50)
    tags = fields.array.ArrayField(models.CharField(max_length=20))


class Location(models.Model):
    name = models.CharField(max_length=50)
    location = fields.hstore.HStoreField()


class MyJson(models.Model):
    json = json_field.JSONField()


class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
