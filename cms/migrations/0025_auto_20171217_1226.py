# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-12-17 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0024_shop_shopname'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='birth_val',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='food',
            name='only_val',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
