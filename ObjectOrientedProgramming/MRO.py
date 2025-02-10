# Case-1 ####################################################################

# class A:
#     def m1(self):
#         print("Class-A method")
# class B(A):
#     def m1(self):
#         print("Class-B method")
# class C(A):
#     def m1(self):
#         print("Class-C method")
# class D(B,C):
#     def m1(self):
#         print("Class-D method")
# d = D()
# d.m1()

# Case-2 ####################################################################

# class A:
#     def m1(self):
#         print("Class-A method")
# class B(A):
#     def m1(self):
#         print("Class-B method")
# class C(A):
#     def m1(self):
#         print("Class-C method")
# class D(B,C):
#     pass
# d = D()
# d.m1() #Output will be Class_B method since we have declared as D(B,C) b first and then C

# Case-3 ####################################################################

# class A:
#     def m1(self):
#         print("Class-A method")
# class B(A):
#     pass
# class C(A):
#     def m1(self):
#         print("Class-C method")
# class D(B,C):
#     pass
# d = D()
# d.m1()

# Case-4 ####################################################################
class A:
    def m1(self):
        print("Class-A method")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
d = D()
d.m1()
