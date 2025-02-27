a = 10

def something():
    global a
    a = 15
    print("inside fun ", a)

something()

print('outside ', a)

#* accessing both local and global variable in a function

b = 10
print(id(b))

def doSomething():
    b = 15
    x = globals()['b']
    print(id(x))
    print("inside fun ", b)

    globals()['b'] = 20

doSomething()

print('Outside ', b)