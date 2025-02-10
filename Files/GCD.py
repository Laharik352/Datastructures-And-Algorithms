from math import gcd
# print(gcd(8,12))
# first = int(input("Enter the first number: "))
# second = int(input("Enter the second number: "))
# fac1 =[]
# fac2 = []
# common = []
# for i in range(1,first+1):
#     if first%i == 0:
#         fac1.append(i)
# # print(fac1)
# for j in range(1,second+1):
#     if second%j == 0:
#         fac2.append(j)
# # print(fac2)
# for k in fac1:
#     if k in fac2:
#         common.append(k)
# print("The gcd of {} and {} is {}".format(first, second, common[-1]))

# def gcd(first, second):
#     fac1 = []
#     fac2 = []
#     common = []
#     for i in range(1, first + 1):
#         if first % i == 0:
#             fac1.append(i)
#     # print(fac1)
#     for j in range(1, second + 1):
#         if second % j == 0:
#             fac2.append(j)
#     # print(fac2)
#     for k in fac1:
#         if k in fac2:
#             common.append(k)
#     return ("The gcd of {} and {} is {}".format(first, second, common[-1]))
# print(gcd(14,63))

# def gcd(first, second):
#     common = []
#     for i in range(1, min(first, second)+1):
#         if first%i == 0 and second%i == 0:
#             common.append(i)
#     return ("The gcd of {} and {} is {}".format(first, second, common[-1]))
# print(gcd(14,63))


# def gcd(first, second):
#     for i in range(1, min(first, second)+1):
#         if first%i == 0 and second%i == 0:
#             gcd = i  # There is not use of the list here becuase...it goes in order and the largest one will be at the end by default
#     return ("The gcd of {} and {} is {}".format(first, second, gcd))
# print(gcd(14,63))

'''Go from max to min'''
def gcd(m,n):
    i = min(m,n)
    while i > 0:
        if m%i == 0 and n%i == 0:
            return ("The gcd of {} and {} is {}".format(m, n, i))
        else:
            i-=1
print(gcd(14,63))
