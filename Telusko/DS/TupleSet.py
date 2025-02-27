# tuples is same as list but the only difference is that list is mutable and tuples are immutable (values cannot be changed)

# we cannot use square brackets, it will be considered as list so use round brackets
tup = (10, 20, 30, 30)
print(tup)
print(tup[1])
# tup[1] = 33 # This will give an error as tuples are immutable

print(tup.count(30)) # This will return the number of times 30 is present in the tuple

# When to use tuple - When you have a fixed set of values, use tuple
# When to use list - When you have a dynamic set of values, use list
# Tuple is faster than list because it is immutable and iteration is faster in tuple than list

set = {10, 20, 30, 30, 40, 50} # This is a set, it will not allow duplicates and it will not maintain the order

print(set) # This will remove the duplicates
# print(s[2]) # This will give an error as set does not support indexing, because we dont know the order