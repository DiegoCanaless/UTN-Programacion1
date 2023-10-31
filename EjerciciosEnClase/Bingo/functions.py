def create_cardboard():
    cardboard_f = []
    line = []
    print('Ingrese un numero entre el 1 y el 75 sin repetir...')
    # Itero la cantidad de números que tendrá el carton
    for i in range(1, 26):
        while True:
            is_same = False
            number = int(input(f'Posición: {i}, Ingrese un numero: '))
            # Verifico si dentro de las listas de la lista madre el número está y hago demás validaciones...
            for tuple_f in zip(*cardboard_f):
                if number in tuple_f:
                    is_same = True
            if number < 0 or number > 75:
                print(f'El numero introducido no está en los parámetros indicados...')
                continue
            elif number in line or is_same:
                print(f'El numero ya ha sido ingresado antes...')
                continue
            else:
                break
        # Si el número ingresado pasa las validaciones lo agrego a la lista, si ya son 5 elementos los que contiene
        # La agrego a la lista madre como tupla y posteriormente la vacío para empezar otra vez.
        line.append(number)
        if i % 5 == 0:
            cardboard_f.append(tuple(line))
            line.clear()
    # Retorno el valor creado
    return cardboard_f


def horizontal_line(cardboard_f, cardboard_found_f):
    for i in range(0, 5):
        if cardboard_f[i] == cardboard_found_f[i]:
            print(f'BINGO!!, Horizontal en la fila {i+1}')
            return True
    return False


def vertical_line(cardboard_f, cardboard_found_f):
    vertical_card = []
    vertical_card_found = []
    for i in range(0, 5):
        for j in range(0, 5):
            # Creo listas de ambos cartones con sus verticales para verificar si son las mismas
            vertical_card.append(cardboard_f[j][i])
            vertical_card_found.append(cardboard_found_f[j][i])
            if j == 4:
                if vertical_card == vertical_card_found:
                    print(f'Bingo!!! Vertical en la columna {i+1}')
                    return True
                else:
                    vertical_card.clear()
                    vertical_card_found.clear()
    return False


def major_diagonal_line(cardboard_f, cardboard_found_f):
    diagonal_card = []
    diagonal_card_found = []
    for i in range(0, 5):
        # Creo listas de ambos cartones con sus diagonales para verificar si son las mismas
        diagonal_card.append(cardboard_f[i][i])
        diagonal_card_found.append(cardboard_found_f[i][i])
    if diagonal_card == diagonal_card_found:
        print(f'Bingo!!! en la diagonal principal')
        return True
    return False


def reverse_diagonal_line(cardboard_f, cardboard_found_f):
    diagonal_card = []
    diagonal_card_found = []
    j = 4
    for i in range(0, 5):
        # Creo listas de ambos cartones con sus diagonales para verificar si son las mismas
        diagonal_card.append(cardboard_f[i][j])
        diagonal_card_found.append(cardboard_found_f[i][j])
        j -= 1
    if diagonal_card == diagonal_card_found:
        print(f'Bingo!!! en la diagonal inversa')
        return True
    return False


