# un diccionario español - ingles

# 1 recibir y agregar a mi diccionario
# recibir texto
# casa:house
# casa:house;platano:banana;perro:dog

# 2 traducir
# escribir texto y traducir litermente
# casa azul -> house blue
# casa azul -> house    

diccionario_espanol_ingles = {}

def agregar_datos():
    global diccionario_espanol_ingles
    datos = input("Agrega datos con el formato español:ingles;español:ingles")
    lista_entradas = datos.split(";")
    for entrada in lista_entradas:
        # texto ejemplo perro:dog
        separado = entrada.split(":")
        diccionario_espanol_ingles.update({separado[0]: separado[1]})
        diccionario_espanol_ingles[separado[0]] = separado[1]
    # lista_mapas = 
    pass

def traducir():
    pass


print(diccionario_espanol_ingles)
diccionario_espanol_ingles.update({"casa": "house", "perro": "dog"})
print(diccionario_espanol_ingles)

continuar = True
while continuar:
    print("Ejecutamos")
    opcion = int(input("1) Agregar Entrada\n" \
        "2)Traducir:\nSelecciona opcion:"))

    if opcion == 1:
        agregar_datos()
    elif opcion == 2:
        traducir()
    continuar = input("Seguimos (S/N)").strip().upper() == "S"


