# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-04 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_auto_20190204_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('-created_at',), 'permissions': (('greate_group', 'Can greate group'), ('add_post', 'Can add post to group'), ('delete_post', 'Can delete post in group'), ('update_post', 'Can update post in group'))},
        ),
    ]
