# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-02 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='has_like',
            field=models.BooleanField(default=False),
        ),
    ]
