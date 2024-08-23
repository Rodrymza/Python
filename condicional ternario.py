verificar=False
edad=0
while not verificar:
    edad=int(input("Ingresa tu edad: "))
    verificar= True if edad>=1 and edad<99 else False
    if verificar==False: print("Ingresa una edad correcta")
mensaje= "Eres mayor de edad" if edad>=18 else "Eres menor de edad"
print(mensaje)