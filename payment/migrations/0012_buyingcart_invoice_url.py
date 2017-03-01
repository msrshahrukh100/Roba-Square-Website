# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_auto_20170213_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyingcart',
            name='invoice_url',
            field=models.URLField(default=b'/'),
        ),
    ]
