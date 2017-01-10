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
            name='Connections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('following', models.ForeignKey(related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='socialuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Connection',
                'verbose_name_plural': 'Connections',
            },
        ),
        migrations.CreateModel(
            name='RecentlyViewed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(related_name='rvproducts', to='shopping.ProductDescription')),
                ('user', models.ForeignKey(related_name='recentlyviewed', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'Recently Viewed',
                'verbose_name_plural': 'Recently Viewed',
            },
        ),
        migrations.AlterUniqueTogether(
            name='recentlyviewed',
            unique_together=set([('user', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='connections',
            unique_together=set([('user', 'following')]),
        ),
    ]
