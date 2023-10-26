# while True: 
#     print('Se Ejecuta')

counter = 0

while counter < 10:
    counter += 1
    print(counter)

while counter < 20:
    counter += 1
    if counter == 15:
        break
    print(counter)

while counter < 30:
    counter += 1
    if counter < 25:
        continue
    print(counter)