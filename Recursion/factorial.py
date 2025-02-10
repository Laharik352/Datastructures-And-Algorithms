'''To find the factorial of a number using recursion'''
def fact(n):
    # print(n)
    if n == 0:      # Base case
        return 1
    else:
        return n*fact(n-1)
print(fact(4))