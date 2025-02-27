def person(name, age):# formal arguments
    print(name)
    print(age)

person("Navin", 28) # actual arguments

person(age=29, name="navin") # positional arguments

def person1(name, age=18):
    print(name)
    print(age)

person1("Navin", 30) # default arguments

def sum(a, *b): # b is a tuple, variable length arguments
    c = a
    for i in b:
        c = c + i
    print(c)

sum(5,6,34,78)

def person2(name, **data): # data is a dictionary and this is Keyworded variable length arguments
    print(name)

    for i,j in data.items():
        print(i,j)

person2('Kiran', age=28, city='Chennai', mob=9865432)