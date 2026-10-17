contador = 0 
suma = 0

numeros = []
for i in range(1, 6):
    print ("Ingrese un número", i)
    numero = int(input())
    numeros.append(numero)

    suma = suma + (int(numero))
    contador = contador + 1

print("Los números ingresados son:")
for n in numeros:
    print(n)

promedio = suma / contador

print ("El promedio de los datos registrados es: ", promedio)
