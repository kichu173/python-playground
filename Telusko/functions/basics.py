def greet():
    print("Hello, World!")

greet()

def add(x, y):
    return x + y


result = add(2, 10)
print(result)

def add_sub(a, b):
    c = a + b
    d = a - b
    return c,d


res1,res2 = add_sub(20, 10)
print(res1, res2)
