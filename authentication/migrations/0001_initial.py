# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import authentication.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change_profile_pic', models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=authentication.models.upload_location_user, blank=True)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('date_of_birth', models.CharField(max_length=20, null=True, blank=True)),
                ('phonenumber', models.CharField(max_length=15, null=True, blank=True)),
                ('profession', models.CharField(max_length=100, null=True, blank=True)),
                ('name_of_institute', models.CharField(max_length=200, null=True, blank=True)),
                ('user', models.OneToOneField(related_name='user_information', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
