

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1) # 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, 2! = 2 * 1!, 1! = 1 * 0! = 1

n = int(input("Enter a number: "))
res = fact(n)
print(res)