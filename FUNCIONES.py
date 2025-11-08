import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import graficos as gr

#PUNTO 1: LECTURA Y PROCESAMIENTO
#escribo los nombres de mis csv aca arriba por si quiero cambiar el archivo que le doy o el nombre del nuevo
entrada_p = "pacientes_final.csv"
salida_p = "pacientes_2025.csv"

entrada_s= "ecg_id_pacient.csv"
salida_s="ecgpacientes_2025.csv"

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
def leer_pacientes(entrada_p):
    with open(entrada_p, "r", encoding="utf-8-sig", newline="") as p:
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

def dar_alta_paciente(entrada_p):
    # Leer pacientes existentes
    pacientes = leer_pacientes(entrada_p)

    # Obtener datos del nuevo paciente
    nombre = input("Ingresa el nombre y apellido del nuevo paciente: ")
    # salida_p [eval(linea.strip()) for linea in lineas]input("Ingrese
    edad = int(input("Ingrese edad: "))
    peso = float(input("Ingrese peso (Kg): "))
    altura = float(input("Ingrese altura (m): "))
    sistolica = input("Ingrese sistolica (MMHG): ")
    diastolica = input("Ingrese diastolica (MMHG): ")
    temperatura =input("Ingrese temperatura (°c): ")
    f_card = input("Ingrese frecuencia cardiaca: ")
    n_oxigeno = input("Ingrese nivel de oxigeno: ")
    glucosa = input("Ingrese glucosa: ")  
    colesterol = input("Ingrese colesterol: ")
    pulsoximetro_r = input("Ingrese pulsoximetro rojo: ")             
    pulsoximetro_ir = input("Ingrese pulsoximetro infrarrojo: ")                 
    # Crear el nuevo registro y agregarlo
    nuevo_paciente = {
        "ID": generar_id(),
        "NOMBRE": nombre,
        "EDAD": edad,
        "PESO": peso,
        "ALTURA": altura,
        "SISTOLICA": sistolica,
        "DIASTOLICA": diastolica,
        "TEMPERATURA": temperatura,
        "F_CARD": f_card,
        "N_OXIGENO": n_oxigeno,
        "GLUCOSA": glucosa,
        "COLESTEROL": colesterol,
        "PULSOXIMETRO_R": pulsoximetro_r,
        "PULSOXIMETRO_IR": pulsoximetro_ir}
    pacientes.append(nuevo_paciente)

    # Escribir la lista actualizada de nuevo en el archivo
    salida_p = "pacientes_2025.csv"
    escribir_archivo(salida_p, pacientes)####
    
def escribir_archivo(ruta, lista):
    with open(ruta, 'w', encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keysdeclinicas)
        writer.writeheader()
        writer.writerows(lista)
            #escribe el contenido de la variable paciente en un archivo, asegurándose de que cada paciente quede en una línea separada

    print("Paciente dado de alta exitosamente.")
def generar_id():
    pacientes, imc, pam, clasificacion = archivos_aux(salida_p)

    lista_ids = [p["id_paciente"] for p in pacientes]

    numeros = [int(i[1:]) for i in lista_ids if i.startswith("P") and i[1:].isdigit()]
    
    nuevo_numero = max(numeros) + 1 if numeros else 1
    
    new=f"P{nuevo_numero:04d}"

    return new
def eliminar_paciente(id, entrada_p):
    filas_filtradas = []
    pacientes_eliminados = []
    with open(entrada_p, "r", encoding="utf-8-sig") as archivo:
                reader = csv.DictReader(archivo)
                fieldnames = reader.fieldnames
                for fila in reader:
                    if fila["ID"] != id:
                        filas_filtradas.append(fila)
                    else:
                        pacientes_eliminados.append(fila)
                        
    with open("pacientes_eliminados", "w", encoding="utf-8-sig", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=fieldnames)
        writer.writeheader
        writer.writerow(pacientes_eliminados)
    salida_p = "pacientes_2025.csv"
    escribir_archivo(salida_p, filas_filtradas)####
        
    return

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
        
        if(imc == -1 or pam == -1 or oxim == -1 or rgc == -1):
            eliminar_paciente(paciente["ID"], entrada_p)
            
    return

#reescribo 
def sumar_info_pacientes(entrada_p):
    pacientes = leer_pacientes(entrada_p)
    salida_p = "pacientes_2025.csv"
    calcular_valores(pacientes)
    for paciente in pacientes:        
        paciente["CLASIFICACION"] = triage_paciente(paciente)
    with open(salida_p, "w", encoding="utf-8-sig", newline="") as archivo: #archivo q escribo
            writer = csv.DictWriter(archivo, fieldnames=keysdeclinicas)
            writer.writeheader()
            writer.writerows(pacientes)

#PUNTO 2: Analisis de ECG
def abrir_archivos(ruta):
    with open(ruta, "r") as f:
            return np.array([float(x.strip()) for x in f.readlines()])
import csv

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

#devuelve max min y promedio

def acceder_ecg(entrada_s):
    datos = []
    try:
        with open(entrada_s, "r", encoding="utf-8-sig") as archivo:
            reader = csv.reader(archivo)
            header = next(reader)
            indice = header.index('ecg_file')
            
            for linea in reader:
                datos.append(linea[indice])
                #encontro datos y los guardo
            
    except Exception as e: #no se pudo abrir el archivo ya esta
        print(f"Error en la lectura de archivos ECG: {e}")
        return None, None
    
    return datos

def ecg_senyales(entrada_s):
    max_señales = []
    min_señales = []
    prom_señales = []

    datos = acceder_ecg(entrada_s)
    for dato in datos:
        ruta = os.path.join(r"C:\Users\camila\OneDrive\Documents\proyectos\ecg_signals", dato)
        señales = abrir_archivos(ruta)
        #señales = acceder_ecg(entrada_s)
        max_señales.append({"archivo": dato, "max": float(señales.max())})
        min_señales.append({"archivo": dato, "min": float(señales.min())})
        prom_señales.append({"archivo": dato, "promedio": sum(datos)/len(datos)})
            #uso funciones integradas
            #ahora tengo un diccionario con los valores maximos y minimos relacionado al key de archivo 
    return max_señales, min_señales, prom_señales

def buscar_paciente(id):
    id_limpio = id.strip().upper()
    if not id_limpio.startswith("P"):
        id_limpio = "P" + id_limpio

    try:
        with open(salida_p, mode="r", encoding="utf-8-sig") as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                if id_limpio == fila.get("ID", "").strip().upper():
                    return {
                        "ID": id_limpio,
                        "NOMBRE": fila.get("NOMBRE", "").upper(),
                        "EDAD": fila.get("EDAD", ""),
                        "PESO": fila.get("PESO", ""),
                        "ALTURA": fila.get("ALTURA", ""),
                        "SISTOLICA": fila.get("SISTOLICA", ""),
                        "DIASTOLICA": fila.get("DIASTOLICA", ""),
                        "TEMPERATURA": fila.get("TEMPERATURA", ""),
                        "F_CARD": fila.get("F_CARD", ""),
                        "N_OXIGENO": fila.get("N_OXIGENO", ""),
                        "GLUCOSA": fila.get("GLUCOSA", ""),
                        "COLESTEROL": fila.get("COLESTEROL", ""),
                        "PULSOXIMETRO_R": fila.get("PULSOXIMETRO_R", ""),
                        "PULSOXIMETRO_IR": fila.get("PULSOXIMETRO_IR", ""),
                        "IMC": float(fila.get("IMC", 0.0)),
                        "PAM": float(fila.get("PAM", 0.0)),
                        "SPO2": float(fila.get("SPO2", 0.0)),
                        "RGC": float(fila.get("RGC", 0.0)),
                        "CLASIFICACION": fila.get("CLASIFICACION", "0")
                    }
    except Exception as e:
        print(f"Error al buscar paciente: {e}")

    return None  # Si no se encuentra el paciente

def buscar_paciente_por_apellido(apellido):
    apellido_limpio = apellido.strip().upper()

    try:
        with open(salida_p, mode="r", encoding="utf-8-sig") as archivo:
            reader = csv.DictReader(archivo)
            resultados = []

            for fila in reader:
                nombre_completo = fila.get("NOMBRE", "").strip().upper()
                # Si el apellido aparece en el nombre
                if apellido_limpio in nombre_completo:
                    resultados.append({
                        "ID": fila.get("ID", "").strip().upper(),
                        "NOMBRE": nombre_completo,
                        "EDAD": fila.get("EDAD", ""),
                        "PESO": fila.get("PESO", ""),
                        "ALTURA": fila.get("ALTURA", ""),
                        "SISTOLICA": fila.get("SISTOLICA", ""),
                        "DIASTOLICA": fila.get("DIASTOLICA", ""),
                        "TEMPERATURA": fila.get("TEMPERATURA", ""),
                        "F_CARD": fila.get("F_CARD", ""),
                        "N_OXIGENO": fila.get("N_OXIGENO", ""),
                        "GLUCOSA": fila.get("GLUCOSA", ""),
                        "COLESTEROL": fila.get("COLESTEROL", ""),
                        "PULSOXIMETRO_R": fila.get("PULSOXIMETRO_R", ""),
                        "PULSOXIMETRO_IR": fila.get("PULSOXIMETRO_IR", ""),
                        "IMC": float(fila.get("IMC", 0.0)),
                        "PAM": float(fila.get("PAM", 0.0)),
                        "SPO2": float(fila.get("SPO2", 0.0)),
                        "RGC": float(fila.get("RGC", 0.0)),
                        "CLASIFICACION": fila.get("CLASIFICACION", "0")
                    })
            contador = len(resultados)
            if contador != 1:
                print(f"Hay {contador} pacientes con este apellido")
                for i in range(contador):
                    print(f"{i}.{resultados[i]['ID']}, {resultados[i]['NOMBRE']}")
                seleccion = int(input("Ingrese el numero de quien busca"))
                try:
                    paciente_elegido = resultados[seleccion]
                    for clave, valor in paciente_elegido.items():
                        print(f"{clave}: {valor}")

                except (ValueError, IndexError):
                    print("Selección inválida.")
            return

    except Exception as e:
        print(f"Error al buscar paciente por apellido: {e}")

    return

#PUNTO 3: Clasificacion y triage
def triage_paciente (id):
    try:
        fc = float(id.get("F_CARD", 0) or 0)
        pam = float(id.get("PAM", 0) or 0)
        temp = float(id.get("TEMPERATURA", 0) or 0)
        oxi = float(id.get("N_OXIGENO", 0) or 0)
        imc = float(id.get("IMC", 0) or 0)
        glu = float(id.get("GLUCOSA", 0) or 0)
        col = float(id.get("COLESTEROL", 0) or 0)
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

#PUNTO 4: Reporte y Visualizacion
#PUNTO 4: Reporte y Visualizacion 
def reporte_general(salida_p):
        try:
            with open(salida_p, mode="r", encoding="utf-8-sig") as archivo:
                reader = csv.DictReader(archivo)
                print("\n---REPORTE DE PACIENTES---")
                print("-"*80)
                print("ID  |NOMBRE  |EDAD  |IMC  |PAM  |SPO2  |RGC  |TRIAGE  ")
                print("-"*80)

                for fila in reader:
                    #saco los datos del diccionario
                    nombre = fila.get("NOMBRE", "")
                    edad = fila.get("EDAD", "")
                    peso = fila.get("PESO", "")
                    altura = fila.get("ALTURA", "")
                    sist = fila.get("SISTOLICA", "")
                    diast = fila.get("DIASTOLICA", "")
                    temp = fila.get("TEMPERATURA", "")
                    oxi = fila.get("N_OXIGENO", "")
                    gluc = fila.get("GLUCOSA", "")
                    col = fila.get("COLESTEROL", "")
                    fcard = fila.get("F_CARD", "")
                    pr = fila.get("PULSOXIMETRO_R", "")
                    pir = fila.get("PULSOXIMETRO_IR", "")
                    try:
                        peso = float(peso)
                        altura = float(altura)
                        sist = float(sist)
                        diast = float(diast)
                        pr = float(pr)
                        pir = float(pir)
                        gluc = float(gluc)
                        col = float(col)
                        oxi = float(oxi)
                        temp = float(temp)
                    except:
                        continue
                    imc = calcular_imc(peso, altura)
                    pam = calcular_pres_am(diast, sist)
                    spo2 = calcular_porcentaje_R_IR(pr, pir)
                    rgc = calcular_relacion_gc(gluc, col)
                    #diccionario con valores para el triage
                    p = {"F_CARD" : fcard, "PAM" : pam, "TEMPERATURA" : temp, "N_OXIGENO" : oxi, 
                        "IMC" : imc, "GLUCOSA" : gluc, "COLESTEROL" : col}
                    color = triage_paciente(p)

                    print("Nombre:", nombre)
                    print("Edad:", edad)
                    print("IMC:", imc)
                    print("PAM:", pam)
                    print("Saturación O2:", spo2)
                    print("Relación Glucosa/Colesterol:", rgc)
                    print("Color del triage:", color)
                    print("-" * 80)
        except Exception as e:
            print(f"Error al generar el reporte: {e}")
            return None

#FUNCIONES EXTRAS
def pacientes_criticos(salida_p):
    try:
        with open(salida_p, mode="r", encoding="utf-8-sig") as archivo:
            reader = csv.DictReader(archivo) #crea un objeto que toma la primera fila del archivo CSV como los nombres de las columnas
            criticos = []

            for fila in reader:
                color = triage_paciente(fila)
                if color == "Rojo":
                    criticos.append(fila)

            if not criticos:
                print("No hay pacientes en estado crítico (Rojo).")
                return
            else:
                print("\n---PACIENTES EN ESTADO CRÍTICO---")
                for p in criticos:
                    print(f"\nID: {p['ID']}")
                    print(f"Nombre: {p['NOMBRE']}")
                    print(f"Edad: {p['EDAD']} años")
                    print(f"Temperatura: {p['TEMPERATURA']} °C")
                    print(f"Frecuencia Cardíaca: {p['F_CARD']} bpm")
                    print(f"Presión Arterial Media: {p['PAM']}")
                    print(f"Saturación O₂: {p['N_OXIGENO']} %")
                    print(f"Glucosa: {p['GLUCOSA']} mg/dL")
                    print(f"Colesterol: {p['COLESTEROL']} mg/dL")
                    print(f"IMC: {p['IMC']}")
                    print("-" * 50) #línea separadora entre cada paciente para más orden
                

    except Exception as e:
        print(f"Error al mostrar pacientes críticos: {e}")
    
    return

def calcular_imc_general(salida_p):
    try:
        with open(salida_p, "r", encoding="utf-8-sig") as archivo:
            reader = csv.DictReader(archivo)
            imcs = [] #lista para imcs validos

            for fila in reader: #recorro cada fila del csv
                try:
                    imc = float(fila.get("IMC", 0)) #imc individual
                    if imc > 0:  #valores válidos
                        imcs.append(imc) #agrego a la lista
                except:
                    continue 

            if not imcs:
                print("No hay datos válidos para calcular el IMC general.")
                return None

            imc_promedio = sum(imcs) / len(imcs)
            print(f"IMC promedio general: {imc_promedio:.2f}")
            return imc_promedio

    except Exception as e:
        print(f"Error al calcular IMC general: {e}")
        return None
    
def promedio_edad(salida_p):
    try:
        with open(salida_p, mode="r", encoding="utf-8-sig") as archivo:
            reader = csv.DictReader(archivo) #DictReader transforma cada fila en un diccionario
            suma_edades = 0 #acumulador
            cont = 0

            for fila in reader: 
               edad_original = fila.get("EDAD", "").strip()
               if edad_original == "": 
                   continue
               
               try: 
                   edad_numeric = float(edad_original)
               except Exception:
                    continue  
               
               if edad_numeric <=0: #verifico que la edad sea razonable
                   continue
               suma_edades += edad_numeric
               cont += 1
            if cont == 0:
                print("No se encontraron edades válidas en el archivo.")
                return None
            promedio =float(suma_edades/cont)
            print(f"Promedio de edad general: {promedio:.2f} años (sobre {cont} pacientes).")
    except Exception as e:
        print(f"Error al calcular el promedio de edad: {e}")
        return None
    
def extremos_f_card():
    try:
        with open(salida_p, mode="r", encoding="utf-8-sig") as archivo:
                reader = csv.DictReader(archivo)
                pacientes = [] #para guardar diccionarios de pacientes validos
                valores = [] #para guardar solo las frecuencias

                for fila in reader:
                    f_card_original = fila.get("F_CARD", "").strip() #valor que esta en la columna (F_CARD) de cada fila
                    if f_card_original == "":
                        continue #si esta vacia la salteo
                    try:
                        f_card = float(f_card_original)
                    except Exception:
                        continue
                    #guardo el paciente y su frecuencia
                    pacientes.append({ "ID" : fila.get("ID" , ""),
                                    "NOMBRE" : fila.get("NOMBRE", ""),
                                    "EDAD" : fila.get("EDAD", ""),
                                    "F_CARD" : f_card
                                    })
                    valores.append(f_card) #guardo el numero

                if not pacientes:
                    print("No hay pacientes con frecuencia cardíaca válida.")
                    return None
                
                #obtengo las frecuencias maximas y minimas
                max_f = max(valores)
                min_f = min(valores)

                #filtro todos los pacientes que tienen la frecuencia mínima y máxima
                pacientes_min = []
                for p in pacientes:
                    if p["F_CARD"] == min_f:
                        pacientes_min.append(p)
                pacientes_max = []
                for p in pacientes:
                    if p["F_CARD"] == max_f:
                        pacientes_max.append(p)

                pacientes_min = []
                for p in pacientes:
                    if p["F_CARD"] == min_f: 
                        pacientes_min.append(p) #egrega el diccionario p al final de la lista

                print(f"Frecuencia cardíaca MÍNIMA: {min_f} bmp (pacientes: {len(pacientes_min)})") 
                for p in pacientes_min:
                    print(f"ID: {p['ID']} | Nombre: {p['NOMBRE']} | Edad: {p['EDAD']} | F_CARD: {p['F_CARD']}")
                print("-"*60)
                print(f"Frecuencia cardíaca MÁXIMA: {max_f} bmp (pacientes: {len(pacientes_max)})") 
                for p in pacientes_max:
                    print(f"ID: {p['ID']} | Nombre: {p['NOMBRE']} | Edad: {p['EDAD']} | F_CARD: {p['F_CARD']}")

    except Exception as e:
        print(f"Error al obtener extremos de F_CARD: {e}")
        return None
#--MENU--
def menu():
    while True:
        print("\n--- Menú---")
        print("1. Buscar paciente")
        print("2. Dar de baja/alta")
        print("3. Gráficos")
        print("4. Pacientes en estado crítico") #mostrar a los de rojo (críticos)
        print("5. Promedio general de IMC") 
        print("6. Promedio de edad de los pacientes")
        print("7. ")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case 1:
                print("a.Buscar por apellido")
                print("b.Buscar por ID")
                minimenu1()
            case 2:
                print("a.Dar de baja ID")
                print("b.Dar de alta")
                minimenu2()
            case 3:
                print("a.Gráfico clasificacion de triage")
                print("b.Gráfico de ECG")
                print("c.Gráfico de IMC vs. PAM")
                minimenu3()
            case 4:
                pacientes_criticos()
            case 5:
                promedio_imc_general ()
            case 6:
                print("hola")
            case 7:
                print("hola")
            case 8:
                print("Saliendo del programa.")
                break # Sale del bucle while
            case _:
                print("Opción no válida.")
def minimenu1 ():
    sub_op=input("Seleccione una subopcion: ")
    if sub_op == "a":
        apellido=input("Ingrese el apellido del paciente que busca")
        buscar_paciente_por_apellido(apellido)    
    elif sub_op == "b":
        id=input("Ingrese el ID del paciente que busca")
        buscar_paciente(id)
    else:
        print("Sub-opción inválida.")
def minimenu2 ():
    sub_op=input("Seleccione una subopcion: ")
    if sub_op == "a":
        id=input("Ingrese el ID del paciente que desea eliminar")
        eliminar_paciente(id, salida_p)
    elif sub_op == "b":
        dar_alta_paciente(salida_p)
    else:
        print("Sub-opción inválida.")
def minimenu3 ():
    sub_op=input("Seleccione una subopcion: ")
    if sub_op == "a":
        print("hola")
        #fun
    elif sub_op == "b":
        gr.graficar_lineas_senyales(salida_p, entrada_s)
    elif sub_op== "c":
        grafico_dispersion()
    else:
        print("Sub-opción inválida.")
        grafico_dispersion()
    else:
        print("Sub-opción inválida.")

