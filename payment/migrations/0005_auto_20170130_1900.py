# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0004_buyingcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyingcart',
            name='status',
            field=models.CharField(default=b'Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='buyingcart',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 30, 13, 30, 33, 287445, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyingcart',
            name='user',
            field=models.ForeignKey(related_name='user_bought_cart', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
