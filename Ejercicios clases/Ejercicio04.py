"""Crear clase animal y clases heredadas perro y gato que tengan metodo ladrar y maullar"""

class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
        self.patas = 4
        
class Perro(Animal):
    def hacersonido(self):
        print(f"{self.nombre} ladra")
    def tipo(self):
        print(f"{self.nombre} es un perro y tiene {self.patas} patas")

class Gato(Animal):
    def hacersonido(self):
        print(f"{self.nombre} maulla")
        
    def tipo(self):
        print(f"{self.nombre} es un gato y tiene {self.patas} patas")
        
my_cat=Gato("Snickers")
my_cat.hacersonido()
my_cat.tipo()

my_dog = Perro("Firulaus")
my_dog.hacersonido()
my_dog.tipo()