print ("Por favor digite su salario mensual: ")
salario = float(input())
if salario <= 500000:
    impuesto = 0
elif salario > 500000 and salario <= 1000000:
    impuesto = salario * 0.10
else:
    impuesto = salario * 0.20

salario_final = salario - impuesto
print("El impuesto a pagar es: $", impuesto)
print("El salario final después de impuestos es: $", salario_final)
