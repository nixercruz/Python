'''
Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos.  
'''

cantidad_alumnos = int(input("Por favor digita la cantidad de alumnos dentro del aula de clase: "))

suma_general = 0
suma_hombres = 0
suma_mujeres = 0

cant_hombres = 0
cant_mujeres = 0


for i in range (cantidad_alumnos):
    sexo = input("Por favor digite 'M' si el alumno es masculino o 'F' si el alumno es mujer: ") .lower()
    if sexo == "m":
        edad = int(input("Por favor digite la edad del alumno: "))
        cant_hombres += 1
        suma_hombres += edad
        suma_general += edad
    elif sexo == "f":
        edad = int(input("Por favor digite la edad del alumno: "))
        cant_mujeres += 1
        suma_mujeres += edad
        suma_general += edad
    else:
        print ("Opción no valida")

promedio_general = suma_general / cantidad_alumnos 
promedio_hombres = suma_hombres / cant_hombres
promedio_mujeres = suma_mujeres / cant_mujeres

print ("La edad promedio de los alumnos es: ",promedio_general)
print ("La edad promedio de los alumnos hombres es: ", promedio_hombres)
print ("La edad promedio de las alumnas es: ", promedio_mujeres)