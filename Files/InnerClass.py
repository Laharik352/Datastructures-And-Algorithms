# class Employee:
#     def __init__(self, empId, empName, empSal):
#         self.empId = empId
#         self.empName = empName
#         self.empSal = empSal
#     def display(self):
#         print("Employee ID:", self.empId)
#         print("Employee Name", self.empName)
#         print("Employee Salary:", self.empSal)
#
# #How to access the members of one class into the other class
# class Test:  # This is static method since we are not using self, and accessing it using Test (Class name)
#     def modify(emp):
#         emp.empSal = emp.empSal +10000
#         emp.display()
# e = Employee(1234, "Yahdav", 70000)
# Test.modify(e)


# class Outer:
#     def __init__(self):
#         print("Outer class object creation..")
#     def m2(self):
#         print("Outer class method")
#     class Inner:
#         def __init__(self):
#             print("Inner class object creation..")
#         def m1(self):
#             print("Inner class object creation")
# o = Outer()
# i =o.Inner()
# i.m1()
# print("*"*25)
# o.m2()
# o.m1() # will not work
#i.m2() # Will not work

class Person:
    def __init__(self,name, dd, mm, yyyy ):
        self.name = name
        self.dob = self.DOB(dd, mm, yyyy)

    def display(self):
        print("Name:", self.name)
        self.dob.display()

    class DOB:
        def __init__(self, dd, mm, yyyy):
            self.dd = 15
            self.mm = 8
            self.yyyy = 1947

        def display(self):
            print("DOB:{}/{}/{}".format(self.dd, self.mm, self.yyyy))

p = Person('Sunny', 15, 8, 1947)
p.display()
p.dob.display()
