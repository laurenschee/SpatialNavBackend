# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Task(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    name = models.CharField(editable=True, max_length=128, unique=False, default="MST")
    details = JSONField(editable=True, default={})

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Task, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)


class UserTask(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    task = models.ForeignKey(Task, related_name='instance')
    owner = models.ForeignKey('auth.User', related_name='task')
    active = models.BooleanField(editable=True, default=False)
    complete = models.BooleanField(editable=True, default=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(UserTask, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)


# class UserLog(models.Model):
#     created_at = models.DateTimeField(editable=False)
#     updated_at = models.DateTimeField(editable=False)
#     task = models.ForeignKey(Task, related_name='instance')
#     owner = models.ForeignKey('auth.User', related_name='task')
#     results = JSONField(editable=True, default={})
#
#     def save(self, *args, **kwargs):
#         ''' On save, update timestamps '''
#         if not self.created_at:
#             self.created_at = timezone.now()
#         self.updated_at = timezone.now()
#         return super(UserLog, self).save(*args, **kwargs)
#
#     class Meta:
#         ordering = ('created_at',)