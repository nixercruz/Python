print("Por favor ingrese el precio del producto.")
precio = float(input())
porcentaje_iva = 0.19
iva = precio * porcentaje_iva
print("El IVA del producto es: ", iva) 
print("El precio total del producto con IVA es: ", precio + iva)
