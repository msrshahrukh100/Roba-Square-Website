# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import blog.models
from django.conf import settings
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSlider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageField(help_text=b'Images to be displayed on the slider', height_field=b'height_field', width_field=b'width_field', upload_to=blog.models.upload_location_blog_promotion)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('header', models.CharField(help_text=b'The heading to be displayed on the slider.', max_length=100)),
                ('content', models.CharField(help_text=b'The text content which is to be displayed on the slider.', max_length=150)),
                ('link_text', models.CharField(help_text=b'The text which is used to link the url, eg. Buy Now, Shop here .', max_length=100)),
                ('link', models.URLField(help_text=b'The link of the product or category which is targeted to.')),
                ('alignment', models.CharField(default=b'left', help_text=b'How you wish the text to appear on the slider?', max_length=10, choices=[(b'center', b'center'), (b'left', b'left'), (b'right', b'right')])),
            ],
            options={
                'verbose_name': 'Images on the blog promotion slider',
                'verbose_name_plural': 'Images on the blog promotion slider',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'title', unique=True, editable=False)),
                ('image', models.ImageField(height_field=b'height_field', width_field=b'width_field', upload_to=blog.models.upload_location, blank=True, help_text=b'A landscape image ie width greater than height for the parallax', null=True)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('publish_it', models.BooleanField(default=False)),
                ('draft', models.BooleanField(default=False, verbose_name=b'Select if it is a draft. Draft posts are not published.')),
                ('show_about_the_author', models.BooleanField(default=True, verbose_name=b"Select if u wish to display the 'About the Author' section along with your post")),
                ('about_the_author', models.CharField(max_length=200, null=True, verbose_name=b"Write about yourself, which you want to be displayed in the 'About the Author' section", blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='userblogposts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='PostViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=100)),
                ('session', models.CharField(max_length=100)),
                ('viewed_on', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(related_name='postviews', to='blog.Post')),
                ('user', models.ForeignKey(related_name='userblogviewed', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
