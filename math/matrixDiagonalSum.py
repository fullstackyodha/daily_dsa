def diagonalMatrixSum(mat):
    colleft, colright = 0, len(mat) - 1
    sum = 0

    for row in range(0, len(mat)):
        if row != colleft or row != colright:
            sum += mat[row][colleft] + mat[row][colright]
        else:
            sum += mat[row][colleft]

        colleft += 1
        colright -= 1

    return sum


print(diagonalMatrixSum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
