# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-12-12 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_remove_shop_shopname'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shopname',
            field=models.CharField(default=1, max_length=255, verbose_name='店名'),
        ),
    ]
