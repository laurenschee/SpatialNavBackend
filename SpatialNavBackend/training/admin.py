# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Slide

# Register your models here.

class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'week', 'level', 'day', 'slide_num', 'details')
    model = Slide


admin.site.register(Slide, SlideAdmin)