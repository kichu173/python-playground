from numpy import *

arr = array([1,2,3,4,5], int)

for i in arr:
    i += 5
    print(i, "values after adding 5")

print()

for i in range(len(arr)):
    # print(i) # goes from 0 to 4
    print(arr[i], "values before adding 5")
    arr[i] += 5

print(arr)

arr = arr + 5
print(arr)

arr1 = array([6,7,8,9,10], int)
arr2 = array([1,3,5,7,9], int)

arr3 = arr1 + arr2
print(arr3)

print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(max(arr1))
print(min(arr1))
print(sort(arr1))
print(unique(arr1))
print(concatenate([arr1, arr2]))

# copying the array

arr4 = array([2,6,8,1,3])

arr5 = arr4

print(arr4)
print(arr5)

# print the address of the arrays we created
print(id(arr4))
print(id(arr5))

# shallow copy - if you modify the original array, the copied array will also be modified
arr6 = arr4.view() # creates a new address for the copied array

arr4[1] = 7

print(arr4)
print(arr6)

print(id(arr4))
print(id(arr6))

# deep copy - if you modify the original array, the copied array will not be modified and also get two new addresses for both arrays
arr7 = arr4.copy()

arr4[2] = 9

print(arr4)
print(arr7)

print(id(arr4))
print(id(arr7))