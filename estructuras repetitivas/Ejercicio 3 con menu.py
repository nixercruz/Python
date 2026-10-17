def pedir_calificaciones():
    calificaciones = []
    for i in range(20):
        calificacion = float(input("Por favor digite la calificación del alumno " + str(i + 1) + ": "))
        calificaciones.append(calificacion)
    return calificaciones

def mostrar_resultados(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    calificacion_mas_alta = max(calificaciones)
    calificacion_mas_baja = min(calificaciones)

    print("\n--- RESULTADOS ---")
    print("El promedio de las calificaciones es:", promedio)
    print("La calificación más alta es:", calificacion_mas_alta)
    print("La calificación más baja es:", calificacion_mas_baja)

calificaciones = []

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Registrar calificaciones")
    print("2. Ver resultados (Promedio, Alta, Baja)")
    print("3. Salir")
    
    opcion = input("Elija una opción (1-3): ")
    
    if opcion == "1":
        calificaciones = pedir_calificaciones()
    elif opcion == "2":
        if len(calificaciones) == 0:
            print("Primero debe ingresar las calificaciones en la opción 1.")
        else:
            mostrar_resultados(calificaciones)
    elif opcion == "3":
        print("¡Saliendo del programa!")
        break
    else:
        print("Opción no válida, intente de nuevo.")