# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_auto_20170211_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyingcart',
            name='paymentid',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='refunds',
            name='refund_amount_to_user',
            field=models.BooleanField(default=False, help_text=b'Setting this field to true refunds the amount to the user.'),
        ),
    ]
