# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0012_buyingcart_invoice_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refund_requests',
            name='refund_item',
            field=models.ForeignKey(related_name='refunds', on_delete=django.db.models.deletion.DO_NOTHING, to='payment.BuyingCart'),
        ),
    ]
