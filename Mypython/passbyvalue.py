# def hello(x):
#     x = 34              #Here we are changing the value inside the function, it will not affect the value of x i.e;12 outside the function
#     print("Before print:",id(x))
#     print(x)
#     print("After print:",id(x))
#     return
# x=12                # THis value of 12 is not affected outside the function
# hello(x)            # Here we are passing only the copy of the value and not the original value
# print(id(x))
# hello(13)

#Call by value: We have a variable, if we make any changes to that variable inside the function, then these changes
#will not be affected to the variable outside the function

#Call by reference: We have a variable, if we make any changes to that variable inside the function, then these changes
#will be affected to the variable even outside the function
'''
Call by Value
The most common strategy is the call-by-value evaluation, sometimes also called pass-by-value.
This strategy is used in C and C++, for example. In call-by-value, the argument expression is evaluated,
and the result of this evaluation is bound to the corresponding variable in the function. So, if the
expression is a variable, a local copy of its value will be used, i.e. the variable in the caller's
scope will be unchanged when the function returns.
Call by Reference
In call-by-reference evaluation, which is also known as pass-by-reference, a function gets an implicit
reference to the argument, rather than a copy of its value. As a consequence, the function can modify the
argument, i.e. the value of the variable in the caller's scope can be changed. The advantage of call-by-reference
consists in the advantage of greater time- and space-efficiency, because arguments do not need to be copied.
On the other hand this harbours the disadvantage that variables can be "accidentally" changed in a function call.
So special care has to be taken to "protect" the values, which shouldn't be changed.

To come back to our initial question what is used in Python: The authors who call the mechanism call-by-value and
those who call it call-by-reference are stretching the definitions until they fit.
Correctly speaking, Python uses a mechanism, which is known as "Call-by-Object", sometimes also called
"Call by Object Reference" or "Call by Sharing".
If you pass immutable arguments like integers, strings or tuples to a function, the passing
acts like call-by-value. The object reference is passed to the function parameters. They can't be changed within
the function, because they can't be changed at all, i.e. they are immutable. It's different, if we pass mutable
arguments. They are also passed by object reference, but they can be changed in place in the function. If we pass a
list to a function, we have to consider two cases: Elements of a list can be changed in place, i.e. the list will be
changed even in the caller's scope. If a new list is assigned to the name, the old list will not be affected, i.e. the
list in the caller's scope will remain untouched.
'''

print("===========================================")
print("Pass by value")
def increment(a):
    a+=1
    print("+++",id(a))
    print(a)

num = 1
print(id(num))
increment(num)
print(num)      # The num value remains to be 1 only
print(id(num))


print("++++++++++++++++++++++++++++++++++++++++++++++")
print("Pass by reference")
def add_more(lst):
    lst.append(5)
    print("_____",id(lst),"----")
    print(lst)
mylst = [1,2,3,4]
print(id(mylst))
add_more(mylst)
print(mylst)
print(id(mylst))
