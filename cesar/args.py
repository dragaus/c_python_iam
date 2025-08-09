import sys
argumentos = sys.argv
print('hola')
print(argumentos)

"--version"
"-v"

match argumentos[1]:
    case "-h":
        print("Ayuda")