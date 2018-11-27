from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .models import *
from .user import *
from .ItemSet import *
from .Main_Screen import *
from .Animal_Book import *
from .AuctionBase import *
from .BackgroundSet import *
from .Shop import *

user = User.get_instance()
itemset = ItemSet()
auctionPlace = AuctionBase()
backgroundSet = BackgroundSet()
shop1 = Shop()

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
    #user.update_gold()
    print("hello")
    context = {
        'gold': user.gold,
        'instance' : user.instance,
    }
    return render(request, 'game/home.html', context)


def auction(request):
    a1 =AuctionSlot1.get_instance()
    auction = {

        'auction1': a1,
        'auction2': AuctionSlot2.animal,
        'auction3': AuctionSlot3.animal,

    }
    if request.method == "POST":
        print("HELLO!!")
        amount = request.POST['amount']
        print(type(amount))
        a1.bid(amount)
        return render(request, 'game/auction.html', auction)


    return render(request, 'game/auction.html', auction)


def book(request):
    ab = AnimalBook
    animals = {'animals': ab.animalarray,
    }
    return render(request, 'game/book.html', animals)


def inventory(request):
    if request.method == "POST":
        print("HELLO!!")
        if request.POST.get("itemname") is not None:
            item = int(request.POST.get("itemname"))
            print(item)

            for i in range (0, len(itemset.itemarray)):
                #print(itemset.itemarray[i]['itemID'])
                if itemset.itemarray[i]['itemID'] == item:
                    shop1.buyItem(item)
        elif request.POST.get("bgname") is not None:
            bg = int(request.POST.get("bgname"))
            #print("background")
            #print(bg)
            for i in range(0, len(backgroundSet.backgroundarray)):
                #print("bgID")
                #print(backgroundSet.backgroundarray[i]['bgID'])
                if backgroundSet.backgroundarray[i]['bgID'] == bg:
                    shop1.buyBackground(bg)
    userItems ={
        # 'itemName' : user.ownItems['itemName'],
        # 'url': user.ownItems['url'],
        'items' : user.ownItems,
        'bgs' : user.ownBackground,
        'animals' : user.ownAnimals,
    }
    return render(request, 'game/inventory.html', userItems)


def shop(request):

    everything = {'items' : itemset.itemarray,
                  'backgrounds' : backgroundSet.backgroundarray}

    return render(request, 'game/shop.html', everything)


def result(request): #from auction end
    print("result!")
    a1 =AuctionSlot1.get_instance()
    if a1.player_won():
        print("Player won!")
        user.ownAnimals.append(a1.animal)
    a1.auction_close()
    auction = {

        'auction1': a1,
        'auction2': AuctionSlot2.animal,
        'auction3': AuctionSlot3.animal,

    }
    return render(request,'game/auction.html',)

# def buy(request):
#     if request.method == "POST":
#         print("HELLO!!")
#         #my_var = dict.get( key , default )
#         #amount = request.POST['animalname']
#         item = int(request.POST.get("itemname"))
#         for i in range (0, len(itemset.itemarray)):
#             print(itemset.itemarray[i]['itemID'])
#             if itemset.itemarray[i]['itemID'] == item:
#                 print("buy item")
#                 shop1.buyItem(item)
#
#         print(item)
#     userItems ={
#         # 'itemName' : user.ownItems['itemName'],
#         # 'url': user.ownItems['url'],
#         'items' : user.ownItems
#     }
#     return render(request, 'game/inventory.html', userItems)