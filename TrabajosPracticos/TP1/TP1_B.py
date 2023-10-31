import math

print("ejercicio 1")
print(" ")

base = float(input("ingrese la base del rectanculo \n"))
altura = float(input("ingrese la altura del rectanculo \n"))

area = base * altura
perimetro = 2 * (base + altura)

print("el area del rectangulo es de: ", area )
print("el perimetro del rectangulo es de: ", perimetro )

print("--------------------------------------------------")

print("ejercicio 2")
print(" ")

cateto1 = float(input("Ingrese la longitud del primer cateto: \n"))
cateto2 = float(input("Ingrese la longitud del segundo cateto: \n"))


hipotenusa = math.sqrt(cateto1**2 + cateto2**2)


print("La longitud de la hipotenusa es: ", hipotenusa)

print("--------------------------------------------------")

print("ejercicio 3")
print(" ")

num1 = float(input("ingrese el primer numero: \n"))
num2= float(input("Ingrese el segundo nuemro: \n"))

print("suma: ",num1+num2,", resta: ",num1-num2,", multiplicacion: ",num1*num2,", division: ", num1/num2 )

print("--------------------------------------------------")

print("ejercicio 4")
print(" ")

fahrenheit = int(input("ingrese los grados farenheit: \n"))

celcius = (fahrenheit-32)*5/9

print("fahrenheit: ", fahrenheit," celcius: ", celcius)

print("--------------------------------------------------")

print("ejercicio 5")
print(" ")

print("¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?")
print(" ")
print("a): A = input(nombre, ¿Cuál es tu canción favorita?)")
print("el error esta en que el input debe recibir solo un argumento, que es el mensaje")
print("la solucion es poner solo el mensaje y quitar la variable ´nombre´")
print(" ")

print("b):  precio = input(“Precio: “) ; total = precio + (precio * 0.1)")
print("el error esta en que el input devuelve una variable de tipo string ")
print("la solucion es agregar el tipo de dato que queremos recibir del input, ya sea int o float")
print(" ")

print("c):  edad = int(input(“Edad: “))print(tu edad es, edad)")
print("el error esta en el print")
print("la solucion es agregarle las comillas al mensaje para que no salte error al ejecutar")
print(" ")

print("d):  edad = int(input(“Edad: “))print(“Veamos si tu edad es 18…”, edad=18)")
print("el error esta al querer mostrar la edad en el print")
print("la solucion seria sacar agregar un if para verificar si edad es igual a 18")
print(" ")

A = input("¿Cuál es tu canción favorita?")

precio = float(input("Precio: "))
total = precio + (precio * 0.1)

edad = int(input("Edad: "))
print("tu edad es", edad)

edad = int(input("Edad: "))
if(edad==18):
    print("tu edad es 18")
else :
    print("tu edad no es 18, es ", edad)

print("--------------------------------------------------")

print("ejercicio 6")
print(" ")

promedio=0
for n in range(3):

    num= int(input("ingrese un numero \n"))
    promedio+=num

promedio=promedio/3

print("el promedio de los numeros ingresados es de: ", promedio)

print("--------------------------------------------------")

print("ejercicio 7")
print(" ")

minutos = int(input("Ingrese la cantidad de minutos: "))


horas = minutos // 60
minutos_restantes = minutos % 60


print(minutos, " minutos son ", horas ," horas y ", minutos_restantes ," minutos.")

print("--------------------------------------------------")

print("ejercicio 8")
print(" ")

sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))

venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))

comision = (venta1 + venta2 + venta3) * 0.10

salario_total = sueldo_base + comision

print("El monto total de comisión es: ",comision)
print("El salario total del vendedor es: ",salario_total)

print("--------------------------------------------------")

print("ejercicio 9")
print(" ")

total_compra = float(input("Ingrese el total de la compra: "))

descuento = total_compra * 0.15

monto_a_pagar = total_compra - descuento

print("El monto a pagar después del descuento es:", monto_a_pagar)

print("--------------------------------------------------")

print("ejercicio 10")
print(" ")

parcial1 = float(input("Ingrese la calificación del primer parcial: "))
parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
parcial3 = float(input("Ingrese la calificación del tercer parcial: "))

examen_final = float(input("Ingrese la calificación del examen final: "))

trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

print("La calificación final del alumno en Algoritmos es:", calificacion_final)

print("--------------------------------------------------")

print("ejercicio 11")
print(" ")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

distancia = abs(numero1 - numero2)

print("La distancia entre los dos números es:", distancia)

print("--------------------------------------------------")

print("ejercicio 12")
print(" ")

numero = float(input("Ingrese un número: "))

raiz_cuadrada = numero ** 0.5
raiz_cubica = numero ** (1/3)

print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)
print("La raíz cúbica de", numero, "es:", raiz_cubica)

print("--------------------------------------------------")

print("ejercicio 13")
print(" ")

numero = int(input("Ingrese un número de dos cifras: "))

if 10 <= numero <= 99:
    cifra_unidades = numero % 10
    cifra_decenas = numero // 10

    numero_invertido = cifra_unidades * 10 + cifra_decenas

    print("El número invertido es:", numero_invertido)

else:
    print("El número ingresado no tiene dos cifras.")

print("--------------------------------------------------")

print("ejercicio 14")
print(" ")

A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))

temp = A
A = B
B = temp

print("El valor de A después del intercambio es:", A)
print("El valor de B después del intercambio es:", B)

print("--------------------------------------------------")

print("ejercicio 15")
print(" ")

hora_partida = input("Ingrese la hora de partida en formato HH:MM:SS: ")

T = int(input("Ingrese el tiempo de viaje en segundos: "))

hora_llegada = int(hora_partida[:2]) * 3600 + int(hora_partida[3:5]) * 60 + int(hora_partida[6:]) + T

hh= hora_llegada // 3600
mm = (hora_llegada % 3600) // 60
ss= hora_llegada % 60

print("Hora de llegada a la ciudad B:", hh, ":", mm, ":", ss)

print("--------------------------------------------------")

print("ejercicio 16")
print(" ")

nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")

iniciales = nombre[0] + apellido1[0]

print("Las iniciales son:", iniciales)

print("--------------------------------------------------")

print("ejercicio 17")
print(" ")

usuario = input("Por favor, ingrese su nombre: ")

print("Ahora estás en la matrix,", usuario , ".")

print("--------------------------------------------------")

print("ejercicio 18")
print(" ")

costo_cena = float(input("Ingrese el costo de la cena en el restaurante: "))

servicio = costo_cena * 0.062

propina = costo_cena * 0.10

monto_final = costo_cena + servicio + propina

print("El monto final a pagar es:", monto_final)

print("--------------------------------------------------")

print("ejercicio 19")
print(" ")

dia = int(input("Ingrese el día de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento: "))
anio = int(input("Ingrese el año de su nacimiento: "))

print("La fecha de nacimiento es:", dia, "/", mes, "/", anio)

print("--------------------------------------------------")

print("ejercicio 20")
print(" ")

dia = int(input("Ingrese el día de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento: "))
anio = int(input("Ingrese el año de su nacimiento: "))

fecha_nacimiento = f"{dia:02d}{mes:02d}{anio}"

print("La fecha de nacimiento es:", fecha_nacimiento)

print("--------------------------------------------------")

print("ejercicio 21")
print(" ")

km_por_litro = float(input("Cuántos kilómetros por litro puede recorrer su moto: "))
capacidad_tanque = float(input("Cuántos litros de combustible cabe en el tanque: "))
distancia_total = float(input("Cuántos kilómetros recorrerán en total: "))

tanques_necesarios = distancia_total / (km_por_litro * capacidad_tanque)

print("Necesitarán", int(tanques_necesarios), "tanques de combustible para el viaje.")

print("--------------------------------------------------")

