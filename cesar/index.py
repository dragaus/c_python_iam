import sys

argumentos = sys.argv

abecdario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
size_abecedario = len(abecdario)
debe_cifrar = False
mensaje = ""
valor_cifrado = 0

def ayuda():
    mensaje_ayuda ="""
    Usa este pograma para cifrar y decifrar en cesar
    -h es para ayuda
    -c es para cifrar
    -d es para decifrar
    -n ingresa el codigo para cifrar o decifrar
    -m mensaje que quieres cifrar o disifrar
    """
    print(mensaje_ayuda)
    # print("Usa este pograma para cifrar y decifrar en cesar")
    # print("-h es para ayuda")
    # print("-c es para cifrar")
    # print("-d es para decifrar")
    # print("-n ingresa el codigo para cifrar o decifrar")
    # print("-m mensaje que quieres cifrar o disifrar")
    exit()

try:
    if argumentos[1] == "-h" or argumentos[1] == "--help":
        ayuda()
    
    if not "-c" in argumentos and not "-d" in argumentos:
        print("Ingresa -c o -d para cifrar o decifrar")
        exit()
    elif "-c" in argumentos:
        debe_cifrar = True

    if not "-n" in argumentos:
        print("ingresa -n numero de cifrado")
        exit()
    else:
        indice = argumentos.index("-n")
        valor_cifrado = int(argumentos[indice + 1])
        print(f"valor de cifrado es {valor_cifrado}")

    if not "-m" in argumentos:
        print("Ingresa -m con el mensaje")
    else:
        mensaje = argumentos[argumentos.index("-m") +1]
except:
    ayuda()

def cifrar(palabra, codigo):
    palabra = palabra.lower()
    palabra_cifrada = ""
    for caracter in palabra:
        if caracter == " ":
            palabra_cifrada += " "
            continue 
        indice = abecdario.index(caracter)
        palabra_cifrada = palabra_cifrada + abecdario[(indice + codigo) % size_abecedario]
    return palabra_cifrada

def decifrar(plabara, codigo):
    plabara = plabara.lower()
    palabara_decifrada = ""
    for caracter in plabara:
        if caracter == " ":
            palabara_decifrada += " "
            continue 
        indice = abecdario.index(caracter)
        encontrar_indice_correcto = (indice -codigo) % size_abecedario
        palabara_decifrada += abecdario[encontrar_indice_correcto]
    return palabara_decifrada

if debe_cifrar:
    cifrado = cifrar(mensaje, valor_cifrado)
    print(cifrado)
else:
    decifrado = decifrar(mensaje, valor_cifrado)
    print(decifrado)