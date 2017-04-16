# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170322_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postviews',
            name='session',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
