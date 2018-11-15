

class Item:

    item_Id = 0
    itemType = ""
    price = 0

    def __init__(self, itemid, itemtype, price):
        self.item_Id = itemid
        self.itemType = itemtype
        self.price = price

    def get_Item(self):
        return self.item_Id



    def get_Item_Price(self):
        return self.price

