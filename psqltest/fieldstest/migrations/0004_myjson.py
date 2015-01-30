# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.serializers.json
import decimal
import postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fieldstest', '0003_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyJson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('json', postgres.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
            ],
        ),
    ]
