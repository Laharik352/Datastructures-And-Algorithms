'''Assertions: Assertions is used for the purpose of debugging
Debugging: THe process of identifying and fixing the Bug is called debugging
Bug: The deviation of the expected output from the received output leads to a bug
The easiest way of debugging is by using the print statement. Many times we use too many print statements for debugging,
forget to remove the print statements after fixing the bug. and the code will become ugly and performance will come down.
To overcome this problem we use alternative called ASSERTIONS
The biggest advantage of print statement is You do not need to delete these statements. Based on the requirement, you can either enable the assertion or disable them.
Assertions must always be used either in the Development environment or the Test environment. But never in the production environment
Defect: A problem in the Development environment
Bug: A problem in the Testing environment
Error: A problem in production environment

Two types of assertions:
1. Simple version:
assert conditional_expression --> If the actual condition and the conditional expression is true. Then continue. Else return AssertionError.
2. Very Simple version (Augmented version):
Here, we print a statement as to why we got assertion error instead of printing just 'AssertionError'
assert conditional_expression, message -----> so upon failure, we get...AssertionError: message
Augmented version is always recommended
'''
############################################################################################################

# '''Simple Version'''
# x=10
#
# # assert x > 10   #False
# assert x == 10  #True
#
# print(x)

############################################################################################################

# '''Augmented Version'''
# x=10
#
# assert x > 10, 'Here x value must be greater than 10 but it is not'   #False
# # assert x == 10  #True
#
# print(x)

############################################################################################################

'''Note: to disable the assertions.....we can use python -O Assertions.py 
Capital O
We have to put '-O' while running the program'''

def squareIt(x):
    return x**x     # Instead of giving x*x or x**2.....i've given this.

assert squareIt(2)==4, 'The square of 2 must be 4'
assert squareIt(3)==9, 'The square of 3 must be 9'
assert squareIt(4)==16, 'The square of 4 must be 16'
print(squareIt(2))
print(squareIt(3))
print(squareIt(4))