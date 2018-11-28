from threading import Timer
from .user import *
from abc import ABC, abstractmethod
from .AuctionSlot import *
from .Animal import *
class AuctionSlot1(AuctionSlot):

    auctionID = 0
    total = 0
    AI_total = 0
    isOpen = False
    animal = Animal(0,"empty desc",0,"")
    instance = None
    user = User.get_instance()

    @staticmethod
    def get_instance():
        if AuctionSlot1.instance is None:
            AuctionSlot1()
            print("AuctionSlot1 instance created")
        return AuctionSlot1.instance

    def __init__(self,auctionID, animal):
        if AuctionSlot1.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.auctionID = auctionID
            self.animal = animal;
            self.isOpen = True
            self.total = self.animal.price
            self.AI_total = self.animal.price +1

            AuctionSlot1.instance = self

    def player_won(self):
        if self.total > self.AI_total:
            print(self.total)
            self.user.gold = self.user.gold -self.total
            return True
        else:
            return False

    def auction_close(self):
        print("Closing Auction")
        #self.isOpen = False
        self.instance = None

    def bid(self, amount):
        self.total += int(amount)