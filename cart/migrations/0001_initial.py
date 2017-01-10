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
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('products', models.ForeignKey(related_name='incart', to='shopping.ProductDescription')),
                ('user', models.ForeignKey(related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('products', models.ForeignKey(related_name='inwishlist', to='shopping.ProductDescription')),
                ('user', models.ForeignKey(related_name='wishlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
