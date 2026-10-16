'''
Calcular el total a pagar por la compra de zapatillas. Si se compran tres  o más zapatillas se aplica un descuento del 20% sobre el total de la compra y si son menos de tres zapatillas un descuento del 10%. Mostrar en pantalla, el valor de la compra, el valor del descuento y el valor a pagar una vez aplicado el descuento. 
'''
cantidad = int(input( " Por favor digite la cantidad de pares de zapatillas comprados "))
preccio_total = int(input( " Digite el valor total de su compra "))
precio_final = 0
descuento = 0

if cantidad >= 3:
    descuento = preccio_total * 0.20
    precio_final = preccio_total - descuento
else:
    descuento = preccio_total * 0.10
    precio_final = preccio_total - descuento

print (" El valor de la compra es: $", preccio_total)
print (" El valor del descuento aplicado es: $", descuento)
print (" El valor de la compra con el descuento aplicado es: $", precio_final)

