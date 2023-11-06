
def is_mutant(adn_list):

    for row in adn_list:
        for column in range(len(row) - 3):
            if len(set(row[column:column+4])) == 1:
                return True

    for i in range(len(adn_list[0])):
        column = [row[i] for row in adn_list]
        for j in range(len(column) - 3):
            if len(set(column[j:j+4])) == 1:
                return True

    for i in range(len(adn_list) - 3):
        for j in range(len(adn_list[0]) - 3):
            diagonal = [adn_list[i+k][j+k] for k in range(4)]
            if len(set(diagonal)) == 1:
                return True

    return False

