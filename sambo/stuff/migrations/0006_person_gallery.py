# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-04 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
        ('stuff', '0005_auto_20180304_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Gallery', verbose_name='Галлерея'),
        ),
    ]
