# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import shopping.models


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
                ('category_description', models.CharField(max_length=300)),
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
            name='Product_Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(null=True, blank=True)),
                ('price', models.PositiveIntegerField()),
                ('stockcount', models.PositiveIntegerField(default=0)),
                ('gender', models.CharField(max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Unisex', b'Unisex'), (b'0', b'Not Applicable')])),
                ('new_product', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='shopping.Categories', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=5, choices=[(b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL')])),
                ('color', models.CharField(max_length=30)),
                ('stockcount', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(to='shopping.Product_Description', null=True)),
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
            field=models.ForeignKey(related_name='products', to='shopping.Products'),
        ),
    ]
