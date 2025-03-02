from numpy import *

arr = array([1,2,3,4,5,6], int)
max = arr[0]

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]

print("Max value is: ", max)