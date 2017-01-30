# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_auto_20170129_1236'),
        ('payment', '0003_onlinetransactionsdetail_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyingCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=5)),
                ('quantity', models.CharField(max_length=3)),
                ('instamojo_request_id', models.CharField(max_length=150)),
                ('product', models.ForeignKey(related_name='buying_cart', to='shopping.ProductDescription')),
            ],
        ),
    ]
