'''Implementation of bubble sort'''
# def BubbleSort(arr):
#     for n in range(len(arr)-1, 0, -1):
#         # print(n)
#         for k in range(n):
#             # print(k)
#             if arr[k] > arr[k+1]:
#                 temp = arr[k+1]
#                 arr[k+1] = arr[k]
#                 arr[k] = temp
#     return arr
# print(BubbleSort([5,2,3,7]))

# # One liner code for bubble sort
# def swap(param, param1):
#     (param, param1) = (param1, param)
# def bubblesort(arr):
#     [swap(arr[k+1], arr[k]) for n in range(len(arr)-1,0,-1) for k in range(n) if arr[k] > arr[k+1]]
#     return arr
# print(bubblesort([5,2,3,7]))

#
# Simple and most easiest way
def bubblesort(arr):
    for i in range(len(arr)-1):     # len(arr)-1 used because we should not get index out of bound exception when the element reaches last element
        for j in range(len(arr)-1): # len(arr)-1 used because we should not get index out of bound exception when the element reaches last element since we compare with next index element
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubblesort([3,2,4,1,5]))