# class A:
#     '''Example one of Loopholes of Super() method'''
#     a = 10
#     def __init__(self):
#         self.b = 20
# class B(A):
#     def m1(self):
#         print(super().a)
#         #print(super().b) # From the child class, you cannot call parent class instance variables...this is  a loophole
#         print(self.b)  # Hence use 'self' to do this
# c = B()
# c.m1()

class P:
    def __init__(self):
        print("Parent Constructor")
    def m1(self):
        print("Parent class instance method")
    @classmethod
    def m2(cls):
        print("Parent class class method")
    @staticmethod
    def m3():
        print("parent class static method")
class C(P):
    def __init__(self):   #From constructor of the child class
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    def m4(self):   #From instance method of child class
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
c = C()
c.m4()
