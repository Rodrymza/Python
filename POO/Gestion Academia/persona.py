from nota import Nota
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} Edad: {self.edad}")
        
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia
        
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre},  Materia: {self.materia}")

        
class Estudiante(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.lista_notas = []
        
    def mostrar_notas(self):
        nota: Nota
        print("".center(30, "-"))
        print(f"Notas del alumno: {self.nombre}")
        for nota in self.lista_notas:
            nota.mostrar_nota()
        
    def calcular_promedio(self):
        nota: Nota
        total = float(sum([nota for nota.valor in self.lista_notas]))
        return round(total/len(self.lista_notas), 2)
    
    def agregar_nota(self, nota: Nota):
        self.lista_notas.append(nota)
        print(f"Nota de {nota.catedra} agregada")
            
    
