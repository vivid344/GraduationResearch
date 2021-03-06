# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-12-18 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0025_auto_20171217_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(default=1, max_length=8000, verbose_name='レビュー')),
                ('shop', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='review_shop', to='cms.Shop', verbose_name='店舗')),
            ],
        ),
        migrations.AlterField(
            model_name='food',
            name='shop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='food_shop', to='cms.Shop', verbose_name='店舗'),
        ),
    ]
