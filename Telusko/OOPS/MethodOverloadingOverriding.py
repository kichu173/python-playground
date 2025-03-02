class Student:
    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s = 0
        # Method overloading is not supported in Python, but you can achieve it by using default values for the parameters
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a

        return s

s1 = Student(58,69)
print(s1.sum(5,9))

# Method overriding - If you have a method in the parent class and you want to change the implementation of that method in the child class, then you can do that by overriding that method in the child class

class A:

    def show(self):
        print('in A show')

class B(A):

    def show(self):
        print('in B show')

a1 = B()
a1.show() # This will call the show method of class B, not A. This is method overriding