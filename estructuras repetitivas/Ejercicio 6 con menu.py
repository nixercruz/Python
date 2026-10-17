def registrar_personas():
    cantidad_total = int(input("Ingrese la cantidad total de personas en el salón de clases: "))

    hombres = 0
    mujeres = 0

    for i in range(cantidad_total):
        genero = input("Por favor digite el género de la persona " + str(i + 1) + " 'm' para masculino o 'f' para femenino: ")
        if genero == "m":
            hombres += 1
        elif genero == "f":
            mujeres += 1
            
    return cantidad_total, hombres, mujeres

def mostrar_resultados(hombres, mujeres):
    print("\n--- RESULTADOS ---")
    print("La cantidad de hombres es:", hombres)
    print("La cantidad de mujeres es:", mujeres)

cantidad_total = 0
hombres = 0
mujeres = 0
registrado = False

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Registrar personas y géneros")
    print("2. Ver resultados")
    print("3. Salir")
    
    opcion = input("Elija una opción (1-3): ")
    
    if opcion == "1":
        cantidad_total, hombres, mujeres = registrar_personas()
        registrado = True
        print("\n ¡Registro completado!")
    elif opcion == "2":
        if not registrado:
            print("Primero debe registrar los datos en la opción 1.")
        else:
            mostrar_resultados(hombres, mujeres)
    elif opcion == "3":
        print("¡Saliendo del programa!")
        break
    else:
        print("Opción no válida, intente de nuevo.")