# https://www.youtube.com/watch?v=kGcUtckifXc&list=LL&index=2&t=2s
# Master These 10 Python Functions

# 1st useful function to know - print
age = 23
name = "Sam"

print("My name is", name, "and I am", age, "years old.")# My name is Sam and I am 23 years old. (if you notice you no need to provide spaces as if we do using + operator for concatenation)
print("My name is", name, "and I am", age, "years old.", sep="|")# My name is|Sam|and I am|23|years old. sep is used to separate the values with the given value.

print("hello world") # by default it adds \n at the end of the line.
print("hello world", end=" | ") # end is used to add the given value at the end of the line.
print("I am", name)

# 2nd useful function to know
# help() # allows to print out the documentation of a python function.
help('string')
help('print')

def test_func(a, b):
    """
    a: value 1
    b: value 2

    returns: int
    """
    return a + b

help(test_func) # This will print the documentation of the function test_func.

# 3rd useful function to know
# range function is used to iterate through values in a for loop
# also used to generate a list of numbers
rng = range(10) # acts as the stop, its going to go up to the value of 10 but not include 10

print(rng) # returns the range object, which is an iterator
print(list(rng))

rng = range(2, 10) # start, stop

print(list(rng))

rng = range(2, 10, 2)  # start, stop, step

print(list(rng))

rng = range(10, -10, -2)  # start, stop, step

print(list(rng))

# for i in range(10):
#     print(i)

# 4th useful function to know - map
# map() func - allows to apply a function to every single item in an iterable object like a list or a tuple or a set or a dictionary or a string or a range.

strings = ["my", "world", "apple", "pear"]

# traditional way
newStringsList = []
for el in strings:
    length = len(el)
    newStringsList.append(length)
print(newStringsList)

# using map()
lengths = map(len, strings) # len is a in-built function and strings is an iterable object
lengths1 = map(lambda x: x + "s", strings)  # lambda is an anonymous function, x is the parameter(each element from strings(iterable) is passed to x) and x + "s" is the return value. This lambda function takes each element from strings and adds "s" at the end of it.
print(list(lengths))
print(list(lengths1))

def add_s(x):
    return x + "s"

lengths2 = map(add_s, strings) # add_s is a function and strings is an iterable object
print(list(lengths2))

# 5th useful function to know - filter
# filter() func - it will take all items in the iterable object, then pass it to a compatible function.

def longer_than_4(el):
    return len(el) > 4

filtered = filter(longer_than_4, strings) # longer_than_4 is a function and strings is an iterable object
filtered1 = filter(lambda x: len(x) > 4, strings)
print(list(filtered))
print(list(filtered1))

# 6th useful function to know - sum
# sum() functon - return the sum of all the different numbers from an iterable object (list/set/tuple/dictionary)

numbers = {1,4.5,5,23,2}
print(sum(numbers, start=5)) # doesnt matter so long as the values inside the iterable are numbers, int or float.
# start is an optional parameter, if you want to add a value to the sum of the iterable object.

# 7th useful function to know - sorted
# sorted() function - used to sort the values in an iterable object.
numbers1 = [4,5,2,3,-1,0,9]
sorted_nums = sorted(numbers1) # numbers1 is a list
print(sorted_nums)
sorted_nums1 = sorted(numbers1, reverse=True) # numbers1 is a list, reverse is an optional parameter, if you want to sort the values in descending order.
print(sorted_nums1)

people = [ # people is a list of dictionaries
    {"name": "Sam", "age": 23},
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20}
]

sorted_people = sorted(people, key=lambda person: person["age"]) # key takes a python function, which is going to be applied to every single item in the iterable object. In this case, it is going to take the age of each person and sort the people based on their age.
sorted_people1 = sorted(people, key=lambda person: person["age"], reverse=True)

print(sorted_people)
print(sorted_people1)

# 8th useful function to know - enumerate
# enumerate() function - you can have index and element at the same time.

tasks = ['task1', 'task2', 'task3', 'task4']

for idx in range(len(tasks)):
    task = tasks[idx]
    print(f"{idx + 1}: {task}")

print("-----------")

for idx in tasks:
    print(idx)

print("-----------")

for idx, el in enumerate(tasks):
    print(f"{idx + 1}: {el}") # returns tuples

print(list(enumerate(tasks))) # returns a list of tuples

#9th useful function to know - zip
# zip() - used to combine two or more iterable objects into a single iterable object.
# Automatically handles when one iterable object has more objects than the other.

names = ["Alice", "Bob", "Sam"]
age = [22, 23, 24]

for i in range(min(len(names), len(age))):
    print(f"{names[i]} is {age[i]} years old.")

"""
The min(len(names), len(age)) is used as a safety measure to prevent index errors when looping through two lists that might have different lengths. 
For example, if names has 3 elements and age has 2 elements
names = ["Alice", "Bob", "Sam"]       # length 3
age = [22, 23]                        # length 2

Using min(len(names), len(age)) would return 2, ensuring we only iterate up to the length of the shorter list.
This prevents an IndexError that would occur if we tried to access age[2] which doesn't exist. 
If we had used just len(names) or len(age) without min(), and tried to access an index beyond the bounds of either list, our code would crash with an IndexError: list index out of range
"""

gender = ["Male", "Male"]

combined = list(zip(names, age, gender)) # list of tuples
print(combined)

for name, age, gender in combined:
    print(f"{name} is {age} years old is {gender}")

# 10th useful function to know - open
# open() - used to open a file, it returns a file object, which has a bunch of methods and attributes that can be used to collect information about the file, read the file, write to the file, etc.

file = open("test.txt", "w") # override a file if it already exists, if it doesnt exist, it will create a new file.
# clear everything that is inside of it.

file.write("Hello World\nMy name is Kiran")

file.close() # close the file, to avoid memory leaks.

# best way to write the above code for open
with open("test.txt", "r") as file: # r - read mode, file.close() is not needed, it will automatically close the file when the block of code is done executing.
    text_read = file.read()
    print(text_read)

with open("test.txt", "a") as file:
    file.write("\nI am 23 years old.") # append to the file, if it doesnt exist, it will create a new file. If exists, it will add the text to the end of the file and not overwrite everything in file.
