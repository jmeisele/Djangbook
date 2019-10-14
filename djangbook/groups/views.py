from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db import IntegrityError
from groups.models import Group, GroupMembers
from django.shortcuts import get_object_or_404
from django.contrib import messages

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description') #Fields they are able to create
    model = Group
    # form_class = forms.UserCreateForm
    # Does not execute until submit done on form
    # success_url = reverse_lazy('list_groups')
    # template_name = 'accounts/signup.html'

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group
    # success_url = reverse('list_groups')
    success_url = reverse_lazy('list_groups')

    def get_queryset(self):
        return Group.objects.all().order_by('name')

class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        
        try:
            GroupMembers.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request,'Warning already a member!')
        else:
            messages.success(self.request,'You are now a member')
        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.GroupMembers.objects.filter(user = self.request.user, group__slug=self.kwargs.get('slug')).get()
        except models.GroupMembers.DoesNotExist:
            messages.warning(self.request, 'Sorry you are not in this group')
        else:
            membership.delete()
            messages.success(self.request, 'You have lefgt the group')
        return super().get(request, *args, **kwargs)