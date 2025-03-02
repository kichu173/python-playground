from numpy import *

arr1 = array([1,2,3,4,5], int)
arr2 = array([5,4,3,2,1], int)

# Ensure both arrays are of the same length
if len(arr1) == len(arr2):
    result = array([0] * len(arr1), int) # array([0, 0, 0, 0, 0]) - [0] * len(arr1): This creates a list of zeros with the same length as arr1.
    for i in range(len(arr1)):
        result[i] = arr1[i] + arr2[i]
    print(result)
else:
    print("Arrays are not of the same length.")