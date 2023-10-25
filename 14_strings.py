text = 'Ella sabe programar en Python'
print('JavaScript' in text)
print('Python' in text)

if 'Python' in text:
    print('Python está en el texto')
else:
    print('Python no está en el texto')

size = len('Python')
print(size)

print(text.upper())
print(text.lower())
print(text.count('a'))
print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Python'))
print(text.replace('Python', 'JavaScript'))

text_2 = 'este es un titulo'
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print('213'.isdigit())