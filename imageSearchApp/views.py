from django.shortcuts import render
from django.db import models
# Create your views here.


# imageSearchApp > views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import ImageData, Image


def index(request):
    return render(request, 'imageSearchApp/index.html')


def search_image(request):
    user_input_group = request.POST['groupContent']
    user_input_name = request.POST['nameContent']
    user_input_date = request.POST['dateContent']
    imagedata = ImageData()
    imagedata.group = user_input_group
    imagedata.name = user_input_name
    imagedata.date = user_input_date

    # group = models.ImageData(group=user_input_group)
    # name = models.ImageData(name=user_input_name)
    # date = models.ImageData(date=user_input_date)
    
    images = Image()
    return render(request, 'imageSearchApp/')



