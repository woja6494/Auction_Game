from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .models import *
from .user import *
from .Main_Screen import *

user = User()
def main(request):  # handle traffic of blog
    # if request.method == 'POST':
    #     #start = request.POST['start']
    #return HttpResponse(request, render(request, 'game/main.html', {'title': 'Main'}))
    return render(request, 'game/main.html', {'title': 'Main'})
    # request, template name what want to render,
    # third passes into template and access it on template


def about(request):
    return render(request, 'game/about.html', {'title': 'About'})


def home(request):
    user.update_gold()
    print("hello")
    context = {
        'gold': user.gold,
        'instance' : user.instance,
    }
    return render(request, 'game/home.html', context)


def auction(request):
    return render(request, 'game/auction.html', {'title': 'auction'})


def book(request):
    return render(request, 'game/book.html', {'title': 'book'})


def inventory(request):
    return render(request, 'game/inventory.html', {'title': 'inventory'})


def shop(request):
    return render(request, 'game/shop.html', {'title': 'shop'})


def load(request):
    return render(request, 'game/load.html', {'title': 'load'})
# Create your views here.')
