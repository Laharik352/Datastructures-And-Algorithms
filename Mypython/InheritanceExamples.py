# class Person:
#     '''THis example shows the Is-A functionality'''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat_n_drink(self):
#         print("Eat buryani and drink beer")
#
# class Employee(Person):
#     def __init__(self,name, age, eId, esal):
#         super().__init__(name, age) #When an Employee object is created, the name and age will be initialized by the parent class. The eId and esal will be
#         self.eId = eId
#         self.esal = esal
#     def work(self):
#         print("Python Work")
#     def empInfo(self):
#         print("Name of Employee:", self.name)
#         print("Employee age:", self.age)
#         print("Employee ID:", self.eId)
#         print("Employee sal:", self.esal)
# e = Employee("Durga", 12, 1122332, 1000000)
# e.eat_n_drink()
# e.work()
# e.empInfo()


# ####################################################################################################
# # This example demonstrates both Is-A and Has-A relationship
# class Car:
#     def __init__(self, name, model, colour):
#         self.name = name
#         self.model = model
#         self.colour = colour
#     def getInfo(self):
#         print("\tCar name:", self.name)
#         print("\tCar model:", self.model)
#         print("\tCar colour:", self.colour)
# class Person:
#     '''THis example shows the Is-A functionality'''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat_n_drink(self):
#         print("Eat buryani and drink beer")
#
# class Employee(Person): #Employee is a person, employee has a car
#     def __init__(self,name, age, eId, esal, ecar):
#         super().__init__(name, age) #When an Employee object is created, the name and age will be initialized by the parent class. The eId and esal will be initialized by the child class
#         self.eId = eId
#         self.esal = esal
#         self.ecar = ecar
#     def work(self):
#         print("Python Work")
#     def empInfo(self):
#         print("Name of Employee:", self.name)
#         print("Employee age:", self.age)
#         print("Employee ID:", self.eId)
#         print("Employee sal:", self.esal)
#         print("Employee Car details:")
#         self.ecar.getInfo()
# c = Car("Innova", 2011, "blue")
# e = Employee("Durga", 12, 1122332, 1000000, c)
# e.eat_n_drink()
# e.work()
# e.empInfo()

# ###################################################################################################
#
# class Parent:
#     '''Single Inheritance'''
#     def m1(self):
#         print("Parent class method")
# class Child(Parent):
#     def m2(self):
#         print("Child class mehtod")
# c = Child()
# c.m1()
# c.m2()

# ###################################################################################################
#
# class Parent:
#     '''Multi-level Inheritance'''
#     def m1(self):
#         print("Parent class method")
# class Child(Parent):
#     def m2(self):
#         print("Child class method")
# class SubChild(Child):
#     def m3(self):
#         print("Sub-Child method")
# s = SubChild()
# s.m1()
# s.m2()
# s.m3()

# ###################################################################################################
#
# class Parent:
#     '''Hierarchial Inheritance'''
#     def m1(self):
#         print("Parent class method")
# class Child1(Parent):
#     def m2(self):
#         print("Child-1 class method")
# class Child2(Parent):
#     def m3(self):
#         print("Child-2 method")
# c1 = Child1()
# c1.m1()
# c1.m2()
# c2 = Child2()
# c2.m1()
# c2.m3()

# ###################################################################################################
#
# class Parent1:
#     '''Multiple Inheritance----Case1'''
#     def m1(self):
#         print("Parent-1 method")
# class Parent2:
#     def m2(self):
#         print("Parent-2 method")
# class Child(Parent1, Parent2):
#     def m3(self):
#         print("Child Method")
# c = Child()
# c.m1()
# c.m2()
# c.m3()

# ###################################################################################################
#
# class Parent1:
#     '''Multiple Inheritance----Case2'''
#     def m1(self):
#         print("Parent-1 method")
# class Parent2:
#     def m1(self):
#         print("Parent-2 method")
# class Child(Parent1, Parent2): #Based on the order we mention, the priority will be set.
#     def m3(self):              #Here, Parent1 will be given higher priority
#         print("Child Method")
# c = Child()
# c.m1() #Parent-1 method
# c.m3() #Child Method

# ###################################################################################################
#
# class Parent1:
#     '''Multiple Inheritance----Case3'''
#     def m1(self):
#         print("Parent-1 method")
# class Parent2:
#     def m1(self):
#         print("Parent-2 method")
# class Child(Parent2, Parent1): #Based on the order we mention, the priority will be set.
#     def m3(self):              #Here, Parent2 will be given higher priority than Parent1
#         print("Child Method")
# c = Child()
# c.m1() #Parent-2 method
# c.m3() #Child Method

###################################################################################################

class A(B):
    def m1(self):
        print("Class-A method")
class B(A):
    def m2(self):
        print("Class-B method")
