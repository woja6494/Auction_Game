from .Item import *


class ItemSet:
    itemList = {}
    itemarray = []
    # def addItem(self, item_name, num_id, item_type, price):
    #     self.ItemList.update({item_name: Item(num_id, item_type, price)})
    instance = None

    @staticmethod
    def get_instance():
        if ItemSet.instance is None:
            ItemSet()
            print("BackgroundSet instance created")
        return ItemSet.instance

    def __init__(self):
        if ItemSet.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ItemSet.instance = self


    itemList.update({"sofa": Item(1, "sofa", 500, "/static/images/sofa1.jpg")})
    itemList.update({"chair": Item(2, "chair", 500,"/static/images/chair1.jpg")})
    itemList.update({"lightstand": Item(3, "lightstand", 500,"/static/images/lightstand1.jpg")})

    for key, value in itemList.items():

        itemarray.append({
            'itemName': key,
            'itemType': value.itemType,
            'itemID' : value.item_Id,
            'price': value.price,
            'url' : value.url,
         })