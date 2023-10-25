my_dict = {}
print(type(my_dict))

my_dict = {
    'Avion': 'Aeronave que vuela',
    'name': 'Juan',
    'age': 25,
    'last_name': 'Perez',
}

print(my_dict)

# len() regresa el número de elementos
print(len(my_dict))

# Buscar un elemento por su llave
print(my_dict['name'])

# get() regresa el valor de la llave indicada
print(my_dict.get('age'))
print(my_dict.get('phone'))

# in regresa True si la llave existe en el diccionario
print('name' in my_dict)
print('phone' in my_dict)