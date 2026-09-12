print ("Por favor ingrese el valor total de la compra: ")
valor_total = int(input())
if valor_total > 100000:
    descuento = valor_total * 0.10
    valor_final = valor_total - descuento
    print ("Se aplicó un descuento del 10%")
    print ("El valor final a pagar es: ", valor_final)
else:
    print ("No se aplicó ningún descuento")
