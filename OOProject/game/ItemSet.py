from .Item import *


class ItemSet:
    itemList = {}
    itemarray = []
    # def addItem(self, item_name, num_id, item_type, price):
    #     self.ItemList.update({item_name: Item(num_id, item_type, price)})

    itemList.update({"sofa": Item(1, "sofa", 500)})
    itemList.update({"chair": Item(2, "chair", 500)})
    itemList.update({"lightstand": Item(3, "lightstand", 500)})

    for key, value in itemList.items():

        itemarray.append({
         'itemName': key,
         'itemType': value.itemType,
         'price': value.price
         })