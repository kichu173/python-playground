# In list for every element we store the index of the next element and the data of the element. This is how the list is implemented in python.
# Dictionary is a key value pair. It is a hash table. It is a collection of key value pairs. It is unordered and changeable. No duplicate members.
# Dictionary is mutable, we can add, remove and change the elements of a dictionary.
# If you pass them b/n different functions, any changes you make to them inside the function will apply outside the function as well.

myDict = {1: 'apple', 2: 'banana', 3: 'orange', "four": "mango"}

# Accessing the value using the key
print(myDict[2]) # banana
print(myDict['four']) # mango

# Accessing the value using the get method
print(myDict.get(3)) # orange
print(myDict.get("four")) # mango

# Accessing the value using the get method with a default value
print(myDict.get(4, 'Not found')) # Not found

print(myDict)

# Print the keys
print(myDict.keys()) # dict_keys([1, 2, 3])
print(myDict.values()) # dict_values(['apple', 'banana', 'orange'])

for e in myDict.keys():
    print(myDict[e])

print('----------')

for i,j in myDict.items():
    print(i,j)
