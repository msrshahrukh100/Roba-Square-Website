# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170322_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postviews',
            name='session',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
