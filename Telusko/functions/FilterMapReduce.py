from functools import reduce

nums = [3, 2, 6, 8, 4, 6, 2, 9]

print(nums)

evens = list(filter(lambda n: n % 2 == 0, nums)) # The filter function will apply the lambda function to each element of the nums list. If the lambda function returns True, the element will be added to the new list. If the lambda function returns False, the element will not be added to the new list. The second argument of the filter function is the list that we are filtering.

print(evens) # [2, 6, 8, 4, 6, 2]

def is_odd(n):
    return n % 2 != 0

odd = list(filter(is_odd, nums))

print(odd) # [3, 9]

# map - takes the value from the list, applies the operation and returns a new value
doubles = list(map(lambda n: n * 2, nums)) # The map function will apply the lambda function to each element of the nums list and return a new list with the results.
print(nums)
print(doubles)

# reduce - takes the value from the list, applies the operation and returns a single value

sum = reduce(lambda a, b: a + b, nums) # The reduce function will apply the lambda function to the first two elements of the nums list. Then it will apply the lambda function to the result of the first two elements and the third element of the nums list. It will continue this process until it reaches the end of the list. The final result will be the sum of all the elements of the nums list.
print(sum)