i = 1  # initialization
while i <= 5:  # condition
    print(i, " KKK ", end="") # end="" will not move cursor to next line while print does, prints statement in same line
    j = 1
    while j <= 4:
        print("rocks ", end="")
        j += 1
    i += 1  # increment / decrement
    print()
