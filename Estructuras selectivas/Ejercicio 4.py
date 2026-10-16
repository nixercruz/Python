'''
 En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un color  que se escoge al azar. Si el color de la balota es rojo  el descuento es del 15% sobre el total de la compra, la balota es verde el descuento es del 20%. Si  el color es diferente a los indicados no obtendrá descuento.  Imprimir el valor de la compra, el color de la balota, el descuento y el valor a pagar. 
'''

color = input(" Por favor ingrese un color ")
valor_compra = int(input("Por favor digite el valor total de su compra "))
descuento = 0

if color == "rojo":
    descuento = valor_compra * 0.15
elif color == "verde":
    descuento = valor_compra * 0.20
else:
    print ("No otiene descuento")

valor_final = valor_compra - descuento

print("El valor de la compra es: $", valor_compra)
print("El color de la balota es: ", color)
print("El valor del descuento es: $", descuento)
print("El valor final con el descuento aplicaddo es: $", valor_final)