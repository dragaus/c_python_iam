# El usuario debe ser capaz de ingresar 
# peso en kg y altura en metros
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en m: "))

imc = round(peso / altura ** 2, 2)

print(f"Tu imc es de {imc}")