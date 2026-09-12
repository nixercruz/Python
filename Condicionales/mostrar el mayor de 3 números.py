print ("Por favor ingrese el primer número: ")
num1 = int(input())
print ("Por favor ingrese el segundo número: ")
num2 = int(input())
print ("Por favor ingrese el tercer número: ")
num3 = int(input())

if num1 > num2 and num1 > num3:
    print ("El número mayor es: ", num1)
elif num2 > num1 and num2 > num3:
    print ("El número mayor es: ", num2)
else:
    print ("El número mayor es: ", num3)
     