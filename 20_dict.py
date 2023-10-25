person = {
    'name': 'Juan',
    'age': 25,
    'last_name': 'Perez',
    'lang': ['Python', 'JavaScript', 'C', 'C++', 'C#', 'Java', 'PHP']
}

print(person)

person['name'] = 'Pedro'
person['age'] -= 1
person['lang'].append('Go')
print(person)

# del elimina un elemento del diccionario
del person['last_name']
print(person)

# pop elimina un elemento del diccionario
person.pop('age')
print(person)

# items regresa los elementos del diccionario
print(person.items())

# keys regresa las llaves del diccionario
print(person.keys())

# values regresa los valores del diccionario
print(person.values())