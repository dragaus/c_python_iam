import csv

with open('clima.csv', 'r') as csv_archivo:
    data = csv.reader(csv_archivo)
    maximas=[]
    for fila in data:
        print(fila)
        maximas.append(fila[1])
    print(maximas)

# archivo = open('clima.csv', 'r')
# texto = archivo.readlines()


# data_lineas = [linea.strip().split(',') for linea in texto]
# print(data_lineas[1][0])

###--Dia--Max--Min--Prob
###--Lun--009--007--015%
###--Mar--010--006--005%
