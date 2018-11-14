from .user import *
from .Item import *
from .Background import *

class Shop:

    itemList = []
    backgroundList = []
    user = User.getInstance()


    def buyItem(self,item):
        item.get_Item_Pricie()
        if self.user.gold > item.price: #user gold > item price
            self.user.gold - item.price
            self.user.ownItems.append(item)


    def buyBackground(self,background):
        background.get_Background_Price()
        if self.user.gold > background.price:
            self.user.gold - background.price
            self.user.ownBackground.append(background)