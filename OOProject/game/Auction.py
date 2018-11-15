from threading import Timer


class Auction:


    max_auction_number = 3
    currAuctionNumber = 0
    auctionPrice = 0
    AIList = []
    time = 0
    currentPrice = 0
    auctionAnimal = 0
    bid_player = 0
    def addAI(self,ai):
        self.AIList.append(ai)

    def bid(self, AIList): #AI bidding




    def create_auction(self):
        if self.currAuctionNumber < self.max_auction_number:

