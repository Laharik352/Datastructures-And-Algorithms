# class Student:
#     '''This is a class of student and his marks'''
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def display(self):
#         print("Student name:", self.name)
#         print("Marks of the student is", self.marks)
#     def grade(self):
#         if self.marks >= 60:
#             print("student is grade 1")
#         elif self.marks >= 50:
#             print("student is grade 2")
#         elif self.marks >= 35:
#             print("Student is grade 3")
#         else:
#             print("Student has failed")
# n = input("Enter Number of student in class: ")
# for i in range(int(n)):
#     name = input("Enter the name of the Student: ")
#     marks = int(input("Enter the student marks: "))
#     s = Student(name, marks)
#     s.display()
#     s.grade()
#     print("*"*20)
#


# class Student:
#     '''This is a class of student and his marks using getters and setters'''
#     def setName(self, name):
#         self.name = name
#     def getName(self):
#         return self.name
#     def setMarks(self, marks):
#         self.marks = marks
#     def getMarks(self):
#         return self.marks
#
# n = input("Enter Number of student in class: ")
# for i in range(int(n)):
#     name = input("Enter the name of the Student: ")
#     marks = int(input("Enter the student marks: "))
#     s = Student()
#     s.setName(name)
#     s.setMarks(marks)
#     print("Your name is {} and marks is {}".format(s.getName(),s.getMarks()))


# class Animal:
#     '''THis is the class for representation of class method'''
#     legs = 4
#     @classmethod
#     def walk(cls, name):
#         print('{} walks with {} legs'.format(name, cls.legs))
#         # print('{} walks with {} legs'.format(name, Animal.legs)) # THis will also work
# Animal.walk('Dog')
# Animal.walk('Cat')

# Write a program to track the number of objects created for a class
class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count + 1
    @classmethod
    def getNoOfObjects(cls):
        print("Number of objects created:", cls.count)
t1=Test()
t2=Test()
Test.getNoOfObjects()
# t2.getNoOfObjects() #THis will also work
