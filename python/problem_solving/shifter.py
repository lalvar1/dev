import copy
# [1,2,3]
# [4,5,6]
# [7,8,9]
#
# [7,4,1]
# [8,5,2]
# [9,6,3]

test_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotate(array_list):
    aux_array = copy.deepcopy(array_list)
    for total_array_index, array in enumerate(aux_array):
        for array_index, num in enumerate(array):
            array_list[array_index][-1-total_array_index] = num
    return array_list


def rotate_editorial(A):
    # transpose the matrix
    for i in range(len(A)):
        for j in range(i, len(A)):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    N = len(A)
    # swap columns moving inwards from outwards
    for i in range(N / 2):
        for j in range(N):
            A[j][i], A[j][N - 1 - i] = A[j][N - 1 - i], A[j][i]
    return A


print(rotate(test_array))

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# [1,2,3]
# [4,5,6]
# [7,8,9]
#
# [7,4,1]
# [8,5,2]
# [9,6,3]


