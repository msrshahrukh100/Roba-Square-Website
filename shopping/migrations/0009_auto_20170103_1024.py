# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0008_auto_20170103_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_description',
            field=models.TextField(),
        ),
    ]
