from game import user



class PlayerHome:

    max_item = 0   # max number of item that player can place at home
    max_animal = 0
    curr_item_num = 0
    curr_animal_num = 0
    curr_background = 0
    def placeItem(self,item):
        if self.curr_item_num < self.max_item and user.getOwnItem(item):
            #place it

    def placeBackground(self, background):
        if user.getOwnBackground(background):
            self.curr_background = background

    def placeAnimal(self,animal):
        if self.curr_animal_num < self.max_item and user.getOwnAnima(animal):
            #place it somehow





