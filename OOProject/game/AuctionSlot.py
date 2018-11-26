from threading import Timer
from .Auction import *

class AuctionSlot:

    auctionID = 0
    downTime = 0
    runTime = 0
    animal = None
    instance = None

    def __init__(self,auctionID, animal):
        #self.runTime = Timer(runtime,self.winAuction())
        self.auctionID = auctionID
        #self.runTime.start()
        self.animal  = animal;



    def end_auction(self):
        self.downTime = Timer(60, Auction.create_auction(self.AuctionID,500))


    #
    # def winAuction(self, currentPrice):
    #     if self.bid_player > currentPrice:
    #         #put animal in players bag
    #     else:
    #         #nothing happen
