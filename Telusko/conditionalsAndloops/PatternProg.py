row = 4
for i in range(row):  # range(4) - starts from 0 and end at 3
    print("# ", end="")
    col = 3
    for j in range(col):  # The for loop in Python automatically increments the loop variable, so you don't need to manually increment i and j.
        print("# ", end="")
    print()

print()

row1 = 4
col1 = 0
for i in range(row1):
    print("* ", end="")
    for j in range(col1):
        print("* ", end="")
    col1 += 1
    print()

print()

row2 = 4
col2 = 3
for i in range(row2):
    print("# ", end="")
    for y in range(col2):
        print("# ", end="")
    col2 -= 1
    print()
