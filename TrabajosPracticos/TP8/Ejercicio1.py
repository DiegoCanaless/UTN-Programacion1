def cant_digit(num):

    if num < 10:
        return 1
    else:
        return 1 + cant_digit(num // 10)


number = int(input("Ingrese un numero: "))

digitos = cant_digit(number)

print("La cantidad de digitos en el numero fueron: ", digitos)


