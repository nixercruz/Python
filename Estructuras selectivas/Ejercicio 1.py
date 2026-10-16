''''
Determinar si un aprendiz aprueba o desaprueba Algoritmia, sabiendo que aprobará si su promedio de tres calificaciones es mayor o igual a 70; reprueba en caso contrario
'''
aprendiz = input("Ingrese el nombre del aprendiz: ")
calificacion1 = float(input("Ingrese la primera calificación: "))
calificacion2 = float(input("Ingrese la segunda calificación: "))
calificacion3 = float(input("Ingrese la tercera calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

if promedio >= 70:
    print(aprendiz, "aprueba Algoritmia.")
else:
    print(aprendiz, "desaprueba Algoritmia.")
    