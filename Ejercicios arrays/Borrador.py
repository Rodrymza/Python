
def agregar_estudiante(nombre,nota):
    global notas_estudiantes
    notas_estudiantes = {nombre.capitalize(): nota}

notas_estudiantes = {"Ruiz": 8,
                     "Hernandez": 7}


import random
numeros = [random.randint(0,20) for i in range(15)]

for apellido, nota in notas_estudiantes.items():
    print(apellido, nota)