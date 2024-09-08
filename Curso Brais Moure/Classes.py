    ###Classes###

class Person:
    def __init__(self, name, surname, age):     #constructor de clase
        self.name = name
        self.surname = surname
        self.age = age

    def saludar(self):          #funciones especificas de la clase
        print(f"Hola! Mi nombre es {self.name} y tengo {self.age} años")
    def deletrear_nombre(self):
        for i in self.name:
            print(i)

    def __str__(self) -> str:       #funcion para determinar como se representa el objeto en una cadena de texto
        return f"{myperson.surname}, {myperson.name}"

myperson=Person("Rodrigo","Ramirez", 33)
myperson.saludar()

myperson.surname="Duran"        #los valores pueden cambiarse fuera del constructor de clase

myperson.saludar()

print(myperson)