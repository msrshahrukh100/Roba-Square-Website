# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productreviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='content',
            new_name='review',
        ),
    ]
