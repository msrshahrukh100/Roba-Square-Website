# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20170120_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailsOfProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribute', models.CharField(help_text=b'Product description attributes eg, weight, material etc', max_length=70)),
                ('value', models.CharField(help_text=b'Values of the product description attribute', max_length=100)),
                ('product', models.ForeignKey(related_name='productdetails', to='shopping.ProductDescription', null=True)),
            ],
        ),
    ]
