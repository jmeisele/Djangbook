from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from . models import Group, GroupMembers

# Create your views here.


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group
    # form_class = forms.UserCreateForm
    # Does not execute until submit done on form
    success_url = reverse_lazy('list_groups')
    # template_name = 'accounts/signup.html'


class SingleGroup(generic.DetailView):
    model = Group


class ListGroups(generic.ListView):
    model = Group
    success_url = reverse_lazy('list_groups')
