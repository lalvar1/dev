from math import floor, sqrt


def sqrt_binary_search(num):
    # if num == 1 or num == 0:
    #     return num
    # mid*mid = operation searched
    start = 0
    end = num
    while start <= end:
        mid = (start + end)//2
        if mid*mid == num:
            return mid
        elif mid*mid < num:
            start = mid + 1
        else:
            end = mid - 1
    return start-1


print(sqrt_binary_search(10))
