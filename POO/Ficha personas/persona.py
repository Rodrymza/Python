from funciones import pedir_entero
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.edad = 0    
        self.direccion = ""
    
    def set_edad(self):
        self.edad = pedir_entero(f"Ingrese edad de {self.nombre}")
        
    def set_ubicacion(self):
        self.direccion = input(f"Ingrese direccion de {self.nombre}\n").title()
        
    def __str__(self):
        return f"{self.apellido}, {self.nombre} \nEdad {self.edad} \nDireccion: {self.direccion}"
    
    def editar_persona(self):
        self.nombre = input("Ingrese nombre de persona\n").title()
        self.apellido = input("Ingrese apellido de la persona\n").title()
        self.set_edad()
        self.set_ubicacion().title()