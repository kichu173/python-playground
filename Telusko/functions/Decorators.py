# Decorators - A function which takes a function as an argument and returns a function as an output. You can add extra features to the existing function without modifying it.
def div(a,b):
    return a/b


def smart_divide(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner


res = div(2, 4)
print(res) # 0.5

div1 = smart_divide(div) # This is the decorator (You can change the behaviour of existing function without modifying it at the compile time itself)
print(div1(2,4)) # This is the function that is being decorated
