## 1 ... 100
## 101  
## 5050

## 1 .. 200
## 201
## 201 * 100
## 20

def calculadora_gauss():
    numero_a_calcular = int(input('Hasta que numero quieres sumar')) + 1
    numero_final = 0
    for i in range(numero_a_calcular):
        numero_final += i
        print(i)
    print(numero_final)


calculadora_gauss()

