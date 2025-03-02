class Computer:
    # attributes (variables)
    # behaviour (methods) - functions in OOPs we call it as methods
    # Class is a bluprint/ design of an object, Object is an instance of a class

    def __init__(self, cpu, ram):# special method - it will be getting called automatically when you create an object. Parameters are Object, cpu, ram
        print("in init")
        self.cpu = cpu
        self.ram = ram


    def config(self): # self is the object which you are passing, ex: Computer.config(com1) or com1.config() - both are same, automatically com1 objects passes to self
        print("Configuration is ", self.cpu, self.ram)

com1 = Computer('i5', 16) # Object creation - constructor
# com1.config() # Method calling
Computer.config(com1) # Method calling - another way of calling method

com2 = Computer('Ryzen 3', 8)
com2.config() # Method calling