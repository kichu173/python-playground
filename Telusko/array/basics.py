from array import *

vals = array("i", [5,9,8,4,2])
print(vals)

# vals.reverse()


for i in vals:
    print(i)

newArr = array(vals.typecode, (a for a in vals))

for e in newArr:
    print(e, " ", end="")

print()
print("Using while loop")
i = 0
while i < len(newArr):
    print(newArr[i])
    i+=1