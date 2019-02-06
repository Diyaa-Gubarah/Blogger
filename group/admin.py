# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from group import models

# Register your models here.
admin.site.register(models.Group)
admin.site.register(models.Membership)
