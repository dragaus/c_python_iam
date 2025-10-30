from ollama import chat

model = "gemma3:1b"

informacion_agente = """
Eres un agente que va a ayudar en el aprendizaje del frances.
Cualquier otra pregunta que no sea relacionada a ello, respondela con 'no puedo ayudarte con ello'

"""

conversacion = [
    {"role": "system", "content": informacion_agente },
    {"role": "user", "content": "¿cuanto seria la suma de 2 +2"}
]

respuesta = chat(model=model, messages=conversacion)
print(respuesta.message.content)