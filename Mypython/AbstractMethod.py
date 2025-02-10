'''from abc import ABC, abstractmethod  #ABC-Abstract Base Class
class Shape(ABC):  #An interface for an object is a set of mehtods and attributes on that object.
    @abstractmethod     #In Python, we can use an abstract base class to define and enforce an interface.
    def area(self):
        pass
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

shape = Shape() #If we dont want to instantiate our class like this, we use abstract method. Now this will
# not work since the Shape is and abstract class. We have declared it as Shape(ABC)
square = Square(5)  # This will also not work since Square has inherited Shape which is abstract class
# To make use of the area and the perimeter methods, we have to implement them in the base class only.
'''

# ###############################################################################################

from abc import ABC, abstractmethod  #ABC-Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self, side):
        self.side = side
        return self.side * self.side

    def perimeter(self, side):
        self.side = side
        return self.side * 4


class Square(Shape):
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.side * self.side  # Since the area is @abstractmethod, we have to access it by implementing it in the base class
square = Square(5)
print(square.perimeter(5))  # Since the perimeter is not @abstractmethod, we can access it directly like this
print(square.area())


###############################################################################################

# from abc import ABC, abstractmethod  #ABC-Abstract Base Class
# class MyInterface(ABC):
#     @abstractmethod
#     def fun1(self):
#         print("Hi")
# class MyClass(MyInterface):
#     pass   #This will not work. We need to implement fun1 in sub class also
#     def fun1(self):
#         print("Hello")
# m1 = MyClass()
# m1.fun1()

#################################################################################################

# Python program showing
# abstract base class work

from abc import ABC, abstractmethod


class Polygon(ABC):

    # abstract method
    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
    def setnosides(self, side):     # Encapsulation
        self.side = side
    def getnosides(self):
        return self.side


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")

    # Driver code


R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()
R.setnosides(5)
print(R.getnosides())

K = Hexagon()
K.noofsides()
