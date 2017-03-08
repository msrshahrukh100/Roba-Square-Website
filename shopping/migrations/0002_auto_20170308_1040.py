# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdescription',
            name='actual_price',
            field=models.PositiveIntegerField(default=0, help_text=b'The actual price of the product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productdescription',
            name='discount_percent',
            field=models.PositiveIntegerField(default=0, help_text=b'Percentage of discount provided'),
            preserve_default=False,
        ),
    ]
