


class Auction:


    auction_number = 0
    auctionPrice = 0
    AIList = []
    time = 0
    currentPrice = 0
    auctionAnimal = 0
    bid_player = 0
    def addAI(self,ai):
        self.AIList.append(ai)

    def bid(self, AIList): #AI bidding


    def winAuction(self, currentPrice):
        if self.bid_player > currentPrice:
            #player won


