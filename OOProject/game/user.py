import time
from django.views import generic


class User:
    gold = 0
    goldIncrease = False
    while goldIncrease:
        gold += 1
        time.sleep(1)
