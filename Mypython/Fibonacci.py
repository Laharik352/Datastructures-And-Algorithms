# def fib(c):
#     a,b =0,1
#     for i in range(c):
#         a,b = b, a+b
#     return a
# print(fib(5))

def simplegenerator():
    yield 1
    yield 2
    yield 3
for i in simplegenerator():
    print(i)

x = simplegenerator()
print(x.__next__())
print(x.__next__())
print(next(x))