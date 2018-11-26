from .Animal import *


class AnimalBook:

    animalList = {}
    animalarray = []
    #Listunlock = []
    animalkey = ["Cat","Macaque","Corgi","Chihuahua","Squirrel","Whitehorse"]
    instance = None

    @staticmethod
    def get_instance():
        if AnimalBook.instance is None:
            AnimalBook()
            print("BackgroundSet instance created")
        return AnimalBook.instance

    def __init__(self):
        if AnimalBook.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AnimalBook.instance = self


    animalList.update({"Cat": Animal(1, "A cute cat", 500,"/static/images/cat.jpg")})
    animalList.update({"Macaque": Animal(2, "Funny looking macaque", 500,"/static/images/macaque.jpg" )})
    animalList.update({"Corgi": Animal(3, "Welsh Corgi is its full breed name", 500,"/static/images/corgi.jpg")})
    animalList.update({"Chihuahua": Animal(4, "Listed in top 3 evil dog", 500, "/static/images/chihuahua.jpg")})
    animalList.update({"Squirrel": Animal(5, "The cutest animal in the world", 500,"/static/images/squirrel.jpg")})
    animalList.update({"Whitehorse": Animal(6, "A knight's favorite", 500 ,"/static/images/whitehorse.jpg" )})
    for key, value in animalList.items():
        i = 0
        animalarray.append({
            'animalName': key,
            'image' : value.url,
            'description' : value.description,
        })
