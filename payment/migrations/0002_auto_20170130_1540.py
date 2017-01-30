# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onlinetransactionsdetail',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='onlinetransactionsdetail',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 30, 10, 9, 59, 995065, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
