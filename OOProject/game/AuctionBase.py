from .Auction import *


class AuctionBase:
    auction = Auction()
    if AuctionSlot1.instance is None:
        auction.create_auction(1)
        # print("Auction 1 instance")
        # print(AuctionSlot1.get_instance)
        # print(AuctionSlot1.animal.animal_ID)