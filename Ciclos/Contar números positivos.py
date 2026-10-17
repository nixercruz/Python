print ("Por favor ingrese la cantidad de datos que quiere digitar para contar positivos")
cantidad_numeros = input()

positivos = 0

for i in range (1, int(cantidad_numeros) + 1):
    print("Por favor ingrese el número ", i)
    numero = int(input())
    if numero > 0:
        positivos = positivos + 1

print ("La cantidad de números positivos es: ", positivos)
