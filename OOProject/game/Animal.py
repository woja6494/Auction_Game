


class Animal:

    animal_ID = 0
    description = ""
    rarity = ""
    url = None

    def __init__(self, aid, dc, price, url):
        self.animal_ID = aid
        self.description = dc
        self.price = price
        self.url = url

    def get_Animal(self):
        return self.animal_ID


    def get_Description(self):
        return self.description

    def change_description(self, dc):
        self.description = dc

