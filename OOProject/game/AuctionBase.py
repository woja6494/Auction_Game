from .AuctionFactory import *


class AuctionBase:
    auction = AuctionFactory()
    if AuctionSlot1.instance is None:
        auction.create_auction(1)
    elif AuctionSlot2.instance is None:
        auction.create_auction(2)
    elif AuctionSlot3.instance is None:
        auction.create_auction(3)


