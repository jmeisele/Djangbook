from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

app_name = 'groups'

# Create your url patterns here
urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create_group'),
    path('posts/in/<slug:slug>', views.SingleGroup.as_view(), name='single'),
    path('list/', views.ListGroups.as_view(), name='list_groups'),
    path('join/<slug:slug>', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug:slug>', views.LeaveGroup.as_view(), name='leave'),
]
