import time
from django.views import generic


class User:
    gold = 0
    goldIncrease = False
    ownAnimals = []
    ownItems = []
    ownBackground = []
    instance = None
    while goldIncrease:
        gold += 1
        time.sleep(1)


    @staticmethod
    def get_instance():
        if User.instance is None:
            User()
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

