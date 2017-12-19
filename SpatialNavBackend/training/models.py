# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from SpatialNavBackend.constants import *

# Create your models here.


class Slide(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    week = models.IntegerField(editable=True, choices=TRAINING_WEEK_CHOICES, default=1)
    level = models.IntegerField(editable=True, choices=TRAINING_LEVEL_CHOICES, default=1)
    day = models.IntegerField(editable=True, choices=TRAINING_DAY_CHOICES, default=1)
    slide_num = models.IntegerField(editable=True, default=0)
    details = JSONField(editable=True, null=True, default={})

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Slide, self).save(*args, **kwargs)

    def get_city(self, *args, **kwargs):
        ''' Get city name from week number '''
        if self.week:
            for i,c in TRAINING_WEEK_CHOICES:
                if i == self.week:
                    return c
        return None

    class Meta:
        ordering = ('created_at',)