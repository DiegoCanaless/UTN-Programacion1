from random import randint
from functions import *

while True:

    # Uso una función para crear el cartón, donde hago listas de 5 y las agrego a una lista madre convirtiendolas en
    # tuplas
    cardboard = create_cardboard()

    print('Cartón obtenido:')

    # Imprimo el cartón obtenido
    for i in range(0, 5):
        for j in range(0, 5):
            print("{:4d}".format(cardboard[i][j]), end=' ')
        print(' ')

    print('Inicio del Juego'.center(50, '-'))

    # Creo un cartón el cual ire rellenando con los números que correspondas con las bolas y el cartón inicial.
    cardboard_found = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    while True:
        i = 0
        j = 0
        number = randint(1, 75)
        print(f'El número de la bola extraída es: {number}')

        # Recorro la lista madre y notifico si el número al azar corresponde con alguno del cartón inicial
        for i in range(0, 5):
            for j in range(0, 5):
                if number == cardboard[i][j]:
                    print(f'El numero de la bola ha sido encontrado en el carton.')
                    print(f'Posición: fila {i+1}, columna {j+1}')
                    # Remplazo el 0 con el número correspondiente
                    cardboard_found[i][j] = number
        # Uso funciones para verificar si las horizontales, verticales y diagonales están completas
        is_horizontal = horizontal_line(cardboard, cardboard_found)
        is_vertical = vertical_line(cardboard, cardboard_found)
        is_major_diagonal = major_diagonal_line(cardboard, cardboard_found)
        is_reverse_diagonal = reverse_diagonal_line(cardboard, cardboard_found)

        # En el caso de que alguna lo sea, notifico que es Bingo y salgo del bucle
        if is_horizontal:
            break
        elif is_vertical:
            break
        elif is_major_diagonal:
            break
        elif is_reverse_diagonal:
            break

    # Imprimo los dos cartones y posteriormente consulto si volverá a jugar
    print('Cartón Inicial: ')
    for i in range(0, 5):
        for j in range(0, 5):
            print("{:4d}".format(cardboard[i][j]), end=' ')
        print(' ')

    print('Cartón Final: ')
    for i in range(0, 5):
        for j in range(0, 5):
            print("{:4d}".format(cardboard_found[i][j]), end=' ')
        print(' ')

    exit_game = input('Quieres volver a jugar? si/no: ').lower()
    if exit_game == 'si':
        continue
    else:
        print(f'Gracias por jugar!')
        break





