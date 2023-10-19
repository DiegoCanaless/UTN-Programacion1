import getpass
print('---Kachipum V2.5/2---')
options = ['piedra','papel','tijera']
play=input('Desea jugar?: ')

while play.lower() == 'si':
    
    player1 = getpass.getpass('Jugador 1, ingrese piedra, papel o tijera: ')
    player1 = player1.lower()
    
    player2 = getpass.getpass('Jugador 2, ingrese piedra, papel o tijera: ')
    player2 = player2.lower()
    if player1 and player2 in options:
        if player1 == 'piedra' and player2 == 'tijera':
            print(f'Jugador 1: {player1}, Jugador 2: {player2}')
            print(f'El ganador es: Jugador 1')
        elif player1 == 'papel' and player2 == 'piedra':
            print(f'Jugador 1: {player1}, Jugador 2: {player2}')
            print(f'El ganador es: Jugador 1')
        elif player1 == 'tijera' and player2 == 'papel':
            print(f'Jugador 1: {player1}, Jugador 2: {player2}')
            print(f'El ganador es: Jugador 1')
        elif player1 == 'tijera' and player2 == 'piedra':
            print(f'Jugador 1: {player1}, Jugador 2: {player2}')
            print(f'El ganador es: Jugador 2')
        elif player1 == 'papel' and player2 == 'tijera':
            print(f'Jugador 1: {player1}, Jugador 2: {player2}')
            print(f'El ganador es: Jugador 2')
        elif player1 == 'piedra' and player2 == 'papel':
            print(f'Jugador 1: {player1}, Jugador 2: {player2}')
            print(f'El ganador es: Jugador 2')
        else:
            print(f'Jugador 1: {player1}, Jugador 2: {player2}')
            print('empate')
        print('¡Gracias por jugar!')
        break
    else:
        print('Una de las dos opciones fue ingresada incorrectamente...')
        continue