import numpy as np
import matplotlib.pyplot as plt
import csv
import os

#PUNTO 1: LECTURA Y PROCESAMIENTO
#escribo los nombres de mis csv aca arriba por si quiero cambiar el archivo que le doy o el nombre del nuevo
entrada = "pacientes_final.csv"
salida = "pacientes_2025.csv"

#keys de las columnas q necesito
keysdeclinicas = [
    "ID", "NOMBRE", "EDAD", "PESO",
    "ALTURA", "SISTOLICA", "DIASTOLICA",
    "TEMPERATURA", "F_CARD", "N_OXIGENO", 
    "GLUCOSA", "COLESTEROL","PULSOXIMETRO_R", "PULSOXIMETRO_IR",
    "IMC", "PAM", "SPO2", "RGC", "CLASIFICACION"
]

pacientes = [] #guardo los pecientes en una lista

#abro el archivo para leerlo y guardar lo necesario
with open(entrada, "r", encoding="utf-8-sig", newline="") as p:
    reader = csv.DictReader(p)

    for fila in reader:
        id_paciente = fila["paciente_id"]
        paciente = {"ID": id_paciente,
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
with open(salida, "w", encoding="utf-8-sig", newline="") as archivo: #archivo q escribo
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

def calcular_porcentaje_R_IR(percent_r, percent_ir):
    porcentaje_r_ir = 0.0
    sum_r_ir = percent_r + percent_ir
    if(sum_r_ir<=0):
        print("Revise valores ingresados")
    else:
        porcentaje_r_ir = 100*(percent_ir/(sum_r_ir))
    
    return porcentaje_r_ir

def calcular_imc(masa, altura):
    imc = 0.0
    if (altura<=0):
        print("La altura ingrsada es incorrecta")
        print("Revise valores ingresados")
    elif(masa<=0):
        print("La masa ingresada es incorrecta")
        print("Revise los valores ingresados")
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
        print("El porcentaje de colesterol es inválido.")
        print("Revise los valores ingresados")
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

    return pacientedatos

#reescribo 
with open("pacientes_nuevo.csv", "w", encoding="utf-8-sig", newline="") as archivo: #archivo q escribo
        writer = csv.DictWriter(archivo, fieldnames=keysdeclinicas)
        writer.writeheader()
        calcular_valores(pacientes)
        writer.writerows(pacientes)

#PUNTO 2: Analisis de ECG
def ecg():
    with open ('ecg_id_pacient.csv', "r",encoding="utf-8-sig") as archivo:
        datos= []
        max_señales = [] 
        reader=csv.reader(archivo)
        header=next(reader)
        indice = header.index('ecg_file')
        for linea in reader:
            datos.append(linea[1])
        print(datos)
#calcule y retorne valor maximo y minimo de señal
        for dato in datos:
            ruta =os.path.join(r"C:\Users\camila\OneDrive\Documents\proyectos\ecg_signals", dato)
            señales = abrir_archivos(ruta)
            max_s=señales.max()
            max_señales.append(max_s)
        print(max_señales)
        #valor_min = min (datos)
#calcule y retorne el promedio de la señal
        #promedio = sum(datos)/len(datos) #uso funciones integradas
    return 
#PUNTO 3: Clasificacion y triage
def triage_paciente ()

  
