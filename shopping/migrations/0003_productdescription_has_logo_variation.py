# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20170126_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdescription',
            name='has_logo_variation',
            field=models.BooleanField(default=True, help_text=b'Check it if the product has a logo variation of itself.'),
        ),
    ]
