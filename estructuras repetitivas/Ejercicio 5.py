'''
 Una persona debe realizar un muestreo con 50 personas para determinar el promedio de peso de los niños, jóvenes, adultos y ancianos  que existen en su zona. 
'''

pesos = []
for i in range(50):
    peso = float(input("Por favor digite el peso de la persona " + str(i + 1) + ": "))
    pesos.append(peso)

promedio = sum(pesos) / len(pesos)
print("El promedio de los pesos es:", promedio)