def buscar_categoria(diccionario, categoria):
      if diccionario.get(categoria):
            print(f"Categoria {categoria}:", end="\n-")
            print(*diccionario[categoria],sep="\n-",)
      else:
            print("Categoria no encontrada")

def crear_diccionario(ingreso_usuario, diccionario):
      if diccionario==0:
            diccionario = {} 
      dato = tuple(ingreso_usuario.split(" "))
      for elemento in dato:
                  valores = elemento.split(":")
                  if diccionario.get(valores[0]):
                        if not valores[1] in diccionario[valores[0]]:
                         diccionario[valores[0]].add(valores[1])
                  else:
                        set = {valores[1]}
                        diccionario[valores[0]] = set
      return diccionario

mostrar_categorias = lambda diccionario : print("Categorias:", *diccionario.keys(), sep=" - ")

def mostrar_elementos(diccionario):
      for clave in diccionario:
            print(f"Categoria {clave}:", end="\n-")
            print(*diccionario[clave], sep="\n-")


productos = crear_diccionario("fruta:manzana fruta:naranja fruta:mandarina verdura:papa fruta:naranja verdura:lechuga", 0)
productos = crear_diccionario("fruta:kiwi fruta:anana verdura:zapallo",productos)
buscar_categoria(productos, "fruta")
mostrar_categorias(productos)
mostrar_elementos(productos)
