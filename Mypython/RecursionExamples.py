# '''factorial of n using recursion'''
# def fact(n):
#     if (n>=1):
#         return n*fact(n-1)
#     else:
#         return 1
# print(fact(4))

''' Fibonacci numbers using recursion'''
# def fib(n):
#     # fib(1) =1
#     # fib(0) =1
#     if (n>=3):
#         return fib(n-1) + fib(n-2)
#     else:
#         return 1
# print(fib(4))

# '''Inductive definition of Multiplication of 2 numbers'''
# def multiply(m, n):
#     if n>1:
#         return (m+multiply(m,n-1))
#     else:
#         return(m)
# print(multiply(4,3))

# '''Inductive definition of Length of a list'''
# def length(l):
#     if l == []:
#         return 0
#     else:
#         return (1+length(l[1:])) # l[1:] removes the first element in the list
# print(length([1,2,3,4,5,6]))

'''Inductive definition of the sum of list of numbers'''
def sumlist(l):
    if l==[]:
        return 0
    else:
        return (l[0] + sumlist(l[1:]))
print(sumlist([1,2,3,4,5]))
