'''
Set the row and column of a element equal to zero, if the element is equal to zero.
Brute Force Approach
'''
def setZeros(matrix: list[list[int]]) -> None:
	# Write your code here.
    row = len(matrix)
    col = len(matrix[0])
    zero_ind = []
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                zero_ind.append((i,j))
    for ind in zero_ind:
        for c in range(col):
            matrix[ind[0]][c] = 0
        for r in range(row):
            matrix[r][ind[1]] = 0
    return matrix

'''
Optimized
'''
def setZeros(matrix: list[list[int]]) -> None:
	# Write your code here.
    row = len(matrix)
    col = len(matrix[0])
    r = [0] * col
    c = [0] * row
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                r[j] = 1
                c[i] = 1
    for i in range(row):
        for j in range(col):
            if matrix[i][j] != 0:
                if r[j] == 1:
                    matrix[i][j] = 0
                    continue
                if c[i] == 1:
                    matrix[i][j] = 0
                    continue
    return matrix