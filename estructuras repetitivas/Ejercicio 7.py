'''
La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad de Ibagué,  cuantos entran con calcomanía de cada color.
'''

rojo = 0
verde = 0
azul = 0 
rosa = 0
amarillo = 0

cantidad = int(input("Ingrese la cantidad de autos que entran a la ciudad de Ibagué: "))

for i in range (cantidad):
    ultimo_digito = int(input("Por fav1or digite el último dígito de la placa " + str (1)+ " (0 - 9) "))

    if ultimo_digito == 1 or ultimo_digito == 2:
        amarillo += 1
    elif ultimo_digito == 3 or ultimo_digito == 4:
        rosa += 1
    elif ultimo_digito == 5 or ultimo_digito == 6:
        rojo += 1
    elif ultimo_digito == 7 or ultimo_digito == 8:
        verde += 1
    elif ultimo_digito == 9 or ultimo_digito == 0:
        azul += 1

print("La cantidad total de autos registrados es: ", cantidad)
print("El total de autos con la calcomanía amarilla es: ", amarillo)
print("El total de autos con calcomanía rosa es: ", rosa)
print("El total de autos con calcomanía roja es: ", rojo)
print("El total de autos con calcomanía verde es: ", verde)
print("El total de autos con calcomanía azul es: ", azul)
