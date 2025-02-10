# class P:
#     d = 20
#     def __init__(self):
#         self.a = 10
#         print("Constructor")
#     def m1(self):
#         print("Parent class Instance method")
#     @classmethod
#     def m2(cls):
#         print("Parent class class method")
#     @staticmethod
#     def m3():
#         print ("Parent class static method")
# class C(P):
#     pass
# c = C()
# print(c.a)
# print(c.d)
# c.m1()
# c.m2()
# c.m3()

# ###################################################################################################
#
# class Parent:
#     def m1(self):
#         print("Parent class method")
# class Child(Parent):
#     def m2(self):
#         print("Child class mehtod")
# c = Child()
# c.m1()
# c.m2()


###################################################################################################

class P:
    a = 10
    def __init__(self):
        self.b = 20
class C(P):
    c = 30
    def __init__(self):
        super().__init__()
        self.d = 40
c = C()
print(c.a, c.b, c.c, c.d)

