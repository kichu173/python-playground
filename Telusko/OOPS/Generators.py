# In python, Generators are used to create iterators. It is a function that returns an object (iterator) which we can iterate over (one value at a time).

def top_ten():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq # In Python, the yield keyword is used in functions to turn them into generators. You use it to return a generator object that can be iterated over.
        n += 1

for i in top_ten():
    print(i)

print('------------')

# Generator function using 'yield'
def generator_example():
    for i in range(3):
        yield i  # returns one value each time and pauses. The state of the function is remembered. The next time the function is called, execution continues from the last yield statement.

for value in generator_example():
    print(value)  # prints 0, 1, then 2

print('------------')

# Using return statement
def return_example():
    for i in range(3):
        return i  # returns one value and stops


example = return_example()
print(example)  # prints 0
