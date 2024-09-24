"""Crear clase persona y el metodo saludar"""
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad= edad
        self.genero= genero
    
    def presentacion(self):
        print(f"Hola! Mi nombre es {self.nombre}, tengo {self.edad} años y mi genero es {self.genero}")
        
my_persona=Persona("Rodrigo", 32, "varon")
my_persona.presentacion()

my_persona.nombre="Edgardo"
my_persona.presentacion()