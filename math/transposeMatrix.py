def transpose(mat):
    rows, cols = len(mat), len(mat[0])
    res = [[0] * rows for _ in range(cols)]
    
    for row in range(rows):
        for col in range(cols):
            res[col][row] = mat[row][col]
            
    return res

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))