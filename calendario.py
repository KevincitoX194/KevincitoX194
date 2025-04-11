import numpy as np

# Función para crear la matriz de actividades
def crear_matriz(días: np.ndarray, rango_horario: np.ndarray) -> np.ndarray:
    # Crear una matriz vacía con los días como filas y las horas como columnas
    matriz = np.full((len(días), len(rango_horario)), None, dtype=object)
    return matriz

# Función para obtener las actividades de un día
def obtener_actividades(día: str, matriz: np.ndarray, días: np.ndarray, rango_horario: np.ndarray):
    # Obtener el índice del día en el arreglo de días
    if día in días:
        indice_día = np.where(días == día)[0][0]  # Encuentra el índice del día
        actividades = matriz[indice_día, :]
        
        # Mostrar actividades para ese día
        print(f"\nActividades para {día}:")
        for hora, actividad in zip(rango_horario, actividades):
            print(f"A las {hora}:00, actividad: {actividad if actividad else 'No hay actividad'}")
    else:
        print("Día no válido.")

# Función para ingresar actividades
def ingresar_actividades(matriz: np.ndarray, días: np.ndarray, rango_horario: np.ndarray):
    for i, día in enumerate(días):
        for j, hora in enumerate(rango_horario):
            actividad = input(f"Ingrese actividad para {día} a las {hora}:00: ")
            matriz[i, j] = actividad if actividad.strip() else None

# Función para mostrar el menú y gestionar la interacción
def menu(días: np.ndarray, matriz: np.ndarray, rango_horario: np.ndarray):
    while True:
        print("\nMenú de opciones:")
        print("1) Imprimir las actividades de un día")
        print("2) Imprimir la actividad de un día y hora")
        print("3) Salir del programa")

        opción = input("Seleccione una opción (1-3): ")

        if opción == '1':
            día = input("Ingrese el día (Lunes, Martes, Miércoles, Jueves, Viernes): ").capitalize()
            obtener_actividades(día, matriz, días, rango_horario)
        
        elif opción == '2':
            día = input("Ingrese el día (Lunes, Martes, Miércoles, Jueves, Viernes): ").capitalize()
            try:
                hora = int(input("Ingrese la hora (de 7 a 23): "))
                if día in días and 7 <= hora <= 23:
                    # Obtener índice del día
                    indice_día = np.where(días == día)[0][0]
                    # Obtener la actividad correspondiente a esa hora
                    actividad = matriz[indice_día, hora - 7]
                    print(f"\nActividad para {día} a las {hora}:00: {actividad if actividad else 'No hay actividad'}")
                else:
                    print("Día o hora no válidos.")
            except ValueError:
                print("Por favor, ingrese una hora válida.")
        
        elif opción == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

# Configuración de las constantes
HORA_INICIO = 7
HORA_FINALIZACION = 23
DIAS_ACTIVIDAD = np.array(["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])
RANGO_HORARIO = np.arange(HORA_INICIO, HORA_FINALIZACION + 1)

# Crear la matriz vacía de actividades
calendario_vacío = crear_matriz(DIAS_ACTIVIDAD, RANGO_HORARIO)

# Ingresar las actividades
ingresar_actividades(calendario_vacío, DIAS_ACTIVIDAD, RANGO_HORARIO)

# Mostrar el menú
menu(DIAS_ACTIVIDAD, calendario_vacío, RANGO_HORARIO)

