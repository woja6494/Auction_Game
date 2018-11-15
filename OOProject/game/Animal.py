


class Animal:

    animal_ID = 0
    description = ""
    unlocked = False
    rarity = ""

    def __init__(self, aid, dc, price):
        self.animal_ID = aid
        self.description = dc
        self.price = price

    def get_Animal(self):
        return self.animal_ID

    def is_Unlocked(self):
        return self.unlocked

    def get_Description(self):
        return self.description

    def change_description(self, dc):
        self.description = dc

