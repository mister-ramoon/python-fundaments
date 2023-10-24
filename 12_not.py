print(not True) # False
print(not False) # True

print('NOT AND')
print('not True and True =', not True and True) # False
print('not True and False =', not True and False) # False
print('not False and True =', not False and True) # True
print('not False and False =', not False and False) # False

stock = input('Ingresa el número de stock: ')
stock = int(stock)
print(not (stock >= 100 and stock <= 1000))