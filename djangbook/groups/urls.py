from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'groups'

# Create your url patterns here
urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('posts/in/<slug>', views.SingleGroup.as_view(), name='single'),
]
