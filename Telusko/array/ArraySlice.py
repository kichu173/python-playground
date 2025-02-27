name = 'Youtube'
print(name[0])
print(name[6])
print(name[-1])
print(name[-2])
print(name[0:2])# start with index 0 to 1, 2 is exclusive
print(name[1:4])
print(name[1:])# start with index 1 to end
print(name[:4])# start with index 0 to 3, 4 is exclusive
print(name[3:10])# start with index 3 to 9, 10 is exclusive
# string is immutable in python
# name[0:3] = 'my' # TypeError: 'str' object does not support item assignment
print('my ' + name[3:])
myname = "Kiran Kumar"
print(len(myname))

#-7-6-5-4-3-2-1
# Y O U T U B E
# 0 1 2 3 4 5 6