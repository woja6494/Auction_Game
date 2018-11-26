from .Background import *


class BackgroundSet:

    backgroundList = {}
    backgroundarray =[]
    backgroundNumber = 0
    itemSlot_Number = 0
    price = 0
    itemSlotPosition = 1
    animalSlot_Number = 1
    instance = None

    @staticmethod
    def get_instance():
        if BackgroundSet.instance is None:
            BackgroundSet()
            print("ItemSet instance created")
        return BackgroundSet.instance

    def __init__(self):
        if BackgroundSet.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            BackgroundSet.instance = self
    itemSlots = [(448, 124)]# pixel of item slot
    animalSlot = [(823, 578)]

    # def addBackground(self, bg_name, bg_id, islot_num, aslot_num, price, itemSlots, animalSlots):
    #     bg_name = BackGround(bg_id, islot_num, aslot_num, price, itemSlots, animalSlots)
    #     self.backgroundList.append(bg_name)

#self,bg_id, islot_num, aslot_num, price, itemSlots, animalSlots
    backgroundList.update({"bg1": BackGround(1,1,1,2000,[(404,404)],[(123,508)],"/static/images/bg1.jpg")})
    backgroundList.update({"bg2": BackGround(2,1,1,2000,[(404,404)],[(123,508)],"/static/images/bg2.jpg")})


    for key, value in backgroundList.items():
        backgroundarray.append({
            'bgName': key,
            'bgID' : value.backgroundID,
            'price' : value.price,
            'url': value.url,

        })
