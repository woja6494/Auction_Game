from .Background import *


class BackgroundSet:

    backgroundList = []

    backgroundNumber = 0
    itemSlot_Number = 0
    price = 0
    itemSlotPosition = 1
    animalSlot_Number = 1

    itemSlots = [(448, 124)]# pixel of item slot
    animalSlot = [(823, 578)]

    def addBackground(self, bg_name, bg_id, islot_num, aslot_num, price, itemSlots, animalSlots):
        bg_name = BackGround(bg_id, islot_num, aslot_num, price, itemSlots, animalSlots)
        self.backgroundList.append(bg_name)


