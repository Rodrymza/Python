"""Solicitar longitud de un lista que contendra elementos solo te tipo entero e ir pidiendo elementos uno a uno, al
final mostrar los elementos ingresados y la suma total de todos los elementos"""

size=int(input("Ingresa el tamaño de la lista a crear\n"))
int_list=[]
suma=0
for i in range(size):
    int_list.append(int(input(f"Ingrese el elemento {i+1}\n")))
    suma+=int_list[i]
   
print(f"Los elementos ingresados fueron: {int_list}")
print(f"La suma de los elementos ingresados da: {suma}")
print("Suma con funcion sum", sum(int_list))