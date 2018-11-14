


class BackGround:

    backgroundID = 0
    itemSlot_Number = 0
    animalSlot_Number = 1
    price = 0
    itemSlots = [(448, 124)]# pixel of item slot
    animalSlot = [(823, 578)]

    def __init__(self,bg_id, islot_num, aslot_num, price, itemSlots, animalSlots):
        self.backgroundID = bg_id
        self.itemSlot_Number = islot_num
        self.animalSlot_Number = aslot_num
        self.price = price
        self.itemSlots = itemSlots
        self.animalSlot = animalSlots


    def get_Background(self):
        return self.backgroundNumber

    def get_Background_Price(self):
        return self.price

    def get_ItemSlot_Number(self):
        return self.get_ItemSlot_Number

    def get_AnimalSlot_Number(self):
        return self.get_AnimalSlot_Number

    def get_ItemSlots(self):
        return self.itemSlots

    def get_AnimalSlots(self):
        return self.animalSlot



