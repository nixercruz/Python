aprendices = []
edades = []

cantidad = int(input("Por favor digite la cantidad de aprendices que va a registrar "))

for i in range (cantidad):
    nombre = input("DIgite el nombre del aprendiz ").lower()
    aprendices.append(nombre)
    edad = int(input("Por favor digite la edad del aprendiz "))
    edades.append(edad)

print(aprendices)
print(edades)

edad_mayor = max(edades)
posicion = edades.index(edad_mayor)

print ("El aprendiz con mayor edad es: ", aprendices[posicion]," la edad del aprendiz es: ", edades[posicion])

aprendices.insert(1, "Sandra Milena Cruz Molano")

print(aprendices)

aprendices_18 = edades.count(18)

print ("La cantidad de aprendices con 18 años es: ",aprendices_18)

aprendices.append("Juan carlos")
print(aprendices)

aprendices.remove ("Sandra Milena Cruz Molano")
print(aprendices)

aprendices.index ("Juan carlos")

print("Los primeros 10 aprendices de la lista son: ", aprendices[:10])

print("Los últimos 10 aprendices de la lista son: ", aprendices[-10:])

print("Los elementos desde el índice 10 hasta el índice 20 son: ", aprendices[10:21])

print("Los elementos de la lista con índice par son: ", aprendices[::2])
