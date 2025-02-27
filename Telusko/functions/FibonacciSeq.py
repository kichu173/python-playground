def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n < 0:
        print("Invalid Number")
        return
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print("{} ".format(c), end="")
    return c


val = int(input("Enter the value of n: "))
fib(val) #val= 5 - 0 1 1 2 3

def fib1(n):
    if n <= 0:
        print("Invalid Number")
        return None
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    print(a)
    return a

val = int(input("Enter the value: "))
fib1(val)