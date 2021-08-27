from django.shortcuts import render

# Create your views here.


# imageSearchApp > views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Group, Name, Date, Image


def index(request):
    return render(request, 'imageSearchApp/index.html')


def search_image(request):
    user_input_group = request.POST['groupContent']
    user_input_name = request.POST['nameContent']
    user_input_date = request.POST['dateContent']
    images = Image(
    return render(request, 'imageSearchApp/')

