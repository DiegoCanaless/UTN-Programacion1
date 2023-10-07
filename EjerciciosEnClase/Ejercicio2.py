#Ejercicio 1

cant_corrimiento = input("Ingrese la cantidad de corrimiento: ")
cant_corrimiento = int(cant_corrimiento)

abc = "abcdefghijklmnñopqrstuvwxyz"

palabras_nuevas =[]

for i in range(5):
    palabra=(input('Ingrese una palabra: '))
    palabra_nueva = " "
    for letra in palabra:
        if letra in abc:
            indice = (abc.index(letra) + cant_corrimiento) % len(abc)
            palabra_nueva += abc[indice]
        else:
            palabra_nueva += letra
    palabras_nuevas.append(palabra_nueva)


print("Palabras cifradas:")
for palabra in palabras_nuevas:
    print(palabra)

#Ejercicio 2

par=0
impar=0
numero= None
while(numero !=0):
    numero=int(input('Ingrese un número, ingrese 0 cuando quiera finalizar: '))
    if numero % 2 == 0:
        par += 1
    else:
        impar +=1
print("Cantidad de numeros pares: " + str(par))
print("Cantidad de numeros impares: " +str(impar))
