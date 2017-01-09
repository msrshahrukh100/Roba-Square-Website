# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productreviews', '0005_productsuggestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsuggestions',
            name='user',
            field=models.ForeignKey(related_name='suggestions', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
