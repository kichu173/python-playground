def add():
    print("result 1 is ")
    print("__name__ " + __name__)

def sub():
    print("result 2 is ")

def main():
    add()
    sub()

# main() # This main is also getting executed when I call add() in the SpecialVariableName2Ex1, which is not needed and to avoid this we need to use __main__ in the SpecialVariableName2Ex1.

if __name__ == '__main__':
    main() # This will avoid the execution of main() in the SpecialVariableName2Ex1.