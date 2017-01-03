# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_auto_20170103_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='link_text',
            field=models.CharField(default='linl', max_length=100),
            preserve_default=False,
        ),
    ]
