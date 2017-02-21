# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping', '0004_auto_20170129_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkOrders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.CharField(max_length=20)),
                ('base', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('user', models.ForeignKey(related_name='bulkorders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
