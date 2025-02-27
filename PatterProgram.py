#1            1             *
#12           2 2           **
#123          3 3 3         ***
#1234         4 4 4 4       ****
#12345        5 5 5 5 5     *****

rows = int(input("Enter number of rows: "))
for i in range(1, rows+1): #row iteration
    for j in range(1, i+1):
        print(j, end=" ")
    print('')

rows = int(input("Enter number of rows: "))
for i in range(1, rows+1): #row iteration
    for j in range(1, i+1):
        print(i, end=" ")
    print('')

rows = int(input("Enter number of rows: "))
for i in range(1, rows+1): #row iteration
    for j in range(1, i+1):
        print("*", end=" ")
    print('')