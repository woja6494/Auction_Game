from .user import *
from .Item import *
from .BackgroundSet import *
from .ItemSet import *

class Shop:

    itemList = ItemSet.itemList
    backgroundList = BackgroundSet.backgroundList
    user = User.get_instance()


    def buyItem(self,itemID):
        price = ItemSet.itemarray[itemID-1]['price']
        if self.user.gold > price: #user gold > item price
            self.user.gold = self.user.gold - price
            print("usergold")
            print(self.user.gold)
            self.user.ownItems.append(ItemSet.itemarray[itemID-1])
            print("ITEM ADDED")


    def buyBackground(self,bgID):
        index = bgID -1
        price = BackgroundSet.backgroundarray[index]['price']
        if self.user.gold > price:
            self.user.gold = self.user.gold - price
            print("usergold")
            print(self.user.gold)
            self.user.ownBackground.append(BackgroundSet.backgroundarray[index])
            print("BG ADDED")

