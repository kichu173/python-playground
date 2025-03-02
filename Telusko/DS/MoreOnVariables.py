a = 10
b = 10

# Whenever you create multiple variables with the same value, Python will point them to the same memory location (memory optimization)
print(id(a))
print(id(b))

c = 9
d = c

print(id(c))
print(id(d))

c = 8
print(id(c))
print(id(d))
print(d)

# Constants - Capital letters are used to represent constants
PI = 3.14 # This can be override but it is a convention to use capital letters for constants and not to change the value
print(type(PI)) # to find the type of variable - <class 'float'>