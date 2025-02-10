'''Insertion sort implementation'''
def insertion_sort(arr):
    for i in range(len(arr)):
        position = i
        # print(i)
        while position>0 and arr[position - 1] > arr[position]:
            # print(arr)
            (arr[position], arr[position - 1]) = (arr[position - 1], arr[position])
            # print("**",arr)
            position = position - 1
    return arr
print(insertion_sort([5,3,7,2]))