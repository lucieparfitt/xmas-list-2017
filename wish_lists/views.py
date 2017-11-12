from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    item_list = Item.objects.all()
    context = {
        "item_list": item_list
    }
    return render(request, "wish_lists/home.html", context = context)
