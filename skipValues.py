# i/p: [1,2,3,4,5,6,7,8,9,10]
# o/p: [1,2,3,4,6,7,8,10]
inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = []
for i in inputList:
    if i == 5 or i == 9:
        continue
    output.append(i)
print(output)

# How do you iterate over keys and values in a dictionary?
my_dict = {'a': 1, 'b': 2}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
