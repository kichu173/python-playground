#! There is no conecpt of pass by value or pass by reference in python, it is pass by object reference. Everything in python is an object

def update(x):
    print(id(x))

    x = 8
    print(id(x))  # the moment we change the value, address changes | Strings, Integers, Floats, Tuples are immutable
    print("x ", x)


a = 10
print(id(a))
update(a)
print("a ", a)


def update1(lst):
    print(id(lst))

    lst[1] = 25
    print(id(lst)) # id is same, list is mutable
    print("x ", lst)


lst = [10, 20, 30]
print(id(lst))
update1(lst)
print("lst ", lst)
