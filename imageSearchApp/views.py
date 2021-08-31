from typing_extensions import ParamSpecArgs
from django.shortcuts import render
from django.db import models
# Create your views here.


# imageSearchApp > views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import ImageData, Image
# from django.db.models import Q
# # .filter(Q(title="제목") | Q(content="내용"))를 쓸 때 필요

def index(request):
    return render(request, 'imageSearchApp/index.html')


def search_image(request):
    user_input_group = request.POST.get('group_Content')
    user_input_name = request.POST.get('name_Content')
    user_input_date = request.POST.get('date_Content')
    #.get()은 key가 존재하면 value를 리턴

    imagedata = ImageData.objects.filter(
        group='user_input_group',
        name='user_input_name',
        date='user_input_date'
    )
    images = imagedata.image.all()

    # id = ImageData.objects.filter(
    #     group='user_input_group',
    #     name='user_input_name',
    #     date='user_input_date'
    # ).value('id')[0]['id']

    # image = Image.objects.get(ImageData=id)
    context = {'image' : images}
    return render(request,'imageSearchApp/search.html', context)

def save_page(request):
    pass

def save_data(request):
    imagedata = ImageData()
    user_input_group = request.POST.get('group_Content')
    user_input_name = request.POST.get('name_Content')
    user_input_date = request.POST.get('date_Content')
    imagedata.group = user_input_group
    imagedata.name = user_input_name
    imagedata.date = user_input_date
    imagedata.save()

    image = Image()
    imagedata_filtered = ImageData.objects.filter(
        group='user_input_group',
        name='user_input_name',
        date='user_input_date'
    )    
    image.imagedata = imagedata_filtered
    image.image_path = request.POST['image_path_Content']
    image.image_url = request.POST['image_url_Content']
    image.save()

    
    # group = models.ImageData(group=user_input_group)
    # name = models.ImageData(name=user_input_name)
    # date = models.ImageData(date=user_input_date)
    
    return render(request, 'imageSearchApp/')



    # id = ImageData.objects.filter(
    #     group='user_input_group',
    #     name='user_input_name',
    #     date='user_input_date'
    # ).value('id')[0]['id']
