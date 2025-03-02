values = []
for x in range(10):
    values.append(x)

print(values)

#* List Comprehension
# Basic List Comprehensions
values = [x + 1 for x in range(10)] # every element x in for loop is appended to the list values, whole left x is the value added to list for every single iteration in the for loop

print(values)

# Comprehension Condition
# Get all the even numbers from 0 - 50
evens = []
for x in range(51):
    if x % 2 == 0:
        evens.append(x)

print(evens)

evens = [num for num in range(51) if num % 2 == 0] # if placed in right is for filtering the values to be added to the list
print(evens)

#* Comprehension With Multiple Conditions

# Strings that start with "a" and end with "y"
options = ["any", "albany", "apple", "world", "hello",""]
valid_strings = []

for el in options:
    if len(el) <= 1:
        continue
    if el.startswith("a") and el.endswith("y"):
        valid_strings.append(el)
print(valid_strings)

valid_strings = [
    el
    for el in options
    if len(el) >= 2 # all the conditions to be true for the element to be added to the list
    if el[0] == "a"
    if el[-1] == "y"
]

print(valid_strings)

# Multiple List Comprehension
# Flattening a matrix (list of lists)
matrix = [[1,2,3], [4,5,6], [7,8,9]] # 3x3 matrix
flattened = []

for row in matrix:
    for num in row:
        flattened.append(num)

print(flattened)
print(matrix)

flattened = [num for row in matrix for num in row] # for loop inside for loop
print(flattened)

# If/Else In A Comprehension
# Categorize numbers as even or odd

categories = []

for num in range(10):
    if num % 2 == 0:
        categories.append("even")
    else:
        categories.append("odd")

print(categories)

categories = [
    "even" if num % 2 == 0 else "odd" # if else in the left of for loop is for inserting the value in the list
    for num in range(10)
]

# Transformation In Comprehension

def square(x):
    return x**2

squared_numbers = [square(x) for x in range(10) if x % 2 == 0]# filtering happens first and then the transformation

print(squared_numbers)

# Dictionary Comprehension
# Creating a dictionary

pairs = [(0, "apple"), (1, "banana"), (2, "cherry")]# list of tuples/ pairs

my_dict = {
    k:v
    for k,v in pairs
}

print(my_dict)

# Set comprehension
# Removing duplicates from a list while applying a function

nums = [1,2,2,3,3,3,4,4,4,4]

unique_squares = {x**2 for x in nums}

print(unique_squares)
