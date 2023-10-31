
"""1. Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse."""
"""new_list = []
number = None
while (True):
    number = int(input("Ingresa un número, ingresa 0 cuando desees salir: "))
    if number == 0:
        break

    else:
        new_list.append(number)
print(new_list)"""
"""2. A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar."""
"""number_choose = int(input("Ingrese un número para eliminar en la lista: "))
if number_choose in new_list:
    new_list.remove(number_choose)
    print(new_list)
else:
    print("El número " + str(number_choose) + " no pertenece a la lista.")"""
"""3. Imprimir la sumatoria de todos los números de la lista."""
"""addition = 0
for number in new_list:
    addition = addition + number
print("La suma de los valores de la lista es: " + str(addition))"""
"""4. Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella."""
"""number_for_list = int(input("Ingrese un número: "))
minor_list = []
for number in new_list:
    if number < number_for_list:
        minor_list.append(number)
for number in minor_list:
    print(number)"""

"""5. Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella.
 Por ejemplo, si la lista original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]"""
"""list_for_tuple = []
for number in new_list:
   numero = new_list.count(number)
   new_tuple = (number,numero)
   list_for_tuple.append(new_tuple)

unique_tuples = []
for number in set(new_list):
    count = new_list.count(number)
    unique_tuples.append((number, count))

print(unique_tuples)"""
"""6. Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. A continuación, 
solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.
a. Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
b. Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
c. Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
"""
"""students_primary = []
students_secondary = []
while(True):
    student_p = input("Ingrese el nombre de pila de los estudiantes de nivel primario, cuando quiera salir ingrese X: ")
    if student_p == "x":
        break
    else:
        students_primary.append(student_p)
while(True):
    student_s = input("Ingrese el nombre de pila de los estudiantes de nivel secundario, cuando quiera salir ingrese X: ")
    if student_s == "x":
        break
    else:
        students_secondary.append(student_s)
all_students =students_primary + students_secondary
unique_students = list(set(all_students))
print("Nombres de todos los alumnos de nivel primario y secundario (sin repeticiones):")
print(unique_students)
duplicates = [name for name in unique_students if all_students.count(name) > 1]
print("Nombres que se repiten entre los alumnos de nivel primario y secundario:")
print(duplicates)

unique_primary = list(set(students_primary))
unique_secondary = list(set(students_secondary))
names_unique_to_primary = [name for name in unique_primary if name not in unique_secondary]
print("Nombres de nivel primario que no se repiten en los de nivel secundario:")
print(names_unique_to_primary)

"""

#7.	Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada caracter, en todos los strings ingresados. Ejemplo:"r":5 "%"":3 "a":8 "9":1
"""
frequency_list = {}
contador = 0
while contador < 10:
    ingreso = input("Ingrese un string de cualquier cosa: ")

    for char in ingreso:
        if char in frequency_list:
            frequency_list[char] += 1
        else:
            frequency_list[char] = 1
    contador +=1

for char,count in frequency_list.items():
    print(f"{char} : {count}")
"""
#8.	Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10, participaron en un campeonato de fútbol con modalidad todos contra todos.
"""
goals = [
    [7, 2, 1, 1, 1, 1, 0, 3, 8, 2],
    [6, 4, 2, 0, 2, 3, 0, 2, 7, 3],
    [4, 7, 0, 0, 3, 5, 7, 5, 4, 0],
    [3, 9, 0, 8, 4, 8, 5, 1, 5, 1],
    [2, 7, 5, 3, 6, 2, 3, 9, 4, 3],
    [1, 1, 4, 4, 1, 4, 2, 3, 1, 6],
    [7, 2, 3, 5, 0, 8, 1, 8, 5, 5],
    [9, 3, 2, 6, 6, 4, 8, 1, 6, 2],
    [4, 6, 1, 9, 4, 5, 4, 2, 0, 0],
    [2, 5, 7, 8, 3, 1, 3, 3, 1, 0]
]


victory= [0] * 10
tie=  [0]*10
defeats= [0]*10
goal_difference =[0]*10
points = [0]*10

for i in range(10):
    for j in range(10):
        if i != j:
            if goals[i][j] > goals[j][i]:
                victory[i] += 1
                points[i] += 3
            elif goals[i][j] < goals[j][i]:
                defeats[i] += 1
            else:
                tie[i] += 1
                points[i] += 1

        goal_difference[i] += goals[i][j] - goals[j][i]

for team in range(10):
    print(f"Equipo {team + 1}:")
    print(f"Triunfos: {victory[team]}")
    print(f"Empates: {tie[team]}")
    print(f"Derrotas: {defeats[team]}")
    print(f"Diferencia de Goles: {goal_difference[team]}")
    print(f"Puntos: {points[team]}")
    print("=" * 20)


"""
"""
9.	Escribir un programa que simule el juego clásico de Memoria (Memotest) utilizando matrices. El juego 
consiste en un tablero de cartas boca abajo y el objetivo es encontrar todas las parejas de cartas iguales."""
# Ejercicio 9

"""
# Parejas
couples = [
        ["AA", "BB", "CC", "DD"],
        ["FF", "AA", "EE","FF"],
        ["BB", "DD", "EE", "CC"]]
# Cartas
cards = [
        ["㋡", "㋡", "㋡", "㋡"],
        ["㋡", "㋡", "㋡", "㋡"],
        ["㋡", "㋡", "㋡", "㋡"]]

count = 0

print("        ---- Bienvenido a MemoTest ----")
print("** Encuentre las 6 parejas del siguente tablero indicando las respectivas filas y columnas:")
print("** ATENCION: Los indices tanto para fila y columna van desde 0 a 3")
while True:
    # Muestro el estado de las cartas adivinadas (o no)
    print("\n* Estado actual *")
    for row in cards:
        for element in row:
            print(element, end= "  ")
        print()
    
    # Pido las posiciones de las cartas a adivinar
    while True:
        print("\n** PRIMERA CARTA:")
        row_1 = int(input("- Fila: "))
        column_1 = int(input("- Columna: "))
        # Valido que la posicion de la primera carta sea valida
        valid_index = funciones.valid_index(row_1, column_1)

        if valid_index == False:
            continue
        
        while True:
            print("** SEGUNDA CARTA:")
            row_2 = int(input("- Fila: "))
            column_2 = int(input("- Columna: "))
            # Valido que la posicion de la segunda carta sea valida
            valid_index = funciones.valid_index(row_2, column_2)

            if valid_index == False:
                continue
            else:
                break
        break

    # Verifico si se ha acertado
    if (row_1 == row_2) and (column_1 == column_2):
        print("\n** Ha ingresado la misma posicion, intente nuevamente!")
    elif couples[row_1][column_1] == couples[row_2][column_2]:
        # En caso de acertar, "volteo" las cartas adivinadas
        print("\n** ¡Pareja adivinada! **")
        cards[row_1][column_1] = couples[row_1][column_1]
        cards[row_2][column_2] = couples[row_2][column_2]
        # Sumo 1 al contador, que si llega a 6 indica que se han encontrado todas las parejas
        count += 1
    else:
        print("\n** ¡Mala suerte! **")

    if count == 6:
        print("\n **** JUEGO TERMINADO, ¡HA ENCONTRADO TODAS LAS PAREJAS ****")

        # Muestro el resultado final una vez mas

        for row in cards:
            for element in row:
                print(element, end= "  ")
            print()
        break
    """

"""
#Ejercicio 11
""11. Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en
el diccionario."""

"""symbols= {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
print("Euro, Dollar, Yen")

choice=input("Ingrese el nombre de una de las divisas anteriores y yo le devolvere su simbolo \n")
print(" ")

if choice.capitalize() in symbols:

    print(symbols[choice.capitalize()])

else:

    print("La divisa ingresada no se encuentra en las mencionadas anteriormente")"""


#Ejercicio 12
"""12. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en
un diccionario. Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> años, vive
en <dirección> y su número de teléfono es <teléfono>’."""

"""exit=False

user_data={}

name=input("Ingrese su nombre completo \n")
user_data["name"]=name

while exit==False:

    age=input("Ingrese su edad \n")

    if int(age)>0:

        exit=True
        user_data["age"]=age

    else:

        print("valor incorrecto intente nuevamente")
    

home_address=input("Ingrese su direccion \n")
user_data["home_address"]=home_address

exit=False

while exit==False:

    phone_number=input("Ingrese su numero de telefono \n")

    if int(phone_number)>0:

        exit=True
        user_data["phone_number"]=phone_number

    else:

        print("valor incorrecto intente nuevamente")
    

print(f"{user_data['name']} tiene {user_data['age']} años, vive en {user_data['home_address']} y su numero de telefono es {user_data['phone_number']}")"""





#Ejercicio 13
"""13. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al
usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos
de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello."""

"""exit=False

fruits = {
    'manzana': 125,
    'banana': 150,
    'naranja': 200,
    'uva': 225,
    'pera': 300
}
print("manzana,banana, naranja, uva, pera")
print("Ingrese la fruta que desea y la cantidad de kilos que va a llevar")
fruit=input("Fruta: \n")
if fruit.lower() in fruits:

    
    while exit ==False:
        kgs=input("Ingrese la cantidad de kilos que llevara\n")

        if int(kgs)>0:
            
            print(f"El precio de su compra es de {fruits[fruit.lower()]*int(kgs) } $ ")
            exit=True

        else:
            print("valor incorrecto intente nuevamente")


else:

    print("La fruta ingresa no se encuentra")"""