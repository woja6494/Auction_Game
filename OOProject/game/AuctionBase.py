from .AuctionFactory import *


class AuctionBase:
    auction = AuctionFactory()
    if AuctionSlot1.instance is None:
        auction.create_auction(1)
        # print("Auction 1 instance")
        # print(AuctionSlot1.get_instance)
        # print(AuctionSlot1.animal.animal_ID)

