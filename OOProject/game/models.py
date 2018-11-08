from django.db import models
import time

# Create your models here.


class User(models.Model):
    gold = 0
    goldIncrease = False
    while goldIncrease:
        print(gold)
        time.sleep(1)
