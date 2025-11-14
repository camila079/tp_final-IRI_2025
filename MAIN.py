import menu as m
import FUNCIONES as eu
import time

entrada_p="pacientes_final.csv"
eu.sumar_info_pacientes(entrada_p)

while True:
    #eu.sumar_info_pacientes(entrada_p)
    print("---SISTEMA DE PACIENTES---")
    time.sleep(0.5)
    print("Iniciando programa...")
    time.sleep(0.5)
    if m.volver_al_menu():
        m.menu()
    else: break
