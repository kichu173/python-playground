# List is mutable (add/remove/insert elements), ordered, allows duplicate elements

nums = [25,12,36,95,14]

print(nums)
print(nums[3])
print(nums[2:])
print(nums[-1])

names = ["navin", "Kiran", "john", "mike"]
print(names)

values = [9.5, "Kiran", 25, 12.5]
print(values)

misc = [nums, names]
print(misc)

nums.append(45)
print(nums)

# nums.clear() # clear the list
nums.insert(2, 77) # insert 77 at index 2
print(nums)

nums.remove(36) # remove 36 from the list
print(nums)

# nums.pop(1) # remove the element at index 1
nums.pop() # remove the last element from the list, you can pass index to remove element at that index

# del nums[2:] # remove elements from index 2 to end

nums.extend([29,38,59,47]) # add these elements to the list
print(nums)

min(nums)
max(nums)
sum(nums)
nums.sort()
print(nums)
print(type(nums)) # <class 'list'>