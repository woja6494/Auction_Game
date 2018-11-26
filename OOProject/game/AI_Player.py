from abc import ABC, abstractmethod
import random


class AIPlayer(ABC):

    AI_ID = 0
    money = 0

    @abstractmethod
    def bid(self):
        rand = random.randint(1,100)
        return
