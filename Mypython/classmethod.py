# class Student(object):
#
#     @classmethod
#     def from_string(cls, name_str):
#         first_name, last_name = map(str, name_str.split(' '))
#         student = cls(first_name, last_name)
#         return student
#
# scott = Student.from_string('Scott Robinson')
# print(scott)

# class Dummy(object):
#
#     @classmethod
#     def some_function(cls,*args,**kwargs):
#         print(cls)
#
# #both of these will have exactly the same effect
# Dummy.some_function()
# Dummy().some_function()

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 23)
person2 = Person.fromBirthYear('mayank', 1996)  #You are not creating an instance here, you are only creating a reference to the cls function to access its functionality

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

'''Here, we have two class instance creator, a constructor and a fromBirthYear method.

Constructor takes normal parameters name and age. While, fromBirthYear takes class, name and birthYear, calculates the current age by subtracting it with the current year and returns the class instance.

The fromBirthYear method takes Person class (not Person object) as the first parameter cls and returns the constructor by calling cls(name, date.today().year - birthYear), which is equivalent to Person(name, date.today().year - birthYear)

Before the method, we see @classmethod. This is called a decorator for converting fromBirthYear to a class method as classmethod().

Factory methods are those methods which return a class object (like constructor) for different use cases.'''


class Shape(object):
    # this is an abstract class that is primarily used for inheritance defaults
    # here is where you would define classmethods that can be overridden by inherited classes
    @classmethod
    def from_square(cls, square):
        # return a default instance of cls
        return cls
print(Shape.from_square(3))