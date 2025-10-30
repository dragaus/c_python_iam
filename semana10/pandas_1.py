import pandas as pd

## DataFrame y Series 

## DataFrame
df = pd.read_csv('clima.csv')

##Series
# print(df['Max'])
# print(df.Max)

print(df)

dicccionario = df.to_dict()
# print(dicccionario)
lista_maximas = df.Max.to_list()
# print(lista_maximas)

## suma de todos elementos entre el numero de elementos = promedio

promedio = sum(lista_maximas) / len(lista_maximas)
# print(promedio)

# print(df.Max.mean())

## mean es promedio en ingles

# print(df.Max.max())

print(df[df.Dia == "Viernes"])

## encontrar la iunformacion del dia donde la temperatura maxima se la menor

print(df[df.Max == df.Max.min()])
print(df[df.Max < df.Max.mean()])
print(df[df.Lluvia_Probabilidad > 45])

## Celcius a F  F = (C * 1.8) + 32
## Encontrar la temperatura maxima y minima del lunes en Farenheit

## Encontar la informacion del lunes
def celcius_farenheit(c):
    return(c *1.8)+32

lunes = df[df.Dia == "Lunes"]


print(celcius_farenheit(lunes.Max))
print(celcius_farenheit(lunes.Min))

data_dic = {
    "Estudiantes": ["Mario", "Juan", "Toño"],
    "Calificaciones": [100, 20, 80]
}

estudiantes_df = pd.DataFrame(data_dic)
print(estudiantes_df)

estudiantes_df.to_csv('estudiantes.csv', index=False)