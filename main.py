import random

options = ('piedra', 'papel', 'tijera')

user_option = input('piedra, papel o tijera: ')
user_option = user_option.lower()

if user_option not in options:
    print('Opción no válida')
    exit()

computer_option = random.choice(options)

print(user_option)
print(computer_option)

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