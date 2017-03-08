# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20170308_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdescription',
            name='price',
            field=models.PositiveIntegerField(default=0, help_text=b'The price of the product in positive integers'),
        ),
    ]
