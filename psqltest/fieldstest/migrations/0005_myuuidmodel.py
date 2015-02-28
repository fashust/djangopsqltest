# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fieldstest', '0004_myjson'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUUIDModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
            ],
        ),
    ]
