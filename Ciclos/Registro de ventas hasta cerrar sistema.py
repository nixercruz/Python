total = 0
ventas = 0

while True:
    entrada = input("Ingrese el valor de la venta o 'cerrar' para salir: ")

    if entrada.lower() == "cerrar":
        break

    try:
        precio = float(entrada)
        if precio > 0:
            total = total + precio
            ventas = ventas + 1
            print("Venta registrada: $", precio)
        else:
            print("El precio de la venta debe ser mayor a 0")
    except ValueError:
        print ("Entrada no válida. Ingrese un número o escriba ´cerrar´.")

print("EL total de ventas realizadas es: ", ventas)
print("El precio total acumulado es: ", total)
