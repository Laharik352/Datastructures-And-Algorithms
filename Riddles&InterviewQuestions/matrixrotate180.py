
def matrix180(mat):
    N=3
    i=N-1
    while (i>=0):
        j=N-1
        while (j>=0):
            print(mat[i][j], end=" ")
            j=j-1
        print()
        i=i-1
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
matrix180(mat)
'''output
9 8 7
6 5 4
3 2 1'''
