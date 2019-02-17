# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.db import models
from group.models import Group

User = get_user_model()
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, related_name='post_user', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name="post_group", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    like = models.ManyToManyField(User, through="Like")


    def get_absolute_url(self):
        return reverse("post:post_detail", kwargs={"pk": self.pk})

    def post_comments(self):
        """return number of comment for current post"""
        return self.comments.filter(post__id=self.pk) # comments comes from related_name inside Comment Model

    def __str__(self):
        return '{} post'.format(self.title)

    class Meta:
        ordering = ["-created_at"]





class Like(models.Model):
    post = models.ForeignKey(
        Post, related_name="post_who_got_like", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='user_who_give_like', on_delete=models.CASCADE)
    num_of_like = models.PositiveIntegerField(default=0)

    def increment_like(self):
        self.num_of_like += 1
        self.save()

    def decrement_like(self):
        if self.num_of_like <= 0:
            self.num_of_like = 0
            self.save()
        else:
            self.num_of_like -= 1
            self.save()

    def __str__(self):
        return '{} has {} likes by {}'.format(self.post.title,self.num_of_like,self.user.username)

    class Meta:
        permissions = (
           ("add_like_to_post", "Can add like to post"),
           ("remove_like", "Can remove like from post"),
       )

class Comment(models.Model):
   """ Comment Table Fields """
   post = models.ForeignKey(
       Post,on_delete=models.CASCADE, related_name='comments')

   comment_auther = models.CharField(max_length=200)
   comment_text = models.TextField(max_length=500, blank=False)
   comment_create_date = models.DateTimeField(auto_now=True)

   # used by createview
   def get_absolute_url(self):
       return reverse("post:post_detail", kwargs={"pk": self.post.pk})


   def __str__(self):
       return 'this comment wrote by: %s, in the : %s post' % (self.comment_auther, self.post)
