x = 3.3
print(x)
y = 1.1 + 2.2
print(y)

print(x == y) # False

y_str = format(y, '.2g')
print('y_str =',y_str)
print(y_str == str(x)) # True

print(y, x)
tolerance = 0.00001
print(abs(y-x) < tolerance) # True