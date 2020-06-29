# find min positive integer in list


def solution(A):
    # write your code in Python 3.6
    max_ = max(A)
    if max_ <= 0:
        return 1
    else:
        # A = sorted(A)
        # positives = [num for num in A if num > 0]
        for i in range(1, max_):
            if i not in A:
                return i


print(solution([1, 3, 6, 4, 1, 2]))
