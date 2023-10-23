name = 'Ramón'
last_name = 'Ruiz'
print(name, last_name)

# Concatenación
full_name = name + ' ' + last_name
print(full_name)

quote = "I'm a programmer"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template)

template2 = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template2)

template3 = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template3)