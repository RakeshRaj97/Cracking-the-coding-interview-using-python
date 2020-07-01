''' algorithm to set the entire row and column to zero
if an element in the MxN matrix is zero'''


def set_zero_row(matrix, r):
    #loop through the columns
    col = len(matrix[0])
    for i in range(col):
        matrix[r][i]=0

def set_zero_col(matrix, c):
    #loop through the rows
    row = len(matrix)
    for i in range(row):
        matrix[i][c]=0


def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row = []
    col = []

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                row.append(x)
                col.append(y)

    for r in row:
        set_zero_row(matrix, r)

    for c in col:
        set_zero_col(matrix, c)

    return matrix

a = (
  [1,2,0,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16]
)
print(zero_matrix(a))

