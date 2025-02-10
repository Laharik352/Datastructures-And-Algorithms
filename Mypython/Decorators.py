'''Here we represent the functionality of decorators'''
# I have a division function, this will give me zero division error when b is zero. And this is an exception.
# I want to handle that exception but without changin/touching the original div function
# This can be done using decorators
# Decorators are used to extend the functionality of already existing function without modification of the function

# @checkZero
# def div(a,b):
#     return a/b

def checkZero(func):    # this is a decorator function

    def inner(a,b):     # In this function, I am doing exception handling
        if b==0:
            print("You can't divide by zero")
            return
        return func(a,b)
    return inner

@checkZero          # We use "@" instead of div = checkZero(div) OR div1 = checkZero(div) statement
def div(a,b):
    return a/b

# div1 = checkZero(div)    # Here we are creating a new function using the checkzero function that is internally using the div function
                         # We can create a new function since everything in python in an object
#div = checkZero(div)    # This will also work, we can rename the new function with the same name as the old function


#print(div1(10,0))
print(div(10,0))        # We give "@checkZero" as an alternative for "div = checkZero(div)" statement
print(div(10,1))




