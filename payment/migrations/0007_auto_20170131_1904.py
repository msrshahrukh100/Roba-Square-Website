# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping', '0004_auto_20170129_1236'),
        ('payment', '0006_auto_20170131_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyingCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=5)),
                ('quantity', models.CharField(max_length=3)),
                ('price', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('phonenumber', models.CharField(max_length=15)),
                ('method_of_payment', models.CharField(max_length=20)),
                ('instamojo_request_id', models.CharField(max_length=150, null=True, blank=True)),
                ('status', models.CharField(default=b'Pending', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(related_name='buying_cart', to='shopping.ProductDescription')),
                ('user', models.ForeignKey(related_name='user_bought_cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='onlinebuyingcart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='onlinebuyingcart',
            name='user',
        ),
        migrations.DeleteModel(
            name='OnlineBuyingCart',
        ),
    ]
