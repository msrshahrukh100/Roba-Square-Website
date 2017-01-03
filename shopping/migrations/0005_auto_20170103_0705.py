# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_auto_20170103_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_description',
            name='gender',
            field=models.CharField(max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Unisex', b'Unisex'), (b'0', b'N/A')]),
        ),
    ]
