def registrar_alumnos():
    cantidad_alumnos = int(input("Por favor digita la cantidad de alumnos dentro del aula de clase: "))

    suma_general = 0
    suma_hombres = 0
    suma_mujeres = 0

    cant_hombres = 0
    cant_mujeres = 0

    for i in range(cantidad_alumnos):
        sexo = input("Por favor digite 'M' si el alumno es masculino o 'F' si el alumno es mujer: ").lower()
        if sexo == "m":
            edad = int(input("Por favor digite la edad del alumno: "))
            cant_hombres += 1
            suma_hombres += edad
            suma_general += edad
        elif sexo == "f":
            edad = int(input("Por favor digite la edad del alumno: "))
            cant_mujeres += 1
            suma_mujeres += edad
            suma_general += edad
        else:
            print("Opción no valida")

    promedio_general = suma_general / cantidad_alumnos if cantidad_alumnos > 0 else 0
    promedio_hombres = suma_hombres / cant_hombres if cant_hombres > 0 else 0
    promedio_mujeres = suma_mujeres / cant_mujeres if cant_mujeres > 0 else 0
    
    return promedio_general, promedio_hombres, promedio_mujeres

def mostrar_resultados(promedio_general, promedio_hombres, promedio_mujeres):
    print("\n--- RESULTADOS ---")
    print("La edad promedio de los alumnos es: ", promedio_general)
    print("La edad promedio de los alumnos hombres es: ", promedio_hombres)
    print("La edad promedio de las alumnas es: ", promedio_mujeres)

promedio_general = 0
promedio_hombres = 0
promedio_mujeres = 0
registrado = False

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Registrar alumnos y edades")
    print("2. Ver promedios de edad")
    print("3. Salir")
    
    opcion = input("Elija una opción (1-3): ")
    
    if opcion == "1":
        promedio_general, promedio_hombres, promedio_mujeres = registrar_alumnos()
        registrado = True
        print("\n✅ ¡Registro completado!")
    elif opcion == "2":
        if not registrado:
            print("Primero debe registrar los datos en la opción 1.")
        else:
            mostrar_resultados(promedio_general, promedio_hombres, promedio_mujeres)
    elif opcion == "3":
        print("¡Saliendo del programa!")
        break
    else:
        print("Opción no válida, intente de nuevo.")