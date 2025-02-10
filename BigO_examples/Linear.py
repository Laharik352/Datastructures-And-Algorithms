'''Example of Linear-0(n) function'''
# def printvalues(n):
#     for i in range(1,n+1):
#         print(i)
# printvalues(5)      #Output value depends on input value (directly proportional)

# def func_1(lst):
#     for item in lst:
#         print(item)
# lst  = [1,2,3]
# func_1(lst)

# def func_2(lst):           # Here the big O is 0(2n) but we need to concentrate on the fastest growing term that is n. Also 2*infinity=infinity
#     for item in lst:       # So, we ignore "2". Now the order for the func_2 is O(n)
#         print(item)
#     for item in lst:
#         print(item)
# lst  = [1,2,3]
# func_2(lst)

def comp(lst):
    print(lst[0])   # O(1)

    mid = int(len(lst)/2)    # O(n/2)= O(1/2 * n)
    for i in lst[ :mid]:
        print(i)

    for x in range(10):     # O(10)=O(constant)
        print("hello world")
lst=[1,2,3,4,5,6]
comp(lst)       # O(1+n/2+10)=O(n)