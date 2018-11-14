from threading import Timer
from .Auction import *

class AuctionSlot:

    AuctionID = 0;
    downTime = 0;
    runTime = 0;

    def __init__(self,auctionID,runtime):
        self.runTime = Timer(runtime,self.winAuction())
        self.runTime.start()




    def end_auction(self):
        self.downTime = Timer(60, Auction.create_auction(self.AuctionID,500))



    def winAuction(self, currentPrice):
        if self.bid_player > currentPrice:
            #put animal in players bag
        else:
            #nothing happen
