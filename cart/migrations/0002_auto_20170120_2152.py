# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': "User's Cart", 'verbose_name_plural': "User's Cart"},
        ),
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name': "User's Wishlist", 'verbose_name_plural': "User's Wishlist"},
        ),
    ]
