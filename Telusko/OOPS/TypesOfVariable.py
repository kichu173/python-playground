# Two types of variables - Instance variable and class(static) variable

class Car:

    # variable defined outside the __init__ method and inside a class it is a class(static) variable
    wheels = 4

    def __init__(self):
        self.mil = 10 # Instance variables
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8 # This will change the value of mil for c1 only, this is an instance variables (for a particular instance). If you change one object it will not affect other object.

Car.wheels = 5

print(c1.mil, c1.com, Car.wheels)
print(c2.mil, c2.com, Car.wheels)

# static variables - What if you want to have a variable which will change it will affect all other objects

# - namespace is an area where you create and store object/variable
#- class namespace(where you will store all the class variables), instance namespace (where you will create all instance variables), global namespace, built-in namespace