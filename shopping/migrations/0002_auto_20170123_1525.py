# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import shopping.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=sorl.thumbnail.fields.ImageField(help_text=b'Image of the category. It is displayed on the front page. It depicts the category of product', height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_cat),
        ),
        migrations.AlterField(
            model_name='imagesofproducts',
            name='image',
            field=sorl.thumbnail.fields.ImageField(help_text=b'Image showing the different views of the product', height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_pro),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=sorl.thumbnail.fields.ImageField(help_text=b'Images to be displayed on the slider', height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_sli),
        ),
    ]
