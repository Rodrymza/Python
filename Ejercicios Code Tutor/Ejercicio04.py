personas = {}
for _ in range(3):
    nombre = input("Ingrese el nombre de la persona:\n")
    edad = int(input("Ingrese la edad de la persona:\n"))
    personas[nombre] = edad

busqueda = input("ingrese un nombre a buscar\n")
if personas.get(busqueda):
    print(f"{busqueda.capitalize()} tiene {personas[busqueda]} años")
else:
    print("Persona no encontrada")