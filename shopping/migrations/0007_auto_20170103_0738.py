# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_auto_20170103_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product',
            field=models.ForeignKey(related_name='prod', to='shopping.Product_Description', null=True),
        ),
    ]
