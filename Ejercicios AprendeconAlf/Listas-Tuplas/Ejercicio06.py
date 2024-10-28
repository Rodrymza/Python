materias = ["Matematica", "Historia", "Lengua", "Historia", "Fisica", "Quimica"]
notas = []
borrar = []
for elemento in materias:
    nota = int(input(f"Ingrese la nota de {elemento}"))
    if nota>=6:
        borrar.append(elemento)
    else:
        notas.append(nota)
        
for elemento in borrar:
    materias.remove(elemento)
print("Materias a recursar:")

for materia, nota in zip(materias, notas):
    print(f"{materia}: {nota}")
