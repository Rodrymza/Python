"""Gestion de invitados en Python"""

class datos:
    def __init__(self, name, surname, id):
        self.name=name
        self.surname=surname
        self.id=id
        
personas=[]
personas.append(datos("Ramirez", "Rodrigo", 36499229))
personas.append(datos("Arancibia", "Rocio", 38473146))
opc=0
while opc!=4:
    print("________________________________")
    print("Gestion de invitados")
    print("Menu principal")
    print("Seleccione opcion deseada: ")
    print("1 - Añadir invitados")
    print("2 - Ver lista invitados")
    print("3 - Gestion Ingreso")
    print("4 - Salir")
    print("________________________________")
    opc=int(input())
    if opc<1 or opc>3:
        print("***")
        print("Opcion no valida!")
        print("***")
    match opc:
        case 1:
            print("________________________________")
            print("Añadiendo nuevo invitado:")
            surname=(input("Ingrese apellido del invitado: ").title())
            name=(input("Ingrese nombre del invitado: ").title())
            id=int(input("Ingrese DNI del invitado: "))
            personas.append(datos(name,surname,id))
            print("________________________________")
        case 2: 
            print("________________________________")
            cont=1
            for invitado in personas:
                print(f"{cont} - {invitado.surname}, {invitado.name} - DNI: {invitado.id}")
                cont+=1
            print("________________________________")
        case 3: 
            found=False
            print("________________________________")
            buscar=input("Ingrese nombre a buscar: ")
            for invitado in personas:
                if invitado.name==buscar.title() or invitado.surname==buscar.title() or str(invitado.id)==buscar:
                    print(f"Invitado encontrado: {invitado.surname}, {invitado.name}, {invitado.id}")
                    found=True
                    print("________________________________")
            print("*** No se encontro invitado con el dato suministrado***") if found==False else print("")
            
                