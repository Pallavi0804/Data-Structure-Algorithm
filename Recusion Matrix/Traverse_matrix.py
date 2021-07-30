def traverse_matrix(i,j,str):
    n = m = 3
    matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
    if j == m and i == n:
        print(str)
        return
    # Pick R
    if j < m and matrix[i][j+1] == 1:
        traverse_matrix(i,j+1,str+'R')
    # Pick D
    if i < n and matrix[i+1][j] == 1:
        traverse_matrix(i+1,j,str+'D')

str = ""
i = j =0
traverse_matrix(i,j,str)

