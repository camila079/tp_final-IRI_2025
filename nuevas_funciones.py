#LIBRERIA PARA HACER VENTANAS CON BOTONES 
import tkinter as tk

def imprimir_en_ventana():
    etiqueta.config(text="¡Hola desde el botón!")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Este es el nombre de la ventana")
ventana.geometry("300x500")

# Crear botón
boton = tk.Button(ventana, text="click aqui", command=imprimir_en_ventana)
boton.pack(pady=10)

# Crear etiqueta donde se imprimirá el texto
etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

# Ejecutar la ventana
ventana.mainloop()
