# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_auto_20170103_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_description',
            field=models.TextField(max_length=400),
        ),
    ]
