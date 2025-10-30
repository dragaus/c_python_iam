import pandas as pd

data = pd.read_csv("wines_SPA.csv")

# print(data)

# print(data.describe())

# print(data.region.unique())

# print(data.region.value_counts())


## Tabla donde descreiban las regiones el promedio de puntuacion por region y el promedio de precio

## {"region": {"promedio_valor": float, "promedio_precio": float}}
## {"0": {"region": "rioja","promedio_valor": 20, "promedio_precio": 30}}

regiones = data.region.unique()

promedios_rating = []
promedios_precio = []
for r in regiones:
    region = data[data.region == r]
    promedios_rating.append(region.rating.mean())
    promedios_precio.append(region.price.mean())


esquema = {"regiones": regiones, 
           "promedio_rating": promedios_rating, "promedio_precio": promedios_precio}

df = pd.DataFrame(esquema)

## calidad_precio promedio_precio / promedio_rating

print(df)
# print(df[df.promedio_precio == df.promedio_precio.min()])

df["calidad_precio"] = df["promedio_precio"] / df["promedio_rating"]

# arriba de 50 el promedio es caro = true o false
df["es_caro"] = df["promedio_precio"] > 50
print(df)
df.to_csv("nueva_vino.csv")
