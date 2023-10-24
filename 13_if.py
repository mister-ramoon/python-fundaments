if True:
    print('Debería imprimirse')

if False:
    print('No debería imprimirse')

pet = input('Ingresa el tipo de mascota: ')

if pet == 'perro':
    print('Guau!')
elif pet == 'gato':
    print('Miau!')
elif pet == 'pez':
    print('...')
else:
    print('No sé que dice')

stock = int(input('Ingresa el número de stock: '))

if stock >= 100 and stock <= 1000:
    print('El stock es suficiente')
else:
    print('El stock no es suficiente')