from curso import Curso
from alumno import Alumno

class GestionCurso:
    def __init__(self):
        pass
    
    def main(self):
        mi_curso = Curso("Programacion I")
        while True:
            
            print("Seleccione la opcion deseada\n1 Agregar alumnos al curso \n2 Mostrar Notas \n3 Cambiar nota")
            respuesta = input()
            match respuesta:
                case "1": 
                    mi_curso.agregar_alumno()
                case "2": 
                    mi_curso.mostrar_alumnos()
                case "3":
                    mi_curso.cambiar_nota_alumno()
                case "4": 
                    break
                
            
app = GestionCurso()
app.main()
    
    
    
    