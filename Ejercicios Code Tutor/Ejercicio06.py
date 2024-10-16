from random import randint

def crear_estudiantes(cantidad):
    global materias
    estudiantes = {}
    for i in range(cantidad):
        nombre = input("Ingrese nombre del alumno\n")
        notas = []
        for elemento in materias:
            #notas.append(int(input(f"Ingresa nota de {elemento} \n")))
            notas.append(randint(5,10))
        estudiantes[nombre] = notas
    return estudiantes

promedio = lambda lista : round(sum(lista)/len(lista),2)

def promedios_alumnos(diccionario):
    promedios_dict = {}
    for clave, valor in diccionario.items():
        promedios_dict[clave] = promedio(valor)
    return promedios_dict

def promedio_mayor(diccionario):
    claves = [clave for clave in diccionario]
    max = diccionario[claves[0]]
    estudiante_mayor = claves[0]
    for clave in claves:
        if diccionario[clave] > max:
            max = diccionario[clave]
            estudiante_mayor = clave
    print(f"El estudiante de mejor promedio es {estudiante_mayor.capitalize()}, con promedio {diccionario[estudiante_mayor]}")

materias = ["Lengua", "Matematica", "Historia"]

#creacion de diccionario estudiantes y notas
notas_estudiantes = crear_estudiantes(4)
#sacar promedio y devolverlo en un nuevo diccionario
promedios_estudiantes = promedios_alumnos(notas_estudiantes)

print(notas_estudiantes)

print(promedios_estudiantes)
promedio_mayor(promedios_estudiantes)