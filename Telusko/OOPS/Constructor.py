class Computer:
    # pass # pass is a keyword in python which does nothing, it is used when a statement is required syntactically but you do not want any command or code to execute.

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def update(self): # self is a reference to the object
        self.age = 29

    def compare(self, c2): # parameters - self(who is calling), c2(whom to compare)
        if self.age == c2.age:
            return True
        else:
            return False

c1 = Computer('Navin', 28)
c2 = Computer('Kiran', 28) # Every time you create an obj, it's allocated to new space in Heap memory

print(id(c1))
print(id(c2))

c1.name = 'Rashi'
c1.age = 12

c1.update() # This will update the age of c1 object --> def update(c1)

print(c1.name)
print(c1.age)

print(c2.name)
print(c2.age)

if c1.compare(c2): # c1 will become 'self' to the compare method
    print("They are same")
else:
    print("They are different")

# Size of an object?
# Depends on the no. of variables and size of each variable

# Who allocates size to object?
# Constructor allocates size to object