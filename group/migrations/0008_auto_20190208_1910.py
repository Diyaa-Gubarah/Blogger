# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-08 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0007_auto_20190204_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_joined',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
