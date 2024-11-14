from persona import Estudiante, Profesor
from academia import Academia
from curso import Curso
lista_profesores = [Profesor("Jose Fernandes", 45, "Matematica"),
                    Profesor("Viviana Gonzalez", 39, "Ingles"),
                    Profesor("Mauro Estevez", 33, "Educacion Fisica")]

lista_cursos = [Curso("Programacion Python"),
                Curso("Programacion Java"),
                Curso("Bases de datos")]
    
def main():
    global academia
    academia = Academia("Code Academy")
    while True:
        print("Selecciona la opcion deseada \n1 Agregar curso \n2 Añadir alumno a curso " +
              "\n3 Mostrar cursos \n4 Mostrar estudiantes de curso \n5 Salir")
        opcion = input()
        match opcion:
            case "1": 
                nuevo_curso = crear_curso()
                print("Asigne un profesor al curso:")
                profesor = seleccionar_profesor()
                nuevo_curso.asignar_profesor(profesor)
                academia.agregar_curso(nuevo_curso)



def crear_curso() :
    nombre = input("Ingrese nombre del curso: ")
    nuevo_curso = Curso(nombre)
    
    return nuevo_curso

def crear_profesor():
    nombre = input("Ingresa nombre del profesor: ")
    edad = int(input("Ingresa edad del profesor: "))
    materia = input("Ingresa materia del profesor: ")
    nuevo_profesor = Profesor(nombre, edad, materia)
    return nuevo_profesor

def seleccionar_profesor():
    profesores: Profesor
    while True:
        if len(academia.lista_profesores) > 0:
            for i, profesores in enumerate(academia.lista_profesores, start=1):
                print(f"{i} - {profesores.nombre} / {profesores.materia}")
            print(f"{i+1} - Nuevo profesor")
            opcion = int(input("Seleccciona profesor: ")) 
            if opcion >= 0 and opcion <= len(academia.lista_profesores):
                return academia.lista_profesores[opcion-1]
            elif opcion == len(academia.lista_profesores)+1:
                return crear_profesor()
            else:
                print("Opcion no valida")
        else:
            print("No hay profesores cargados")
            return crear_profesor()
        
         
main()