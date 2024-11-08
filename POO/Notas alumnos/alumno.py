import funciones
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_notas = {}
    
    def cargar_notas(self):
        while True:
            nombre = input("Ingrese nombre de la materia:\n").title()
            nota = int(input("Ingrese nota\n"))
            self.lista_notas[nombre] = nota
            respuesta = input("Desea agregar mas notas?\n")
            if respuesta == "n":
                break
    
    def mostrar_notas(self):
        print(self.nombre.center(30,"*"))
        for nombre, nota in self.lista_notas.items():
            print(f"{nombre}: {nota}")
            
    def calcular_promedio(self):
        total = 0.0
        for nota in self.lista_notas.values():
            total += nota
        promedio = float(total / len(self.lista_notas))
        print(f"El promedio del alumno {self.nombre} es {round(promedio, 2)}")
        
    def mostrar_catedras(self):
        print("Lista de Materias:")
        for catedra, nota in self.lista_notas.items():
            print(f"{catedra} - {nota}")
    
    def cambiar_nota(self):
        while True:
            print("Seleccione la catedra a cambiar de nota")
            self.mostrar_catedras()
            catedra = input()
            if self.lista_notas.get(catedra):
                print(f"Nota anterior {catedra}: {self.lista_notas[catedra]}")
                self.lista_notas[catedra] = funciones.pedir_entero(f"Ingrese nueva nota de {catedra}")
                print("Nota cambiada exitosamente")
                return
            else:
                print("No seleccionaste una catedra")
            
        