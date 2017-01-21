# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20170120_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='showfollowers',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='showfollowing',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='showrecentlyviewed',
            field=models.BooleanField(default=True),
        ),
    ]
