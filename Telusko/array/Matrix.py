from numpy import *

arr = array([
    [1,2,3],
    [4,5,6]
])

print(arr.dtype)
print(arr.ndim) # what is the dimension of the array - 1D or 2D
print(arr.shape) # what is the shape of the array - 2 rows, 3 columns
print(arr.size) # what is the size of the array - 6 elements

arr2 = arr.flatten() # flatten the array to 1D

print(arr2)

arr3 = arr2.reshape(2,3) # reshape the array to 2D

print(arr3)

arr1 = array([
    [1,2,3,6],
    [4,5,6,7]
])

m = matrix(arr1)

print(m)

m1 = matrix('1 2 3; 4 5 6; 7 8 9')

print(m1)
print(diagonal(m1))
print(m1.max())
print(m1.min())

m2 = matrix('1 2 3; 6 8 5; 2 6 7')
m3 = m1 + m2
m4 = m1 * m2

print(m3)
print(m4)