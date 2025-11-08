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

####################### CODIGO PARA PROBAR FUNCIONES DE GRAFICOS ################
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

file= "pacientes_final.csv"
entrada_p = "pacientes_nuevo.csv"
salida_p = "pacientes_nuevo.csv"

keysdeclinicas = [
    "ID", "NOMBRE", "EDAD", "PESO",
    "ALTURA", "SISTOLICA", "DIASTOLICA",
    "TEMPERATURA", "F_CARD", "N_OXIGENO", 
    "GLUCOSA", "COLESTEROL","PULSOXIMETRO_R", "PULSOXIMETRO_IR",
    "IMC", "PAM", "SPO2", "RGC", "CLASIFICACION"
]

pacientes = [] #guardo los pecientes en una lista


def triage_paciente (p):
    try:
        fc = float(p.get("F_CARD", 0) or 0)
        pam = float(p.get("PAM", 0) or 0)
        temp = float(p.get("TEMPERATURA", 0) or 0)
        oxi = float(p.get("N_OXIGENO", 0) or 0)
        imc = float(p.get("IMC", 0) or 0)
        glu = float(p.get("GLUCOSA", 0) or 0)
        col = float(p.get("COLESTEROL", 0) or 0)
    except AttributeError:
        return "Error"

    # Clasifico por prioridad descendente
    criterios = [
        ("Negro", fc == 0 and pam == 0),
        ("Rojo", temp and temp > 39.5),
        ("Rojo", oxi and oxi < 85),
        ("Rojo", pam and (pam < 60 or pam > 120)),
        ("Naranja", temp and 38.5 <= temp <= 39.5),
        ("Naranja", fc and (fc < 50 or fc > 120)),
        ("Naranja", oxi and 85 <= oxi <= 92),
        ("Naranja", imc and imc > 40),
        ("Amarillo", temp and 37.5 <= temp < 38.5),
        ("Amarillo", glu and glu > 180),
        ("Amarillo", col and col > 240),
        ("Verde", imc and 25 <= imc <= 30),
        ("Verde", glu and col and glu > 100 and col > 200),
    ]

    for color, condicion in criterios:
        if condicion:
            return color

    return "Azul"

def archivos_aux(ruta):
    with open(ruta, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        imc = []
        pam = []
        clasificacion = []
        pacientes = []

        for row in reader:
            id_actual = row["ID"]
            imc_val = float(row["IMC"])
            pam_val = float(row["PAM"])
            clase = triage_paciente(row)

            pacientes.append({
                "id_paciente": id_actual,
                "imc": imc_val,
                "pam": pam_val,
                "clasificacion": clase
            })

            imc.append(imc_val)
            pam.append(pam_val)
            clasificacion.append(clase)

    return pacientes, imc, pam, clasificacion

def calcular_porcentaje_R_IR(percent_r, percent_ir):
    porcentaje_r_ir = 0.0
    sum_r_ir = percent_r + percent_ir
    if(sum_r_ir<=0):
        porcentaje_r_ir = -1 #le asigno un valor para indicar que el valor es incorrecto
    else:
        porcentaje_r_ir = 100*(percent_ir/(sum_r_ir))
    
    return porcentaje_r_ir

def calcular_imc(masa, altura):
    imc = 0.0
    if (altura<=0):
        imc = -1 #le asigno un valor para indicar que el valor es incorrecto
    elif(masa<=0):
        imc = -1
    else: 
        imc = float(masa)/pow(float(altura),2)
    return imc 

def calcular_pres_am(p_dias,p_sis):
    pam = 0.0
    pam = (((2*float(p_dias))+float(p_sis))/3)
    return pam

def calcular_relacion_gc(gluc, colest):
    gc = 0.0
    if (colest<=0):
        gc = -1 #le asigno un valor para indicar que el valor es incorrecto
    else: 
        gc = float(gluc)/float(colest)
    
    return gc

def calcular_valores(pacientedatos): #calcula el imc y etc y le das el dic del paciente
    #longitud_datos = len(pacientedatos)
    imc = 0.0 #Indice de masa corporal    
    pam = 0.0 #Presion arterial media
    oxim = 0.0 #Indice de SpO2
    rgc = 0.0 #Relacion glucosa-colesterol
    for paciente in pacientedatos:
        #IMC= masa/altura*altura
        masa = paciente["PESO"]
        altura = float(paciente["ALTURA"])
        imc = calcular_imc(masa, altura)
        paciente["IMC"] = imc  
              
        #pam =PDias+(PSis+PDias)/3
        pres_diastolica = paciente["DIASTOLICA"]
        pres_sistolica = paciente["SISTOLICA"]
        pam = calcular_pres_am(pres_diastolica, pres_sistolica)
        paciente["PAM"]= pam

        #oximetria = 100*(IF/(R+IF))
        porcentaje_roja= float(paciente["PULSOXIMETRO_R"])
        porcentaje_infrarroja= float(paciente["PULSOXIMETRO_IR"])
        # calcular_porcentaje_R_IR()
        oxim = calcular_porcentaje_R_IR(porcentaje_roja, porcentaje_infrarroja)
        paciente["SPO2"] = oxim
        
        #rgc = glu/col
        glucosa = paciente["GLUCOSA"]
        colesterol = paciente["COLESTEROL"]
        rgc = calcular_relacion_gc(glucosa, colesterol)
        paciente["RGC"]= rgc
            
    return

def leer_pacientes(file):
    pacientes = []
    with open("pacientes_final.csv", "r", encoding="utf-8-sig", newline="") as p:
        reader = csv.DictReader(p)

        for fila in reader:
            paciente = {"ID": fila["paciente_id"],
                        "NOMBRE": fila["nombre_paciente"].upper(),
                        "EDAD": fila["edad"],
                        "PESO": fila["peso_kg"],
                        "ALTURA": fila["altura_m"],
                        "SISTOLICA": fila["sistolica_mmHg"],
                        "DIASTOLICA": fila["diastolica_mmHg"],
                        "TEMPERATURA": fila["temperatura_C"],
                        "F_CARD": fila["frecuencia_cardiaca_lpm"],
                        "N_OXIGENO": fila["nivel_oxigeno_perc"],
                        "GLUCOSA": fila["glucosa_mg_dL"],
                        "COLESTEROL": fila["colesterol_mg_dL"],
                        "PULSOXIMETRO_R": fila["pulsoximetro_r_perc"],
                        "PULSOXIMETRO_IR": fila["pulsoximetro_ir_perc"],
                        "IMC": 0.0,                         
                        "PAM": 0, 
                        "SPO2": 0, 
                        "RGC": 0,
                        "CLASIFICACION": 0
                        }
            pacientes.append(paciente)
    #try:
        #y corrijo errores en el ingreso de archivos (pending....)
    with open(salida_p, "w", encoding="utf-8-sig", newline="") as archivo: #archivo q escribo
        writer = csv.DictWriter(archivo, fieldnames=keysdeclinicas)
        writer.writeheader()
        for paciente in pacientes:
            #float
            paciente["DIASTOLICA"] = round(float(paciente["DIASTOLICA"]), 2)
            paciente["SISTOLICA"] = round(float(paciente["SISTOLICA"]), 2)
            paciente["TEMPERATURA"] = round(float(paciente["TEMPERATURA"]), 2)
            paciente["PESO"] = round(float(paciente["PESO"]), 2)
            paciente["ALTURA"] = round(float(paciente["ALTURA"]), 2)
            #int
            paciente["N_OXIGENO"] = round(int(paciente["N_OXIGENO"]))
            paciente["EDAD"] = round(int(paciente["EDAD"]))
            paciente["GLUCOSA"] = round(int(paciente["N_OXIGENO"]))
            paciente["COLESTEROL"] = round(int(paciente["COLESTEROL"]))
            writer.writerows(pacientes)
    return pacientes

def sumar_info_pacientes(entrada_p):
    pacientes = leer_pacientes(entrada_p)
    salida_p = "pacientes_2025.csv"

    calcular_valores(pacientes)  # Calcula IMC, PAM, etc.

    for paciente in pacientes:
        paciente["CLASIFICACION"] = triage_paciente(paciente)

    with open(salida_p, "w", encoding="utf-8-sig", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=keysdeclinicas)
        writer.writeheader()
        writer.writerows(pacientes)


def graficas_barras_estado(ruta):           
    pacientes, imc, pam, clasificacion = archivos_aux(ruta)
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

leer_pacientes(file)
sumar_info_pacientes("pacientes_nuevo.csv")
a = graficas_barras_estado("pacientes_2025.csv")
