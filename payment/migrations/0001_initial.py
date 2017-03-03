# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('paymentid', models.CharField(max_length=150, null=True, blank=True)),
                ('cod_unique_id', models.CharField(max_length=150, null=True, blank=True)),
                ('status', models.CharField(default=b'Pending', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('invoice_url', models.URLField(default=b'/')),
                ('returned', models.BooleanField(default=False)),
                ('product', models.ForeignKey(related_name='buying_cart', to='shopping.ProductDescription')),
                ('user', models.ForeignKey(related_name='user_bought_cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OnlineTransactionsDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.CharField(max_length=200)),
                ('buyer', models.EmailField(max_length=200)),
                ('buyer_name', models.CharField(max_length=200)),
                ('buyer_phone', models.CharField(max_length=15, null=True, blank=True)),
                ('currency', models.CharField(max_length=5)),
                ('fees', models.CharField(max_length=100)),
                ('longurl', models.URLField()),
                ('mac', models.CharField(max_length=100)),
                ('payment_id', models.CharField(max_length=150)),
                ('payment_request_id', models.CharField(max_length=150)),
                ('purpose', models.CharField(max_length=250)),
                ('shorturl', models.URLField(max_length=100)),
                ('status', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='online_transactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Refund_requests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(max_length=200)),
                ('refund_amount_to_user', models.BooleanField(default=False, help_text=b"Setting this field to true refunds the amount to the user's account.Set it to true only after you receive the products")),
                ('refund_item', models.ForeignKey(related_name='refunds', on_delete=django.db.models.deletion.DO_NOTHING, to='payment.BuyingCart')),
                ('user', models.ForeignKey(related_name='refundrequest', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RefundsHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('refundid', models.CharField(max_length=50)),
                ('payment_id', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=20)),
                ('refundtype', models.CharField(max_length=5)),
                ('body', models.CharField(max_length=200)),
                ('refund_amount', models.CharField(max_length=50)),
                ('total_amount', models.CharField(max_length=50)),
                ('created_at', models.CharField(max_length=100)),
                ('user', models.ForeignKey(related_name='refundhistory', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
