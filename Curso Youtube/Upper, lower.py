"""Al igual que title estos metodos sirven para dar formato en mayusculas y minusculas y para verificar ese formato en una cadena derterminada"""

cadena="Buenos dias"

print(f"Cadena sin formato {cadena}")

print(f"Cadena en minusculas {cadena.lower()}")
print(f"Cadena en mayusculas {cadena.upper()}")

cadena=cadena.upper()

print(f"Transformamos la cadena en mayusculas, y lo verificamos con upper: {cadena.isupper()}")
print(f"Verificamos tambien que la cadena no esta en minisculas: {cadena.islower()}")