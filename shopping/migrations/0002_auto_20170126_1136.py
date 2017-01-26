# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRelationsForLogo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='productdescription',
            name='has_logo',
            field=models.BooleanField(default=False, help_text=b'Check it if the product has logo and is to be shown to the user separately'),
        ),
        migrations.AddField(
            model_name='productrelationsforlogo',
            name='product',
            field=models.ForeignKey(related_name='relatedproduct', to='shopping.ProductDescription', help_text=b'Chose the product which has a logo version of itself.'),
        ),
        migrations.AddField(
            model_name='productrelationsforlogo',
            name='related_to',
            field=models.ForeignKey(related_name='havinglogo', to='shopping.ProductDescription', help_text=b'Choose the product that has a logo.'),
        ),
    ]
