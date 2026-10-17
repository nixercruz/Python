suma = 0

while True:
    entrada = input("Ingrese un número (o 'fin' para terminar): ")
    
    if entrada.lower() == "fin":
        break
        
    try:
        numero = float(entrada)
        suma = suma + numero
    except ValueError:
        print("Por favor, ingrese un número válido o 'fin'.")

print("La suma total es: ", suma)
