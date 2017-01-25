# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='about_the_author',
            field=models.CharField(help_text=b"Optional. Write about yourself which you want to display in the 'About the Author' section.", max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='show_about_the_author',
            field=models.BooleanField(default=True, help_text=b"Select if you want 'About the author' section to be shown along with your post."),
        ),
    ]
