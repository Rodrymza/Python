"""agregar al menos 3 plantas con al menos 2 sectores
mostrar nombre del parque, total de cada planta y 
area total del parque industrial"""
from planta import Planta
from parqueIndustrial import ParqueIndustrial
from sector import Sector
class Main:
    def main():
        parque = ParqueIndustrial(input("Ingrese el nombre del parque industrial: "))
        while True:
            planta = Main.crear_planta()
            parque.agregar_planta(planta)
            respuesta = input("Desea agregar mas plantas")
            if respuesta.lower == "n":
                break
            
        parque.mostrar_parque()
    
    @staticmethod    
    def crear_planta():
        nombre = input("Ingrese el nombre de la nueva Plata: ")
        planta = Planta(nombre)
        while True:
            nuevo_sector = Main.crear_sectores()
            planta.agregar_sector(nuevo_sector)
            respuesta = input("Desea agregar mas sectores? (s/n)")
            if respuesta.lower() == "n":
                planta.total_area_planta()
                return planta
    @staticmethod
    def crear_sectores():
        nombre = input("Ingrese el nombre del Sector: ")
        area = float(input("Ingrese el area del Sector: "))
        sector = Sector(nombre, area)
        return sector
    
    
Main.main()