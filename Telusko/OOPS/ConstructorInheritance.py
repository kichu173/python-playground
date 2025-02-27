# Subclass can access all teh features of Super class
# but
# Super class cannot access any features of Sub Class

class A: # Super / Parent class

    def __init__(self):
        print('In A init')

    def feature1(self):
        print('Feature 1 is working')

    def feature2(self):
        print('Feature 2 is working')

class B(A): # Inheriting A, class B is child class of A (B is sub / child class)

    def __init__(self):
        super().__init__() # Calling init of Super class
        print('In B init')

    def feature3(self):
        print('Feature 3 is working')

    def feature4(self):
        print('Feature 4 is working')

    def feat(self):
        super().feature1()

# If you create object of sub class it wil first try find init of sub class if it is not found then it wil call init of Super class
#* If you have call super then it will first call init of super class then call init of sub class
a1 = B()
a1.feat()

# Multiple inheritance
# A B
#  \/
#  C
# class A , class B, class C(A,B) - C is inheriting A and B - It uses MRO - Method Resolution Order and follows left to right order, left gets priority over right