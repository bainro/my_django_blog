# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170917_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=300)),
                ('order', models.IntegerField(blank=True, default=None, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caption', to='blog.Post')),
            ],
        ),
    ]
