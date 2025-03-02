# Generators vs Iterators
# Iterators - are objects that can be iterated upon, traverse a sequence of numbers, container, particularly lists without having to store them off. They have two methods: __iter__() and __next__()
# Generators - A routine that can be used to control the iteration behavior of a loop. A generator is very similar to a function that returns an array.
# https://www.youtube.com/watch?v=u3T7hmLthUU

# Iterators explained

import sys

x = [1,2,3,4,5,6,7,8,9,10]

print(sys.getsizeof(x)) # 136
print(sys.getsizeof(range(1,11))) # 48

for el in x:
    print(el)



for i in range(1,11):
    print(i)

y = map(lambda x: x * 2, x)
print(y) # <map object at 0x7f8b1c1b8d30>

for el in y: # map object is an iterator.
    print(el)

print(sys.getsizeof(list(y))) # 184
print(sys.getsizeof(y))# 48

# Generators use case
# When to use? - When you want to iterate over a sequence of numbers, but you don't want to store them all in memory at the same time.
# You want to generate them one by one.

def csv_reader(file_name):
    for row in open(file_name, 'r'):
        yield row

csv_gen = csv_reader('requirements.txt')
print(next(csv_gen))

