# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-31 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_group_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='photo',
        ),
    ]