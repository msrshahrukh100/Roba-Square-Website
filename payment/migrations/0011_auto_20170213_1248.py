# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0010_auto_20170212_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refund_requests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(max_length=200)),
                ('refund_amount_to_user', models.BooleanField(default=False, help_text=b"Setting this field to true refunds the amount to the user's account.Set it to true only after you receive the products")),
                ('refund_item', models.ForeignKey(related_name='refunds', to='payment.BuyingCart')),
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
        migrations.RemoveField(
            model_name='refunds',
            name='refund_item',
        ),
        migrations.DeleteModel(
            name='Refunds',
        ),
    ]
