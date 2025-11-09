import MENU as m
import FUNCIONES as eu
entrada_p = "pacientes_final.csv"
salida_p = "pacientes-2025.cvs"

def main():
    print("---SISTEMA DE PACIENTES---")
    eu.sumar_info_pacientes(entrada_p)
    while True:
        if m.volver_al_menu():
                m.menu()
