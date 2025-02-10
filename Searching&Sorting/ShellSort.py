'''Implementation of shell sort'''
def ShellSort(arr):
    sublistcount = len(arr)//2
    while sublistcount > 0:     #Until it becomes one single element
        for start in range(sublistcount):
            gap_insertion_sort(arr, start, sublistcount)
        # print(sublistcount)
        # print(arr)
        sublistcount = sublistcount//2
    return arr

def gap_insertion_sort(arr, start, gap):
    for i in range(start+gap, len(arr), gap):
        position = i
        while position >= gap and arr[position - gap] > arr[position]:
            (arr[position-gap], arr[position]) = (arr[position], arr[position-gap])
            position = position - gap
    return arr
print(ShellSort([45,67,23,45,21,24,7,2,6,4,90]))
