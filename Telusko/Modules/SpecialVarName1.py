import Calc # When you are importing Calc, then it becomes a module for this file

print("Special Var says " + __name__) # __main__ is the name of the file that is being executed

def main():
    print("Hello")
    print("Welcome User")

if __name__ == '__main__':
    main() # This is the entry point of the file