from array import *

arr = array('i', [])

n = int(input("Enter the length of the array: "))

for i in range(n):
    # print(i) # 0 1 2 3 4
    x = int(input("Enter the next value: "))
    arr.append(x)

print("The array values are: ")
for i in arr:
    print(i," ", end="")

val = int(input("\nEnter the value to search for: "))
k = 0
for i in arr:
    if i == val:
        print("The value is found at index: ", k)
        break
    k+=1

print(arr.index(val)) # This will return the index of the value in the array