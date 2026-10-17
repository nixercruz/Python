'''
Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio ,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos que tiene una altura  menor o igual a 1.50 cm. El programa debe finalizar cuando la edad sea igual a 0. 
'''

hombres = 0
mujeres = 0
suma = 0
total = 0
c1 = 0
c2 = 0

while True:
    edad = int(input("Por favor digite la edad del alumno (0 para salir): "))
    if edad == 0:
        break
    sexo = input("Sexo (H/M): ").lower()
    altura = float(input("Por favr ingrese la altura del alumno: "))
    
    total += 1
    suma += altura
    
    if sexo == "h":
        hombres += 1
    elif sexo == "m":
        mujeres += 1
        
    if altura > 1.70:
        c1 += 1
    elif altura <= 1.50:
        c2 += 1

print("La cantidad de hombres es:", hombres)
print("La cantidad de mujeres es:", mujeres)
print("La altura promedio es:", suma / total if total > 0 else 0)
print("Alumnos con altura mayor a 1.70:", c1)
print("Alumnos con altura menor o igual a 1.50:", c2)