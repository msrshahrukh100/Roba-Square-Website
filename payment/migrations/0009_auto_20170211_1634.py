# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_auto_20170131_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refunds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(max_length=200)),
                ('refund_amount_to_user', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='buyingcart',
            name='invoice',
        ),
        migrations.AddField(
            model_name='refunds',
            name='refund_item',
            field=models.ForeignKey(related_name='refunds', to='payment.BuyingCart'),
        ),
    ]
