### Conditionals ###

my_condition = True
if my_condition: #es lo mismo que if my_condition==True
    print("Se ejecuta la condicion del if")  #la orden se ejecuta solo si la condicion se cumple
    
my_condition= 5 * 2

if my_condition: 
    print("Se ejecuta la condicion del segundo if")  #la orden se ejecuta si la condicion tiene al menos un valor
                                                     # cualquier valor que no sea 0 en booleano es verdadero
                                                     
if my_condition>10:
    print("Es mayor que 10")
else:
    print("Es menor o igual a 10")    
                                                     
print("La ejecucion continua")

#elseif sirve para evaluar varias condiciones 

if my_condition<10:
    print("El valor es menor a es 10")
elif  my_condition==10:
    print("El valor es 10")
else:
    print("El valor es mayor a 10")
    
