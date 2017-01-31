# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_auto_20170131_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyingcart',
            name='cod_unique_id',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='buyingcart',
            name='invoice',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
