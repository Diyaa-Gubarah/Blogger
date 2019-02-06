# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify

User = get_user_model()
# Create your models here.
# https://docs.djangoproject.com/en/1.11/topics/db/models/#extra-fields-on-many-to-many-relationships


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')

    """Generally, ManyToManyField instances should go in the object that’s going to be edited on a form.Members is in Group (rather than member having a group ManyToManyField ) because it’s more natural to think about a group having members."""
    members = models.ManyToManyField(User, through="Membership")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Group,self).save(*args, **kwargs)


    def get_absolute_url(self):
        """ This tells Django how to calculate the URL for an object by return a string that can be used to refer to the object over HTTP.. Django uses this in its admin interface, and any time it needs to figure out a URL for an object.Any object that has a URL that uniquely identifies it should define this method."""

        return reverse('group:group_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


    def current_group_post(self):
        return self.post_group.filter(group__id = self.pk)

    class Meta:
        ordering = ('-created_at',)
        permissions = (
           ("greate_group", "Can greate group"),
           ("add_post", "Can add post to group"),
           ("delete_post", "Can delete post in group"),
           ("update_post", "Can update post in group"),
       )



class Membership(models.Model):
    user = models.ForeignKey(
        User, related_name='group_member', on_delete=models.CASCADE)
    group = models.ForeignKey(
        Group, related_name="memberships", on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now=True)

    def __str__(self):
        return '{} who is member in {}'.format(self.user.username,self.group.name)
