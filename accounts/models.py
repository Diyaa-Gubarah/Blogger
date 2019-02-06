# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import PermissionsMixin, User
from django.db import models

# Create your models here.
class User(User, PermissionsMixin):

    def __str__(self):
        return "{}".format(self.username)
