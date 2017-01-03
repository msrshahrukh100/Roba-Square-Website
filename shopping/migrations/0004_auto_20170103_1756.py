# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_auto_20170103_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdescription',
            name='category',
            field=models.ForeignKey(related_name='products_desc', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='shopping.Categories', null=True),
        ),
    ]
