# Anonymous Function or Lambda Function - A function without a name

def square(x):
    return x * x


res = square(5)
print(res)

# Functions are objects in python, we can pass function to a function

# anonymous func
f = lambda a: a * a  # here first 'a' is the argument

res1 = f(6)
print(res1)

f1 = lambda a, b: a + b  # here first 'a' and 'b' are the arguments

res2 = f1(5, 6)
print(res2)

