segundos=int(input("Ingrese la cantidad de segundos: "))

horas=segundos//3600
minutos=(segundos%3600)//60
segundos=((segundos%3600)%60)

print(horas,minutos,segundos)