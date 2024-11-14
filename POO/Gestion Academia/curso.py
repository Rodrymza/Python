from persona import Profesor, Estudiante
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesor: Profesor  = None
        self.lista_estudiantes = []
        
    def mostrar_curso(self):
        print(f"Curso: {self.nombre} \nProfesor: {self.profesor.nombre}")
        print(f"Total de alumnos {len(self.lista_estudiantes)}")
        
    def mostrar_estudiantes(self):
        estudiante: Estudiante
        print("".center(30, "-"))
        print(f"Lista de estudiantes para la catedra: {self.nombre}")
        for estudiante in self.lista_estudiantes:
            estudiante.mostrar_datos()
        
    def asignar_profesor(self, profesor: Profesor):
        self.profesor = profesor
        print(f"Profesor: {profesor.nombre} asignado a {self.nombre}")
        
    def agregar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
    