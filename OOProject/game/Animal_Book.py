from .Animal import *


class AnimalBook:

    animalList = {}
    animalarray = []
    #Listunlock = []

    animalList.update({"cat": Animal(1, "", 500)})
    animalList.update({"macaque": Animal(2, "", 500)})
    animalList.update({"corgi": Animal(3, "", 500)})
    animalList.update({"chihuahua": Animal(3, "", 500)})
    animalList.update({"squirrel": Animal(3, "", 500)})
    animalList.update({"whitehorse": Animal(3, "", 500)})

    for key, value in animalList.items():
        animalarray.append({
            'animalName': key,
        })
