palabra="Hola como va"
encontrado=False
n=0
letrabuscar="i"
for i in range (0,len(palabra),1):
    if (palabra[i:i+1])==letrabuscar:
        encontrado=True
        n=n+1
    
if encontrado:
    print("Se encontro lo buscado")
    print("Se encontro la letra",letrabuscar,n,"veces")
else:
    print("No se encontro la letra",letrabuscar)
