class datos:
    def __init__(self, apellido, nombre):
        self.apellido=apellido
        self.nombre=nombre

personas=[]

personas.append(datos("Ramirez", "Rodrigo"))
personas.append(datos("Arancibia", "Rocio"))

for persona in personas:
    print(f"{persona.apellido}, {persona.nombre}")