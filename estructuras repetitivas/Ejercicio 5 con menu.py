def pedir_pesos():
    pesos = []
    for i in range(50):
        peso = float(input("Por favor digite el peso de la persona " + str(i + 1) + ": "))
        pesos.append(peso)
    return pesos

def mostrar_promedio(pesos):
    promedio = sum(pesos) / len(pesos)
    print("\n--- RESULTADO ---")
    print("El promedio de los pesos es:", promedio)

pesos = []

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Registrar pesos")
    print("2. Ver promedio de los pesos")
    print("3. Salir")
    
    opcion = input("Elija una opción (1-3): ")
    
    if opcion == "1":
        pesos = pedir_pesos()
    elif opcion == "2":
        if len(pesos) == 0:
            print("Primero debe registrar los pesos en la opción 1.")
        else:
            mostrar_promedio(pesos)
    elif opcion == "3":
        print("¡Saliendo del programa!")
        break
    else:
        print("Opción no válida, intente de nuevo.")