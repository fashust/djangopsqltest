from django.db import models


class PoolTestModels(models.Model):

    name = models.CharField(max_length=5)
