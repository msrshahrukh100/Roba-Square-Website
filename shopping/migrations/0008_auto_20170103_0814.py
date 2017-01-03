# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0007_auto_20170103_0738'),
    ]

    operations = [
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
                ('link', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='shopping.Categories', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product_description',
            name='category',
        ),
        migrations.AlterField(
            model_name='products',
            name='product',
            field=models.ForeignKey(related_name='prod', to='shopping.ProductDescription', null=True),
        ),
        migrations.DeleteModel(
            name='Product_Description',
        ),
    ]
