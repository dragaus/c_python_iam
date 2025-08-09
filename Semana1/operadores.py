# nombre = input("¿Cuál es tu nombre? ")
# apellido = "Paramo"

# print(nombre + " " + apellido)

# cita = 'Edison dijo: "hjgjhhbjhk kjhaskjdas" '
# contraccion = "d'italia"

# dos_lineas = '''
# Esta es una multi linea
# aqui es otra linea
# aqui es otra
# '''

# print(dos_lineas)

# edad_texto = input('¿Cuantos años tienes? ')
# edad = int(edad_texto)

# edad = edad + 50
# # print(nombre + edad)

# # Pedro paramo tiene 32 años
# print(nombre + " " + apellido + " tiene " + str(edad) + " años")
# print(f"{nombre} {apellido} tiene {edad} años")

conchas = int(input('¿Cuantas conchas se vendieron?'))
cuernito = int(input('¿Cuantos cuernitos se vendieron?'))
bolillos = int(input('¿Cuantas bolillos se vendieron?'))
bolillos_tarde  = int(input('¿Cuantos bolillos de vendieron despues de las 3?'))

concha_precio = 10
bolillo_precio = 3
cuernito_precio = 15
descuento = .50

# + - * /
venta_total = 0
venta_total += concha_precio * conchas
venta_total += bolillo_precio * (bolillos - bolillos_tarde)
venta_total += bolillos_tarde * (bolillo_precio * descuento)
venta_total += cuernito * cuernito_precio

venta_total_texto = f"La venta total fue de {venta_total}"

print(venta_total_texto)
