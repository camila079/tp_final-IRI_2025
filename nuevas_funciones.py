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
#------------------------
#Funciones para debuggear
def eliminar_paciente(id, entrada_p):
    filas_filtradas = []
    pacientes_eliminados = []

    # Leer archivo y filtrar
    with open(entrada_p, "r", encoding="utf-8-sig") as archivo:
        reader = csv.DictReader(archivo)
        fieldnames = reader.fieldnames

        for fila in reader:
            if fila["ID"] != id:
                filas_filtradas.append(fila)
            else:
                pacientes_eliminados.append(fila)

    # Reescribir archivo con las filas filtradas
    with open(salida_p, "w", encoding="utf-8-sig", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filas_filtradas)

    return filas_filtradas
