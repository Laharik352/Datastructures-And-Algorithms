def merge(A,B):
    C, m, n = [], len(A), len(B)
    i, j = (0,0)
    while i+j < m+n:
        if i == m:
            C.append(B[j])
            j = j+1
        elif j == n:
            C.append(A[i])
            i = i + 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i = i + 1
        elif A[i] > B[j]:
            C.append(B[j])
            j = j + 1
    return C
# print(merge(list(range(0,100, 2)), list(range(1, 75, 2))))

def mergesort(A, left, right):
    if right -left <= 1:            # IF the length is 1 or 0, then return the same
        return(A[left:right])
    if right - left > 1:
        mid = (left + right)//2
        L = mergesort(A, left, mid) #else, divide and go till all the elements have been split till one element
        R = mergesort(A, mid, right)
        return(merge(L,R))
l = list(range(0,100, 2))+list(range(1, 50, 2))

print(mergesort(l, 0, len(l)))

