'''
 Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos. Realizar un algoritmo para calcular el promedio  y la calificación más alta y  más baja de todo el grupo.  
'''

calificaciones = []

for i in range(20):
    calificacion = float(input("Por favor digite la calificación del alumno " + str(i + 1) + ": "))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / len(calificaciones)
calificacion_mas_alta = max(calificaciones)
calificacion_mas_baja = min(calificaciones)

print("El promedio de las calificaciones es:", promedio)
print("La calificación más alta es:", calificacion_mas_alta)
print("La calificación más baja es:", calificacion_mas_baja)
