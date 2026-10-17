'''
Leer 20 números e imprimir cuantos son  positivos, cuantos negativos y cuantos neutros. 
'''

positivos = 0
negativos = 0
neutros = 0

for i in range (5):
    numero = float(input("Por favor digite el número para determinar si es positivo, negativo o neutro: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1

print ("La cantidad de números positivos es: ", positivos)
print ("La cantidad de números negativos es: ", negativos)
print ("La cantidad de números neutros es: ", neutros)