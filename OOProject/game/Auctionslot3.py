from threading import Timer
from abc import ABC, abstractmethod
from .AuctionSlot import *
from .Animal import *

class AuctionSlot3:

    auctionID = 0
    downTime = 0
    runTime = 10
    total = 0
    AI_total = 0
    isOpen = False
    animal = Animal(0,"empty desc",0,"")
    instance = None
    user = User.get_instance()

    @staticmethod
    def get_instance():
        if AuctionSlot3.instance is None:
            AuctionSlot3()
            print("AuctionSlot3 instance created")
        return AuctionSlot3.instance

    def __init__(self,auctionID, animal):
        if AuctionSlot3.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.auctionID = auctionID
            # self.runTime.start()
            self.animal = animal;
            self.isOpen = True
            self.total = self.animal.price
            self.AI_total = self.animal.price +1

            AuctionSlot3.instance = self

    def player_won(self):
        if self.total > self.AI_total:
            print(self.total)
            self.user.gold = self.user.gold -self.total
            return True
        else:
            return False

    def auction_close(self):
        print("Closing Auction")
        self.isOpen = False
        self.instance = None

    def bid(self, amount):
        self.total += int(amount)