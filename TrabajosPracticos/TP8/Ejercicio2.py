def potencia(number1, number2):

    if number1 == number2:
        return True
    elif number1 < number2:
        return False
    else:
        return potencia(number1/ number2, number2)


num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if potencia(num1, num2):
    print(f"El numero {num1} es potencia de {num2}")
else:
    print(f"El numero {num1} no es potencia de {num2}")