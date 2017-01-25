# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170125_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='about_the_author',
            field=models.CharField(max_length=200, null=True, verbose_name=b"Write about yourself, which you want to be displayed in the 'About the Author' section", blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='show_about_the_author',
            field=models.BooleanField(default=True, verbose_name=b"Select if u wish to display the 'About the Author' section along with your post"),
        ),
    ]
