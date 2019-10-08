from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'groups'

# Create your url patterns here
urlpatterns = [
    path('group_list/', views.ListGroups.as_view(), name='list_groups'),
    path('group_create/', views.CreateGroup.as_view(), name='create_group'),
    path('group_single/', views.SingleGroup.as_view(), name='single_group'),
]
