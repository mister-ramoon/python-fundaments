for element in range(20):
    print(element)
    
my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)

my_tuple = ('Python', 'JavaScript', 'C', 'C++', 'C#', 'Java', 'PHP')
for element in my_tuple:
    print(element)

product = {
    'name': 'book',
    'quantity': 3,
    'price': 4.99
}

for element in product:
    print(product[element])

for key, value in product.items():
    print(key, value)

people = [
    {
        'name': 'Juan',
        'age': 25,
    },
    {
        'name': 'Pedro',
        'age': 35,
    },
    {
        'name': 'Jorge',
        'age': 45,
    },
    {
        'name': 'Luis',
        'age': 55,
    },
    {
        'name': 'Ana',
        'age': 65,
    },
    {
        'name': 'Maria',
        'age': 75,
    }
]

for person in people:
    print(person['name'], person['age'])