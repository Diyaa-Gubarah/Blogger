# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-02 17:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_remove_group_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_member', to=settings.AUTH_USER_MODEL),
        ),
    ]