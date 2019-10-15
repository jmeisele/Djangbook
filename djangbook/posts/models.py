from django.db import models
from django.urls import reverse # When someone does a post, where are we going to send them back to?
from django.conf import settings

import misaka
from groups.models import Group
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model() # Connect curent post to whoever is logged in as the user

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete='cascade')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete='cascade')
    
    def __str__(self):
        return self.message 
    
    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk':self.pk})
    
    class Meta:
        ordering = ['-created_at'] # Minus sign so we see them in descending order ~ most recent post at the top
        unique_together = ['user', 'message']