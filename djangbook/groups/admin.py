from django.contrib import admin
from . import models

# Register your models here.


class GroupMemberInline(admin.TabularInline): 
    model = models.GroupMembers


admin.register(models.Group)
# admin.register(models.GroupMembers)
