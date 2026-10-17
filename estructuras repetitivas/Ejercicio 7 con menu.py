def registrar_autos():
    rojo = 0
    verde = 0
    azul = 0 
    rosa = 0
    amarillo = 0

    cantidad = int(input("Ingrese la cantidad de autos que entran a la ciudad de Ibagué: "))

    for i in range(cantidad):
        ultimo_digito = int(input("Por favor digite el último dígito de la placa " + str(i + 1) + " (0 - 9): "))

        if ultimo_digito == 1 or ultimo_digito == 2:
            amarillo += 1
        elif ultimo_digito == 3 or ultimo_digito == 4:
            rosa += 1
        elif ultimo_digito == 5 or ultimo_digito == 6:
            rojo += 1
        elif ultimo_digito == 7 or ultimo_digito == 8:
            verde += 1
        elif ultimo_digito == 9 or ultimo_digito == 0:
            azul += 1
            
    return cantidad, amarillo, rosa, rojo, verde, azul

def mostrar_resultados(cantidad, amarillo, rosa, rojo, verde, azul):
    print("\n--- RESULTADOS ---")
    print("La cantidad total de autos registrados es: ", cantidad)
    print("El total de autos con la calcomanía amarilla es: ", amarillo)
    print("El total de autos con calcomanía rosa es: ", rosa)
    print("El total de autos con calcomanía roja es: ", rojo)
    print("El total de autos con calcomanía verde es: ", verde)
    print("El total de autos con calcomanía azul es: ", azul)

cantidad = 0
amarillo = rosa = rojo = verde = azul = 0
registrado = False

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Registrar autos y calcomanías")
    print("2. Ver resultados")
    print("3. Salir")
    
    opcion = input("Elija una opción (1-3): ")
    
    if opcion == "1":
        cantidad, amarillo, rosa, rojo, verde, azul = registrar_autos()
        registrado = True
        print("\n✅ ¡Registro completado!")
    elif opcion == "2":
        if not registrado:
            print("Primero debe registrar los datos en la opción 1.")
        else:
            mostrar_resultados(cantidad, amarillo, rosa, rojo, verde, azul)
    elif opcion == "3":
        print("¡Saliendo del programa!")
        break
    else:
        print("Opción no válida, intente de nuevo.")