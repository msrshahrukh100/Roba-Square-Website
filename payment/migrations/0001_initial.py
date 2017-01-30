# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineTransactionsDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.CharField(max_length=200)),
                ('buyer', models.EmailField(max_length=200)),
                ('buyer_name', models.CharField(max_length=200)),
                ('buyer_phone', models.CharField(max_length=15, null=True, blank=True)),
                ('currency', models.CharField(max_length=5)),
                ('fees', models.CharField(max_length=100)),
                ('longurl', models.URLField()),
                ('mac', models.CharField(max_length=100)),
                ('payment_id', models.CharField(max_length=150)),
                ('payment_request_id', models.CharField(max_length=150)),
                ('purpose', models.CharField(max_length=250)),
                ('shorturl', models.URLField(max_length=100)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
