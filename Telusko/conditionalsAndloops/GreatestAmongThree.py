x, y, z = map(int, input("Enter three numbers separated by spaces: ").split())

if x >= y and x >= z:
    print(f"{x} is greatest")
elif y >= z:
    print(f"{y} is greatest")
else:
    print(f"{z} is greatest")