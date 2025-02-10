'''Implementation of quick sort'''
'''Easy method'''
# def quicksort(arr):
#     lesser = []
#     greater = []
#     equal = []
#     if len(arr) > 1:
#         pivot = arr[0]
#         for x in arr:
#             if x>pivot:
#                 greater.append(x)
#             if x<pivot:
#                 lesser.append(x)
#             if x==pivot:
#                 equal.append(x)
#         return sorted(lesser)+equal+sorted(greater)
#     else:
#         return arr
# print(quicksort([7,3,11,13,2,4,56]))

'''Second easy method'''
def quickSort(array, begin=0, end=None):
    if end is None:
        end = len(array)-1
    def _quickSort(array, begin, end):
        if begin>=end:
            return
        pivot = partition(array, begin, end)
        _quickSort(array, begin, pivot-1)
        _quickSort(array, pivot+1, end)
        # print(array)
    return _quickSort(array,begin, end)
def partition(array, begin, end):
    pivot=begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot+=1
            # print(pivot)
            array[i], array[pivot] = array[pivot], array[i]
            # print("",array)
    array[pivot], array[begin] = array[begin], array[pivot]
    # print(array)
    # print("+", array)
    return pivot
print((quickSort([7,3,11,13,2,4,56])))



# def quicksort(arr):
#     quicksorthelp(arr, 0, len(arr)-1)
#     return arr
#
# def quicksorthelp(arr,first, last):
#     if first<last:
#         splitpoint = partition(arr, first, last)
#
#         quicksorthelp(arr, first, splitpoint-1)     # the half to the right of splitpoint
#         quicksorthelp(arr,splitpoint+1, last)       # the half to the left of splitpoint
#     return arr
# def partition(arr,first,last):
#     pivotvalue = arr[first]
#     leftmark = first+1
#     rightmark = last
#     done = False
#     while not done:
#         while leftmark<=rightmark and arr[leftmark] <= pivotvalue: # as long as the leftmark less than right mark and the value of the left mark is less than the pivotvalue
#             leftmark+=1     #We move towards the right
#         while arr[rightmark] >= pivotvalue and rightmark >= leftmark: # as long as the right mark is greater than the left mark and value of right mark is greater the pivot value
#             rightmark-=1    #We move towards the left
#         if rightmark<leftmark:      #Crossing point of the leftmark and the rightmark
#             done = True
#         else:
#             (leftmark, rightmark) = (rightmark, leftmark)
#     (arr[first],arr[rightmark]) = (arr[rightmark], arr[first])
#     return rightmark
#
# print(quicksort([7,3,11,13,2,4,56]))

'''Second Method'''
# def quickSort(A, l, r):
#     if r-l <= 1:    # for the arrays which are of length 1 or 0 #Base case
#         return ()
#     yellow = l + 1
#     # print(yellow)
#     for green in range(l+1, r):
#         if A[green] <= A[l]:
#             (A[yellow], A[green]) = (A[green], A[yellow])       #pivot, <=pivot, >=pivot
#             # print("", A, l + 1, yellow, green)
#             yellow = yellow + 1
#     (A[l], A[yellow-1]) = (A[yellow-1], A[l])       #<=pivot, pivot, >=pivot
#     quickSort(A, l, yellow-1)
#     quickSort(A, yellow, r)
#     return A
# print(quickSort([43,32,22,78,63,57,91,13], 1, 8))
