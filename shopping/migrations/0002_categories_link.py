# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='link',
            field=models.URLField(default='asdsa', max_length=300),
            preserve_default=False,
        ),
    ]
