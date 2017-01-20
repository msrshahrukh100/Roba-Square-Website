# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productreviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsuggestions',
            options={'verbose_name': 'Product Suggestion', 'verbose_name_plural': 'Product Suggestions'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ['-id'], 'verbose_name': 'Reviews of Products', 'verbose_name_plural': 'Reviews of Products'},
        ),
    ]
