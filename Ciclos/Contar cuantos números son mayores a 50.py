print ("Por favor ingrese la cantidad de datos que quiere digitar para contar mayores a 50")
cantidad_numeros = input()

mayores_50 = 0

for i in range (1, int(cantidad_numeros) + 1):
    print("Por favor ingrese el número ", i)
    numero = int(input())

    if numero > 50:
        mayores_50 = mayores_50 + 1

print("La cantidad de números mayores a 50 es: ", mayores_50)