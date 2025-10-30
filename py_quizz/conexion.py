import requests
from classes.pregunta import Pregunta

base = "http://localhost:5000"

def obtener_pregunta(id):
    req = requests.get(f"{base}/pregunta/{id}")
    json = req.json()
    pregunta = Pregunta(json["pregunta"], 
                        json["respuesta"], json["opciones"])
    return pregunta

def obtener_preguntas_aleatorias(cantidad: int):
    req = requests.get(f"{base}/pregunta/random/{cantidad}")
    json = req.json()
    lista_preguntas = []
    for el in json:
        pregunta = Pregunta(el["pregunta"], 
                            el["respuesta"], el["opciones"])
        lista_preguntas.append(pregunta)
        
    return lista_preguntas
    