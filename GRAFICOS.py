import matplotlib.pyplot as plt
import numpy as np
import FUNCIONES as eu
import os

salida_p = "pacientes_2025.csv"
entrada_sen = "ecg_id_pacient.csv"


def graficar_lineas_senyales(ruta, entrada_sen):
    pacientes = eu.archivos_aux(ruta)
    datos_sen = eu.acceder_ecg(entrada_sen)
    
    # Diccionario para guardar IDs por color
    ids_por_color = {
        "Azul": None, "Verde": None, "Amarillo": None,
        "Naranja": None, "Rojo": None, "Negro": None
    }

    # Asigno el ID de cada color (el primero que aparezca)
    for paciente in pacientes:
        color = paciente["clasificacion"]
        if color in ids_por_color and ids_por_color[color] is None:
            ids_por_color[color] = paciente["id_paciente"]

    # Buscar el archivo ECG correspondiente a cada color
    archivos_ecg = {}
    for color, id_paciente in ids_por_color.items():
        if id_paciente:
            for dato in datos_sen:
                if id_paciente in dato:
                    archivos_ecg[color] = dato
                    break
    
    
    colores = {
        "Azul": "blue", "Verde": "green", "Amarillo": "yellow",
        "Naranja": "orange", "Rojo": "red", "Negro": "black"
    }

    plt.figure(figsize=(12, 8))
    i = 1
    for color, archivo in archivos_ecg.items():
        if not archivo:
            print(f"No hay pacientes en estado {color.lower()}")
            continue
        #
        ruta_archivo = os.path.join(
            r"C:\Users\camila\OneDrive\Documents\proyectos\ecg_signals",
            archivo
        )
        senyales = eu.abrir_archivos(ruta_archivo)
        y = np.array(senyales)

        plt.subplot(2, 3, i)
        plt.plot(y, color=colores[color])
        plt.title(f"ECG - Paciente en estado '{color}'")
        plt.xlabel("Tiempo (seg.)")
        plt.ylabel("Amplitud")
        i += 1
        
    plt.tight_layout()
    plt.show()
    
    return

def graficas_barras_estado(ruta):           
    pacientes = eu.archivos_aux(ruta)
    cant_azul = 0
    cant_verde = 0
    cant_amarillo = 0
    cant_naranja = 0 
    cant_rojo = 0
    cant_negro = 0
    for paciente in pacientes:
        if(paciente["clasificacion"] == "Azul"):
            cant_azul += 1 
        elif(paciente["clasificacion"] == "Verde"):
            cant_verde += 1
        elif(paciente["clasificacion"] == "Amarillo"):
            cant_amarillo += 1
        elif(paciente["clasificacion"] == "Naranja"):
            cant_naranja += 1
        elif(paciente["clasificacion"] == "Rojo"):
            cant_rojo += 1
        elif(paciente["clasificacion"] == "Negro"):
            cant_negro += 1        
            
    fig, ax = plt.subplots()
    x = np.array(["Estado: Azul", "Estado: Verde", "Estado: Amarillo", "Estado: Naranja", "Estado: Rojo", "Estado: Negro"])
    y = np.array([cant_azul, cant_verde, cant_amarillo, cant_naranja, cant_rojo, cant_negro])
    bar_colors = ['tab:blue', 'tab:green', 'yellow', 'tab:orange', 'tab:red', 'black']
    # Crear barras
    ax.bar(x, y, color=bar_colors, width=0.6)
    ax.set_ylabel('Cantidad de pacientes')
    ax.set_title('Pacientes por estado actual')
    plt.xticks(fontsize=10, rotation=20) 
    plt.show()
    
    return

def grafico_dispersion(salida_p):
    try:
        dict_pacientes = eu.archivos_aux(salida_p)
        print("Cantidad de pacientes:", len(dict_pacientes))
        colores = {
            "Azul": "blue",
            "Verde": "green",
            "Amarillo": "yellow",
            "Naranja": "orange",
            "Rojo": "red",
            "Negro": "black"
        }
        
        plt.figure(figsize=(8,6))
        
        for color_nombre, color_valor in colores.items():
            xs = [p["imc"] for p in dict_pacientes if p["clasificacion"] == color_nombre]
            ys = [p["pam"] for p in dict_pacientes if p["clasificacion"] == color_nombre]
            if xs and ys:  # si hay pacientes en ese grupo
                plt.scatter(xs, ys, color=color_valor, label=color_nombre)

        plt.title("Relación IMC vs PAM según clasificación")
        plt.xlabel("Índice de Masa Corporal (IMC)") #2era pos
        plt.ylabel("Presión Arterial Media (PAM)") #2 posc
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        
        plt.show()
    except:
        print("Error, no se pudo ejecutar")
        return
    
def grafico_dispersion(FILE):
    salida_p = FILE
    try:
        dict_pacientes = eu.archivos_aux(salida_p)
        print("Cantidad de pacientes:", len(dict_pacientes))
        colores = {
            "Azul": "blue",
            "Verde": "green",
            "Amarillo": "yellow",
            "Naranja": "orange",
            "Rojo": "red",
            "Negro": "black"
        }
        
        plt.figure(figsize=(8,6))
        
        for color_nombre, color_valor in colores.items():
            xs = [p["imc"] for p in dict_pacientes if p["clasificacion"] == color_nombre]
            ys = [p["pam"] for p in dict_pacientes if p["clasificacion"] == color_nombre]
            if xs and ys:  # si hay pacientes en ese grupo
                plt.scatter(xs, ys, color=color_valor, label=color_nombre)

        plt.title("Relación IMC vs PAM según clasificación")
        plt.xlabel("Índice de Masa Corporal (IMC)") #2era pos
        plt.ylabel("Presión Arterial Media (PAM)") #2 posc
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        
        plt.show()
    except:
        print("Error, no se pudo ejecutar")
    
    return
