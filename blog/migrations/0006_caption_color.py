# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='caption',
            name='color',
            field=models.CharField(default='white', max_length=15),
        ),
    ]
