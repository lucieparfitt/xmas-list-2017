from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    item_list = Item.objects.all()
    context = {
        "item_list": item_list
    }
    return render(request, "wish_lists/home.html", context = context)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        pass
        # Return an 'invalid login' error message.

def logout_view(request):
    logout(request)
    # Redirect to a success page.

def create_user(request):
    form = UserForm()
    return render(request, 'wish_lists/create_user.html', {'form': form})
    # user = User.objects.create_user(username='john',
                                 # email='jlennon@beatles.com',
                                 # password='glass onion')
