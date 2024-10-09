materias = ["Matematica", "Fisica", "Historia", "Lengua"]
notas = []
for materia in materias:
    notas.append(int(input(f"Ingresa nota de {materia}")))

for materia, nota in zip(materias, notas):
    print(f"{materia}: {nota}")
    