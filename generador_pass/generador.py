import random
abecdario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numeros = ['1', '2','3', '4','5','6','7','8','9','0']
simbolos = ['_', '-', '*', '.', '?', '#']

caractere_base = 12

class Esquema_Pass:
    def __init__(self, sitio, usuario, password):
        self.sitio = sitio,
        self.usuario = usuario,
        self.password = password
    
    def to_string(self):
        diccionario = {"sitio": self.sitio, "usuario": self.usuario,  "password": self.password}
        return str(diccionario)

def esquema_desde_texto(texto:str):
    diccionario = eval(texto)
    return Esquema_Pass(diccionario['sitio'], diccionario['usuario'], diccionario['password'])


def interfaz_generacion_pass(path, sitio = "", usuario = ""):
    if len(sitio) < 1:
        sitio = input('¿Para que sitio web vas a generar la contraseña?')
    if len(usuario) < 1:
        usuario = input('¿Que usuario ocupara la contraseña?')

    password = generar_pass()

    esquema = Esquema_Pass(sitio, usuario, password)

    try:
        with open(path, "a") as archivo:
            archivo.write(esquema.to_string() + '\n')
    except:
        print('Sucedio un error intenta mas tarde')

def generar_pass():
    i = 0
    password = ""
    while i < caractere_base:
        seleccion = random.randint(0,2)
        match seleccion:
            case 0:
                password += escoger_letra()
            case 1:
                password += escoger_numero()
            case 2:
                password += escoger_simbolo()
        i += 1
    return password

def escoger_letra():
    indice = random.randint(0, len(abecdario) - 1)
    mayuscula = random.randint(0,1)
    if mayuscula == 0:
        return abecdario[indice].upper()
    return abecdario[indice]

def escoger_numero():
    indice = random.randint(0, len(numeros)-1)
    return numeros[indice]

def escoger_simbolo():
    indice = random.randint(0, len(simbolos)-1)
    return simbolos[indice]