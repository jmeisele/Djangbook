from django.urls import path, include
from . import views

# Create your url patterns here
urlpatterns = [
    path('', views.SignUp.as_view(), name = 'signup'),
]
