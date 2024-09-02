### Functions ###
def my_function():
        print("Esto es una funcion")

def nombre():
    return input("Dime tu nombre\n")        

my_function()

def sum_two_numbers(first_number, second_number: int): #con los dos puntos y el tipo de dato se suguiere al usuario el tipo de dato a enviar cuando escribe la funcion
    try:
        first_number, second_number = int(first_number), int(second_number)
        print(first_number+second_number)
    except:                                                     #casteo y bloque except para controlar el tipo de dato
        print("No ingresaste numeros")
sum_two_numbers(5,4)

sum_two_numbers(4,2)
sum_two_numbers("3","h")

#funcion con retorno
def sumar(first_value, second_value):
    return first_value+second_value

print(sumar(4,5))

def print_name(name, surname):
    print(f"{name}, {surname}")

print_name("Rodrigo","Ramirez")

print_name(surname="Ramirez", name="Rodrigo")   #pueden pasarse los parametros en otro orden
                                                #si se coloca que parametro se esta enviando
                        
def print_name_defaut(name, surname="Ramirez"):
    print(f"{name}, {surname}")
    
print_name_defaut("Juan")
