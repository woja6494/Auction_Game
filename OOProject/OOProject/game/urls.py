from django.urls import path

from . import views    # . refers current directory.

urlpatterns = [

    path('', views.main, name='game-main'),
    # leave '' for homepage
    #  views.home navigates to views.py file and find home def.
    path('about/', views.about, name = 'game-about'),
    path('home/', views.home, name='game-home'),
    path('load/', views.load, name='game-load'),
    path('auction/', views.auction, name='game-auction'),
    path('book/', views.book, name='game-book'),
    path('inventory/', views.inventory, name='game-inventory'),
    path('shop/', views.shop, name='game-shop'),

]
