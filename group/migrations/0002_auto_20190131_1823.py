# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-31 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='slug_name',
            new_name='slug',
        ),
    ]
