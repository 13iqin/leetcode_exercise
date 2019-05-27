def searchMatrix(matrix, target):
    row = len(matrix) - 1
    col = 0
    while row > 0 and matrix[row][col] > target:
        row -= 1
    while col < len(matrix[0]):
        if matrix[row][col] == target:
            return True
        if target > matrix[row][col]:
            col += 1
        elif row > 0:
            row -= 1
        else:
            return False
    return False