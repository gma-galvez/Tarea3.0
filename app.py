tareas = []

def agregar_tarea(tarea):
    tareas.append(tarea)
    return tareas

if __name__ == "__main__":
    agregar_tarea("Hacer deberes")
    print("Lista de tareas:")
    
    for tarea in tareas:
        print("-", tarea)