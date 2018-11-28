import time
from django.views import generic
from django import template
from .ItemSet import *
register = template.Library()

class User:
    gold = 10000
    ownAnimals = []
    ownItems = [ItemSet.itemarray[0],ItemSet.itemarray[1]]
    ownBackground = []
    instance = None

    @staticmethod
    def get_instance():
        if User.instance is None:
            User()
            print("User instance created")
        return User.instance

    def __init__(self):
        if User.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            User.instance = self



    def update_gold(self):
        self.gold += 100
        return self.gold


