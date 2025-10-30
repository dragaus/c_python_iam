## oso 
## anita lava la tina

def es_palindromo(frase: str):
    frase = frase.lower()
    # print(revertida)
    ##
    frase_limpia = ""
    for caracter in frase:
        if caracter == " ":
            continue
        frase_limpia += caracter
    
    print(frase_limpia)
    revertida = frase_limpia[::-1]
    return frase_limpia == revertida

print(es_palindromo("Oso"))

print(es_palindromo("Anita lava la tina"))