# Types of methods - Instance methods - Actuator Methods and Mutator methods, class methods, static methods - In methods, class and static methods are different

class Student:

    school = 'Telusko'

    def __init__(self, marks1, marks2, marks3):
        self.m1 = marks1
        self.m2 = marks2
        self.m3 = marks3

    def __str__(self): # override the __str__ method to print the object in a custom way (default it will print(s1): <__main__.Student object at 0x000001AB21893C50>)
        return f"m1: {self.m1}, m2: {self.m2}, m3: {self.m3}"

    def avg(self): # This is an instance method - it takes self as an argument
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self): # Instance method - Actuator Method for accessing the instance variable
        return self.m1

    def set_m1(self, value):# Instance method - Mutator Method for setting the instance variable
        self.m1 = value

    @classmethod # Decorators: This is a class method
    def get_school_info(cls): # Class method - It takes cls as an argument
        return cls.school

    @staticmethod # This is a static method
    def info(): # Static method - It does not take self or cls as an argument. When to use: If you are not using the instance variables or class variables in the method, then you can make that method a static method.
        print('This is a student class')

s1 = Student(34, 67, 32)
s2 = Student(43, 76, 23)

print(s1.m1, s1.m2, s1.m3)
print(s1)

print(s1.avg())
print(s2.avg())
print(s1.get_m1())
s1.set_m1(35)
print(s1.get_m1())
print(Student.get_school_info())
Student.info()

