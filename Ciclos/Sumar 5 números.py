print ("A continuación debe digitar 5 números para sumar")

suma = 0

for i in range (1, 5 + 1):
    print ("Por favor digite el número: ", i)
    numero = input ()
    suma = suma + (int(numero))

print ("El resultado de la suma de los 5 números ingresados es:")
print (suma)
