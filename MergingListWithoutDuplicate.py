list1 = [10,10,20,30,40,20,30]
#you should not remove the duplicates from list1, and in output list you should add the unique numbers not available in list1
list2 = [10,20,30,40,50,60]

#output = [10,10,20,30,40,20,30,50,60]

outputList = list1
for value in list2:
    if value not in list1:
        outputList.append(value)
print(outputList)


