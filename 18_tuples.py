numbers = (1, 2, 3, 4)
string = ('Hola', 'Adios', 'Hello', 'Bye')
print(numbers)
print(type(numbers))
print(string)
print(type(string))

print(numbers[0])
print(string[-1])

# index busca el elemento y regresa su posición
print(string.index('Hello'))

# count cuenta cuantas veces aparece un elemento
print(string.count('Hola'))

my_list = list(string)
print(type(my_list))