from persona import Persona
from funciones import pedir_boolean
from funciones import pedir_entero
class GestionPersona:
    def __init__(self):
        self.lista_personas = []
    
    def iniciar_programa(self):
        while True:
            print("Selecione opcion deseada")
            print("1 - Agregar Personas")
            print("2 - Mostrar personas con detalles")
            print("3 - Buscar persona")
            print("4 - Editar persona")
            print("5 - Borrar persona")
            print("6 - Lista corta personas")
            print("7 - Salir")
            ingreso = input()
            match ingreso:
                case "1": 
                    self.agregar_persona()
                case "2": 
                    self.mostrar_personas()
                    input("Presione una tecla para continuar\n")

                case "3": 
                    self.buscarPersonas()
                    input("Presione una tecla para continuar\n")

                case "4": 
                    persona = self.seleccionar_persona()
                    persona.editar_persona()
                    input("Presione una tecla para continuar\n")           
                case "5": 
                    persona = self.seleccionar_persona()
                    print(f"Se borro la persona {persona.apellido}, {persona.nombre}")
                    self.lista_personas.remove(persona)
                    input("Presione una tecla para continuar\n")
                case "6": 
                    self.listar_personas()
                case "7":
                    break
                case _: 
                    print("Opcion invalida")
        
    def agregar_persona(self):
        while True:
            persona = Persona(input("Ingrese nombre\n"), input("Ingresa apellido\n"))
            persona.set_edad()
            persona.set_ubicacion()
            self.lista_personas.append(persona)
            if not pedir_boolean("Desea agregar mas personas(s/n)"):
                break
    
    def buscarPersonas(self):
        encontrado = False
        busqueda = input("Ingrese nombre a buscar\n").title()
        for persona in self.lista_personas:
            if persona.nombre == busqueda or persona.apellido == persona:
                print(persona)
                encontrado = True
        if not encontrado:
            print("No se encontro la persona")
        
    def mostrar_personas(self):
        for persona in self.lista_personas:
            print("Persona".center(25,"-"))
            print(persona)
            
    def seleccionar_persona(self):
        self.listar_personas()
        while True:
            indice = pedir_entero("Seleccione persona") -1
            if indice>= 0 and indice < len(self.lista_personas):
                print(f"Persona selecionada: {self.lista_personas[indice].apellido}, {self.lista_personas[indice].nombre}")
                return self.lista_personas[indice]
            else:
                print("Fuera de rango")        
            
    def listar_personas(self):
        i = 1
        for persona in self.lista_personas:
            print(f"{i} - {persona.nombre}, {persona.apellido}")
            i+=1
    
    def agregarPersonas_lista(self, lista):
        for nombre, apellido, edad, direccion in lista:
            persona = Persona(nombre, apellido)
            persona.edad = edad
            persona.direccion = direccion
            self.lista_personas.append(persona)
                

personas = [
    ["Juan", "Perez", 30, "Calle Falsa 123"],
    ["Maria", "Gonzalez", 25, "Avenida Siempreviva 742"],
    ["Carlos", "Lopez", 40, "Boulevard Libertador 456"],
    ["Laura", "Martinez", 28, "Calle San Martin 987"],
    ["Luis", "Sanchez", 33, "Avenida de Mayo 101"],
    ["Ana", "Ramirez", 27, "Calle Corrientes 110"],
    ["Jorge", "Fernandez", 36, "Avenida Rivadavia 202"],
    ["Sofia", "Diaz", 22, "Calle Belgrano 303"],
    ["Diego", "Garcia", 41, "Boulevard Moreno 404"],
    ["Valentina", "Ruiz", 29, "Calle Lavalle 505"],
    ["Marcelo", "Gutierrez", 34, "Avenida Colon 606"],
    ["Natalia", "Silva", 26, "Calle Alberdi 707"],
    ["Pedro", "Romero", 38, "Avenida La Plata 808"],
    ["Camila", "Torres", 24, "Calle Caseros 909"],
    ["Rodrigo", "Acosta", 31, "Boulevard Alvear 1010"],
    ["Florencia", "Castro", 27, "Calle Moreno 1111"],
    ["Ezequiel", "Medina", 39, "Avenida Pueyrredon 1212"],
    ["Carolina", "Herrera", 30, "Calle Santa Fe 1313"],
    ["Sebastian", "Villalba", 35, "Avenida Entre Rios 1414"],
    ["Lucia", "Mendoza", 23, "Boulevard Mitre 1515"]
]

        
app = GestionPersona()
app.agregarPersonas_lista(personas)
app.iniciar_programa()