#####
# fruta.  precio kg
# Manzana   69
# Banana    35
# Durazno   90
# Naranjas  20

## que fruta compro 
## cuantos kilos compro 
## resultado del precio 
## no exitsa la fruta que quiere comprar y le vamos dar error

diccionario = {"pepe": 3}
frutas = {"manzana": 69, "banana": 35, "durazno": 90, "naranjas": 20}

def calcular_costo():
    global frutas
    fruta = input("¿Que fruta quieres comprar? ").lower()

    if not fruta in frutas:
        print(f"No tenemos {fruta}!")
        return ""

    kilos = input("¿Cuantos kilos quieres? ")
    

    # return f"Compraste {kilos} de {fruta} son {total}"
    return frutas[fruta] * kilos

print(calcular_costo())