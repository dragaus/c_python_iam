from ollama import chat

promt_asistente = """"
Eres un asistenmte que se va a dedicar a enseñar aritmetica.
Tienes la capacidad de usar funciones 
Tu nombre es DescarBot
"""

mensajes = [
    {"role": "system", "content":promt_asistente},
    {"role": "user", "content": "puedes presentarte"}
]

modelo="gemma3:1b"

chat_g = chat(model=modelo, messages=mensajes)

print("DecarBot:", chat_g.message.content)

while True:
    user_input = input("Usurio: ")
    mensajes.append({"role": "user", "content": user_input})

    