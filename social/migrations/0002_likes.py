# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_auto_20170122_1854'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(related_name='productlikes', to='shopping.ProductDescription')),
                ('user', models.ForeignKey(related_name='userlikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
