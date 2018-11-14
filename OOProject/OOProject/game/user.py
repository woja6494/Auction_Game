import time
from django.views import generic
from django import template

register = template.Library()

class User:
    gold = 10000
    goldIncrease = True
    ownAnimals = []
    ownItems = []
    ownBackground = []
    instance = None
    temp = "striiiiing"
    # if goldIncrease:
    #     gold += 1
    #     time.sleep(1)

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


    def getOwnAnimal(self, animal):
        if animal in self.ownAnimals:
            return True
        else:
            return False

    def getOwnItem(self,item):
        if item in self.ownItems:
            return True
        else:
            return False

    def getOwnBackground(self, background):
        if background in self.ownBackground:
            return True
        else:
            return False

    def update_gold(self):
        self.gold += 100
        return self.gold


