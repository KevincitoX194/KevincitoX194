tareas = []

def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def listar_tareas():
    print("Lista de tareas:")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")

while True:
    accion = input("¿Quieres agregar una tarea o listar tareas? (agregar/listar/salir): ")
    if accion == "agregar":
        tarea = input("Ingrese la tarea: ")
        agregar_tarea(tarea)
    elif accion == "listar":
        listar_tareas()
    elif accion == "salir":
        break
    else:
        print("Acción no válida.")