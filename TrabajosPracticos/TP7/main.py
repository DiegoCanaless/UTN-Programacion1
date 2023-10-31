
import funciones
"""1. Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja."""

"""new_list = []
while(True):
    num = int(input("Ingresa una lista de numeros, cuand quieras salir ingresa 0: "))
    if num == 0:
        break
    else:
        new_list.append(num)
print("Lista: " + str(new_list))
funciones.bubble_sort(new_list)
print("Lista ordenada:" + str(new_list))"""
"""2. Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección."""
"""new_word_list = []
while(True):
    word = input("Ingrese una palabra, cuando desee salir ingrese 0: ")
    if word == "0":
        break
    else:
        new_word_list.append(word)
print("Lista: " + str(new_word_list))
funciones.selection_sort(new_word_list)
print("Lista ordenada: "+ str(new_word_list))"""

"""3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor,
año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en función de un campo 
específico, como el año de publicación o el autor."""
# Ejercicio 3

"""

# Lista con diccionarios, cada diccionario contiene informacion sobre X libro
dictionary_list =  [
    {"name": "El código Da Vinci", "author": "Dan Brown", "year": 2003}, 
    {"name": "El gran Gatsby", "author": "Francis Scott Key Fitzgerald " ,"year": 1925},
    {"name": "El niño con el pijama de rayas", "author": "John Boyne", "year": 2006},
    {"name": "La naranja mecánica", "author": "Anthony Burgess", "year": 1962},
    {"name": "Cien años de soledad", "author": "Gabriel García Marquéz", "year": 1967},
    {"name": "Crimen y castigo", "author": "Fyodor Dostoevsky", "year": 1866}]   

# Muestro los libros disponibles
print("------------ Libros disponibles ------------")
for book in dictionary_list:
    print(f"- {book['name']}, ({book['year']}) de {book['author']}")

# Pregunto al usuario como desea ordenarlos
while True:
    option = int(input("\n1) Ordenar alfabeticamente en funcion del nombre del autor. \n2) Ordenar en funcion del año de publicacion. \n3) Salir\n"))
    
    if (option < 1) or (option > 3):
        print("Ingrese una opcion válida")
    else:
        # Si ingreso 1 se ordena por en funcion del nombre del autor
        if option == 1:
            dictionary_list = funciones.bubble_sort_3(dictionary_list, "author")
            print("\n")
            for book in dictionary_list:
                print(f"- {book['author']}: {book['name']}, ({book['year']})")

        # Si ingreso 2 se ordena por año de publicacion
        elif option == 2:
            dictionary_list = funciones.bubble_sort_3(dictionary_list, "year")
            print("\n")
            for book in dictionary_list:
                print(f"- {book['year']}: {book['name']}, de {book['author']}")
        # Si ingreso 3 el programa finaliza
        elif option == 3:
            break
"""

"""4. Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción.
"""
"""new_word_list = []
while(True):
    word = input("Ingrese una palabra, cuando desee salir ingrese 0: ")
    if word == "0":
        break
    else:
        new_word_list.append(word)
print("Lista: " + str(new_word_list))
for i in range(1, len(new_word_list)):
    current_string = new_word_list[i]
    j = i - 1
    while j >= 0 and len(new_word_list[j]) > len(current_string):
        new_word_list[j+1] = new_word_list[j]
        j -= 1
    new_word_list[j+1] = current_string

print(new_word_list)"""

"""5. Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente."""
"""new_list = []
while(True):
    num = int(input("Ingresa una lista de numeros, cuand quieras salir ingresa 0: "))
    if num == 0:
        break
    else:
        new_list.append(num)
print("Lista: " + str(new_list))
funciones.bubble_desc(new_list)
print("Lista ordenada:" + str(new_list))"""

"""6. Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de ordenamiento por conteo."""
"""list_num = [1,4,5,2,10,23,0]
print("Lista: " + str(list_num))
lista_ordenada = funciones.count_sort(list_num)
print("Lista ordenada: " + str(lista_ordenada))"""

"""7. Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que ordene esta lista de manera que primero estén los números ordenados de menor a mayor
y luego las cadenas de caracteres ordenadas alfabéticamente.
"""
"""lista_variada = [1, "Hola", "chau", 3, "Sol", 22, "Mar"]
print("Lista: " + str(lista_variada))
lista_str = []
lista_int = []
for valores in lista_variada:
    if isinstance(valores, str):
        lista_str.append(valores)
    elif isinstance(valores, int):
        lista_int.append(valores)
funciones.selection_sort(lista_str)
funciones.bubble_sort(lista_int)
lista_final = lista_str + lista_int
print("Lista ordenada: " + str(lista_final))"""

"""8. Implementa el algoritmo de ordenamiento  Merge Sort y úsalo para ordenar una lista de números."""

"""
list_of_numbers = [1,4,2,6,5,24]
print("Lista inicial: " + str(list_of_numbers))
funciones.merge_sort(list_of_numbers)
print("lista ordenada: " + str(list_of_numbers))
"""