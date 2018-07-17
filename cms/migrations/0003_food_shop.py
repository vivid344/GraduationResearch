# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-10-14 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_remove_food_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='Shop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Shop', to='cms.Shop', verbose_name='店舗'),
        ),
    ]