# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import authentication.models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='change_profile_pic',
            field=sorl.thumbnail.fields.ImageField(default=b'default.jpg', height_field=b'height_field', width_field=b'width_field', upload_to=authentication.models.upload_location_user, blank=True, null=True),
        ),
    ]
