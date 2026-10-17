'''
un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un algoritmo que lea por cada estudiante la calificación obtenida.
'''

Estudiantes = 23

menor_a_50 = 0
entre_50_y_70 = 0
entre_70_y_80 = 0
mayor_a_80 = 0

for i in range (Estudiantes):
    calificacion = float(input("Por favor digita la calificación del estudiante en una escala de 1 - 100: "))
    if calificacion < 50 :
        menor_a_50 += 1
    elif calificacion >= 50 and calificacion < 70:
        entre_50_y_70 += 1
    elif calificacion >= 70 and calificacion < 80:
        entre_70_y_80 += 1
    else:
        mayor_a_80 += 1

print ("La cantidad de estudiantes con nota menor a 50 es: ", menor_a_50)
print ("La cantidad de estudiantes con una nota entre 50 y 70 es: ", entre_50_y_70)
print ("La cantidaad de estudiantes con nota entre 70 y 80 es: ", entre_70_y_80)
print ("La cantidad de estudiantes con una nota mayor a 80 es: ", mayor_a_80)