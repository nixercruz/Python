'''
En una llantera se ha establecido una promoción de las llantas marca “Todo Terreno”, dicha promoción consiste en lo siguiente: Si se compran menos de cinco llantas el precio es de $300.000 cada una, de $250.000 si se compran de cinco a 10 y de $200.000 si se compran más de 10. Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las llantas que compre
'''

cantidad = int(input(" Por favor digite la cantidad de llantas compradas "))
precio_unidad = 0
precio_total = 0

if cantidad < 5 :
    precio_unidad = 300000 
    precio_total = cantidad * precio_unidad
    print(" El valor unitario de las llantas es: $", precio_unidad)
    print(" El valor total es de: $", precio_total)
elif cantidad >= 5 and cantidad <= 10:
    precio_unidad = 250000
    precio_total = cantidad * precio_unidad
    print(" El valor unitario de las llantas es: $", precio_unidad)
    print(" El valor total es de: $", precio_total)
else:
    precio_unidad = 200000
    precio_total = cantidad * precio_unidad
    print(" El valor unitario de las llantas es: $", precio_unidad)
    print(" El valor total es de: $", precio_total)

