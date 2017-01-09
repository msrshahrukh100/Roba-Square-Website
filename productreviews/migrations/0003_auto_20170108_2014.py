# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productreviews', '0002_auto_20170108_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='rating',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='review',
            field=models.TextField(null=True, blank=True),
        ),
    ]
