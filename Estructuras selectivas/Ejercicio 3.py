'''
Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de bolsos. La empresa, dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante:  Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito al fabricante.  Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante. El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito. Imprimir el valor invertido de su propio dinero, el valor prestado al banco, y el valor del crédito solicitado al fabricante, según sea el caso
'''
monto_total = int(input(" Por favor digite el valor total de la compra "))
dinero_propio = 0
prestamo_banco = 0
credito_fabricante = 0
interes = 0

if monto_total >= 500000:
    dinero_propio = monto_total * 0.55
    prestamo_banco = monto_total * 0.30
    credito_fabricante = monto_total * 0.15
    interes = credito_fabricante * 0.20
else:
    dinero_propio = monto_total * 0.70
    prestamo_banco = 0
    credito_fabricante = monto_total * 0.30
    interes = credito_fabricante * 0.20

print ("El dinero propio invertido es: $", dinero_propio)
print ("El dinero prestado por el banco es: $", prestamo_banco)
print ("El crédito del fabricante es: $", credito_fabricante)
print ("El interés del prestamo del fabricante es: $", interes)
