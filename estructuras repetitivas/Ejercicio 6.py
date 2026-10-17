'''
 Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un total de n personas.
'''

cantidad_total = int(input("Ingrese la cantidad total de personas en el salón de clases: "))

hombres = 0
mujeres = 0

for i in range(cantidad_total):
    genero = input("Por favor digite el género de la persona " + str(i + 1) + " 'M' para masculino o 'F' para femenino: ")
    if genero == "m":
        hombres += 1
    elif genero == "f":
        mujeres += 1

print("La cantidad de hombres es:", hombres)
print("La cantidad de mujeres es:", mujeres)