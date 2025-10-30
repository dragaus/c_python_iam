from tkinter import *
from tkinter import ttk

def cambiar_label():
    global label
    label.config(text="Esta es mi primer accion!")

# def imprimir_nombre():
#     print("nombre")

# def imprimir_suma():
#     print(2 + 2)

# def funcion_ejecuta_funcion(funcion_ex):
#     print("Estoy por ejecutar otra funcion")
#     funcion_ex()

# funcion_ejecuta_funcion(imprimir_nombre)
# funcion_ejecuta_funcion(imprimir_suma)

root = Tk()
root.geometry("500x500")
frame = ttk.Frame(root, padding=20)
frame.grid()

label = ttk.Label(frame, text="Hola Iam")
label.grid(columnspan=2, row=0)

ttk.Button(frame, text="Ok", command=cambiar_label).grid(column=0, row=1)
ttk.Button(frame, text="Cancel").grid(column=1, row=1)
root.mainloop()



