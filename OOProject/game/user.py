import time
from django.views import generic


class User:
    gold = 0
    goldIncrease = False
    ownAnimals = []
    ownItems = []
    ownBackground = []

    while goldIncrease:
        gold += 1
        time.sleep(1)

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

