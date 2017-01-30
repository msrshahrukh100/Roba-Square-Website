# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0002_auto_20170130_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinetransactionsdetail',
            name='user',
            field=models.ForeignKey(related_name='online_transactions', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
