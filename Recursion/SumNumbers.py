'''Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1'''
def sum_num(n):
    # print(n)
    if len(str(n)) == 1:
        return n
    else:
        return n%10 + sum_num(n//10)
print(sum_num(4321))