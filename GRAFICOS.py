import matplotlib.pyplot as plt
import numpy as np
import FUNCIONES as eu
import os

salida_p = "pacientes_2025"
entrada_sen = "ecg_id_pacient.csv"


def graficar_lineas_senyales(ruta, entrada_sen):
    pacientes, imc, pam, clasificacion = eu.archivos_aux(ruta)
    datos_sen = eu.acceder_ecg(entrada_sen)
    graficos_color = []
    for paciente in pacientes:
        #Busco el id de pacientes de cada color(estado del paciente)
        if(paciente["clasificacion"] == "Azul"):
            id_azul = paciente["id_paciente"]
        elif(paciente["clasificacion"] == "Verde"):
            id_verde = paciente["id_paciente"]
        elif(paciente["clasificacion"] == "Amarillo"):
            id_amarillo = paciente["id_paciente"]
        elif(paciente["clasificacion"] == "Naranja"):
            id_naranja = paciente["id_paciente"]
        elif(paciente["clasificacion"] == "Rojo"):
            id_rojo = paciente["id_paciente"]
        elif(paciente["clasificacion"] == "Negro"):
            id_negro = paciente["id_paciente"]
            
        #Accedo a cada uno de los nombres de los archivos de los ids encontrados    
        for dato in datos_sen:
            if id_azul in datos_sen:
                graf_azul = dato
            elif id_verde in datos_sen:
                graf_verde = dato
            elif id_amarillo in datos_sen:
                graf_amarillo = dato
            elif id_naranja in datos_sen:
                graf_naranja = dato
            elif id_rojo in datos_sen:
                graf_rojo = dato
            elif id_negro in datos_sen:
                graf_negro = dato
                
    #graf azul
    ruta_az = os.path.join(r"C:\Users\camila\OneDrive\Documents\proyectos\ecg_signals", graf_azul)
    senyales_az = eu.abrir_archivos(ruta_az)
    y_az = np.array(senyales_az)
    plt.subplot(2, 3, 1)
    plt.plot(y_az, color = 'blue')
    plt.title("ECG - Paciente en estado 'Azul'")
    plt.xlabel("Tiempo(seg.)")
    plt.ylabel("Amplitud")
    
    #graf verde
    ruta_v = os.path.join(r"C:\Users\camila\OneDrive\Documents\proyectos\ecg_signals", graf_verde)
    senyales_v = eu.abrir_archivos(ruta_v)
    y_v = np.array(senyales_v)
    plt.subplot(2, 3, 2)
    plt.plot(y_v, color = 'green')
    plt.title("ECG - Paciente en estado 'Verde'")
    plt.xlabel("Tiempo(seg.)")
    plt.ylabel("Amplitud")
    
    #graf amarillo
    ruta_am = os.path.join(r"C:\Users\camila\OneDrive\Documents\proyectos\ecg_signals", graf_amarillo)
    senyales_am = eu.abrir_archivos(ruta_am)
    y_am = np.array(senyales_am)
    plt.plot(y_am, color = 'yellow')
    plt.title("ECG - Paciente en estado 'Amarillo'")
    plt.xlabel("Tiempo(seg.)")
    plt.ylabel("Amplitud")

    
    #graf naranja
    ruta_nar = os.path.join(r"C:\Users\camila\OneDrive\Documents\proyectos\ecg_signals", graf_naranja)
    senyales_nar = eu.abrir_archivos(ruta_nar)
    y_nar = np.array(senyales_nar)
    plt.plot(y_nar, color = 'orange')
    plt.title("ECG - Paciente en estado 'Naranja'")
    plt.xlabel("Tiempo(seg.)")
    plt.ylabel("Amplitud")

    
    #graf rojo
    ruta_r = os.path.join(r"C:\Users\camila\OneDrive\Documents\proyectos\ecg_signals", graf_rojo)
    senyales_r = eu.abrir_archivos(ruta_r)
    y_r = np.array(senyales_r)
    plt.plot(y_r, color = 'red')
    plt.title("ECG - Paciente en estado 'Rojo'")
    plt.xlabel("Tiempo(seg.)")
    plt.ylabel("Amplitud")
    
    #graf negro
    ruta_neg = os.path.join(r"C:\Users\camila\OneDrive\Documents\proyectos\ecg_signals", graf_negro)
    senyales_neg = eu.abrir_archivos(ruta_neg)
    y_neg = np.array(senyales_neg)
    plt.plot(y_neg, color = 'black')
    plt.title("ECG - Paciente en estado 'Negro'")
    plt.xlabel("Tiempo(seg.)")
    plt.ylabel("Amplitud")
    
    plt.show()
    
    return

def graficas_barras_estado(ruta):           
    pacientes, imc, pam, clasificacion = eu.archivos_aux(ruta)
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

def grafico_dispersion():
    try:
        dict_pacientes = archivos_aux(salida_p)
        x = np.array([float(imc) for imc in dict_pacientes])
        y = np.array([float(pam) for pam in dict_pacientes])
        plt.figure(figsize=(8,6))
        plt.scatter(x,y)
        plt.title("Relación IMC vs PAM según clasificación")
        plt.xlabel("Índice de Masa Corporal (IMC)") #2era pos
        plt.ylabel("Presión Arterial Media (PAM)") #2 posc
        plt.grid(True)
        plt.show()
    except:
        print("Error, no se pudo ejecutar")
