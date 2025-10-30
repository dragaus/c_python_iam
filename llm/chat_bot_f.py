import ollama

model = "llama3.2"

informacion_agente = """
Eres un agente que va a ayudar en el aprendizaje del frances.
Cualquier otra pregunta que no sea relacionada a ello, respondela con 'no puedo ayudarte con ello'
Tambien vas a ayudar a crear practicas del idioma y a mejorar el vocabulario.
Te llamas Oliver.
Si el usuario te habla en español trata de contestar en español en caso contrario usa el frances
"""


mensajes = [
    {"role": "system", "content": informacion_agente},
    {"role": "user", "content": "Hola, ¿Te puedes presentar?"}
]

respuesta = ollama.chat(model=model, messages=mensajes)
print("Oliver: ", respuesta.message.content)


while True:
    input_usuario = input("Tú: ")
    mensajes.append({"role":"user", "content": input_usuario})

    res = ollama.chat(model=model, messages=mensajes, stream=True)

    for chunk in res:
        print(chunk['message']['content'], end='', flush= True)
    
    print("\n")
    # mensajes.append({"role": "assistant", "content": res.message.content})