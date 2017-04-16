# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170317_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postviews',
            name='user',
            field=models.ForeignKey(related_name='userblogviewed', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
