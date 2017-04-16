# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='show_about_the_author',
            field=models.BooleanField(default=True, verbose_name=b"Select if you wish to display the 'About the Author' section along with your post"),
        ),
    ]
