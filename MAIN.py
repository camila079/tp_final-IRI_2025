import numpy as np
import matplotlib.pyplot as plt
import csv

def calcular_porcentaje_R_IR():
    pass

def calcular_valores(pacientedatos): #calcula el imc y etc y le das el dic del paciente
    pacientes_completos = []
    longitud_datos = len(pacientedatos)
    imc = 0.0 #Indice de masa corporal    
    pam = 0.0 #Presion arterial media
    oxim = 0.0 #Indice de SpO2
    rgc = 0.0 #Relacion glucosa-colesterol
    for i in range(longitud_datos):
        #IMC= masa/altura*altura
        masa = pacientedatos[i]["MASA"]
        altura = pacientedatos[i]["ALTURA"]
        imc = float(masa)/pow(float(altura),2)
        pacientes_completos[i]["IMC"].append(imc)
        
        #pam =PDias+(PSis+PDias)/3
        pres_diastolica = pacientedatos[i]["DIASTOLICA"]
        pres_sistolica = pacientedatos[i]["SISTOLICA"]
        pam = float(pres_diastolica)+ ((float(pres_diastolica)+float(pres_sistolica))/3)
        pacientes_completos[i]["PAM"].append(pam)

        #oximetria = 100*(IF/(R+IF))
        porcentaje_roja = pacientedatos[i]["PULSOXIMETRO R"]
        porcentaje_infrarroja = pacientedatos[i]["PULSOXIMETRO IR"]
        calcular_porcentaje_R_IR()
        oxim = 100*(porcentaje_infrarroja/(porcentaje_roja+porcentaje_infrarroja))
        pacientes_completos[i]["SPO2"].append(oxim)
        
        #rgc = glu/col
        glucosa = pacientedatos[i]["GLUCOSA"]
        colesterol = pacientedatos[i]["COLESTEROL"]
        rgc = float(glucosa)/float(colesterol)
        pacientes_completos[i]["RGC"].append(rgc)
    
    return pacientes_completos #AGREGA los CALCULOS A LA LISTA DE PACIENTES
    #PUNTO 2: Analisis de ECG
def analizar_ecg (): #funcion que lee el archivo
    with open ("ecg_id_pacient.csv", encoding="utf-8") as archivo:
        datos=[float(linea.strip()) for linea in archivo] #leer datos del archivo, linea.strip() elimina los caracteres (espacios en blanco por defecto)
#calcule y retorne valor maximo y minimo de señal
        valor_max = max(datos)
        valor_min= min(datos)
#calcule y retorne el promedio de la señal
        promedio = sum(datos)/len(datos) #uso funciones integradas
    return valor_max, valor_min, promedio
#PUNTO 3: Clasificacion y triage
def triage_paciente ()

with open ("pacientes_final.csv","r", encoding="utf-8") as archivo:
  reader=csv.DictReader(archivo)
  headers=reader.fieldnames
  for row in reader:
            ID = row("paciente_id")
            NOMBRE = row["nombre_paciente"]
            EDAD = row["edad"]
            PESO = row["peso_kg"]
            ALTURA = row["altura"]
            SISTOLICA = row["sistolica_mmHg"]
            DIASTOLICA = row["diastolica_mmHg"]
            TEMPERATURA = row["temperatura_C"]
            F_CARD = row["freciencia_cardiaca"]
            N_OXIGENO = row["NIVEL DE OXIGENO"]
            GLUCOSA = row["GLUCOSA"]
            COLESTEROL = row["COLESTEROL"]
            PULSOXIMETRO_ROJA = row["PULSOXIMETRO IR"]
            PULSOXIMETRO_INFRAROJA = row["PULSOXIMETRO R"]


  
