'''
 Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico; la fórmula que se aplica es:  cuando el sexo es femenino : núm. pulsaciones = (220 - edad)/10  y si el sexo es masculino : núm. pulsaciones = (210 - edad)/10 
'''

sexo = input("Por favor ingrese su sexo 'M' para masculino o 'F' para femenino ").lower()
edad = int(input("Por favor digite su edad "))
pulsaciones = 0

match (sexo):
    case "m":
        pulsaciones = (210 - edad) / 10
        print ("El número de pulsaciones por segundo es: ", pulsaciones)
    case "f":
        pulsaciones = (220 - edad) / 10
        print ("EL número de pulsaciones por segundo es: ", pulsaciones)
