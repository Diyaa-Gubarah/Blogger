# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-04 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20190203_1647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'permissions': (('add_like_to_post', 'Can add like to post'), ('remove_like', 'Can remove like from post'))},
        ),
    ]