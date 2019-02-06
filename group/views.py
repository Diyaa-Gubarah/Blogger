from django.contrib import messages
from django.contrib.auth import get_user_model, models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from group.models import (Group, Membership)

User = get_user_model()
# Create your views here.


class GroupList(LoginRequiredMixin, generic.ListView):
    model = Group
    template_name = 'group/groups.html'
    context_object_name = 'groups'


class GroupCreate(LoginRequiredMixin, generic.CreateView):
    model = Group
    template_name = 'group/create_group.html'
    fields = ['name', 'description']


class GroupUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Group
    fields = ['name', 'description']
    template_name = 'group/update_group.html'


class GroupDelete(LoginRequiredMixin, generic.DeleteView):
    model = Group
    success_url = reverse_lazy('group:group_list')


class GroupDetail(LoginRequiredMixin, generic.DetailView):
    model = Group
    queryset = Group.objects.all()


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("group:group_detail", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get("slug"))

        """ let user join to group if he is not join or return 'you already join' """
        obj, user_membership_created = Membership.objects.get_or_create(
            user=self.request.user, group=group)

        current_user = User.objects.get(username=self.request.user.username)

        permission = models.Permission.objects.get(
            codename='add_post', name='Can add post to group')

        if user_membership_created:
            current_user.user_permissions.add(permission)
            print("You are now a member of the {} group.".format(group.name))
        else:
            if not current_user.has_perm('group.add_post'):
                current_user.user_permissions.add(permission)

            print("You, already a member of {}".format(group.name))

        return super(JoinGroup, self).get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('group:group_list')

    def get(self, request, *args, **kwargs):
        try:
            current_user_membership = Membership.objects.get(
                user=self.request.user, group__slug=self.kwargs.get("slug"))
            permission = models.Permission.objects.get(
                codename='add_post', name='Can add post to group')
            current_user = User.objects.get(username=self.request.user.username)
            if current_user.has_perm('group.add_post'):
                current_user.user_permissions.remove(permission)
        except ObjectDoesNotExist:
            print("You can't left this group because you aren't in it.")
        else:
            current_user_membership.delete()
            print("You have successfully left {} group.".format(self.kwargs.get("slug")))
        return super(LeaveGroup, self).get(request, *args, **kwargs)
