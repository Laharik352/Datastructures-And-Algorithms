# class Engine:
#     '''THis is a program to demonstrate the concept of composition in Inheritance (HAS-A relationship)'''
#     a = 10
#     def __init__(self):
#         self.b = 20
#     def m1(self):
#         print("Engine specific funcitonality")
# class Car:
#     def __init__(self):
#         self.engine = Engine()
#     def m2(self):
#         print("Class Car using Engine Functionality")
#         print(self.engine.a)
#         print(Engine().a)
#         print(self.engine.b)
#         self.engine.m1()
# c = Car()
# c.m2()

class Car:
    """Employee HAS - A Car relationship"""
    def __init__(self, name, model, colour):
        self.name = name
        self.model = model
        self.colour = colour
    def getInfo(self):
        print("\tCar name:", self.name)
        print("\tCar model:", self.model)
        print("\tCar colour:", self.colour)
class Employee:
    def __init__(self, empName, empId, empCar ):
        self.empName = empName
        self.empId = empId
        self.empCar = empCar  # A method of one class can access other class functionality by simply creating object. This is HAS - A relationship
    def empInfo(self):
        print("Emp name:",self.empName)
        print("Emp ID:",self.empId)
        print("Emp Car Information....")
        self.empCar.getInfo()  # By using car..it accesses getinfo(). Therefore, Employee class using car class functionality.
car = Car("Innova", "2011", "Grey")
emp = Employee("Shiva", "112233", car)   # We pass car object here
emp.empInfo()


