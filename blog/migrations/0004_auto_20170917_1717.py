# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170917_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail_path',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
