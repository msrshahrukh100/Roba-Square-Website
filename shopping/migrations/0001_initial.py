# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import shopping.models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=200)),
                ('image', models.ImageField(height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_cat)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('category_description', models.TextField(max_length=400)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'category', unique=True, editable=False)),
                ('link_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ImagesOfProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_pro)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(null=True, blank=True)),
                ('price', models.PositiveIntegerField()),
                ('stockcount', models.PositiveIntegerField(default=0)),
                ('gender', models.CharField(max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Unisex', b'Unisex'), (b'0', b'N/A')])),
                ('new_product', models.BooleanField(default=False)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, editable=False)),
                ('category', models.ForeignKey(related_name='products_desc', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='shopping.Categories', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=5, choices=[(b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL'), (b'0', b'N/A')])),
                ('color', models.CharField(max_length=30)),
                ('stockcount', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(related_name='prod', to='shopping.ProductDescription', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_sli)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('header', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=150)),
                ('link_text', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('alignment', models.CharField(default=b'left', max_length=10, choices=[(b'center', b'center'), (b'left', b'left'), (b'right', b'right')])),
            ],
        ),
        migrations.AddField(
            model_name='imagesofproducts',
            name='product',
            field=models.ForeignKey(related_name='productimages', to='shopping.Products'),
        ),
    ]
