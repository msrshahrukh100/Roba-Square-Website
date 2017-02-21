# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import shopping.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_bulkorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkorders',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bulkorders',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=1, height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_bulk, help_text=b'Images to be displayed on the slider'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bulkorders',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
