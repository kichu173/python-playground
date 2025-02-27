class Student: # Outer class

    def __init__(self, name, roll_no):
        self.name = name
        self.rollNo = roll_no
        self.lap = self.Laptop() # You can create object of inner class inside the outer class(like this line ex: lap1 = s1.lap), else you can create object of inner class outside the outer class provided you ise the outer class name to call it ex: lap1 = Student.Laptop()

    def show(self):
        print(self.name, self.rollNo)

    class Laptop: # Inner class - When you know that the inner class is only used by the outer class, then you can define the inner class inside the outer class

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Navin', 2)
s2 = Student('Kiran', 3)

s1.show()

print(s1.lap.brand)

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))

lap1.show()
lap1.brand = 'Dell'
lap2.show()
lap1.show()