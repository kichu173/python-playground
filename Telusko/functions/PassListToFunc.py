lst = input("Enter a list of numbers separated by spaces: ").split()

lst = [int(i) for i in lst]

print(lst, [type(i) for i in lst])

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


even, odd = count(lst)
print(f"Even: {even} and Odd: {odd}")
# print("Even: {} and Odd: {}".format(even, odd))

# Assignment (Take 10 names from the user and print the names which have length greater than 5)

lst1 = []
for i in range(10):
    name = input("Enter name {}/10: ".format(i + 1))
    lst1.append(name)

for e in lst1:
    if len(e) > 5:
        print(e)