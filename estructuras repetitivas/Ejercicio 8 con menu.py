def registrar_calificaciones():
    Estudiantes = 23
    menor_a_50 = 0
    entre_50_y_70 = 0
    entre_70_y_80 = 0
    mayor_a_80 = 0

    for i in range(Estudiantes):
        calificacion = float(input("Por favor digita la calificación del estudiante en una escala de 1 - 100: "))
        if calificacion < 50:
            menor_a_50 += 1
        elif calificacion >= 50 and calificacion < 70:
            entre_50_y_70 += 1
        elif calificacion >= 70 and calificacion < 80:
            entre_70_y_80 += 1
        else:
            mayor_a_80 += 1
            
    return menor_a_50, entre_50_y_70, entre_70_y_80, mayor_a_80

def mostrar_resultados(menor_a_50, entre_50_y_70, entre_70_y_80, mayor_a_80):
    print("\n--- RESULTADOS ---")
    print("La cantidad de estudiantes con nota menor a 50 es:", menor_a_50)
    print("La cantidad de estudiantes con una nota entre 50 y 70 es:", entre_50_y_70)
    print("La cantidad de estudiantes con nota entre 70 y 80 es:", entre_70_y_80)
    print("La cantidad de estudiantes con una nota mayor a 80 es:", mayor_a_80)

menor_a_50 = 0
entre_50_y_70 = 0
entre_70_y_80 = 0
mayor_a_80 = 0
registrado = False

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Registrar calificaciones de los estudiantes")
    print("2. Ver resultados de las notas")
    print("3. Salir")
    
    opcion = input("Elija una opción (1-3): ")
    
    if opcion == "1":
        menor_a_50, entre_50_y_70, entre_70_y_80, mayor_a_80 = registrar_calificaciones()
        registrado = True
        print("\n✅ ¡Registro completado!")
    elif opcion == "2":
        if not registrado:
            print("Primero debe registrar las calificaciones en la opción 1.")
        else:
            mostrar_resultados(menor_a_50, entre_50_y_70, entre_70_y_80, mayor_a_80)
    elif opcion == "3":
        print("¡Saliendo del programa!")
        break
    else:
        print("Opción no válida, intente de nuevo.")