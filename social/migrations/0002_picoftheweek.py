# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import social.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicOfTheWeek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=300)),
                ('image', sorl.thumbnail.fields.ImageField(help_text=b'Image for pic of the week', height_field=b'height_field', width_field=b'width_field', upload_to=social.models.upload_location_picoftheweek)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('publish_it', models.BooleanField(default=True)),
                ('user', models.ForeignKey(related_name='picoftheweek', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
