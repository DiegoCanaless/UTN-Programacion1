def valid_index(row, column):
    valid = True
    if (row < 0 or row > 3) or (column < 0 or column > 3):
        print("** La posicion ingresada no existe! Intente nuevamente")
        valid = False
    return valid