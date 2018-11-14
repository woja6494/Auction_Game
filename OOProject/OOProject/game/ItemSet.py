from .Item import *

class ItemSet:
    ItemList =[]




    def addItem(self,item_name, num_id, item_type, price):
        item_name = Item(num_id, item_type, price)
        self.ItemList.append(item_name)




