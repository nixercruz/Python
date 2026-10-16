'''
Calcular el total a pagar por la compra de zapatillas. Si se compran tres  o más zapatillas se aplica un descuento del 25% sobre el total de la compra y si son menos de tres zapatillas un descuento del 10%. Si el precio total de la compra supera el valor de $300.000 mostrar un mensaje a cliente preferencial. Mostrar en pantalla, el valor de la compra, el valor del descuento y el valor a pagar una vez aplicado el descuento. 
'''
cantidad = int(input( " Por favor digite la cantidad de pares de zapatillas comprados "))
precio_total = int(input( " Digite el valor total de su compra "))
precio_final = 0
descuento = 0

if cantidad >= 3:
    descuento = precio_total * 0.25
    precio_final = precio_total - descuento
    if precio_final > 300000:
        print ("Muchas gracias por comprar en nuestra tienda, por su gran compra ahora pertenece a nuestro selecto grupo de clientes preferenciales. ")

else:
    descuento = precio_total * 0.10
    precio_final = precio_total - descuento
    if precio_final > 300000:
            print ("Muchas gracias por comprar en nuestra tienda, por su gran compra ahora pertenece a nuestro selecto grupo de clientes preferenciales. ")


print (" El valor de la compra es: $", precio_total)
print (" El valor del descuento aplicado es: $", descuento)
print (" El valor de la compra con el descuento aplicado es: $", precio_final)

