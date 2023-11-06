name = input("Ingrese su nombre: ")

print("1. Juego de Numeros")
print("2. Juego de palabras")

option = int(input(name + " ingresa el numero del juego que desea jugar: "))

if option == 1:

    # Se inician las variables que se usaran
    larger = 0
    amount = 0
    quantity__pairs = 0
    quantity__odds = 0
    while(True):
        print(name +" ingresa numeros enteros positivos y 0 si desea salir")
        num = int(input())

        #Se ejecuta una condicion distinta por si es que el usuario ingresa cualquier tipo de valor
        if num ==0:
            if quantity__odds>0 and quantity__pairs>0:
                promedio = amount/quantity__odds
                print(name + " el mayor numero par es: " + str(larger))
                print(name + " el promedio de los numeros impares es: " + str(promedio))
                break

            elif quantity__odds==0 and quantity__pairs==0:
                print(name + " no ingresaste numeros pares")
                print(name + " no ingresaste numeros impares")
                break
            elif quantity__pairs>0 and quantity__odds==0:
                print(name + " el mayor numero par es: " + str(larger))
                print(name + " no ingresaste numeros impares")
                break
            elif quantity__pairs==0 and quantity__odds>0:
                print(name + " no ingresaste numeros pares")
                promedio = amount/quantity__odds
                print(name + " el promedio de los numeros impares es: " + str(promedio))
                break

        #Si ocurre que el usuario ingresa un numero menor a 0 el programa volvera a comenzar
        if num<0:
            print(name + " ingresaste un numero menor a 0")
            continue

        #Detecta la cantidad de numeros pares e impares, y asigna un mayor en el caso de los pares
        if num%2 ==0:
            quantity__pairs +=1
            if num > larger:
                larger = num
        else:
            quantity__odds +=1
            amount += num
elif option == 2:
    vocals = {"A": 0, "E" : 0, "I" : 0, "O"  : 0, "U" : 0}
    sentence = input(name + " ingrese una frase: ")
    sentence = sentence.upper()
    
    for i in sentence:
        if i in vocals:
            vocals[i] += 1
    
    print("La cantidad de vocales fueron: ")
    for vowel, quantity in vocals.items():
        print(f"{vowel}: {quantity}")
else:
    print(name + " ingresaste una opcion no valida")