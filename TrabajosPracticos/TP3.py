# Ejercicio 1

# palabra = input("Ingrese una palabra: ")

# for i in range(11):
#   print("N°"+ str(i) + " " +palabra)
""" 2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input('Ingrese su edad: '))
for i in range(edad):
    print(i+1)"""
""" 3- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 
1 hasta ese número separados por comas."""
"""number = int(input("Ingrese un número entero positivo: "))
for i in range(number):
    result = []
    if i % 2 != 0:
        result.append(str(i))

        final_result = ', '.join(result)
        print(final_result)"""
"""4- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
"""
number_4 = int(input("Ingrese un numero entero positivo:"))
arreglo=[]
for i in range((number_4),0,-1):
    arreglo.append(str(i))

arreglo_final = ",".join(arreglo)
print(arreglo_final)"""

"""5-Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""
#Ejercicio5
"""amount = int(input(f'Ingrese la cantidad a invertir: '))
interest = input(f'Ingrese el interés anual: ') 
interest = float(interest.strip('%')) / 100 #Convierto el string generado quitandole el signo porcentual '%', lo convierto a float y calculo el número. 
years = int(input(f'Ingrese el número de años: '))
for i in range(1, years+1):
    amount += amount * interest
    print(f'Capital obtenido el año {i}: ${amount}')"""

""" 6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido. """
#Ejercicio6

"""altura = int(input(f'Ingrese la altura: '))

for i in range(1,altura+1):
    print('*' * i)"""

""" 7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10. """
#Ejercicio7

"""for i in range(1,11):
    for j in range(1,11):
        print(f'{i}*{j} = {i*j}')"""

""" 8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo. """
#Ejercicio8
    
"""numTriangle = int(input("Ingrese un número entero: "))


for i in range(1, numTriangle + 1):
    for j in range(2 * i - 1, 0, -2): #Hago que los numeros se muestren de forma descendente.
        print(j, end=' ')
    print()"""
    



"""12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase.""" 
#Ejercicio 12
"""frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
letra_encontrada = 0

for i in frase:
    if i == letra:
        letra_encontrada += 1
    
print(f"La letra {letra} aparece {letra_encontrada} veces en la frase")"""

"""13-	Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta 
que el usuario escriba “salir” que terminará."""
#Ejercicio 13
"""entrada = input("Ingrese una palabra o numero: ")

while entrada.lower() != "salir":
    print(entrada)
    entrada = input("Ingrese una palabra o numero, si quiere salir ingrese salir: ")"""

"""14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y 
cuáles impares desde el primero hasta el segundo."""
#Ejercicio 14
"""num1 = (int(input("Ingrese el primer numero: ")))
num2 = (int(input("Ingrese el segundo numero: ")))

print(f"Numeros pares entre {num1} y {num2}: ", end= " ")
for i in range(num1,num2+1):
    if i % 2 == 0:
        print(i, end=" ")

print(" ")
print(f"Numeros impares entre {num1} y {num2}: ", end= " ")
for i in range(num1,num2+1):
    if i % 2 != 0:
        print(i, end=" ")

print(" ")"""
    
"""15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores."""
#Ejercicio 15
"""num = int(input("Ingrese un número entero mayor que cero: "))

print(f"Los divisores de {num} son:", end= " ")
for i in range(1,num+1):
    if num % i == 0:
        print(i, end= " ")""" 

"""16-	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos
negativos ha introducido."""
# Ejercicio 16
"""
num = int(input("Cuantos numeros desea introducir?: \n"))

# Ingreso de N numeros y conteo de negativos
numNeg = 0
for i in range(num):
    numIn = int(input("Numero "+ str(i+1)+ ": "))

    if numIn < 0:
        numNeg += 1

print("Se han introducido " + str(numNeg) + " numeros negativos.")

"""

"""17-	Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa
frase (sin repetirlas)."""
# Ejercicio 17
"""
vowels = ["a", "e", "i", "o", "u"]
found_vowels = []
phrase = input("Ingrese una frase cualquiera: \n").lower()

# Verificando e imprimiendo vocales
print("Las vocales que contiene la frase son: ")
for letter in phrase:
    if letter in vowels and letter not in found_vowels:
        print(letter)
        found_vowels.append(letter)

"""

"""18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza 
con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…"""

# Ejercicio 18
"""
print("--Fibonacci-- Los primeros 10 numeros de la sucesion de Fibonacci son los siguientes:")

# Primeros numeros (0 y 1)
num1 = 0
num2 = 1
print(num1)  
print(num2)  

# Demás numeros
for i in range(8):  
    next_num = num1 + num2
    print(next_num)
    num1, num2 = num2, next_num  

"""

"""19- Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la 
cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades 
que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar 
que las cantidades ingresadas sean positivas"""

# Ejercicio 19
"""

amount = float(input("Ingrese la cantidad de dinero que quiere ahorrar: \n"))
money = 0
total = 0

while total < amount:
    money = float(input("Cuanto dinero meterá en la alcancía?: "))
    if money < 0:
        print("Ingrese una cantidad positiva!")
    else:
        total += money
        print("DINERO: " + str(total))

print("Felicidades! Ha podido ahorrar lo que se propuso! (Meta: " + str(amount) + ", Dinero ahorrado: " + str(total) + ")" )

"""
# Ejercicio 20
""""
n = 1
total = 0

while(n!=0):

    num=int(input("Ingrese un el numero a sumar o 0 si desea dejar de sumar\n"))

    if (num!=0):
        total+=num
    
    elif(num==0):
        n=0
        print(" ")
        print("Ingreso 0")
    
    print(" ")

print ( "La suma de los numeros ingresados anteriormente es: ",total)

"""
# Ejercicio 21
"""
n = 1
big_num = 0

while(n!=0):

    num=int(input("Ingrese numeros positivos o 0 para salir\n"))

    if (num>big_num):
        big_num = num
    
    elif(num<0):
        print(" ")
        print("El numero ingresado es negativo, no es valido, intente nuevamente ")

    elif(num==0):
        n=0
        print(" ")
        print("Ingreso 0")
    
    print(" ")

print ( "El numero mas grande es: ",big_num)

"""
# Ejercicio 22
"""
j = 0

while(j != -1):
    print(" ")
    num=input("Ingrese un numero positivo o -1 si desea salir\n")
    total = 0

    if(int(num)>0):
        
        for n in num:
            total+=int(n)
        print(" ")
        print("La suma de los digitos de ",num," es igual a: ",total) 
    elif(int(num)==-1):
        j = -1
        print(" ")
        print("Ingreso -1, saliendo...")
    else:
        print(" ")
        print("valor ingresado no valido intente nuevamente")

"""
# Ejercicio 23 y 24
"""
n = 1
total = 0.0


while(n!=0):

    num=float(input("Ingrese el monto a agregar a la cuenta o 0 para salir\n"))

    if (num>0):
        total += num
    
    elif(num<0):
        print(" ")
        print("El numero ingresado es negativo, no es valido, intente nuevamente ")

    elif(num==0):
        n=0
        print(" ")
        print("Ingreso 0")
    
    print(" ")

if (total>1000):
    print(" ")
    print ("el monto total supera los 1000$, por lo que se le aplica un descuento del 10% ")
    discounted_total=total-total*0.10
    print("monto total es: ",total,"$  y con descuento es: ",discounted_total,"$")
else:
    print(" ")
    print ("el monto total no supera los 1000$, no se le aplica el descuento")
    print("el monto total es: ",total,"$")





"""
# Ejercicio 25
"""
total = 1
j=1

while j !=0:

    num=int(input("Ingrese un numero positivo entero \n"))


    if num>=0:
        for n in range(1,num+1):
            total*=n
        j=0
    else:
        print(" ")
        print("El valor ingresado no es valido, intente nuevamente") 

print(" ")
print("el factorial de ",num," es : ",total)

"""