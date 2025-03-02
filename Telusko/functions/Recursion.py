# recursion - you are calling a func from itself - you are calling a func from a same func

import sys

# to increase the recursion limit
sys.setrecursionlimit(2000)


print(sys.getrecursionlimit()) # default value is 1000

i = 0

def greet():
    global i
    i+=1
    print("Hello", i)
    greet()

greet()