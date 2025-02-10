# Python 3 program to print
# matrix in zig-zag form

# Method to print matrix
# in zig-zag form
def printZigZag(row, col, a):
    evenRow = 0  # starts from the first row
    oddRow = 1  # starts from the next row

    while evenRow < row or oddRow < row:
        if evenRow < row:
            for i in range(col):
                # evenRow will be printed
                # in the same direction
                print(str(a[evenRow][i]),
                      end=" ")

                # Skipping next row so as
            # to get the next evenRow
            evenRow = evenRow + 2

        if oddRow < row:
            for i in range(col - 1, -1, -1):
                # oddRow will be printed in
                # the opposite direction
                print(str(a[oddRow][i]),
                      end=" ")

                # Skipping next row so as
        # to get the next oddRow
        oddRow = oddRow + 2


# Driver Code
r = 3
c = 5

mat = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15]]

printZigZag(r, c, mat)