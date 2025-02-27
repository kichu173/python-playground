nums = [10,20,30,40]

it = iter(nums)

print(it.__next__()) # iterator preserves the state of the list, what is iterator? it is a class that has __next__ method, and it is used to get the next element in a sequence.
print(it.__next__())

for i in nums:
    print(i)
