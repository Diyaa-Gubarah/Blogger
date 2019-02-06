# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from post.models import Post,Like
# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
