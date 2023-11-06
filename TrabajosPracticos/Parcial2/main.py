import functions
from functions import *
# Listas de prueba:
#horizontal_test_list = [('A', 'T', 'G', 'C', 'G', 'A'), ('C', 'A', 'G', 'T', 'G', 'C'), ('T', 'T', 'A', 'T', 'T', 'T'), ('A', 'G', 'A', 'C', 'G', 'G'), ('C', 'C', 'C', 'C', 'T', 'A'), ('T', 'C', 'A', 'C', 'T', 'G')]
#vertical_test_list = [('A', 'T', 'G', 'C', 'G', 'A'), ('C', 'A', 'G', 'T', 'G', 'C'), ('T', 'T', 'A', 'T', 'G', 'T'), ('A', 'G', 'A', 'C', 'G', 'G'), ('G', 'C', 'G', 'T', 'C', 'A'), ('T', 'C', 'A', 'C', 'T', 'G')]
#diagonal_test_list = [('A', 'T', 'G', 'C', 'G', 'A'), ('C', 'A', 'G', 'T', 'G', 'C'), ('T', 'T', 'A', 'T', 'T', 'T'), ('A', 'G', 'A', 'A', 'G', 'G'), ('G', 'C', 'G', 'T', 'C', 'A'), ('T', 'C', 'A', 'C', 'T', 'G')]

list= []
line = []

# Ejecuto bucles fori para ir llenanando cada line con 6 caracteres
for i in range(6):
    for j in range(6):
        while (True):
            sigla__adn = input("Ingrese la base ADN de la persona (A,T,C,G): ").upper()
            if sigla__adn in ["A", "T", "C","G"]:
                line.append(sigla__adn)
                break
            else:
                print("Ingreso un error invalido, Intentelo de nuevo")
    #Cuando la line termina de llenarse la convierto en una tupla y ingreso a la lista
    list.append(tuple(line))
    line.clear()
    print("Salto")
print(list)
print("La cadena de ADN de la persona es: ")

#Imprimo la lista con un formato
for i in range(6):
    for j in range(6):
        print("{:4}".format(list[i][j]), end=' ')
    print()

#ejecuto la funcion is_mutant pasando como parametro la lista llena de tuplas
mutant = is_mutant(list)
print()

if mutant:
    print("       Es un mutante")
else:
    print("       No es mutante")