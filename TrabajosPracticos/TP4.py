#Ejercicio 1
"""
for x in range(1,31,1):
    if x == 4 or x == 6 or x == 10:
        print("Se ha salteado el valor " +str(x))
        continue
    elif x == 15:
        print("La ejecucion del bucle se ha interrumpido cuando x era: "+str(x))
        break
    else:
        print(str(x))
"""

#Ejercicio 2
"""
lista = []
while(True):
    palabra= input("Ingrese una linea: ")
    if len(palabra) == 0:
        break
    elif len(palabra) > 0:
        palabra= palabra.upper()
        lista.append(palabra)
        continue

for i in lista:
    print(str(i))
"""

#Ejercicio 3
"""
cuenta = 100
aux = cuenta
print("Para depositar ingrese   D (Numero a Depositar)")
print("Para retirar ingrese   R (Numero a Retirar)")
print("Para ver el monto en su cuenta ingrese V")
print("Para salir deje el ingreso vacio")

while(True):
    operacion = input("Ingrese la operacion: ")
    if len(operacion) == 0:
        if cuenta> aux:
            print("Ingreso "+ str(cuenta-aux))
            break
        elif cuenta< aux:
            print("Retiro " + str(aux- cuenta))
            break
        else:
            print("No hubieron cambios")
            break
    
    operacion = operacion.upper()
    
    if operacion[0] == "D":
        valor = int(operacion[2:])
        cuenta = cuenta + valor
    elif operacion[0] == "R":
        valor = int(operacion[2:])
        cuenta = cuenta - valor
    elif operacion[0] == "V":
        print(cuenta)
    else:
        print("Ingreso mal la operacion a realizar")
        continue
"""

#Ejercicio 4
"""
primos = 0
while(True):
    num = input("Ingrese un numero mayor a 0: ")

    if num.isdigit():
        num = int(num)
    else:
        print("Ingreso incorrecto")
        continue

    if num == 0:
        print(f"Se ingresaron {primos} numeros primos.")
        break

    primos__num = 0 

    for i in range(1, num+1):
        if num%i == 0:
            primos__num = primos__num+ 1

    if primos__num == 2:
        primos = primos +1        
"""

#Ejercicio 5
"""
year1 = int(input("Ingrese un año: "))
year2 = int(input("Ingrese otro año: "))

if year2 > year1:
    for i in range(year1, year2+1):
        if i%4 == 0 and (i%100 != 0 or i%400 == 0):
            print(i)
elif year1> year2:
    for i in range(year1, year2-1, -1):
        if i%4 == 0 and (i%100 != 0 or i%400 == 0):
            print(i)
"""

#Ejercicio 6
"""
for i in range(1,21):
    if i%2==0:
        print(i)
    else:
        continue
"""

#Ejercicio 7
"""
numeros__lista = [15, 7, 32, 78, 632, 42, 72 ,51 ,7324, 1510, 111, 12, 153, 147, 158, 196, 174, 183, 129, 201]
num = int(input("Ingrese el numero a buscar: "))

for i in numeros__lista:
    if i ==num:
        print(f"Se encontro el numero {num}")
        break
    else:
        print(i)
"""

#Ejercicio 8
"""
while(True):
    num = int(input("Ingresar 1/2/3: "))
    if num == 0:
        print("Apagando programa")
        break
    elif num == 1:
        print("Ingreso 1")
        continue
    elif num == 2:
        print("Ingreso 2")
        continue
    elif num == 3:
        print("Ingreso 3")
        continue
"""



