# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20170125_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='showdob',
            field=models.BooleanField(default=True),
        ),
    ]
