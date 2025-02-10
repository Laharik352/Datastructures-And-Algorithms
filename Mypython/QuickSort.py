'''Quick sort algorithm'''
def quickSort(A, l, r):
    if r-l <= 1:    # for the arrays which are of length 1 or 0
        return ()
    yellow = l + 1
    # print(yellow)
    for green in range(l+1, r):
        if A[green] <= A[l]:
            # print("", A, l+1, yellow, green)
            (A[yellow], A[green]) = (A[green], A[yellow])       #pivot, <=pivot, >=pivot
            yellow = yellow + 1
    (A[l], A[yellow-1]) = (A[yellow-1], A[l])       #<=pivot, pivot, >=pivot
    quickSort(A, l, yellow-1)
    quickSort(A, yellow, r)
    return A
print(quickSort([13,32,22,78,63,57,91,43], 1, 8))