def registrar_datos():
    hombres = 0
    mujeres = 0
    suma = 0
    total = 0
    c1 = 0
    c2 = 0

    while True:
        edad = int(input("Por favor digite la edad del alumno (0 para salir): "))
        if edad == 0:
            break
        sexo = input("Sexo (H/M): ").lower()
        altura = float(input("Por favor ingrese la altura del alumno: "))
        
        total += 1
        suma += altura
        
        if sexo == "h":
            hombres += 1
        elif sexo == "m":
            mujeres += 1
            
        if altura > 1.70:
            c1 += 1
        elif altura <= 1.50:
            c2 += 1
            
    return hombres, mujeres, suma, total, c1, c2

def mostrar_resultados(hombres, mujeres, suma, total, c1, c2):
    print("\n--- RESULTADOS ---")
    print("La cantidad de hombres es:", hombres)
    print("La cantidad de mujeres es:", mujeres)
    print("La altura promedio es:", suma / total if total > 0 else 0)
    print("Alumnos con altura mayor a 1.70:", c1)
    print("Alumnos con altura menor o igual a 1.50:", c2)

hombres = 0
mujeres = 0
suma = 0
total = 0
c1 = 0
c2 = 0
registrado = False

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Registrar datos de los alumnos")
    print("2. Ver resultados")
    print("3. Salir")
    
    opcion = input("Elija una opción (1-3): ")
    
    if opcion == "1":
        hombres, mujeres, suma, total, c1, c2 = registrar_datos()
        registrado = True
        print("\n✅ ¡Registro completado!")
    elif opcion == "2":
        if not registrado:
            print("Primero debe registrar los datos en la opción 1.")
        else:
            mostrar_resultados(hombres, mujeres, suma, total, c1, c2)
    elif opcion == "3":
        print("¡Saliendo del programa!")
        break
    else:
        print("Opción no válida, intente de nuevo.")