numbers = [1, 2, 3, 4, 5]
print(numbers[1])

numbers[-1] = 6
print(numbers)

# append agrega un elemento al final de la lista
numbers.append(7)
print(numbers)

# insert agrega un elemento en la posición indicada
numbers.insert(0, 'hola')
print(numbers)

# index busca el elemento y regresa su posición
tasks = ['Sacar la basura', 'Barrer la entrada', 'Pasear al perro']
new_list = tasks + numbers
print(new_list)

index = new_list.index('Barrer la entrada')
new_list[index] = 'Barrer el patio'
print(new_list)

# remove elimina el elemento indicado
new_list.remove('hola')
print(new_list)

# pop elimina el último elemento de la lista
new_list.pop()
print(new_list)

# reverse invierte el orden de la lista
new_list.reverse()
print(new_list)

# sort ordena la lista
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ['b', 'a', 'c']
strings.sort()
print(strings)