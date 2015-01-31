from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField
from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    search_index = VectorField()

    objects = SearchManager(
        fields=('name', 'description'),
        config='pg_catalog.russian',
        search_field='search_index',
        auto_update_search_field = True
    )
