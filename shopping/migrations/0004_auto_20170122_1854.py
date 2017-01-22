# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_detailsofproducts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailsofproducts',
            options={'verbose_name': 'Details of Products', 'verbose_name_plural': 'Details of Products'},
        ),
    ]
