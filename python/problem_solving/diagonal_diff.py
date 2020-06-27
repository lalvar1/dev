# absolute diff between the two diagonals sum
def diagonal_difference(arr):
    # Write your code here
    first_diagonal = [row[index] for index, row in enumerate(arr)]
    second_diagonal = [row[-1-index] for index, row in enumerate(arr)]
    return abs(sum(first_diagonal)-sum(second_diagonal))


print(diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
