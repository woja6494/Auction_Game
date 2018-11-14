

class Item:

    item_Id = 0;
    itemType = "something"
    price = 0;

    def __init__(self,id,type,price):
        self.item_Id = id
        self.itemType = type
        self.price = price

    def get_Item(self):
        return self.item_Id



    def get_Item_Price(self):
        return self.price



