'''Lists are nothing but dynamic arrays in python'''
def method1():
    l = []
    for n in range(10):
        l = l + [n]
    print(l)
method1()

def method2():
    l = []
    for n in range(10):
        l.append(n)
    print(l)
method2()

def method3():
    l = [n for n in range(10)]
    print(l)
method3()

def method4():
    l = list(range(10))
    print(l)
method4()
