from curso import Curso
from persona import Profesor
class Academia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_cursos = [] 
        self.lista_profesores = []
        
    def agregar_curso(self, curso: Curso):
        self.lista_cursos.append(curso)
        print(f"Curso {curso.nombre} agregado a {self.nombre}")
        
    def mostrar_cursos(self):
        curso: Curso
        for curso in self.lista_cursos:
            print("".center(30, "-"))
            curso.mostrar_curso()
            
    def mostrar_estudiantes_curso(self):
        curso: Curso
        for i, curso in enumerate(self.lista_cursos, start = 1):
            print(f"{i} - {curso.nombre}")
        while True:
            print("".center(30, "-"))
            seleccion = int(input("Seleccione un curso: "))
            if seleccion >= 0 and seleccion <= len(self.lista_cursos):
                self.lista_cursos[seleccion-1].mostrar_estudiantes()
                return
            else:
                resputesta = input("Seleccion incorrecta, continuar?: ").lower()
                if resputesta == "n": return
        
    def mostrar_profesores(self):
        profesor: Profesor
        for i, profesor in enumerate(self.lista_profesores, start=1):
            print(i, end=" - ")
            profesor.mostrar_datos()
    
    def agregar_profesor(self, profesor: Profesor):
        self.lista_profesores.append(profesor)