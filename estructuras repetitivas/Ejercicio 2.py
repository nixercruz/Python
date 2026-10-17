'''
Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números
'''

suma = 0

for i in range (10):
    positivo = 0
    numero = float(input(" Por favor digite un número en negativo para convertirlo en positivo "))
    if numero < 0:
        positivo = numero *-1
        print("El número", i + 1, "en positivo es: ", positivo)
        suma += positivo
    else:
        print ("El número ingresado no es negativo")

print ("El resultado de la suma de los números positivos es: ", suma)
