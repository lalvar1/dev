# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    # if len(lst) == 0:
    #     return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) <= 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is the remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# Driver program to test above function
#print(*permutation(list('')), sep='\n')


def clean_permutation(lst):
    if len(lst) <= 1:
        return [lst]
    recursion_list = []
    for i in range(len(lst)):
        actual = lst[i]
        remaining_list = lst[:i] + lst[i+1:]
        for p in clean_permutation(remaining_list):
            recursion_list.append([actual] + p)
    return recursion_list


print(*clean_permutation(list('1234')), sep='\n')






