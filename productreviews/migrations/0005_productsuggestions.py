# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productreviews', '0004_reviews_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSuggestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
        ),
    ]
