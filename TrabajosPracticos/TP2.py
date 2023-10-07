
#Ejercicio 1 y 2
"""
years = int(input("Ingrese la cantidad de años de nuestra computadora: "))
if years< 0:
    print('Error, el numero ingresado es menor a 0')
else:
    resultado = "El computador es nuevo" if years<=2 else "El computador es viejo"

    print(resultado)
"""

#Ejercicio 3
""""
first_name = input("Ingrese un nombre: ")
second_name = input("Ingrese un segundo nombre: ")

resultado = "Coincidencia" if first_name[0] == second_name[0]  else "No hay coincidencia"

print(resultado)

"""

#Ejercicio 4 
"""
print('Ingrese A si su candidato elegido es el Verde')
print('Ingrese B si su candidato elegido es el Rojo')
candidato_elegido = input('Ingrese C si su candidato es el Azul: ')
candidato_elegido=candidato_elegido.upper()
if candidato_elegido == 'A':
    print('Su candidato elegido es el Verde.')
elif candidato_elegido == 'B':
    print('Su candidato elegido es el Rojo.')
elif candidato_elegido == 'C':
    print('Su candidato elegido es el Azul.')
else:
    print('el valor ingresado no es correcto')
"""
#Ejercicio 5

"""letra = input("Ingrese una letra: ")
letra = letra.upper()

if len(letra) < 2 :
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print("Es vocal")
    else:
        print("No es vocal")
else:
    print("No se puede procesar el dato")"""

#Ejercicio 6
""""
years = int(input('Ingrese un año: '))
if years % 4 ==0 and (years % 100 != 0 or (years%100==0 and years%400==0)):
    print('Es bisisesto')
else:
    print('No es bisisesto')
"""

#Ejercicio 7
"""
num1= int(input("Ingresa el primer numero: "))
num2= int(input("Ingresa un segundo numero: "))
num3= int(input("Ingresa un tercer numero: "))
menor = 0

if num1<=num2 and num1<num3:
    print("El numero menor es: " + str(num1))
elif num2<=num1 and num2<=num3:
    print("El numero menor es: " + str(num2))
else:
    print("El numero menor es: " + str(num3))
"""

#Ejercicio 8
"""nombre_usuario = input('Ingrese el nombre de usuario: ')
password = input('Ingrese la contraseña: ')
if nombre_usuario == 'Gwenevere' and password == 'excalibur':
    print('Usuario y contraseña correctos. Puede ingresar a Camelot')
else:
    print('Acceso denegado')"""

#Ejercicio 9
name= input("Ingrese su nombre:")
sexo= input("Ingrese su sexo M/F: ")
sexo = sexo.upper()

if sexo == "M":
    if name[0]>"N":
        print("Pertenece al grupo A")
    elif name[0]<"P":
        print("Pertenece al grupo B") 
    else:
        print("Error al ingresar el nombre")
elif sexo == "F":
    if name[0]>"M":
        print("Pertenece al grupo A")
    elif name[0]>"N":
        print("Pertenece al grupo B")
    else:
        print("Error al ingresar el nombre")
else:
    print("Ingresaste mal el sexo")