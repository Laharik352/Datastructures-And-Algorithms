'''Decorators'''
# def smartdivision(func):
#     def inner(a,b):
#         if b==0:
#             return("Stupid...you cant divide a number by zero")
#         else:
#             return(a/b)
#     return inner
# @smartdivision
# def division(a,b):
#     return a/b
# print(division(20,10))
# print(division(20,0))

#OTP generation
from random import *
for i in range(5):
    print(chr(randint(65,65+25)),randint(0,9), chr(randint(65,65+25)), randint(0,9), chr(randint(65,65+25)), sep='')