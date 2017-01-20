# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import shopping.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Categories of Products(Add here)', 'verbose_name_plural': 'Categories of Products(Add here)'},
        ),
        migrations.AlterModelOptions(
            name='imagesofproducts',
            options={'verbose_name': 'Images of products', 'verbose_name_plural': 'Images of products'},
        ),
        migrations.AlterModelOptions(
            name='productdescription',
            options={'verbose_name': 'Description of the product(Add here)', 'verbose_name_plural': 'Description of the product(Add here)'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Images on the slider', 'verbose_name_plural': 'Images on the slider'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='category',
            field=models.CharField(help_text=b'Category of Product, eg. Apparels,Clothing', max_length=200),
        ),
        migrations.AlterField(
            model_name='categories',
            name='category_description',
            field=models.TextField(help_text=b'Description of the category in 400 characters.It is displayed on the front page', max_length=400),
        ),
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(help_text=b'Image of the category. It is displayed on the front page. It depicts the category of product', height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_cat),
        ),
        migrations.AlterField(
            model_name='categories',
            name='link_text',
            field=models.CharField(help_text=b'This text is used for linking the url of the category, eg. Buy Now, Shop Now. ', max_length=100),
        ),
        migrations.AlterField(
            model_name='imagesofproducts',
            name='image',
            field=models.ImageField(help_text=b'Image showing the different views of the product', height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_pro),
        ),
        migrations.AlterField(
            model_name='productdescription',
            name='category',
            field=models.ForeignKey(related_name='products_desc', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='shopping.Categories', help_text=b'Choose the category of product.', null=True),
        ),
        migrations.AlterField(
            model_name='productdescription',
            name='description',
            field=models.TextField(help_text=b"Product description here. Don't include size and color information. Write about product quality , specification, material etc.", null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='productdescription',
            name='gender',
            field=models.CharField(help_text=b'Gender for whom this product is meant for.', max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Unisex', b'Unisex'), (b'0', b'N/A')]),
        ),
        migrations.AlterField(
            model_name='productdescription',
            name='name',
            field=models.CharField(help_text=b'Name of the product, eg.T-shirt, Cup, Hoody, etc.', max_length=250),
        ),
        migrations.AlterField(
            model_name='productdescription',
            name='new_product',
            field=models.BooleanField(default=False, help_text=b'Wether this product is newly added or not. New products are separately displayed on the front page.'),
        ),
        migrations.AlterField(
            model_name='productdescription',
            name='price',
            field=models.PositiveIntegerField(help_text=b'The price of the product in positive integers'),
        ),
        migrations.AlterField(
            model_name='productdescription',
            name='stockcount',
            field=models.PositiveIntegerField(default=0, help_text=b'The number of items which are available in the stock'),
        ),
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.CharField(help_text=b'Color of the product', max_length=30),
        ),
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(help_text=b'Size of the product.', max_length=5, choices=[(b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL'), (b'0', b'N/A')]),
        ),
        migrations.AlterField(
            model_name='products',
            name='stockcount',
            field=models.PositiveIntegerField(default=0, help_text=b'The number of items which are available in the stock'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='alignment',
            field=models.CharField(default=b'left', help_text=b'How you wish the text to appear on the slider?', max_length=10, choices=[(b'center', b'center'), (b'left', b'left'), (b'right', b'right')]),
        ),
        migrations.AlterField(
            model_name='slider',
            name='content',
            field=models.CharField(help_text=b'The text content which is to be displayed on the slider.', max_length=150),
        ),
        migrations.AlterField(
            model_name='slider',
            name='header',
            field=models.CharField(help_text=b'The heading to be displayed on the slider.', max_length=100),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(help_text=b'Images to be displayed on the slider', height_field=b'height_field', width_field=b'width_field', upload_to=shopping.models.upload_location_sli),
        ),
        migrations.AlterField(
            model_name='slider',
            name='link',
            field=models.URLField(help_text=b'The link of the product or category which is targeted to.'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='link_text',
            field=models.CharField(help_text=b'The text which is used to link the url, eg. Buy Now, Shop here .', max_length=100),
        ),
    ]
