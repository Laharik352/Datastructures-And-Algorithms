'''Fibonacci sequence using recursive method'''
def fib_rec(n):
    if n<=1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)
print(fib_rec(2))
print(fib_rec(3))
print(fib_rec(4))
print(fib_rec(5))
print(fib_rec(10))

'''Fibonacci sequence using Dynamic programming (Memoization)'''
#Cache
n=100
cache=[None]*(n)
def fib_dyn(n):
    #Base case
    if n<=1:
        return n
    #Check if the fib(n) is available in the cache
    if cache[n] != None:
        return cache[n]
    #keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return cache[n]

print(fib_dyn(10))




'''Fibonacci sequence using Iterative programming'''
def fib_iter(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a
print(fib_iter(10))
print(fib_iter(0))
print(fib_iter(1))
print(fib_iter(2))