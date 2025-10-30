from generador import interfaz_generacion_pass, Esquema_Pass
from obtener_valores import obtener_valores_guardados

path = "pass.txt"
valores_guardados = obtener_valores_guardados(path)

opcion = input('¿Quieres generar u obtener una contraseña (G/O)\n').upper()

def pregunta_comfirmacion(mensaje):
    respuesta = input(f'{mensaje}(S/N)').upper()
    return respuesta == "S"

if opcion == 'G':
    interfaz_generacion_pass(path)
elif opcion == "O":
    sitio = input('De que sitio ocupas tu contraseña?')
    coincidencias : list[Esquema_Pass] = []
    for val in valores_guardados:
        if val.sitio == sitio:
            coincidencias.append(val)

    # Este lugar se encarga de resolver conflictos
    if len(coincidencias) < 1:
        print('No tienes nunguna contraseña guardada para este sitio')
        if pregunta_comfirmacion('¿Quieres generar una contraseña ahora?'):
            interfaz_generacion_pass(path, sitio)
    elif len(coincidencias) == 1:
        print(f"Tu contraseña es {coincidencias[0].password}")
    else:
        print('Tienes mas de un usuario guardado para ese sitio')
        usuario = input('¿Que usuario neceitas?')
        se_encontro_usuario = False
        for coincidencia in coincidencias:
            if coincidencia.usuario == usuario:
                se_encontro_usuario = True
                print(f"Tu contraseña es {coincidencia.password}")
        if not se_encontro_usuario:
            print(f'No tienes nunguna contraseña guardada para {usuario} en {sitio}')
            if pregunta_comfirmacion(f"¿Deseas generar una contraseña para {usuario}?"):
                # interfaz_generacion_pass(path, sitio, usuario)
                interfaz_generacion_pass(path, usuario=usuario, sitio=sitio)


else:
    print("Seleccciona una opcion valida")

