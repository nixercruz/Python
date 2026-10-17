print("Ingrese su nombre")
nombre = input()
print("Por favor ingrese su número de horas trabajadas.")
numero_horas = int(input())
print("Por favor ingrese su tarifa por hora.")
tarifa_hora = int(input())
salario = numero_horas * tarifa_hora


print ("El empleado", nombre, "trabajó ", numero_horas, "horas y el valor por hora es: ", tarifa_hora,". El salario total es: $", salario)

