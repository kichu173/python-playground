class A: # Super / Parent class
    def feature1(self):
        print('Feature 1 is working')

    def feature2(self):
        print('Feature 2 is working')

class B(A): # Inheriting A, class B is child class of A (B is sub / child class)

    def feature3(self):
        print('Feature 3 is working')

    def feature4(self):
        print('Feature 4 is working')

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature2()
b1.feature3()
b1.feature4()

# Single level inheritance
# A
# ^
# |
# B

# Multi level inheritance
# A
# ^
# |
# B
# ^
# |
# C
# class A, class B(A), class C(B) - C is inheriting B and B is inheriting A

# Multiple inheritance
# A B
#  \/
#  C
# class A , class B, class C(A,B) - C is inheriting A and B