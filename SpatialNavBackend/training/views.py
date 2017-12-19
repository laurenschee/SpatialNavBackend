# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Slide

# Create your views here.

def training_home(request):
    slide = Slide.objects.first()
    city = slide.get_city()
    context =  {
        'slide': slide,
        'city': city,
    }
    return render(request, 'slides/training_home.html', context)