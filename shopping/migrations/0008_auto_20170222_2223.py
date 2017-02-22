# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import shopping.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0007_auto_20170221_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkorders',
            name='image',
            field=sorl.thumbnail.fields.ImageField(help_text=b'Image of the design', height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_bulk),
        ),
    ]
