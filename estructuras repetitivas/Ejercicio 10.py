'''
Escribir un programa que multiplique los 20 primeros números naturales.
'''

resultado = 1

for i in range (1, 21):
    resultado_anterior = resultado
    resultado *= i
    print (resultado_anterior, "X", i, "=", resultado)

print("El resultado de los primeros 20 números naturales es:", resultado)