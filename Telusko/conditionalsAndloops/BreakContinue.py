av = 10

x = int(input("Enter how many candice you want? "))

i = 1
while i <= x:

    if i > av:
        print("Out of stock")
        break # This will break the loop, jump out of the block or loop

    print("Candice")
    i+=1

print("Bye")

for y in range(1,101,1):
    if y % 3 == 0 or y % 5 == 0: # skip the values divisible by 3 or 5 and go back to next iteration
        continue
    print(y)

for i in range(1,101):
    if i % 2 != 0:
        pass # This will pass the control, there is no code so ignore it (use pass when you are not sure what code to put in the block and it skips the block )
    else:
        print(i)

