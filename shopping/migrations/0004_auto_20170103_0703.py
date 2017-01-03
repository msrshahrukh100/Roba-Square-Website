# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_auto_20170103_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_description',
            name='gender',
            field=models.CharField(max_length=5, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Unisex', b'Unisex'), (b'0', b'N/A')]),
        ),
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(max_length=5, choices=[(b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL'), (b'0', b'N/A')]),
        ),
    ]
