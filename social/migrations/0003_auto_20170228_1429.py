# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_picoftheweek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picoftheweek',
            name='publish_it',
            field=models.BooleanField(default=False),
        ),
    ]
