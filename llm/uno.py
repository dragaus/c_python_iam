import ollama

modelo = "llama3.2"

resultado = ollama.generate(model=modelo, 
            prompt="¿Como se dice avion en arabe?")

print(resultado['response'])