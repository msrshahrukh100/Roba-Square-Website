# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0013_auto_20170301_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyingcart',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]
