# Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements),
# such that the sum of the two subarrays is the same. Print the two subarrays.


def is_possible_to_split(arr):
    half = len(arr) // 2
    first_half_sum = sum(arr[:half])
    first_half_index = second_half_index = half
    second_half_sum = sum(arr[half:])
    if first_half_sum > second_half_sum:
        for i, num in enumerate(arr[half - 1::-1]):
            first_half_sum -= num
            second_half_sum += num
            if first_half_sum <= second_half_sum:
                first_half_index -= i - 1
                break
    elif first_half_sum < second_half_sum:
        for i, num in enumerate(arr[half:]):
            second_half_sum -= num
            first_half_sum += num
            if first_half_sum >= second_half_sum:
                second_half_index += i + 1
                break

    if first_half_sum == second_half_sum and half:
        print(*[arr[:first_half_index], arr[second_half_index:]], sep='\n')
    else:
        print('Not possible')


# a = [1, 2, 3, 4, 5, 5]
# is_possible_to_split(a)

# a = [5, 5, 1, 5, 4]
#
# a = []
# a= [5,5]

a = [5, 5, 1, 5, 4]
is_possible_to_split(a)


def is_possible(arr):
    total = sum(arr)
    if total % 2 != 0:
        return 'Not possible'
    target = total/2
    total = 0
    for i, num in enumerate(arr):
        total += num
        if total == target:
            return arr[:i+1], arr[i+1:]
        elif total > target:
            return 'Not possible'

a=[2,2,4]
print(is_possible(a))
