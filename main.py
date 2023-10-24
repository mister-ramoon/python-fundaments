user_option = input('piedra, papel o tijera: ')
computer_option = 'piedra'

if user_option == computer_option:
    print('Empate')
elif user_option == 'piedra' and computer_option == 'papel':
    print('Perdiste')
elif user_option == 'papel' and computer_option == 'tijera':
    print('Perdiste')
elif user_option == 'tijera' and computer_option == 'piedra':
    print('Perdiste')
else:
    print('Ganaste')