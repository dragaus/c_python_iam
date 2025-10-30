from flask import Flask, request
import random

version = "v0.1.0"
preguntas = []
preguntas_incremento = 1

# python -m flask --app <Nombre app> run
# python -m flask --app quizz.py run --host=0.0.0.0
app = Flask(__name__)

@app.route("/")
def health():
    return {"mensaje": "Hola Paco!"}

@app.route("/info")
def info():
    return{
        "version": version,
        "status": "ok"
    }

@app.route("/saludame/<nombre>", methods=["POST", "GET"])
def saludo(nombre):
    if request.method == "GET":
        return {"mensaje": "HOLA MUNDO"}
    else:
        return {"mensaje": f"HOLA {nombre}"}


@app.route("/pregunta", methods=["POST", "GET"])
def pregunta_route():
    global preguntas

    if request.method == "GET":
        return {"preguntas": preguntas}

    data = request.json
    pregunta = data.get("pregunta")
    opciones = data.get("opciones")
    respuesta = data.get("respuesta")

    global preguntas_incremento
    pregunta_id = preguntas_incremento
    preguntas_incremento += 1

    preguntas.append({"pregunta": pregunta, "opciones": opciones,
            "respuesta": respuesta, "id": pregunta_id})


    return {"pregunta": pregunta, "opciones": opciones,
            "respuesta": respuesta, "id": pregunta_id}

@app.route("/pregunta/<int:id>", methods=["GET", "PUT", "DELETE"])
def pregunta_id_route(id : int):
    global preguntas

    pregunta = None
    for p in preguntas:
        if p["id"] == id:
            pregunta = p

    if pregunta == None:
        return {"mensaje": f"No se encontro la pregunta con el id: {id}"}
    
    if request.method == "GET":
        return pregunta
    elif request.method == "DELETE":
        preguntas.remove(pregunta)
        return {"mensaje": "Pregunta eliminada"}
    elif request.method == "PUT":
        data = request.json

        if data != None:
            pr = data.get("pregunta")
            opciones = data.get("opciones")
            respuesta = data.get("respuesta")

            print(pregunta)
            index = preguntas.index(pregunta)
            pregunta["pregunta"] = pr
            pregunta["opciones"] = opciones
            pregunta["respuesta"] = respuesta
            preguntas[index] = pregunta
            return preguntas[index]
        else :
            return {"mensaje": "Necesitamos un json"}
    
    return {"mensaje": ""}

@app.route("/pregunta/random/<int:numero>", methods=["GET"])
def pregunta_random_route(numero: int):
    global preguntas
    nuevo_orden_preguntas = preguntas.copy()
    random.shuffle(nuevo_orden_preguntas)
    return nuevo_orden_preguntas[:numero]