# 1. Solicitar y validar la cantidad total de personas (debe ser mayor a 0)
while True:
    try:
        cantidad_total = int(input("Ingrese la cantidad total de personas en el salon de clases: "))
        if cantidad_total > 0:
            break
        else:
            print("La cantidad debe ser mayor que 0. Intente nuevamente.\n")
    except ValueError:
        print("Debe ingresar un numero entero valido.\n")

hombres = 0
mujeres = 0

# 2. Bucle para ingresar el genero de cada persona
for i in range(cantidad_total):
    while True:
        # Pide el genero usando concatenacion tradicional (+ y str)
        mensaje = "Persona " + str(i + 1) + " de " + str(cantidad_total) + " - Ingrese genero ('M' masculino / 'F' femenino): "
        genero = input(mensaje).strip().lower()
        
        if genero == "m":
            hombres += 1
            break
        elif genero == "f":
            mujeres += 1
            break
        else:
            print("Entrada no valida. Por favor digite 'M' o 'F'.")

# 3. Calculo de porcentajes
porcentaje_hombres = (hombres / cantidad_total) * 100
porcentaje_mujeres = (mujeres / cantidad_total) * 100

# 4. Mostrar reporte de resultados utilizando concatenacion tradicional
print("\n" + "="*35)
print("       RESUMEN DEL SALON")
print("="*35)
print("Total de estudiantes : " + str(cantidad_total))
print("Hombres             : " + str(hombres) + " (" + str(round(porcentaje_hombres, 1)) + "%)")
print("Mujeres             : " + str(mujeres) + " (" + str(round(porcentaje_mujeres, 1)) + "%)")
print("="*35)