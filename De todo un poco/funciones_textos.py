class Textos:
    def __init__(self, string):
        self.string = string
    
    def contar_vocales(self):
        vocales = 0
        for i in self.string:
            if i in "aeiou":
                vocales += 1
        print("El texto tiene", vocales, "vocales")
        
    def eliminar_espacios(self):
        self.string = self.string.strip()
        i=0
        nuevafrase = ""
        while i<len(self.string):
            if self.string[i] == " ":
                while self.string[i+1] == " " and i+1< len(self.string):
                    i += 1
            nuevafrase += self.string[i]
            i += 1
        self.string = nuevafrase
        
    def contar_palabras(self):
        self.eliminar_espacios()
        palabras = 1
        for letra in self.string:
            if letra == " ":
                palabras += 1
        print(f"El texto ingresado tiene {palabras} palabras")
                
    def contar_letras(self):
        cantidad = 0
        letras = "abcdefghijklmnopqrstuvwxyzáéíóú"
        letras += letras.upper()
        for i in self.string:
            if i in letras:
                cantidad +=1
        print(f"El texto ingresado tiene {cantidad} letras")
    def __str__(self):
        return (self.string)
        
        
palabra = Textos("Rodrigo      Eduardo    Ramirez    ")
palabra.contar_vocales()
palabra.eliminar_espacios()
print(palabra)

texto = Textos( """En un pequeño pueblo, un niño encontró una llave dorada. 
Decidió probarla en la puerta más antigua del lugar. 
Al abrirla, descubrió un jardín mágico donde los animales hablaban y las flores cantaban. 
Cada día, el niño visitaba el jardín, aprendiendo valiosas lecciones de sus nuevos amigos. 
Un día, la llave desapareció, pero el niño nunca olvidó las maravillas que había visto y las lecciones que había aprendido.""")
    
texto.contar_letras()
texto.contar_palabras()
palabra.contar_letras()