'''
 Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: si el promedio obtenido por un alumno en el último periodo es mayor o igual que 4.0, se le hará un descuento del 30% sobre la pensión; si el promedio obtenido es menor que 4.0 deberá pagar la pensión completa, la cual incluye el 10% de IVA. Obtener cuanto debe pagar un alumno. 
'''

promedio = float(input("Por favor digite su promedio correspondiente al último periodo " ))
pension = int (input("Por favor ingrese el valor de la pensión " ))
iva = 0
pension_iva = 0
pension_descuento = 0
descuento = 0

if promedio >= 4:
    descuento = pension * 0.30
    pension_descuento = pension - descuento
    print("Por tu desempeño académico tienes un descuento del 30%, por lo cual el valor de tu pensión queda en: $",pension_descuento)
else:
    iva = pension * 0.10
    pension_iva = pension + iva 
    print("El valor de tu pensión incluyendo el iva es: $", pension_iva)
