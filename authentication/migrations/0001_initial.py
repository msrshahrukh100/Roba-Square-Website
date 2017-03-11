# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import autoslug.fields
import authentication.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=30)),
                ('pincode', models.PositiveIntegerField()),
                ('nearest_landmark', models.CharField(max_length=200, null=True, blank=True)),
                ('user', models.ForeignKey(related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change_profile_pic', sorl.thumbnail.fields.ImageField(default=b'default.jpg', height_field=b'height_field', width_field=b'width_field', upload_to=authentication.models.upload_location_user, blank=True, null=True)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('date_of_birth', models.CharField(max_length=20, null=True, blank=True)),
                ('phonenumber', models.CharField(max_length=15, null=True, blank=True)),
                ('profession', models.CharField(max_length=100, null=True, blank=True)),
                ('name_of_institute', models.CharField(max_length=200, null=True, blank=True)),
                ('showrecentlyviewed', models.BooleanField(default=True)),
                ('showfollowers', models.BooleanField(default=True)),
                ('showfollowing', models.BooleanField(default=True)),
                ('showdob', models.BooleanField(default=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'user', unique=True, editable=False)),
                ('user', models.OneToOneField(related_name='user_information', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Information',
                'verbose_name_plural': 'User Information',
            },
        ),
    ]
