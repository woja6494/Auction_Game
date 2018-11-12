


class Animal:

    animal_ID = 0
    description = ""
    unlocked = False
    rarity = ""

    def get_Animal(self,animalID):
        return animalID

    def is_Unlocked(self):
        return self.unlocked

    def get_Description(self):
        return self.description