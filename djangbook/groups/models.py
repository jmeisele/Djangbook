from django import template
from django.db import models
# Allows removal of characters that aren't alphanumeric
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
import misaka
from django.contrib.auth import get_user_model
User = get_user_model()  # Allows us to call things off current users session
register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMembers')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class GroupMembers(models.Model):
    group = models.ForeignKey(
        Group, related_name='memberships', on_delete='cascade')
    user = models.ForeignKey(
        User, related_name='user_groups', on_delete='cascade')

    def __str__(self):
        return self.user.name

    class Meta:
        unique_together = ('group', 'user')
