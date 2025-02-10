# class Person: '''Case-1'''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
# class Teacher(Person):
#     def __init__(self, name, age, salary, subject):
#         # self.name = name      # Instead of doing like this, let's invoke the variable from parent class
#         # self.age = age
#         super().__init__(name, age)     # Using super for invoking parent class variables
#         self.salary = salary
#         self.subject = subject
#     def display(self):
#         # print("Name:", self.name)  Let's try to avoid this by writing a method in the parent class for name and age since it is being used in display of Teacher and Student
#         # print("Age:", self.age)
#         super().display()       # Invoking the display of parent class. Here, we're invoking the parent class method
#         print("Salary:", self.salary)
#         print("Subject:", self.salary)
# class Student(Person):
#     def __init__(self, name, age, rollno, marks):
#         # self.name = name
#         # self.age = age
#         super().__init__(name, age)
#         self.rollno = rollno
#         self.marks = marks
#     def display(self):
#         # print("Name:", self.name)
#         # print("Age:", self.age)
#         super().display()
#         print("Rollno:", self.rollno)
#         print("Marks:", self.marks)
# t = Teacher("Durga", 32, 10000, "Python")
# t.display()
# s = Student("Ramu", 24, 123, 100)
# s.display()

class A:
    '''Case where there are many classes and all with the same method. In this case, the super() will take the latest method.'''
    def m1(self):
        print("Class A method")
class B(A):
    def m1(self):
        print("Class B method")
class C(B):
    def m1(self):
        print("Class C method")
class D(C):
    def m1(self):
        print("Class D method")
class E(D):
    # def m1(self):
    #     print("Class E method")
    # pass
    def m1(self):
        super().m1()   # By default it will take the immediate parent class method i.e; the one present in D
class F(D):
    def m1(self):
        B.m1(self)     # 1st method
class G(D):
    def m1(self):
        super(D, self).m1() # 2nd method....Here we are calling super of D, so we are calling the m1 method in class C
        #super(A, self).m1() #This will give error since there is no parent class of class A
e = E()
e.m1()
f = F()
f.m1()
g = G()
g.m1()


'''How to call a particular parent class method using super()
+Two ways to do this
1. parentclassname.method.(self)
2. super(parentclassname, self).methodname()
In the second method we are calling super of the parentclassname, so it will go to parentclass of parentclassname mentioned'''