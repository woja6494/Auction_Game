from threading import Timer
from abc import ABC, abstractmethod
from .Animal import *
from .user import *
class AuctionSlot(ABC):

    auctionID = 0
    downTime = 0
    runTime = 10
    total = 0
    AI_total = 0
    isOpen = False
    animal = Animal(0,"empty desc",0,"")
    instance = None
    user = User.get_instance()



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

    def bid(self, amount):
        self.total += int(amount)