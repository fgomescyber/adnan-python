def get_matrix_value(matrix, i, j):
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a list of lists')
    if i < 0 or j < 0:
        raise IndexError('negative indexing not allowed in this lab')
    try:
        return matrix[i][j]
    except IndexError:
        raise IndexError('index out of range - exercise demonstrates bounds checking')

if __name__ == '__main__':
    m = [[1,2,3],[4,5,6]]
    print('m[0][2] =', get_matrix_value(m,0,2))
