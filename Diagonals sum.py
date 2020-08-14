def sum_diagonals(matrix):
    matrix_len = len(matrix)
    first_diag = 0
    second_diag =0
    for i in range(0, matrix_len):
        first_diag += matrix[i][i]
        second_diag += matrix[i][matrix_len - i - 1]
    return first_diag + second_diag
    # flatten = lambda l: [item for sublist in matrix for item in sublist]
    #flat_list = [item for sublist in matrix for item in sublist]
    """upper code means
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    """
    

diag=[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
sum_diagonals(diag)
