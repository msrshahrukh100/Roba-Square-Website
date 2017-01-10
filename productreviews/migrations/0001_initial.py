# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSuggestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('user', models.ForeignKey(related_name='suggestions', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review', models.TextField(null=True, blank=True)),
                ('rating', models.PositiveIntegerField(null=True, blank=True)),
                ('product', models.ForeignKey(related_name='reviews', to='shopping.ProductDescription')),
                ('user', models.ForeignKey(related_name='userreviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
