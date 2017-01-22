# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0003_auto_20170121_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=30)),
                ('pincode', models.PositiveIntegerField()),
                ('nearest_landmark', models.CharField(max_length=200, null=True, blank=True)),
                ('user', models.ForeignKey(related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
