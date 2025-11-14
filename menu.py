import FUNCIONES as eu
import GRAFICOS as gr

entrada_p = "pacientes_final.csv"
salida_p = "pacientes_2025.csv"

entrada_s= "ecg_id_pacient.csv"

#--MENU--

def minimenu1():
    print("\na. Buscar por apellido")
    print("b. Buscar por ID")
    sub_op = input("Seleccione una subopción: ")

    if sub_op == "a":
        apellido = input("Ingrese el apellido: ")
        eu.buscar_paciente_por_apellido(apellido)    
    elif sub_op == "b":
        id_p = input("Ingrese el ID del paciente: ")
        eu.buscar_paciente(id_p)
    else:
        print("Sub-opción inválida.")

def minimenu2(FILE):
    salida_p = FILE
    print("\na. Dar de baja por ID")
    print("b. Dar de alta")
    sub_op = input("Seleccione una subopción: ")

    if sub_op == "a":
        id_p = input("Ingrese el ID del paciente a eliminar: ")
        eu.eliminar_paciente(id_p,FILE)
    elif sub_op == "b":
        eu.dar_alta_paciente(salida_p)
    else:
        print("Sub-opción inválida.")

def minimenu3(FILE):
    salida_p = FILE
    print("\na. Gráfico clasificación de triage")
    print("b. Gráfico de ECG")
    print("c. Gráfico de IMC vs PAM")
    sub_op = input("Seleccione una subopción: ")

    if sub_op == "a":
        gr.graficas_barras_estado(salida_p)
        pass
    elif sub_op == "b":
        gr.graficar_lineas_senyales(salida_p, entrada_s)
        pass
    elif sub_op == "c":
        gr.grafico_dispersion(salida_p)
        pass
    else:
        print("Sub-opción inválida.")

def menu():
    salida_p = "pacientes_2025.csv"
    print("\n--- Menú---")
    print("1. Buscar paciente.")
    print("2. Dar de baja/alta.")
    print("3. Gráficos.")
    print("4. Pacientes en estado crítico.")
    print("5. Promedio general de IMC.") 
    print("6. Promedio de edad de los pacientes.")
    print("7. Análisis de frecuencia cardíaca.")
    print("8. Reporte de todos los pacientes.")
    print("9. Salir.")
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            minimenu1()
        case "2":
            salida_p = "pacientes_2025.csv"
            minimenu2(salida_p)
        case "3":
            salida_p = "pacientes_2025.csv"
            minimenu3(salida_p)
        case "4":
            salida_p = "pacientes_2025.csv"
            eu.pacientes_criticos(salida_p)
        case "5":
            salida_p = "pacientes_2025.csv"
            eu.calcular_imc_general(salida_p)
        case "6":
            salida_p = "pacientes_2025.csv"
            eu.promedio_edad(salida_p)
        case "7":
            salida_p = "pacientes_2025.csv"
            eu.extremos_f_card(salida_p)
        case "8":
            salida_p = "pacientes_2025.csv"
            eu.reporte_general(salida_p)
        case "9":
            print("Saliendo del programa.")
        case _:
            print("Opción no válida.")
def volver_al_menu():
    respuesta = input("Ingresar al menu? si/no ").strip().lower()
    return respuesta in ["si", "sí", "s"]
