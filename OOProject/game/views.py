from django.shortcuts import render



def main(request): #handle traffic of blog
    return render(request, 'game/main.html', {'title': 'Main'})  #request, template name what want to render, thrid passes into template and access it on template

def about(request):
    return render(request, 'game/about.html', {'title': 'About'})

def home(request):
    return render(request, 'game/home.html' )

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
