# Different types of data types in Python
# 1. None: None is a special constant in Python that represents the absence of a value or a null value.
# 2. Numeric: Numeric value can be integer, floating number, boolean or even complex numbers. These values are defined as int, float and complex class in Python.
# 3. Sequence Type: A sequence is an ordered collection of similar or different data types. Python has the following built-in sequence data types:
#     1. String: A string value is a collection of one or more characters put in single, double or triple quotes.
#     2. List: A list object is an ordered collection of one or more data items, not necessarily of the same type, put in square brackets.
#     3. Tuple: A Tuple object is an ordered collection of one or more data items, not necessarily of the same type, put in round brackets.
#     4. Dictionary: Dictionary is an unordered collection of key-value pairs.
#     5. Set: Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.
# 4. Range: The range() function is used to generate a sequence of numbers. It is often used with the for loop to iterate a sequence of numbers.

num = 2.5
print(type(num)) # <class 'float'>
num = 5
print(type(num)) # <class 'int'>
num = 3+5j
print(type(num)) # <class 'complex'>
num = 3>5
print(type(num)) # <class 'bool'>

a = 5.6
b = int(a) # Type casting - Converting one data type to another
print(type(b)) # <class 'int'>
k = float(b)
print(k) # 5.0
print(type(k)) # <class 'float'>

c = complex(b, k)
print(c) # (5+5j)

print(int(True)) # 1
print(int(False)) # 0

st = 'a'
print(type(st)) # <class 'str'>

# range: to generate a sequence of numbers - range(start, stop, step)
# To iterate over a sequence of numbers, you can use range() function. It generates a sequence of numbers but does not store them in memory.
print(list(range(10)))
print(list(range(2,11,2)))