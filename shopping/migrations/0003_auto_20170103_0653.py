# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_categories_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='link_text',
            field=models.CharField(default='as', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_description',
            name='link',
            field=models.URLField(default='fd'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categories',
            name='link',
            field=models.URLField(),
        ),
    ]
