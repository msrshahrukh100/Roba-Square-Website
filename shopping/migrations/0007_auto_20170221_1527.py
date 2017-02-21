# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_auto_20170221_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkorders',
            name='quantity',
            field=models.CharField(max_length=10),
        ),
    ]
