# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_productdescription_has_logo_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.CharField(help_text=b'Color of the product', max_length=30, null=True, blank=True),
        ),
    ]
