'''Implementation of selection sort'''
#Most easiest way
def selection_sort1(arr):
    for i in range(len(arr)):
        minpos = i
        for j in range(i, len(arr)):
            if arr[minpos] > arr[j]:
                minpos = j
        (arr[minpos], arr[i]) = (arr[i], arr[minpos])
    return arr
print(selection_sort1([5,3,7,2]))

def selection_sort(arr):
    for i in range(len(arr)):
        minpos = i
        for j in range(i, len(arr)):
            if arr[j]<arr[minpos]:
                minpos = j
        arr[minpos], arr[i] = arr[i], arr[minpos]
    return arr
print(selection_sort([3,2,4,1,5]))


def selection_sort2(arr):
    for fillsort in range(len(arr)-1, 0, -1):
        positionMax = 0     # here we keep the track of the max element
        for location in range(1, fillsort+1):   #from 1 since already positionMax = 0
            if arr[location] > arr[positionMax]:
                positionMax = location
        temp = arr[fillsort]
        arr[fillsort] = arr[positionMax]
        arr[positionMax] = temp
    return  arr
print(selection_sort2([5,3,7,2]))