# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#     def __add__(self, other):
#         return self.pages + other.pages
#     def __mul__(self, other):
#         return self.pages*other.pages
#     def __sub__(self, other):
#         return self.pages-other.pages
#     def __truediv__(self, other):
#         return self.pages/other.pages
# b1 = Book(200)
# b2 = Book(100)
# b3 = Book(300)
# print(b1+b2)
# print(b1-b2)
# print(b1*b2)
# print(b1/b2)


#
# class Book:
#
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __add__(self, other):
#         total = self.pages + other.pages
#         t = Book(total)
#         return t
#
#     def __mul__(self, other):
#         total = self.pages * other.pages
#         t = Book(total)
#         return t
#
#     def __str__(self):
#         return "The Number of Pages: "+str(self.pages)
#
# b1 = Book(200)
# b2 = Book(100)
# b3 = Book(300)
# b4 = Book(400)
# print(b1 + b2)
# print(b1 * b2)
# print(b1 + b2 + b3)
# print(b1 * b2 * b3 * b4)

class Student:
    def __init__(self, name, marks):
        self.marks = marks
        self.name = name
    def __lt__(self, other):
        return self.marks<other.marks  #The behavior must be coded here
s1 = Student('durga', 100)
s2 = Student('ramu',200)
print(s1<s2)
print(s2<s1)