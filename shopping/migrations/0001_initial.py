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
                ('category', models.CharField(help_text=b'Category of Product, eg. Apparels,Clothing', max_length=200)),
                ('image', models.ImageField(help_text=b'Image of the category. It is displayed on the front page. It depicts the category of product', height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_cat)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('category_description', models.TextField(help_text=b'Description of the category in 400 characters.It is displayed on the front page', max_length=400)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'category', unique=True, editable=False)),
                ('link_text', models.CharField(help_text=b'This text is used for linking the url of the category, eg. Buy Now, Shop Now. ', max_length=100)),
            ],
            options={
                'verbose_name': 'Categories of Products(Add here)',
                'verbose_name_plural': 'Categories of Products(Add here)',
            },
        ),
        migrations.CreateModel(
            name='DetailsOfProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribute', models.CharField(help_text=b'Product description attributes eg, weight, material etc', max_length=70)),
                ('value', models.CharField(help_text=b'Values of the product description attribute', max_length=100)),
            ],
            options={
                'verbose_name': 'Details of Products',
                'verbose_name_plural': 'Details of Products',
            },
        ),
        migrations.CreateModel(
            name='ImagesOfProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(help_text=b'Image showing the different views of the product', height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_pro)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Images of products',
                'verbose_name_plural': 'Images of products',
            },
        ),
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name of the product, eg.T-shirt, Cup, Hoody, etc.', max_length=250)),
                ('description', models.TextField(help_text=b"Product description here. Don't include size and color information. Write about product quality , specification, material etc.", null=True, blank=True)),
                ('price', models.PositiveIntegerField(help_text=b'The price of the product in positive integers')),
                ('stockcount', models.PositiveIntegerField(default=0, help_text=b'The number of items which are available in the stock')),
                ('gender', models.CharField(help_text=b'Gender for whom this product is meant for.', max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Unisex', b'Unisex'), (b'0', b'N/A')])),
                ('new_product', models.BooleanField(default=False, help_text=b'Wether this product is newly added or not. New products are separately displayed on the front page.')),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, editable=False)),
                ('category', models.ForeignKey(related_name='products_desc', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='shopping.Categories', help_text=b'Choose the category of product.', null=True)),
            ],
            options={
                'verbose_name': 'Description of the product(Add here)',
                'verbose_name_plural': 'Description of the product(Add here)',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(help_text=b'Size of the product.', max_length=5, choices=[(b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL'), (b'0', b'N/A')])),
                ('color', models.CharField(help_text=b'Color of the product', max_length=30)),
                ('stockcount', models.PositiveIntegerField(default=0, help_text=b'The number of items which are available in the stock')),
                ('product', models.ForeignKey(related_name='prod', to='shopping.ProductDescription', null=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(help_text=b'Images to be displayed on the slider', height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_sli)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('header', models.CharField(help_text=b'The heading to be displayed on the slider.', max_length=100)),
                ('content', models.CharField(help_text=b'The text content which is to be displayed on the slider.', max_length=150)),
                ('link_text', models.CharField(help_text=b'The text which is used to link the url, eg. Buy Now, Shop here .', max_length=100)),
                ('link', models.URLField(help_text=b'The link of the product or category which is targeted to.')),
                ('alignment', models.CharField(default=b'left', help_text=b'How you wish the text to appear on the slider?', max_length=10, choices=[(b'center', b'center'), (b'left', b'left'), (b'right', b'right')])),
            ],
            options={
                'verbose_name': 'Images on the slider',
                'verbose_name_plural': 'Images on the slider',
            },
        ),
        migrations.AddField(
            model_name='imagesofproducts',
            name='product',
            field=models.ForeignKey(related_name='productimages', to='shopping.Products'),
        ),
        migrations.AddField(
            model_name='detailsofproducts',
            name='product',
            field=models.ForeignKey(related_name='productdetails', to='shopping.ProductDescription', null=True),
        ),
    ]
