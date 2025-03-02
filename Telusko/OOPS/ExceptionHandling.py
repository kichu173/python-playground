# Types of error = Syntax error, Logical error, Runtime error
# What is compile time error - Syntax error is a compile time error.
# What is runtime error - Logical error and runtime error are runtime errors. It occurs when you run the program.

a = 5
b = 2

try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter a number: "))
    print(k)
except ZeroDivisionError as e:
    print("Hey, you cannot divide a number by zero.", e)
except ValueError as e:
    print("Invalid Input", e)
except Exception as e:
    print("Hey, you cannot divide a number by zero.", e)

finally:
    print("Resource Closed")