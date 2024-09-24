"""Crear clase coche con marca, modelo y año
metodo que diga que el coche esta en marcha
crear varios coches y llamar al metodo arrancar"""

class Autos:
    def __init__(self, marca, modelo, anio:int):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def arrancar(self,valor):
        if valor>=1:
            print(f"El {self.marca} {self.modelo} esta en marcha")
        else:
            print(f"El {self.marca} {self.modelo} no esta en marcha")

auto1=Autos("Peugeot","308", 2018)
auto1.arrancar(0)

auto2=Autos("Fiat", "Toro", 2020)
auto2.arrancar(1)