# This matrix does a 90 degree rotation of the matrix
N = 4
def rotatematrix(mat):
    for x in range(0,int(N//2)):
        for y in range(x, N-x-1):
            temp = mat[x][y]
            mat[x][y]=mat[y][N-x-1]
            mat[y][N-x-1] = mat[N-x-1][N-y-1]
            mat[N-x-1][N-y-1] = mat[N-y-1][x]
            mat[N-y-1][x]=temp
def printMatrix(mat):
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end=" ")
        print("")

a = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 16]]
rotatematrix(a)
printMatrix(a)
