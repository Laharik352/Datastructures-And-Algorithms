def fact(n):
    if n>0:
        mul = 1
        for i in range(n,1,-1):
            mul = mul*i
    else:
        mul = 1
    return mul
print(fact(5))

