from array import *

arr = array('i', [5,9,8,4,2])

x = int(input("Enter the index to delete: "))

for i in range(x,len(arr) -1):
    print(arr[i]," ", end="")
    arr[i] = arr[i+1]

print()
# Reduce the array size
arr = arr[:-1] # arr[:-1] means we are taking a slice of the array from the beginning up to, but not including, the last element.

for i in arr:
    print(i," ", end="")