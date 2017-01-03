# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20170103_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='link',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='link_text',
        ),
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='asas', editable=False, populate_from=b'category', unique=True),
            preserve_default=False,
        ),
    ]
