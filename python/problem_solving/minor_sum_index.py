from collections import defaultdict
from itertools import combinations

def twoSum(A, B):
    index1=index2=None
    for i, num in enumerate(A):
        for j, num_b in enumerate(A[1:]):
            if num + num_b == B:
                if not index1:
                    index1 = i
                    index2 = j + 1
                elif index2 > j+1:
                    index1 = i
                    index2 = j+1

    if not index1:
        return []
    else:
        return [index1, index2+1]


def two_sum(A, k):
    diffs = {}
    for i, v in enumerate(A):
        if k - v in diffs:
            return [diffs[k - v] + 1, i + 1]
        elif v not in diffs:        # will not save one time, meaning the lowest index
            diffs[v] = i
    return []

# def prettyPrint(A):
#     matrix_parent = []
#     for i in range(-A + 1, A):
#         matrix = []
#         for j in range(-A + 1, A):
#             matrix.append(1 + max(abs(i), abs(j)))
#         matrix_parent.append(matrix)
#     return matrix_parent
#     #return [[1 + max(abs(i), abs(j)) for j in range(-A + 1, A)] for i in range(-A + 1, A)]
#
# print(prettyPrint(4))

a = [1, 1, 1]
b = 2
print(twoSum(a, b))
a = [-1, -10, -5]
b = -5
print(twoSum(a, b))
a = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8]
b = -3
print(two_sum(a, b))




















