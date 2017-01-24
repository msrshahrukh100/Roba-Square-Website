# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import blog.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'title', unique=True, editable=False)),
                ('image', models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=blog.models.upload_location, blank=True)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('publish_it', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='userblogposts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
