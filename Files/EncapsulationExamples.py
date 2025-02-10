# class Hello:
#     def __init__(self, name):
#         self.name = name
#         self.a = 10
#         self._b = 20
#         self.__c = 30  # You can access this private member variable only inside the class but outside the class you cannot access it.
# hello = Hello('name')    #If you want to access and modify it, you have to use getters and setters.
# hello.a                   # private member variable is not visible to the object
# hello._b
# hello.__c #You cannot access c since it is private

# ###############################################################################

# class Car:
#     '''Example 2'''
#     def __init__(self, speed, colour):
#         self.__speed = speed
#         self.colour = colour
#     def set_speed(self, value):
#         self.__speed = value         # You can use the private member variable inside the class or inside any method of the class like this.
#     def get_speed(self):
#         return self.__speed
#     def set_colour(self, colour):
#         self.colour = colour
#     def get_colour(self):
#         return self.colour
# ford = Car(100, "blue")
# ford.set_speed(200)
# ford.__speed = 300 ## This will not work since the speed variable is private and and can be changed only using setters
# ford.colour = "silver" #This will work since the colour is not private. Even by using setters also we can change the value of this variable.
# ford.set_colour("Purple")
# print(ford.get_speed())
# print(ford.colour)
# print(ford.get_colour())
# print(ford.__speed)


###############################################################################


# class Rectangle:
#     '''Example 3'''
#     def __init__(self, height, width):
#         self.__height = height
#         self.__width = width
#     def set_height(self, height):
#         self.__height = height
#     def get_height(self):
#         return self.__height
#     def set_width(self, width):
#         self.__width = width
#     def get_width(self):
#         return self.__width
#     def area(self):
#         return self.get_height() * self.get_width()
#
# r1 = Rectangle(100, 200)
# r1.set_height(400)
# r1.set_width(400)
# print(r1.area())

###############################################################################

class PrivateMethod:
    def __init__(self):
        self.a = 10
        self._b = 20
        self.__c = 30
    def public_method(self):
        print(self.__c)
        print("public method")
    def __private_method(self):
        print("private method")

hello = PrivateMethod()
print(hello.a)
print(hello._b)
hello.public_method()
hello.__private_method()  # You cannot access the private method outside the class. THis will give you error



