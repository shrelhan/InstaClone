# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20171119_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=120),
        ),
    ]
