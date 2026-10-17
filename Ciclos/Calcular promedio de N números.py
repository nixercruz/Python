print ("Por favor ingrese una cantidad de números para calcular su promedio")
n_numeros = input ()

suma = 0

for i in range (1, int(n_numeros) + 1):
    print ("Por favor digite el número: ", i)
    numero = input ()

    suma = suma + (int(numero))

promedio = suma / (int(n_numeros))
print ("El promedio de los números ingresados es: ", promedio)
