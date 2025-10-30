from generador import esquema_desde_texto, Esquema_Pass

def obtener_valores_guardados(path) -> list[Esquema_Pass]:
    valores_guardados = []
    try:
        with open(path, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                valores_guardados.append(esquema_desde_texto(linea))
    except:
        return []
    return valores_guardados