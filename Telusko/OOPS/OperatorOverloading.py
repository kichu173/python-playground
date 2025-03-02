# OperatorOverloading is a way to overload the operators in Python. For example, you can use the + operator to add two numbers and also to concatenate two strings. This is because the + operator is overloaded by the int and str classes. You can also overload the operators in your own classes.

class Student:
    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other): # This is the method to overload the + operator
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1 = Student(58,69)
s2 = Student(60,65)

s3 = s1 + s2 # Internally it calls Student.__add__(s1,s2)

print(s3.m1)

if s1 > s2: # Internally it calls Student.__gt__(s1,s2)
    print("s1 wins")
else:
    print("s2 wins")

print(s1)