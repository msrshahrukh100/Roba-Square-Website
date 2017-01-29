# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170125_1830'),
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
    ]
