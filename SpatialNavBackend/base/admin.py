# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserTask, Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name', 'details')
    model = Task

class UserTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'task', 'owner', 'active', 'complete')
    model = UserTask


admin.site.register(Task, TaskAdmin)
admin.site.register(UserTask, UserTaskAdmin)