# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20170103_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesofproducts',
            name='product',
            field=models.ForeignKey(related_name='productimages', to='shopping.Products'),
        ),
    ]
