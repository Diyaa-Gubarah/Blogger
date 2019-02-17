# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import get_user_model, models
from django.contrib.auth.decorators import login_required, permission_required
# https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin)
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from group.models import Group, Membership
from post.forms import CreatePostForm,CommentForm
from post.models import Comment, Like, Post

# Create your views here.


class PostList(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'post/posts.html'
    context_object_name = 'posts'


class CreatePost(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, generic.CreateView):
    permission_required = 'group.add_post'
    model = Post
    template_name = 'post/create_post.html'
    form_class = CreatePostForm

# https://stackoverflow.com/questions/52106944/how-do-i-raise-permissiondenied-redirect-to-another-page-using-cbv
    login_url = '403html'
    raise_exception = True

    def handle_no_permission(self):
        # add custom message
        messages.error(self.request, 'You have no permission to create post in {} group please join first'.format(
            self.kwargs.get('slug')), extra_tags='alert')
        return super(CreatePost, self).handle_no_permission()

    def test_func(self):
        try:
            current_user_membership = Membership.objects.get(
                user__username=self.request.user.username, group__slug=self.kwargs.get('slug'))
            if current_user_membership:
                print('{} is a member in {} group'.format(
                    self.request.user, current_user_membership.group.name))
                return self.request.user.has_perm('group.add_post')
        except Exception as e:
            print('\n{} must join to this group first\n'.format(self.request.user))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)


class PostDetail(LoginRequiredMixin, generic.DetailView):
    model = Post
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['interacting_users'] = Like.objects.filter(
            post__id=self.kwargs.get("pk")).order_by('user__username')
        return context


class UpdatePost(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'post/update_post.html'


class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('group:group_list')


@login_required
def LikePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    obj, created = Like.objects.get_or_create(
        user=request.user, post=post)

    if created:
        obj.increment_like()
        return redirect('post:post_list')
    else:
        return redirect('post:post_list')


@login_required
def disLikePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    try:
        obj = Like.objects.get(user=request.user, post=post)
    except:
        return redirect('post:post_list')
    else:
        obj.decrement_like()
        obj.delete()
        return redirect('post:post_list')


class CommentCreate(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm


class CommentUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    form_class = CommentForm


@login_required
def CommentDelete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post:post_detail', pk=post_pk)
