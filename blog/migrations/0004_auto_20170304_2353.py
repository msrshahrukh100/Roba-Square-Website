# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170303_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False, verbose_name=b'Select if it is a draft. Draft posts are not published.'),
        ),
    ]
