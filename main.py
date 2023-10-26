import random

options = ('piedra', 'papel', 'tijera')
computer_wins = 0
user_wins = 0

rounds = 1

while True:
    print('*' * 10) 
    print(f'Round {rounds}')
    print('*' * 10)

    print(f'Puntaje: Computadora {computer_wins} - {user_wins} Usuario')

    user_option = input('piedra, papel o tijera: ')
    user_option = user_option.lower()

    if user_option not in options:
        print('Opción no válida')
        continue

    computer_option = random.choice(options)

    print(user_option)
    print(computer_option)

    if user_option == computer_option:
        print('Empate')
    elif user_option == 'piedra' and computer_option == 'papel':
        print('Perdiste')
        computer_wins += 1
    elif user_option == 'papel' and computer_option == 'tijera':
        print('Perdiste')
        computer_wins += 1
    elif user_option == 'tijera' and computer_option == 'piedra':
        print('Perdiste')
        computer_wins += 1
    else:
        print('Ganaste')
        user_wins += 1

    if computer_wins == 2:
        print('Perdiste el juego')
        break

    if user_wins == 2:
        print('Ganaste el juego')
        break

    rounds += 1