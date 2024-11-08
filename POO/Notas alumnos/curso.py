from alumno import Alumno
from funciones import pedir_entero
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_alumnos = []
        
    def agregar_alumno(self):
        while True:
            alumno = Alumno(input("Ingrese nombre del alumno\n").title())
            alumno.cargar_notas()
            self.lista_alumnos.append(alumno)
            respuesta = input("Desea agregar mas alumnos?\n")
            if respuesta == "n":
                break
            
    def listar_alumnos(self):
        indice = 1
        for alumno in self.lista_alumnos:
            print(f"{indice} - {alumno.nombre}")
            
    def mostrar_alumnos(self):
        for alumno in self.lista_alumnos:
            alumno.mostrar_notas()
            alumno.calcular_promedio()
    
    def cambiar_nota_alumno(self):
        while True:    
            self.listar_alumnos()
            alumno = pedir_entero("Seleccione un alumno") -1
            if alumno >= 0 and alumno < len(self.lista_alumnos):
                self.lista_alumnos[alumno].cambiar_nota()
                break
            else:
                print("No seleccionaste una catedra correcta")